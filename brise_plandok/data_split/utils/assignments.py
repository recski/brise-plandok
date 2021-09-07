
import itertools
import logging
import os

import pandas
from brise_plandok.data_split.utils.constants import ANNOTATOR_DOWNLOAD_FOLDER, ASSIGNMENT_ADDITIONAL_HEADER, ASSIGNMENT_DF_HEADER, ASSIGNMENT_TXT, ASSIGNMENT_FILE_HEADER, ASSIGNMENT_XLSX, DOC_HEADER
from brise_plandok.data_split.utils.sentences import sum_sens_for_docs
from numberpartitioning import karmarkar_karp


def load_assigned_docs_as_list(path):
    return list(itertools.chain(*load_assigned_docs_as_df(path).values))


def load_assigned_docs_as_df(path):
    return pandas.read_csv(filepath_or_buffer=path, dtype={ASSIGNMENT_FILE_HEADER[0]: str})


def get_assignment(doc_ids, df, nr_groups):
    numbers, num_to_doc = _get_numbers(doc_ids, df)
    result = _get_partition(numbers, nr_groups)
    logging.info(f"partition created: {result}")
    return _get_doc_partition(result, num_to_doc)


def _get_numbers(doc_ids, df):
    numbers = []
    num_to_doc = {}
    for doc_id in doc_ids:
        mask = df[DOC_HEADER[1]] == doc_id
        num = df.loc[mask, DOC_HEADER[4]].values[0]
        if num not in num_to_doc:
            num_to_doc[num] = []
        num_to_doc[num].append(doc_id)
        numbers.append(num)
    return numbers, num_to_doc


def _get_partition(numbers, num_parts):
    return karmarkar_karp(numbers, num_parts=num_parts)


def _get_doc_partition(result, num_to_doc):
    doc_partition = []
    for i in range(len(result.partition)):
        doc_partition.append([])
    for i, numbers in enumerate(result.partition):
        for num in numbers:
            doc_id = num_to_doc[num][0]
            doc_partition[i].append(doc_id)
            num_to_doc[num] = num_to_doc[num][1:]
    _check_if_all_docs_used(num_to_doc)
    return doc_partition


def _check_if_all_docs_used(num_to_doc):
    for docs in num_to_doc.values():
        if len(docs) != 0:
            raise ValueError(
                f"Some docs were not used in the partition {docs}")


def fill_assignments_with_batch(docs, cycle, assignments, partition):
    assignments[ASSIGNMENT_ADDITIONAL_HEADER[0]] = None
    assignments[ASSIGNMENT_ADDITIONAL_HEADER[1]] = -1
    assignments[ASSIGNMENT_ADDITIONAL_HEADER[2]] = -1
    for i, group in enumerate(cycle.values.tolist()):
        mask = assignments[ASSIGNMENT_DF_HEADER[0]].isin(group)
        assignments.loc[mask, ASSIGNMENT_ADDITIONAL_HEADER[0]
                        ] = ",".join(partition[i])
        assignments.loc[mask, ASSIGNMENT_ADDITIONAL_HEADER[1]
                        ] = sum_sens_for_docs(docs, partition[i])
        _calculate_sum_sentence_after_batch(group, assignments)


def _calculate_sum_sentence_after_batch(group, assignments):
    for annotator in group:
        annotator_mask = assignments[ASSIGNMENT_DF_HEADER[0]] == annotator
        sentences_before = assignments.loc[annotator_mask,
                                           ASSIGNMENT_DF_HEADER[1]]
        sentences_batch = assignments.loc[annotator_mask,
                                          ASSIGNMENT_ADDITIONAL_HEADER[1]]
        assignments.loc[annotator_mask, ASSIGNMENT_ADDITIONAL_HEADER[2]
                        ] = sentences_before + sentences_batch


def update_assignments(doc_ids, annotator, annotator_folder):
    assignment_txt = os.path.join(annotator_folder, annotator, ASSIGNMENT_TXT)
    assignment_xlsx = os.path.join(
        annotator_folder, annotator, ANNOTATOR_DOWNLOAD_FOLDER, ASSIGNMENT_XLSX)
    df = load_assigned_docs_as_df(assignment_txt)
    for doc_id in doc_ids:
        df = df.append(pandas.DataFrame(
            [[doc_id]], columns=ASSIGNMENT_FILE_HEADER), ignore_index=True)
    df.to_csv(path_or_buf=assignment_txt, sep=";", index=False)
    df.to_excel(assignment_xlsx, index=False)
    logging.info(
        f"assignment text files were updated: {assignment_txt}\t{assignment_xlsx}")
