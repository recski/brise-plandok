import argparse
import os

from tuw_nlp.common.eval import get_cat_stats, print_cat_stats

from brise_plandok.baselines.classifiers.bert.brise_bert_evaluator import BriseBertEvaluator
from brise_plandok.baselines.utils import (
    get_x_y_dataframes,
    get_y_pred,
    filter_gold_dict,
)


def evaluate_per_attribute(log_folder, dataset_name):
    attributes = []
    for attr_log_folder in os.listdir(log_folder):
        attributes.append(attr_log_folder.split("_")[-1])
    _, x_valid, y_valid_all_labels = get_x_y_dataframes(dataset_name)

    golds = dict(zip(y_valid_all_labels.ID, y_valid_all_labels.Labels.tolist()))
    golds = filter_gold_dict(golds, attributes)
    preds = {k: set() for k in golds.keys()}

    for attr_log_folder in os.listdir(log_folder):
        attribute = attr_log_folder.split("_")[-1]
        for fn in os.listdir(os.path.join(log_folder, attr_log_folder)):
            if fn.endswith(".model"):
                evaluator = BriseBertEvaluator(
                    attribute, dataset_name, os.path.join(log_folder, attr_log_folder, fn)
                )
                _, logits, true_vals, ids = evaluator.evaluate()
                _, y_pred = get_y_pred(evaluator.attributes, logits)
                for i, pred in enumerate(y_pred[:, 0]):
                    if pred > 0.5:
                        preds[ids[i]].add(attribute)

    print_cat_stats(get_cat_stats(preds.values(), golds.values()))


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--log-folder", help="Path to the log folder.")
    parser.add_argument(
        "-d", "--dataset-name", help="Name of the dataset to test on, one of {train, valid, test}"
    )
    parser.add_argument(
        "-all", action="store_true", help="Set this flag if you evaluate for a joint model."
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    if args.all:
        pass
    else:
        evaluate_per_attribute(args.log_folder, args.dataset_name)
