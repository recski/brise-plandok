import argparse
import os
from statistics import mean, median, stdev

from brise_plandok.constants import DocumentFields, SenFields
from brise_plandok.utils import load_json


def rule_stat(dataset_folders):
    all_sentences_with_rules = 0
    nr_sen_per_doc = []
    nr_rule_per_doc = []
    nr_attr_per_rule = []

    for folder in dataset_folders:
        for filename in os.listdir(folder):
            fn = os.path.join(folder, filename)
            doc = load_json(fn)
            rules_in_doc = 0
            sens_in_doc = 0
            for sen in doc[DocumentFields.SENS].values():
                sens_in_doc += 1
                if SenFields.GOLD_MODALITY in sen and sen[SenFields.GOLD_MODALITY] is not None:
                    all_sentences_with_rules += 1
                    rules_in_doc += 1
                    nr_attr_per_rule.append(len(sen[SenFields.GOLD_ATTRIBUTES].keys()))
            nr_rule_per_doc.append(rules_in_doc)
            nr_sen_per_doc.append(sens_in_doc)
    print_stat(all_sentences_with_rules, nr_attr_per_rule, nr_rule_per_doc, nr_sen_per_doc)


def print_stat(all_sentences_with_rules, nr_attr_per_rule, nr_rule_per_doc, nr_sen_per_doc):
    print(f"Number of all rules: {all_sentences_with_rules}")
    print(f"Mean number of rules per document: {mean(nr_rule_per_doc)}")
    print(f"Median number of rules per document: {int(median(nr_rule_per_doc))}")
    print(f"Stdev of rules per document: {stdev(nr_rule_per_doc)}")
    print(f"Mean number of sens per document: {mean(nr_sen_per_doc)}")
    print(f"Median number of sens per document: {int(median(nr_sen_per_doc))}")
    print(f"Stdev of sens per document: {stdev(nr_sen_per_doc)}")
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
