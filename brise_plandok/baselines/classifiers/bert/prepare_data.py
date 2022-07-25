from torch.utils.data import DataLoader, RandomSampler, SequentialSampler
from transformers import BertTokenizer

from brise_plandok.baselines.classifiers.bert.bert_constants import (
    BATCH_SIZE,
    BERT_TOKENS_MAX_LEN,
    BERT_NAME,
    TEXT_COLUMN,
)
from brise_plandok.baselines.classifiers.bert.brise_dataset import BriseDataset
from brise_plandok.baselines.utils import get_x_y_dataframes
from brise_plandok.constants import TRAIN, VALID


def create_brise_dataset(train_data, valid_data, labels_train_df, labels_valid_df, tokenizer):
    dataset_train = BriseDataset(
        train_data,
        labels_train_df,
        tokenizer,
        BERT_TOKENS_MAX_LEN,
        TEXT_COLUMN,
    )

    dataset_val = BriseDataset(
        valid_data,
        labels_valid_df,
        tokenizer,
        BERT_TOKENS_MAX_LEN,
        TEXT_COLUMN,
    )

    return dataset_train, dataset_val


def create_data_loaders(dataset_train, dataset_val):
    dataloader_train = DataLoader(
        dataset_train,
        sampler=RandomSampler(dataset_train),
        batch_size=BATCH_SIZE,
    )

    dataloader_validation = DataLoader(
        dataset_val, sampler=SequentialSampler(dataset_val), batch_size=BATCH_SIZE
    )

    return dataloader_train, dataloader_validation


def get_datasets(attributes):
    train_data, _, y_train_all_labels = get_x_y_dataframes(TRAIN)
    valid_data, _, y_valid_all_labels = get_x_y_dataframes(VALID)
    tokenizer = BertTokenizer.from_pretrained(BERT_NAME, do_lower_case=True)
    return create_brise_dataset(
        train_data.iloc[:, :2],
        valid_data.iloc[:, :2],
        y_train_all_labels.filter(attributes),
        y_valid_all_labels.filter(attributes),
        tokenizer,
    )
