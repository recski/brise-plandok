import logging
import os
import random
from ast import literal_eval

import numpy as np
import pandas as pd
import torch
from sklearn.metrics import classification_report

from brise_plandok.baselines.constants import (
    ALL_LABELS_SORTED,
    THRESHOLD,
    LOWER,
    UPPER,
    NOT,
)


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
    return feats_df, feats_df.iloc[:, 2:], labels_df


def get_x_y(x_df, y_df, label):
    x = x_df.iloc[:, 2:]
    y = y_df.loc[:, [label]]
    return x, y


def get_attributes_for_experiment(top, min_freq):
    freq_filtered = [attr for attr, freq in ALL_LABELS_SORTED.items() if freq >= min_freq]
    return freq_filtered[:top]


def calculate_loss_weights(label_df):
    return label_df.sum().max() / label_df.sum()


def sigmoid(X):
    return 1 / (1 + np.exp(-X))


def calculate_performance(logits, y_true, attributes):
    target_names = [NOT] + attributes if len(attributes) == 1 else attributes
    probs = sigmoid(logits)
    y_pred = np.where(probs < THRESHOLD, LOWER, UPPER)
    logging.info(classification_report(y_true, y_pred, target_names=target_names))


def epoch_time(start_time, end_time):
    elapsed_time = end_time - start_time
    elapsed_mins = int(elapsed_time / 60)
    elapsed_secs = int(elapsed_time - (elapsed_mins * 60))
    return elapsed_mins, elapsed_secs


def fix_random():
    seed_val = 17
    random.seed(seed_val)
    np.random.seed(seed_val)
    torch.manual_seed(seed_val)
    torch.cuda.manual_seed_all(seed_val)
