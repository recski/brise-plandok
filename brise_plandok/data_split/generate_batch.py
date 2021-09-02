import argparse
from brise_plandok.data_split.assignment_loader import load_assignments
from brise_plandok.data_split.sentence_stat import calculate_sentence_counts
from brise_plandok.data_split.doc_tracking_utils import get_next_batch, load_doc_tracking_data
from brise_plandok.data_split.constants import ANNOTATORS, CYCLE_COL, CYCLE_FILE
import logging
import pandas
import os
import itertools


def generate_batch(doc_tracking_file, batch_size, json_folder, cycle_nr, annotators_folder):
    docs = load_doc_tracking_data(doc_tracking_file)
    next_docs = get_next_batch(docs, batch_size)
    logging.info(f"next documents to assign: {next_docs}")
    calculate_sentence_counts(docs, next_docs, json_folder)
    get_cycle(cycle_nr)
    load_assignments(docs, annotators_folder)
    # assign docs to annotators
    # log
    # print sentence stat before & after
    # break if --dry-run
    # generate excels to xls folder
    # copy excels to annotator folders
    # update assigments
    # update dataset
    pass
    # To do
    # - error handling
    # - documentation
    # - logging


def get_cycle(cycle_nr):
    df = pandas.read_csv(filepath_or_buffer=os.path.join(os.path.dirname(
        __file__), CYCLE_FILE), sep=";", dtype=_generate_dtype())
    cycle_df = df[df[CYCLE_COL] == cycle_nr].drop(CYCLE_COL, axis=1)
    _check_if_all_annotators_in_cycle(cycle_df, cycle_nr)
    return cycle_df


def _check_if_all_annotators_in_cycle(df, cycle_nr):
    annotators_from_cycle = set(itertools.chain(*df.values))
    for annotator in ANNOTATORS:
        if annotator not in annotators_from_cycle:
            raise ValueError(
                f"Annotator {annotator} is not in cycle {cycle_nr}.")


def _generate_dtype():
    dtype = {}
    for i in range(len(ANNOTATORS)):
        dtype['annotator_' + str(i+1)] = str
    return dtype


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--dataset-file", type=str)
    parser.add_argument("-s", "--batch-size", type=int)
    parser.add_argument("-jf", "--json-folder", type=str)
    parser.add_argument("-c", "--cycle", type=int)
    parser.add_argument("-af", "--annotators-folder", type=str)
    # parser.add_argument("-xf", "--xlsx-folder", type=str)
    parser.add_argument("-o", "--override", default=False, action="store_true")
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " +
               "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()
    generate_batch(args.dataset_file, args.batch_size,
                   args.json_folder, args.cycle, args.annotators_folder)


if __name__ == "__main__":
    main()
