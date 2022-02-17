import argparse
import os

import pandas
from brise_plandok.annotation_process.utils.assignments import load_assigned_docs_as_df
from brise_plandok.annotation_process.utils.constants import (
    ANNOTATOR_UPLOAD_FOLDER,
    ANNOTATORS,
    ASSIGNMENT_FILE_HEADER,
)
import logging

UPDATED_HEADER = "uploaded"
TRACKING_SHEET = "tracking"
ANNOTATOR_HEADERS = [
    "Document id",
    "Annotator #1",
    "Annotator #2",
    "Ready for review",
    "ann_1_done",
    "ann_2_done",
]


class ProgressTacker:
    def __init__(self, phase):
        self.phase = phase
        if phase == 1:
            ANNOTATOR_HEADERS[3] += " (label)"
            self.ready_for_review_index = 5
        elif phase == 2:
            ANNOTATOR_HEADERS[3] += " (full)"
            self.ready_for_review_index = 14
        else:
            raise ValueError("Phase must be 1 or 2")

    def get_annotator_progress(self, ann_folder):
        uploaded_dict = {}
        for annotator in ANNOTATORS:
            df = load_assigned_docs_as_df(ann_folder, annotator, self.phase)
            uploaded = self._get_uploaded_docs(
                os.path.join(
                    ann_folder,
                    annotator,
                    "phase" + str(self.phase),
                    ANNOTATOR_UPLOAD_FOLDER,
                )
            )
            df[UPDATED_HEADER] = False
            for doc_id in uploaded:
                mask = df[ASSIGNMENT_FILE_HEADER[0]] == doc_id
                df.loc[mask, UPDATED_HEADER] = True
            logging.info(
                f"progress for {annotator}: {len(uploaded)}/{df.shape[0]}"
            )  # pylint: disable=no-member
            uploaded_dict[annotator] = set(uploaded)
        return uploaded_dict

    def get_ready_docs(
        self, doc_tracking_file, uploaded_dict, first, last, only_yes, only_new
    ):
        df = pandas.read_excel(
            doc_tracking_file,
            sheet_name=TRACKING_SHEET,
            dtype={
                ANNOTATOR_HEADERS[0]: str,
                ANNOTATOR_HEADERS[1]: str,
                ANNOTATOR_HEADERS[2]: str,
            },
        )
        first_idx, last_idx = 0, df.shape[0]
        if first:
            first_idx = df.index[df[ANNOTATOR_HEADERS[0]] == first][0]
        if last:
            last_idx = df.index[df[ANNOTATOR_HEADERS[0]] == last][0] + 1
        if only_new:
            df = df[df[ANNOTATOR_HEADERS[3]].isnull()]
        df = df.iloc[first_idx:last_idx, [1, 3, 4, self.ready_for_review_index]]
        df[ANNOTATOR_HEADERS[-2]] = False
        df[ANNOTATOR_HEADERS[-1]] = False
        for _, row in df.iterrows():
            doc_id = row[ANNOTATOR_HEADERS[0]]
            ann_1 = row[ANNOTATOR_HEADERS[1]]
            ann_2 = row[ANNOTATOR_HEADERS[2]]
            ann_1_done = doc_id in uploaded_dict[ann_1]
            ann_2_done = doc_id in uploaded_dict[ann_2]
            mask = df[ANNOTATOR_HEADERS[0]] == doc_id
            if ann_1_done:
                df.loc[mask, ANNOTATOR_HEADERS[-2]] = True
            if ann_2_done:
                df.loc[mask, ANNOTATOR_HEADERS[-1]] = True
            if ann_1_done & ann_2_done:
                df.loc[mask, ANNOTATOR_HEADERS[3]] = "Yes"
        if only_yes:
            df = df[df[ANNOTATOR_HEADERS[3]] == "Yes"]
        logging.info(f"Documents ready for review:\n{df}")
        twice_annotated = df[df[ANNOTATOR_HEADERS[3]] == "Yes"].shape[0]
        once_annotated = df[
            (df[ANNOTATOR_HEADERS[-2]] is True) | (df[ANNOTATOR_HEADERS[-1]] is True)
        ].shape[0]
        logging.info(f"{twice_annotated} documents have been annotated twice")
        logging.info(f"{once_annotated} documents have been annotated once")

    def _get_uploaded_docs(self, dir):
        return [f.split(".")[0] for f in os.listdir(dir)]


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-af", "--annotator-folder", type=str)
    parser.add_argument("-dt", "--doc-tracking", type=str, default=None)
    parser.add_argument("-f", "--first", type=str, default=None)
    parser.add_argument("-l", "--last", type=str, default=None)
    parser.add_argument("-y", "--only-yes", default=False, action="store_true")
    parser.add_argument("-n", "--only-new", default=False, action="store_true")
    parser.add_argument("-p", "--phase", type=int, default=1)
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : "
        + "%(module)s (%(lineno)s) - %(levelname)s - %(message)s",
    )
    args = get_args()
    progress_tracker = ProgressTacker(args.phase)
    uploaded = progress_tracker.get_annotator_progress(args.annotator_folder)
    if args.doc_tracking:
        progress_tracker.get_ready_docs(
            args.doc_tracking,
            uploaded,
            args.first,
            args.last,
            args.only_yes,
            args.only_new,
        )


if __name__ == "__main__":
    main()
