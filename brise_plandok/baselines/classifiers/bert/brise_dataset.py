import pandas as pd
import torch
from torch.utils.data import Dataset
from transformers import BertTokenizer


class BriseDataset(Dataset):
    def __init__(
        self,
        data: pd.DataFrame,
        labels: pd.DataFrame,
        tokenizer: BertTokenizer,
        max_length: int,
        text_column: str,
    ):
        self.tokenizer = tokenizer
        self.data = data
        self.labels = labels
        self.max_length = max_length
        self.text_column = text_column
        assert len(data) == len(labels)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index: int):
        text = self.data.iloc[index][self.text_column]
        labels = self.labels.iloc[index]

        encoding = self.tokenizer(
            text,
            padding="max_length",
            max_length=self.max_length,
            return_tensors="pt",
        )

        return dict(
            text=text,
            input_ids=encoding["input_ids"].flatten(),
            attention_mask=encoding["attention_mask"].flatten(),
            labels=torch.FloatTensor(labels),
        )
