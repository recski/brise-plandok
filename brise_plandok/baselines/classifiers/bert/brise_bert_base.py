import logging
import os

import numpy as np
import torch

from brise_plandok.baselines.classifiers.bert.bert_constants import BERT_NAME
from brise_plandok.baselines.classifiers.bert.brise_bert_model import BriseBertClassification
from brise_plandok.baselines.classifiers.bert.prepare_data import create_data_loader
from brise_plandok.baselines.constants import RULE_BASED_ATTRIBUTES
from brise_plandok.baselines.utils import (
    fix_random,
)


class BriseBertBase:
    def __init__(self, attribute, test_dataset):
        self.device = torch.device("cpu")
        self.set_gpu()
        fix_random()

        self.attributes = RULE_BASED_ATTRIBUTES if attribute is None else [attribute]
        logging.info(f"attributes to train: {self.attributes}")

        self.model = BriseBertClassification.from_pretrained(
            BERT_NAME,
            num_labels=len(self.attributes),
        )

        self.dataloader_test = create_data_loader(test_dataset, self.attributes)

    def set_gpu(self):
        cuda_available = torch.cuda.is_available()
        logging.info(f"Cuda available: {cuda_available}")
        if cuda_available:
            logging.info(f'GPU is set to {os.environ["CUDA_VISIBLE_DEVICES"]}')
            self.device = torch.device("cuda")

    def evaluate(self):
        self.model.eval()

        loss_val_total = 0
        predictions, true_vals, ids = [], [], []

        for batch in self.dataloader_test:

            ids += batch["id"]

            batch = tuple(
                b.to(self.device) for key, b in batch.items() if key != "text" and key != "id"
            )

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

        loss_val_avg = loss_val_total / len(self.dataloader_test)

        predictions = np.concatenate(predictions, axis=0)
        true_vals = np.concatenate(true_vals, axis=0)

        return loss_val_avg, predictions, true_vals, ids
