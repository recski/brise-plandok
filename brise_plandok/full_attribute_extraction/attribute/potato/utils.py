import inspect
import json
import os

import pandas as pd
from xpotato.dataset.dataset import Dataset

from brise_plandok.constants import AttributesNames
from brise_plandok.full_attribute_extraction.attribute.potato.constants import (
    GOLD_ATTRIBUTES,
    GOLD,
    ANNOTATED_ATTRIBUTES,
    SEGMENTATION_ERROR,
    DO_NOT_ANNOTATE,
    NOT,
)


def _get_attributes(keys):
    return list(set([key for key in keys if key != DO_NOT_ANNOTATE]))


def load_data_to_df(dir_path, only_gold):
    data = []
    for filename in os.listdir(dir_path):
        with open(os.path.join(dir_path, filename), "rt") as f:
            doc = json.load(f)
            if only_gold and not doc[GOLD]:
                continue
            doc_to_df(data, doc)
    df = pd.DataFrame.from_dict(data)
    return df


def doc_to_df(data, doc, labels_present=True):
    for sen in doc["sens"].values():
        if sen[SEGMENTATION_ERROR]:
            continue
        labels = None
        if labels_present:
            if doc[GOLD]:
                labels = _get_attributes(sen[GOLD_ATTRIBUTES].keys())
            else:
                labels = _get_attributes(sen[ANNOTATED_ATTRIBUTES].keys())
        data.append(
            {
                "sen_id": sen["id"],
                "text": sen["text"],
                "labels": labels,
            }
        )


def filter_labels(df, labels_to_keep, empty_label):
    df.labels = df.labels.apply(lambda x: [label for label in x if label in labels_to_keep])
    df.labels = df.labels.apply(lambda x: [empty_label] if len(x) == 0 else x)


def get_data_folder_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def get_manual_feature_folder_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "features", "manual")


def get_label_vocab(labels):
    label_vocab = {}
    for i, l in enumerate(labels):
        label_vocab[l] = i
    return label_vocab


def gen_all_attributes_names():
    for i in inspect.getmembers(AttributesNames()):
        if not i[0].startswith("_"):
            if not inspect.ismethod(i[1]):
                yield i[1]


def get_vocab_for_all_attributes():
    all_attribute_names = [NOT] + [attr_name for attr_name in gen_all_attributes_names()]
    return get_label_vocab(all_attribute_names)


def get_all_manual_features():
    all_features = []
    manual_features_path = get_manual_feature_folder_path()
    for filename in os.listdir(manual_features_path):
        if not filename.endswith(".json"):
            continue
        with open(os.path.join(manual_features_path, filename)) as f:
            rules = json.load(f)
            for attr_name in rules:
                for rule in rules[attr_name]:
                    all_features.append(rule)
    return all_features


def create_potato_dataset(doc):
    data = []
    doc_to_df(data, doc, labels_present=False)
    df = pd.DataFrame.from_dict(data)
    sen_ids = df.sen_id
    dataset = Dataset(get_sentences(df), label_vocab=get_vocab_for_all_attributes(), lang="de")
    dataset.set_graphs(dataset.parse_graphs(graph_format="fourlang"))
    return dataset, sen_ids


def get_sentences(df):
    df_with_nots = df[["text"]]
    df_with_nots.loc[:, "dummy_label"] = NOT
    return df_with_nots.to_records(index=False)
