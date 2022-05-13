import argparse
import os

from brise_plandok import logger
from brise_plandok.annotation_process.utils.assignments import load_assigned_docs_as_df
from brise_plandok.annotation_process.utils.constants import (
    ANNOTATOR_UPLOAD_FOLDER,
    ANNOTATORS,
    ASSIGNMENT_FILE_HEADER,
    DOC_HEADER,
)
from brise_plandok.annotation_process.utils.doc_tracking import load_doc_tracking_data

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
            logger.info(f"progress for {annotator}: {len(uploaded)}/{df.shape[0]}")
            uploaded_dict[annotator] = set(uploaded)
        return uploaded_dict

    def get_ready_docs(self, doc_tracking_file, uploaded_dict):
        assigned_col = DOC_HEADER[2] if self.phase == 1 else DOC_HEADER[7]
        df = load_doc_tracking_data(doc_tracking_file)
        df[DOC_HEADER[8]] = False
        df[DOC_HEADER[9]] = False
        df[DOC_HEADER[10]] = False
        for _, row in df.iterrows():
            doc_id = row[DOC_HEADER[1]]
            ann_1 = row[DOC_HEADER[5]]
            ann_2 = row[DOC_HEADER[6]]
            if not row[assigned_col]:
                continue
            ann_1_done = doc_id in uploaded_dict[ann_1]
            ann_2_done = doc_id in uploaded_dict[ann_2]
            mask = df[DOC_HEADER[1]] == doc_id
            if ann_1_done:
                df.loc[mask, DOC_HEADER[8]] = True
            if ann_2_done:
                df.loc[mask, DOC_HEADER[9]] = True
            if ann_1_done and ann_2_done:
                df.loc[mask, DOC_HEADER[10]] = True
        logger.info(f"Documents ready for review:\n{df}")
        once_annotated = df[(df[DOC_HEADER[8]] == True) | (df[DOC_HEADER[9]] == True)].shape[0]
        twice_annotated = df[(df[DOC_HEADER[10]] == True)].shape[0]
        logger.info(f"{twice_annotated} documents have been annotated twice")
        logger.info(f"{once_annotated} documents have been annotated once")

    def _get_uploaded_docs(self, dir):
        return [f.split(".")[0] for f in os.listdir(dir)]


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-af", "--annotator-folder", type=str)
    parser.add_argument("-dt", "--doc-tracking", type=str, default=None)
    parser.add_argument("-p", "--phase", type=int, default=1)
    return parser.parse_args()


def main():
    args = get_args()
    progress_tracker = ProgressTacker(args.phase)
    uploaded = progress_tracker.get_annotator_progress(args.annotator_folder)
    if args.doc_tracking:
        progress_tracker.get_ready_docs(
            args.doc_tracking,
            uploaded,
        )


if __name__ == "__main__":
    main()
