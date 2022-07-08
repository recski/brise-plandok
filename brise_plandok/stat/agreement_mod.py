import argparse
import os
import statistics

import numpy
from sklearn.metrics import cohen_kappa_score

from brise_plandok.constants import (
    DocumentFields,
    SenFields,
    FullAnnotatedAttributeFields,
    AnnotatedAttributeFields,
    EMPTY,
)
from brise_plandok.stat.constants import (
    DATASET_FOLDERS,
    MACRO,
)
from brise_plandok.stat.utils import make_markdown_table
from brise_plandok.utils import load_json


def calculate_mod_kappa():
    kappa_stat = {}
    for folder in DATASET_FOLDERS:
        for filename in os.listdir(folder):
            fn = os.path.join(folder, filename)
            doc = load_json(fn)
            ann_pair = tuple(
                sorted(
                    [
                        (doc[DocumentFields.FULL_ANNOTATORS][0]),
                        (doc[DocumentFields.FULL_ANNOTATORS][1]),
                    ]
                )
            )
            add_ann_pair_if_not_present(kappa_stat, ann_pair)
            for sen in doc[DocumentFields.SENS].values():
                if not sen[SenFields.SEGMENTATION_ERROR]:
                    add_kappa_stat(
                        ann_pair,
                        kappa_stat,
                        sen,
                    )
    kappa_stat = sort_map(kappa_stat)
    print_stat(kappa_stat)


def sort_map(kappa_stat):
    return {k: v for k, v in sorted(kappa_stat.items(), key=lambda item: item[0])}


def add_ann_pair_if_not_present(kappa_stat, ann_pair):
    assert len(ann_pair) == 2
    if ann_pair not in kappa_stat:
        kappa_stat[ann_pair] = {
            ann_pair[0]: [],
            ann_pair[1]: [],
        }


def add_kappa_stat(ann_pair, kappa_stat, sen):
    gold_mod = sen[SenFields.GOLD_MODALITY]
    if gold_mod is None:
        return
    ann_modalities = {
        ann_pair[0]: EMPTY,
        ann_pair[1]: EMPTY,
    }
    if FullAnnotatedAttributeFields.MODALITY in sen[SenFields.FULL_ANNOTATED_ATTRIBUTES]:
        for mod, annotators in sen[SenFields.FULL_ANNOTATED_ATTRIBUTES][
            FullAnnotatedAttributeFields.MODALITY
        ].items():
            for ann in annotators[AnnotatedAttributeFields.ANNOTATORS]:
                assert ann_modalities[ann] == EMPTY
                ann_modalities[ann] = mod
    for ann, mod in ann_modalities.items():
        assert mod is not None
        kappa_stat[ann_pair][ann].append(mod)


def print_stat(kappa_stat):
    print("# Annotator agreement - Modality")
    print("This statistics is calculated without the sentences with a segmentation error.  ")
    print(
        "Only sentences containing a rule (a.k.a. gold_modality != None) are taken into account."
    )
    kappas = []
    weights = []
    values = [["Annotator pair", "Kappa", "Number of sentences"]]
    for ann_pair, ann_pair_stat in kappa_stat.items():
        ann_1_labels = ann_pair_stat[ann_pair[0]]
        ann_2_labels = ann_pair_stat[ann_pair[1]]
        assert len(ann_1_labels) == len(ann_2_labels)
        number_of_sens = len(ann_1_labels)
        kappa = cohen_kappa_score(ann_1_labels, ann_pair_stat[ann_pair[1]])
        kappas.append(kappa)
        weights.append(number_of_sens)
        values.append([ann_pair, kappa, number_of_sens])
    values.append([MACRO, statistics.mean(kappas), "-"])
    values.append(["weighted", numpy.average(a=kappas, weights=weights), "-"])
    print(make_markdown_table(values))


def get_args():
    parser = argparse.ArgumentParser(description="")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    calculate_mod_kappa()
