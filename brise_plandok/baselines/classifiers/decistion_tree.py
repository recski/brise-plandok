import argparse

import pandas as pd
from graphviz import Source
from sklearn import tree
from sklearn.metrics import classification_report

from brise_plandok.baselines.constants import ALL_LABELS_SORTED, NOT
from brise_plandok.baselines.utils import get_features_df_path, get_labels_df_path
from brise_plandok.constants import TRAIN, VALID


def run():
    x_train, y_train = get_x_y(TRAIN, ALL_LABELS_SORTED[0])
    x_valid, y_valid = get_x_y(VALID, ALL_LABELS_SORTED[0])
    clf = tree.DecisionTreeClassifier(max_depth=5).fit(x_train, y_train)
    y_pred = clf.predict(x_valid)
    print(
        classification_report(
            y_valid[ALL_LABELS_SORTED[0]], y_pred, target_names=[NOT, ALL_LABELS_SORTED[0]]
        )
    )
    save_graph(clf, x_train.columns.tolist(), [NOT, ALL_LABELS_SORTED[0]])


def save_graph(clf, feature_names, class_names):
    graph = Source(
        tree.export_graphviz(
            clf,
            out_file=None,
            feature_names=feature_names,
            class_names=class_names,
        )
    )
    graph.render(f"../output/{ALL_LABELS_SORTED[0]}", view=False, format="pdf")


def get_x_y(sub_dir, label):
    feats_df = pd.read_csv(get_features_df_path(sub_dir))
    labels_df = pd.read_csv(get_labels_df_path(sub_dir))
    x = feats_df.iloc[:, 2:]
    y = labels_df.loc[:, [label]]
    return x, y


def get_args():
    parser = argparse.ArgumentParser(description="")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    run()
