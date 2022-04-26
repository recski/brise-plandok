import argparse

import pandas

from brise_plandok import logger
from brise_plandok.annotation_process.utils.assignments import (
    get_assignment_header,
    load_assigned_docs_as_list,
)
from brise_plandok.annotation_process.utils.constants import (
    ANNOTATORS,
)
from brise_plandok.annotation_process.utils.doc_tracking import load_doc_tracking_data
from brise_plandok.annotation_process.utils.sentences import sum_sens_for_docs


def load_assignments(docs, annotators_folder, phase):
    assignment_header = get_assignment_header(phase)
    df = pandas.DataFrame(columns=assignment_header)
    for annotator in ANNOTATORS:
        df = df.append(
            _add_assignment_for_annotator(
                assignment_header, annotator, annotators_folder, phase, docs
            ),
            ignore_index=True,
        )
    logger.info(f"loaded assignments:\n{df}")
    return df


def _add_assignment_for_annotator(assignment_header, annotator, folder, phase, docs):
    assigned_docs = load_assigned_docs_as_list(folder, annotator, phase)
    sens_nr = sum_sens_for_docs(docs, assigned_docs)
    return pandas.DataFrame([[annotator, sens_nr]], columns=assignment_header)


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--dataset-file", type=str)
    parser.add_argument("-af", "--annotators-folder", type=str)
    parser.add_argument("-p", "--phase", type=int, default=1)
    return parser.parse_args()


def main():
    args = get_args()
    docs = load_doc_tracking_data(args.dataset_file)
    load_assignments(docs, args.annotators_folder, args.phase)


if __name__ == "__main__":
    main()
