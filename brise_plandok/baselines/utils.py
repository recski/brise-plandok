import os
from ast import literal_eval

import pandas as pd
from brise_plandok.baselines.constants import ALL_LABELS_SORTED


def get_labels_df_path(sub_dir):
    return os.path.join(os.path.dirname(__file__), "input", f"{sub_dir}_labels.csv")


def get_features_df_path(sub_dir):
    return os.path.join(os.path.dirname(__file__), "input", f"{sub_dir}_features.csv")


def get_data_df_path(sub_dir):
    return os.path.join(os.path.dirname(__file__), "input", f"{sub_dir}_data.csv")


def get_output_dir(classifier):
    output_dir = os.path.join(os.path.dirname(__file__), "output", classifier)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir


def filter_gold(golds, labels):
    relevant_attrs = set(labels)
    golds = [set(gold) & relevant_attrs for gold in golds]
    return golds


def get_x_y_dataframes(sub_dir):
    feats_df = pd.read_csv(get_features_df_path(sub_dir))
    labels_df = pd.read_csv(get_labels_df_path(sub_dir), converters={"Labels": literal_eval})
    return feats_df, labels_df, feats_df.iloc[:, 2:]


def get_x_y(x_df, y_df, label):
    x = x_df.iloc[:, 2:]
    y = y_df.loc[:, [label]]
    return x, y


def get_attributes_for_experiment(top, min_freq):
    freq_filtered = [attr for attr, freq in ALL_LABELS_SORTED.items() if freq >= min_freq]
    return freq_filtered[:top]
