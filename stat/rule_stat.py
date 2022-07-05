import argparse
import os
from statistics import median

from brise_plandok.constants import DocumentFields, SenFields
from brise_plandok.utils import load_json

DATASET_FOLDERS = ["data/train", "data/valid", "data/test"]


def rule_stat(dataset_folders):
    all_sentences_with_rules = 0
    nr_attr_per_rule = []

    for folder in dataset_folders:
        for filename in os.listdir(folder):
            fn = os.path.join(folder, filename)
            doc = load_json(fn)
            for sen in doc[DocumentFields.SENS].values():
                if SenFields.GOLD_MODALITY in sen and sen[SenFields.GOLD_MODALITY] is not None:
                    all_sentences_with_rules += 1
                    nr_attr_per_rule.append(len(sen[SenFields.GOLD_ATTRIBUTES].keys()))
    print_stat(all_sentences_with_rules, nr_attr_per_rule)


def print_stat(all_sentences_with_rules, nr_attr_per_rule):
    print(f"Number of all rules: {all_sentences_with_rules}")
    print(f"Number of all attributes: {sum(nr_attr_per_rule)}")
    print(
        f"Average number of attributes per rule: {sum(nr_attr_per_rule)/len(nr_attr_per_rule):.3f}"
    )
    print(f"Median of number of attributes per rule: {median(nr_attr_per_rule):.0f}")


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--dataset-folders", nargs="+")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    rule_stat(args.dataset_folders)
