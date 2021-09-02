import argparse
import itertools
from brise_plandok.data_split.sentence_stat import sum_sens_for_docs
import os
from brise_plandok.data_split.doc_tracking_utils import load_doc_tracking_data
from brise_plandok.data_split.constants import ANNOTATORS, ASSIGNMENT_FILE, ASSIGNMENT_DF_HEADER, ASSIGNMENT_FILE_HEADER, DOC_HEADER
import logging
import pandas


def load_assignments(docs, annotators_folder):
    df = pandas.DataFrame(columns=ASSIGNMENT_DF_HEADER)
    for annotator in ANNOTATORS:
        df = df.append(_add_assigment_for_annotator(
            annotator, annotators_folder, docs))
    logging.info(f"loaded assignments:\n{df}")
    return df


def _add_assigment_for_annotator(annotator, folder, docs):
    path = os.path.join(folder, annotator, ASSIGNMENT_FILE)
    assigned_docs = list(itertools.chain(*pandas.read_csv(filepath_or_buffer=path, dtype={
        ASSIGNMENT_FILE_HEADER[0]: str}).values))
    sens_nr = sum_sens_for_docs(docs, assigned_docs)
    return pandas.DataFrame([[annotator, sens_nr]], columns=ASSIGNMENT_DF_HEADER)


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--dataset-file", type=str)
    parser.add_argument("-af", "--annotators-folder", type=str)
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " +
               "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()
    docs = load_doc_tracking_data(args.dataset_file)
    load_assignments(docs, args.annotators_folder)


if __name__ == "__main__":
    main()
