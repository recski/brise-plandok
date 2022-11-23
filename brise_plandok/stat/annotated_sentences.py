import argparse
import os
from collections import Counter

import numpy
from brise_plandok.constants import DocumentFields
from brise_plandok.utils import load_json

DOCS = "docs"
SENS = "sens"

PRACTICE_DOCS = [
    "7374",
    "7857",
    "7990",
    "8065",
    "8250",
]


def calc_annotated_sentences(data_dir):
    stat = {
        DocumentFields.FULL_ANNOTATORS: {
            DOCS: Counter(),
            SENS: Counter(),
        },
        DocumentFields.ANNOTATORS: {
            DOCS: Counter(),
            SENS: Counter(),
        },
    }
    for doc_fn in os.listdir(data_dir):
        if doc_fn.split(".")[0] in PRACTICE_DOCS:
            continue
        doc_path = os.path.join(data_dir, doc_fn)
        doc = load_json(doc_path)
        nr_sens = len(doc[DocumentFields.SENS])
        add_to_stat(doc, nr_sens, stat, DocumentFields.ANNOTATORS)
        add_to_stat(doc, nr_sens, stat, DocumentFields.FULL_ANNOTATORS)
    stat = sort_map(stat)
    print_stat(stat)


def add_to_stat(doc, nr_sens, stat, phase):
    if phase in doc and doc[phase] is not None:
        for ann in doc[phase]:
            stat[phase][SENS][ann] += nr_sens
            stat[phase][DOCS][ann] += 1


def sort_map(stat):
    stat = {k: v for k, v in sorted(stat.items(), key=lambda item: item[0])}
    for phase, phase_stat in stat.items():
        for stat_type, ann_stat in phase_stat.items():
            stat[phase][stat_type] = {
                k: v for k, v in sorted(ann_stat.items(), key=lambda item: item[0])
            }
    return stat


def print_stat(stat):
    print("# Number of annotated sentences\n")
    print_phase(stat[DocumentFields.ANNOTATORS], "Label")
    print_phase(stat[DocumentFields.FULL_ANNOTATORS], "Full")


def print_phase(stat, name):
    print(f"## {name} annotation\n\n```bash")
    agg_docs = []
    agg_sens = []
    for ann in stat[DOCS].keys():
        agg_docs.append(stat[DOCS][ann])
        agg_sens.append(stat[SENS][ann])
        print(f"Annotator {ann}:\n" f"# docs: {stat[DOCS][ann]}\n" f"# sens: {stat[SENS][ann]}\n")
    print(
        f"Docs agg\n" f"avg: {numpy.average(agg_docs):.2f}\n" f"std: {numpy.std(agg_docs):.2f}\n"
    )
    print(
        f"Sens agg\n" f"avg: {numpy.average(agg_sens):.2f}\n" f"std: {numpy.std(agg_sens):.2f}\n"
    )
    print("```")


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--data-folder", help="Path to all annotated documents.")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    calc_annotated_sentences(args.data_folder)
