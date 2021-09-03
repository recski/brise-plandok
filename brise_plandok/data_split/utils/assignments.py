
import itertools
import logging
import os

import pandas
from brise_plandok.data_split.utils.constants import ASSIGNMENT_ADDITIONAL_HEADER, ASSIGNMENT_DF_HEADER, ASSIGNMENT_FILE, ASSIGNMENT_FILE_HEADER
from brise_plandok.data_split.utils.sentences import sum_sens_for_docs


def load_assigned_docs_as_list(path):
    return list(itertools.chain(*load_assigned_docs_as_df(path).values))

def load_assigned_docs_as_df(path):
    return pandas.read_csv(filepath_or_buffer=path, dtype={ ASSIGNMENT_FILE_HEADER[0]: str})


def get_assignment(docs):
    return [docs[:2], docs[2:4], docs[4:6]]


def fill_assigments_with_batch(docs, cycle, assigments, partition):
    assigments[ASSIGNMENT_ADDITIONAL_HEADER[0]] = None
    assigments[ASSIGNMENT_ADDITIONAL_HEADER[1]] = -1
    assigments[ASSIGNMENT_ADDITIONAL_HEADER[2]] = -1
    for i, group in cycle.iterrows():
        mask = assigments[ASSIGNMENT_DF_HEADER[0]].isin(group.values)
        assigments.loc[mask, ASSIGNMENT_ADDITIONAL_HEADER[0]
                       ] = ",".join(partition[i])
        assigments.loc[mask, ASSIGNMENT_ADDITIONAL_HEADER[1]
                       ] = sum_sens_for_docs(docs, partition[i])
        _calculate_sum_sentence_after_batch(group, assigments)


def _calculate_sum_sentence_after_batch(group, assigments):
    for annotator in group:
        annotator_mask  = assigments[ASSIGNMENT_DF_HEADER[0]] == annotator
        sentences_before = assigments.loc[annotator_mask, ASSIGNMENT_DF_HEADER[1]]
        sentences_batch = assigments.loc[annotator_mask, ASSIGNMENT_ADDITIONAL_HEADER[1]]
        assigments.loc[annotator_mask, ASSIGNMENT_ADDITIONAL_HEADER[2]
                    ] = sentences_before + sentences_batch

def update_assignments(doc_ids, annotator, annotator_folder):
    assignment_file = os.path.join(annotator_folder, annotator, ASSIGNMENT_FILE)
    df = load_assigned_docs_as_df(assignment_file)
    for doc_id in doc_ids:
        df = df.append(pandas.DataFrame([[doc_id]], columns=ASSIGNMENT_FILE_HEADER), ignore_index=True)
    df.to_csv(path_or_buf=assignment_file, sep=";", index=False)
    logging.info(f"assignment file {assignment_file} was updated")