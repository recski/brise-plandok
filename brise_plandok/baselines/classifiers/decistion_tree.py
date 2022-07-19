import argparse
import os.path
from ast import literal_eval

import pandas as pd
from graphviz import Source
from sklearn import tree
from sklearn.metrics import classification_report
from tuw_nlp.common.eval import get_cat_stats, print_cat_stats

from brise_plandok.baselines.constants import ALL_LABELS_SORTED, NOT
from brise_plandok.baselines.utils import get_features_df_path, get_labels_df_path, get_output_dir
from brise_plandok.constants import TRAIN, VALID

MAX_DEPTH = 5
TOP = 40


def run():
    print("# Decision tree classifier - report")
    print(f"Run for the top {TOP} attributes with max depth: {MAX_DEPTH}.")
    x_train_df, y_train_df, x_train = get_x_y_dataframes(TRAIN)
    x_valid_df, y_valid_df, x_valid = get_x_y_dataframes(VALID)
    golds = y_valid_df.Labels.tolist()
    golds = filter_gold(golds)
    preds = [set() for i in range(len(golds))]
    for label in ALL_LABELS_SORTED[:TOP]:
        print(f"## {label}")
        print("```bash")
        y_train = y_train_df.loc[:, [label]]
        y_valid = y_valid_df.loc[:, [label]]
        clf = tree.DecisionTreeClassifier(max_depth=MAX_DEPTH, random_state=42).fit(
            x_train, y_train
        )
        y_pred = clf.predict(x_valid)
        for i, pred in enumerate(y_pred):
            if pred > 0.5:
                preds[i].add(label)
        print(classification_report(y_valid[label], y_pred, target_names=[NOT, label]))
        print("```")
        save_graph(clf, x_train.columns.tolist(), [NOT, label], label)
    print("## Summary")
    print_cat_stats(get_cat_stats(preds, golds))


def filter_gold(golds):
    top_attrs = set(ALL_LABELS_SORTED[:TOP])
    golds = [set(gold) & top_attrs for gold in golds]
    return golds


def save_graph(clf, feature_names, class_names, label):
    graph = Source(
        tree.export_graphviz(
            clf,
            out_file=None,
            feature_names=feature_names,
            class_names=class_names,
        )
    )
    graph.render(os.path.join(get_output_dir("decision_tree"), label), view=False, format="pdf")


def get_x_y_dataframes(sub_dir):
    feats_df = pd.read_csv(get_features_df_path(sub_dir))
    labels_df = pd.read_csv(get_labels_df_path(sub_dir), converters={"Labels": literal_eval})
    return feats_df, labels_df, feats_df.iloc[:, 2:]


def get_x_y(x_df, y_df, label):
    x = x_df.iloc[:, 2:]
    y = y_df.loc[:, [label]]
    return x, y


def get_args():
    parser = argparse.ArgumentParser(description="")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    run()
