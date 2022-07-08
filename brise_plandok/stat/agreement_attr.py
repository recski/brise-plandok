import argparse
import os
from collections import Counter

import numpy
from sklearn.metrics import cohen_kappa_score

from brise_plandok.constants import (
    DocumentFields,
    SenFields,
    FullAnnotatedAttributeFields,
)
from brise_plandok.stat.constants import (
    DATASET_FOLDERS,
    FIRST_STAGE_IDS,
    PLACEHOLDER,
)
from brise_plandok.stat.utils import (
    make_markdown_table,
    convert_back_post_processed,
    fill_annotated_attributes,
    get_ann_pair,
)
from brise_plandok.utils import load_json


def calculate_attr_kappa():
    kappa_stat = {}
    attr_stat = Counter()
    annotator_pairs = set()
    with open(FIRST_STAGE_IDS) as f:
        first_stage_gold_ids = f.read().splitlines()

    attr_stat, annotator_pairs = collect_all_attributes(attr_stat, annotator_pairs)
    fill_up_kappa_stat(kappa_stat, attr_stat, annotator_pairs)

    for folder in DATASET_FOLDERS:
        for filename in os.listdir(folder):
            fn = os.path.join(folder, filename)
            doc = load_json(fn)
            ann_pair = get_ann_pair(doc)
            for sen in doc[DocumentFields.SENS].values():
                if (
                    not sen[SenFields.SEGMENTATION_ERROR]
                    and sen[SenFields.GOLD_MODALITY] is not None
                ):
                    add_kappa_stat(
                        ann_pair,
                        kappa_stat,
                        attr_stat,
                        doc[DocumentFields.ID],
                        sen,
                        first_stage_gold_ids,
                    )
    print_stat(kappa_stat, annotator_pairs, attr_stat)


def collect_all_attributes(attr_stat, annotator_pairs):
    for folder in DATASET_FOLDERS:
        for filename in os.listdir(folder):
            fn = os.path.join(folder, filename)
            doc = load_json(fn)
            ann_pair = doc[DocumentFields.FULL_ANNOTATORS]
            assert len(ann_pair) == 2
            annotator_pairs.add(tuple(sorted(ann_pair)))
            for sen in doc[DocumentFields.SENS].values():
                full_annotated_attrs = (
                    set(
                        sen[SenFields.FULL_ANNOTATED_ATTRIBUTES][
                            FullAnnotatedAttributeFields.ATTRIBUTES
                        ].keys()
                    )
                    if FullAnnotatedAttributeFields.ATTRIBUTES
                    in sen[SenFields.FULL_ANNOTATED_ATTRIBUTES]
                    else set()
                )
                all_occurring_attributes = convert_back_post_processed(
                    set(sen[SenFields.GOLD_ATTRIBUTES].keys())
                    | set(sen[SenFields.ANNOTATED_ATTRIBUTES].keys())
                    | full_annotated_attrs
                ).difference({PLACEHOLDER})
                for attr in all_occurring_attributes:
                    attr_stat[attr] += 1
    return {
        k: v
        for k, v in sorted(attr_stat.items(), key=lambda item: (item[1], item[0]), reverse=True)
    }, sorted(annotator_pairs)


def fill_up_kappa_stat(kappa_stat, attr_stat, annotator_pairs):
    for attr in attr_stat:
        kappa_stat[attr] = {}
        for ann_pair in annotator_pairs:
            kappa_stat[attr][ann_pair] = {
                ann_pair[0]: [],
                ann_pair[1]: [],
            }


def add_kappa_stat(ann_pair, kappa_stat, attr_stat, doc_id, sen, first_stage_gold_ids):
    ann_attrs = {
        ann_pair[0]: set(),
        ann_pair[1]: set(),
    }
    fill_annotated_attributes(ann_attrs, doc_id, first_stage_gold_ids, sen)
    for attr in attr_stat.keys():
        kappa_stat[attr][ann_pair][ann_pair[0]].append(attr in ann_attrs[ann_pair[0]])
        kappa_stat[attr][ann_pair][ann_pair[1]].append(attr in ann_attrs[ann_pair[1]])


def print_stat(kappa_stat, annotator_pairs, attr_stat):
    print("# Annotator agreement - Attributes")
    print(
        "This statistics is calculated without the sentences with a segmentation error.  \n"
        "Only sentences containing a rule (a.k.a. gold_modality != None) are taken into account.  \n"
        "We use Cohen's kappa for calculating the inter-annotator agreement: "
        "[cohen_kappa_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html).  \n"
        "Frequencies are calculated as the number of sentences where the attribute appears as either gold or annotated "
        "either in the first or in the second phase."
    )
    print("## Without kappa correction")
    calculate_table(annotator_pairs, kappa_stat, attr_stat)
    print("## With kappa correction")
    print(
        "[cohen_kappa_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html) "
        "results in `nan` if both vectors are uniform and the same."
    )
    print(
        "In the table below, we substituted these `nan` values by the value of complete agreement (1.0)."
    )
    calculate_table(annotator_pairs, kappa_stat, attr_stat, correct_uniform_agreement=True)


def calculate_table(annotator_pairs, kappa_stat, attr_stat, correct_uniform_agreement=False):
    values = []
    append_header(annotator_pairs, values)
    num_of_sentences = check_and_append_weights(kappa_stat, values, annotator_pairs)
    for attr, stat in kappa_stat.items():
        row = [attr, attr_stat[attr], "-", "-"]
        non_nan_kappas = []
        non_nan_weights = []
        for ann_pair, labels in stat.items():
            ann_1_labels = labels[ann_pair[0]]
            ann_2_labels = labels[ann_pair[1]]
            if correct_uniform_agreement:
                if ann_1_labels == ann_2_labels:
                    kappa = 1.0
                else:
                    kappa = cohen_kappa_score(ann_1_labels, ann_2_labels, labels=[True, False])
            else:
                kappa = cohen_kappa_score(ann_1_labels, ann_2_labels, labels=[True, False])
            if not numpy.isnan(kappa):
                non_nan_kappas.append(kappa)
                non_nan_weights.append(num_of_sentences[ann_pair])
            row.append(kappa)
        if len(non_nan_kappas) > 0:
            row[2] = numpy.average(non_nan_kappas)
        else:
            row[2] = numpy.nan
        if len(non_nan_kappas) > 1:
            row[3] = numpy.average(non_nan_kappas, weights=non_nan_weights)
        else:
            row[3] = numpy.nan
        values.append(row)
    print(make_markdown_table(values))


def check_and_append_weights(kappa_stat, values, annotator_pairs):
    num_of_sentences = {}
    for attr, stat in kappa_stat.items():
        for ann_pair, labels in stat.items():
            assert len(labels[ann_pair[0]]) == len(labels[ann_pair[1]])
            if ann_pair not in num_of_sentences:
                num_of_sentences[ann_pair] = len(labels[ann_pair[0]])
            else:
                assert num_of_sentences[ann_pair] == len(labels[ann_pair[0]])
    row = ["Number of sentences", "-", "-", "-"]
    for ann_pair in annotator_pairs:
        row.append(num_of_sentences[ann_pair])
    values.append(row)
    return num_of_sentences


def append_header(annotator_pairs, values):
    header = ["Attr", "Freq", "Macro", "Weighted"]
    for ann_pair in annotator_pairs:
        header.append(ann_pair)
    values.append(header)


def get_args():
    parser = argparse.ArgumentParser(description="")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    numpy.seterr(divide="ignore", invalid="ignore")
    calculate_attr_kappa()
