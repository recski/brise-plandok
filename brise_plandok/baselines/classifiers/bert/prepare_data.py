from torch.utils.data import DataLoader, RandomSampler
from transformers import BertTokenizer

from brise_plandok.baselines.classifiers.bert.bert_constants import (
    BATCH_SIZE,
    BERT_TOKENS_MAX_LEN,
    BERT_NAME,
    TEXT_COLUMN,
)
from brise_plandok.baselines.classifiers.bert.brise_dataset import BriseDataset
from brise_plandok.baselines.utils import get_x_y_dataframes


def create_data_loader(dataset_name, attributes):
    x, y = load_dataset(dataset_name, attributes)
    dataset = create_brise_dataset(x, y)
    return DataLoader(
        dataset,
        sampler=RandomSampler(dataset),
        batch_size=BATCH_SIZE,
    )


def load_dataset(dataset_name, attributes):
    data, _, labels = get_x_y_dataframes(dataset_name)
    return data.iloc[:, :2], labels.filter(attributes)


def create_brise_dataset(x, y):
    tokenizer = BertTokenizer.from_pretrained(BERT_NAME, do_lower_case=True)
    return BriseDataset(
        x,
        y,
        tokenizer,
        BERT_TOKENS_MAX_LEN,
        TEXT_COLUMN,
    )
