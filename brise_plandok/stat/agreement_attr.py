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
    # print(kappa_stat["WidmungInMehrerenEbenen"])
    print_stat(kappa_stat, annotator_pairs)


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
        k: v for k, v in sorted(attr_stat.items(), key=lambda item: item[1], reverse=True)
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


def print_stat(kappa_stat, annotator_pairs):
    print("# Annotator agreement - Attributes")
    print("This statistics is calculated without the sentences with a segmentation error.  ")
    print(
        "Only sentences containing a rule (a.k.a. gold_modality != None) are taken into account."
    )
    values = []
    append_header(annotator_pairs, values)
    weights = check_and_append_weights(kappa_stat, values, annotator_pairs)
    for attr, stat in kappa_stat.items():
        row = [attr, "-", "-"]
        for ann_pair, labels in stat.items():
            ann_1_labels = labels[ann_pair[0]]
            ann_2_labels = labels[ann_pair[1]]
            # if ann_1_labels == ann_2_labels:
            #     kappa = 1.0
            # else:
            #     kappa = cohen_kappa_score(ann_1_labels, ann_2_labels, labels=[True, False])
            kappa = cohen_kappa_score(ann_1_labels, ann_2_labels, labels=[True, False])
            row.append(kappa)
        row[1] = numpy.average(row[3:])
        row[2] = numpy.average(row[3:], weights=weights)
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
    row = ["Number of sentences", "-", "-"]
    weights = []
    for ann_pair in annotator_pairs:
        row.append(num_of_sentences[ann_pair])
        weights.append(num_of_sentences[ann_pair])
    values.append(row)
    return weights


def append_header(annotator_pairs, values):
    header = ["Attr", "Macro", "Weighted"]
    for ann_pair in annotator_pairs:
        header.append(ann_pair)
    values.append(header)


def get_args():
    parser = argparse.ArgumentParser(description="")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    calculate_attr_kappa()
