import json
import os

import pandas as pd
from xpotato.dataset.dataset import Dataset

from brise_plandok.full_attribute_extraction.attribute.potato.constants import (
    NOT,
)
from brise_plandok.full_attribute_extraction.attribute.utils.get_vocab import (
    get_vocab_for_all_attributes,
)
from brise_plandok.full_attribute_extraction.attribute.utils.load_data import append_doc_to_data


def create_potato_dataset_for_doc(doc, graph_format="fourlang"):
    data = []
    append_doc_to_data(data, doc, labels_present=False)
    df = pd.DataFrame.from_dict(data)
    sen_ids = df.sen_id
    dataset = create_potato_dataset(df, graph_format)
    add_graphs_to_dataset(dataset, graph_format)
    return dataset, sen_ids


def create_potato_dataset(df, cache_dir=None):
    return Dataset(
        _get_sentences(df),
        label_vocab=get_vocab_for_all_attributes(),
        lang="de",
        cache_dir=cache_dir,
    )


def _get_sentences(df):
    df_with_nots = df[["text"]]
    df_with_nots.loc[:, "dummy_label"] = NOT
    return df_with_nots.to_records(index=False).tolist()


def add_graphs_to_dataset(dataset, graph_format="fourlang"):
    dataset.set_graphs(dataset.parse_graphs(graph_format=graph_format))


def filter_labels(df, labels_to_keep, empty_label):
    df.labels = df.labels.apply(lambda x: [label for label in x if label in labels_to_keep])
    df.labels = df.labels.apply(lambda x: [empty_label] if len(x) == 0 else x)


def get_data_folder_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def load_features(attributes=None):
    features = []
    features_path = _get_manual_feature_folder_path()
    for filename in os.listdir(features_path):
        if not filename.endswith(".json"):
            continue
        if attributes is None or filename.split(".")[0] in attributes:
            with open(os.path.join(features_path, filename)) as f:
                rules = json.load(f)
                for attr_name in rules:
                    for rule in rules[attr_name]:
                        features.append(rule)
    return features


def _get_manual_feature_folder_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "features", "manual")
