import json
import os

import pandas as pd
from brise_plandok.full_attribute_extraction.attribute.potato.constants import GOLD_ATTRIBUTES, GOLD, \
    ANNOTATED_ATTRIBUTES, SEGMENTATION_ERROR, DO_NOT_ANNOTATE, NOT


def _get_attributes(keys):
    return list(set([key for key in keys if key != DO_NOT_ANNOTATE]))


def load_data_to_df(dir_path, only_gold):
    data = []
    for filename in os.listdir(dir_path):
        with open(os.path.join(dir_path, filename), "rt") as f:
            doc = json.load(f)
            if only_gold and not doc[GOLD]:
                continue
            for sen in doc["sens"].values():
                if sen[SEGMENTATION_ERROR]:
                    continue
                if doc[GOLD]:
                    labels = _get_attributes(sen[GOLD_ATTRIBUTES].keys())
                else:
                    labels = _get_attributes(sen[ANNOTATED_ATTRIBUTES].keys())
                data.append({
                    "sen_id": sen["id"],
                    "text": sen["text"],
                    "labels": labels,
                })
    df = pd.DataFrame.from_dict(data)
    return df


def filter_labels(df, labels_to_keep, empty_label):
    df.labels = df.labels.apply(lambda x: [label for label in x if label in labels_to_keep])
    df.labels = df.labels.apply(lambda x: [empty_label] if len(x) == 0 else x)


def get_data_folder_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def get_label_vocab(labels):
    label_vocab = {}
    for i, l in enumerate(labels):
        label_vocab[l] = i
    return label_vocab
