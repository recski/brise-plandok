import argparse
import os

import pandas
from brise_plandok.data_split.utils.assignments import load_assigned_docs_as_df
from brise_plandok.data_split.utils.constants import ANNOTATOR_UPLOAD_FOLDER, ANNOTATORS, ASSIGNMENT_FILE_HEADER, ASSIGNMENT_TXT
import logging

UPDATED_HEADER = 'uploaded'
TRACKING_SHEET = 'tracking'
ANNOTATOR_HEADERS = ["Document id", "Annotator #1",
                     "Annotator #2", "Ready for review", 
                     "ann_1_done", "ann_2_done"]


def get_annotator_progress(ann_folder):
    uploaded_dict = {}
    for annotator in ANNOTATORS:
        assignment_file = os.path.join(ann_folder, annotator, ASSIGNMENT_TXT)
        df = load_assigned_docs_as_df(assignment_file)
        uploaded = _get_uploaded_docs(os.path.join(
            ann_folder, annotator, ANNOTATOR_UPLOAD_FOLDER))
        df[UPDATED_HEADER] = False
        for doc_id in uploaded:
            mask = df[ASSIGNMENT_FILE_HEADER[0]] == doc_id
            df.loc[mask, UPDATED_HEADER] = True
        logging.info(
            f"progress for {annotator}: {len(uploaded)}/{df.shape[0]}")  # pylint: disable=no-member
        uploaded_dict[annotator] = set(uploaded)
    return uploaded_dict


def get_ready_docs(doc_tracking_file, uploaded_dict, first, last):
    df = pandas.read_excel(doc_tracking_file, sheet_name=TRACKING_SHEET,
                           dtype={
                               ANNOTATOR_HEADERS[0]: str,
                               ANNOTATOR_HEADERS[1]: str,
                               ANNOTATOR_HEADERS[2]: str,
                           })
    first_idx, last_idx = 0, df.shape[0]
    if first:
        first_idx = df.index[df[ANNOTATOR_HEADERS[0]] == first][0]
    if last:
        last_idx = df.index[df[ANNOTATOR_HEADERS[0]] == last][0]
    df = df.iloc[first_idx:last_idx, [0, 2, 3, 4]]
    df = df.loc[df[ANNOTATOR_HEADERS[3]].isnull(), :]
    df[ANNOTATOR_HEADERS[-2]] = False
    df[ANNOTATOR_HEADERS[-1]] = False
    for i, row in df.iterrows():
        doc_id = row[ANNOTATOR_HEADERS[0]]
        ann_1 = row[ANNOTATOR_HEADERS[1]]
        ann_2 = row[ANNOTATOR_HEADERS[2]]
        ann_1_done = doc_id in uploaded_dict[ann_1]
        ann_2_done = doc_id in uploaded_dict[ann_2]
        if ann_1_done:
            df.iloc[i, [-2]] = True
        if ann_2_done:
            df.iloc[i, [-1]] = True
        if ann_1_done & ann_2_done:
            df.iloc[i, [-3]] = "Yes"
    logging.info(f"Documents ready for review:\n{df}")


def _get_uploaded_docs(dir):
    return [f.split('.')[0] for f in os.listdir(dir)]


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-af", "--annotator-folder", type=str)
    parser.add_argument("-dt", "--doc-tracking", type=str, default=None)
    parser.add_argument("-f", "--first", type=str, default=None)
    parser.add_argument("-l", "--last", type=str, default=None)
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " +
               "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()
    uploaded = get_annotator_progress(args.annotator_folder)
    if args.doc_tracking:
        get_ready_docs(args.doc_tracking, uploaded, args.first, args.last)


if __name__ == "__main__":
    main()
