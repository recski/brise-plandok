import logging
import os
import time

import numpy as np
import torch
from tqdm import tqdm
from transformers import AdamW, get_linear_schedule_with_warmup

from brise_plandok.baselines.classifiers.bert.bert_constants import BERT_NAME
from brise_plandok.baselines.classifiers.bert.brise_bert_model import BriseBertClassification
from brise_plandok.baselines.classifiers.bert.prepare_data import get_datasets, create_data_loaders
from brise_plandok.baselines.constants import RULE_BASED_ATTRIBUTES
from brise_plandok.baselines.utils import (
    epoch_time,
    calculate_performance,
    fix_random,
    calculate_loss_weights,
)


class BriseBertTrainer:
    def __init__(self, gpu, epochs, model_checkpoint, output_folder, use_weights, lr):
        self.epochs = epochs
        self.device = torch.device("cpu")
        self.set_gpu(gpu)
        fix_random()
        self.output_folder = output_folder

        dataset_train, dataset_val = get_datasets()
        self.dataloader_train, self.dataloader_val = create_data_loaders(
            dataset_train, dataset_val
        )

        self.model = BriseBertClassification.from_pretrained(
            BERT_NAME,
            num_labels=len(RULE_BASED_ATTRIBUTES),
        )
        self.set_model(model_checkpoint, use_weights, dataset_train)

        self.optimizer = AdamW(self.model.parameters(), lr=lr, eps=1e-8)
        logging.info(f"Learning rate is set to {lr}")

        self.scheduler = get_linear_schedule_with_warmup(
            self.optimizer,
            num_warmup_steps=0,
            num_training_steps=len(self.dataloader_train) * self.epochs,
        )

    def set_gpu(self, gpu_nr):
        cuda_available = torch.cuda.is_available()
        logging.info(f"Cuda available: {cuda_available}")
        if cuda_available and gpu_nr is not None:
            os.environ["CUDA_VISIBLE_DEVICES"] = gpu_nr
            logging.info(f'GPU is set to {os.environ["CUDA_VISIBLE_DEVICES"]}')
            self.device = torch.device("cuda")

    def set_model(self, model_checkpoint, use_weights, dataset_train):
        if model_checkpoint is not None:
            self.model.load_state_dict(torch.load(model_checkpoint, map_location=self.device))
        _ = self.model.to(self.device)
        for p in self.model.base_model.parameters():
            p.requires_grad = False
        self.set_loss_weights(use_weights, dataset_train)

    def set_loss_weights(self, use_weights, dataset_train):
        loss_weights = calculate_loss_weights(dataset_train.labels)
        loss_weights_tensor = (
            torch.Tensor(loss_weights.to_list()).to(self.device) if use_weights else None
        )
        self.model.set_loss_weights(loss_weights_tensor)
        if use_weights:
            logging.info(f"Loss weights are set to\n{loss_weights}")

    def evaluate(self):
        self.model.eval()

        loss_val_total = 0
        predictions, true_vals = [], []

        for batch in self.dataloader_val:
            batch = tuple(b.to(self.device) for key, b in batch.items() if key != "text")

            inputs = {
                "input_ids": batch[0],
                "attention_mask": batch[1],
                "labels": batch[2],
            }

            with torch.no_grad():
                outputs = self.model(**inputs)

            loss = outputs[0]
            logits = outputs[1]
            loss_val_total += loss.item()

            logits = logits.detach().cpu().numpy()
            label_ids = inputs["labels"].cpu().numpy()
            predictions.append(logits)
            true_vals.append(label_ids)

        loss_val_avg = loss_val_total / len(self.dataloader_val)

        predictions = np.concatenate(predictions, axis=0)
        true_vals = np.concatenate(true_vals, axis=0)

        return loss_val_avg, predictions, true_vals

    def train(self):
        best_val = None
        for epoch in tqdm(range(1, self.epochs + 1)):

            start_time = time.time()

            self.model.train()

            loss_train_total = 0

            progress_bar = tqdm(
                self.dataloader_train, desc="Epoch {:1d}".format(epoch), leave=False, disable=False
            )
            for batch in progress_bar:
                self.model.zero_grad()

                batch = tuple(b.to(self.device) for key, b in batch.items() if key != "text")

                inputs = {
                    "input_ids": batch[0],
                    "attention_mask": batch[1],
                    "labels": batch[2],
                }

                outputs = self.model(**inputs)

                loss = outputs[0]
                loss_train_total += loss.item()
                loss.backward()

                torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1.0)

                self.optimizer.step()
                self.scheduler.step()

                progress_bar.set_postfix(
                    {"training_loss": "{:.3f}".format(loss.item() / len(batch))}
                )

            logging.info(f"\nEpoch {epoch}")

            loss_train_avg = loss_train_total / len(self.dataloader_train)
            logging.info(f"Training loss: {loss_train_avg}")

            val_loss, logits, true_vals = self.evaluate()
            logging.info(f"Validation loss: {val_loss}")

            if best_val is None or best_val[0] > val_loss:
                checkpoint_file = f"{self.output_folder}/finetuned_BERT_epoch_{epoch}.model"
                logging.info(f"Saving checkpoint to {checkpoint_file}")
                torch.save(self.model.state_dict(), checkpoint_file)
                if best_val is not None:
                    logging.info(
                        f"New best val_los: {val_loss} - old: {best_val[0]} from epoch {best_val[1]}"
                    )
                    old_checkpoint_file = (
                        f"{self.output_folder}/finetuned_BERT_epoch_{best_val[1]}.model"
                    )
                    logging.info(f"Removing old checkpoint from {old_checkpoint_file}")
                    os.remove(old_checkpoint_file)
                best_val = (val_loss, epoch)

            calculate_performance(logits, true_vals)

            end_time = time.time()

            epoch_mins, epoch_secs = epoch_time(start_time, end_time)
            logging.info(f"Epoch: {epoch + 1:02} | Epoch Time: {epoch_mins}m {epoch_secs}s")
