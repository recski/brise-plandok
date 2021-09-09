import argparse
import os
from brise_plandok.data_split.utils.assignments import load_assigned_docs_as_df
from brise_plandok.data_split.utils.constants import ANNOTATOR_UPLOAD_FOLDER, ANNOTATORS, ASSIGNMENT_FILE_HEADER, ASSIGNMENT_TXT
import logging
        
UPDATED_HEADER = 'uploaded'

def get_annotator_progress(ann_folder):
    uploaded_dict = {}
    for annotator in ANNOTATORS:
        assignment_file = os.path.join(ann_folder, annotator, ASSIGNMENT_TXT)
        df = load_assigned_docs_as_df(assignment_file)
        uploaded = _get_uploaded_docs(os.path.join(ann_folder, annotator, ANNOTATOR_UPLOAD_FOLDER))
        df[UPDATED_HEADER] = False
        for doc_id in uploaded:
            mask = df[ASSIGNMENT_FILE_HEADER[0]] == doc_id
            df.loc[mask, UPDATED_HEADER] = True
        logging.info(f"progress for {annotator}: {len(uploaded)}/{df.shape[0]}")  # pylint: disable=no-member
        uploaded_dict[annotator] = uploaded
    return uploaded_dict

def get_ready_docs(doc_tracking_file, uploaded):
    
    pass

def _get_uploaded_docs(dir):
    return [f.split('.')[0] for f in os.listdir(dir)]

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-af", "--annotator-folder", type=str)
    parser.add_argument("-dt", "--doc-tracking", type=str, default=None)
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " +
               "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()
    uploaded = get_annotator_progress(args.annotator_folder)
    if args.doc_tracking:
        get_ready_docs(args.doc_tracking, uploaded)


if __name__ == "__main__":
    main()
