import argparse
from brise_plandok.data_split.utils.assignments import load_assigned_docs_as_list
from brise_plandok.data_split.utils.constants import ANNOTATORS, ASSIGNMENT_DF_HEADER, ASSIGNMENT_FILE, ASSIGNMENT_FILE_HEADER
from brise_plandok.data_split.utils.sentences import sum_sens_for_docs
from brise_plandok.data_split.utils.doc_tracking import load_doc_tracking_data
import os
import logging
import pandas


def load_assignments(docs, annotators_folder):
    df = pandas.DataFrame(columns=ASSIGNMENT_DF_HEADER)
    for annotator in ANNOTATORS:
        df = df.append(_add_assigment_for_annotator(
            annotator, annotators_folder, docs), ignore_index=True)
    logging.info(f"loaded assignments:\n{df}")
    return df


def _add_assigment_for_annotator(annotator, folder, docs):
    path = os.path.join(folder, annotator, ASSIGNMENT_FILE)
    assigned_docs = load_assigned_docs_as_list(path)
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
