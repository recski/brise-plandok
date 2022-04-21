import itertools
import os

import pandas
from numberpartitioning import karmarkar_karp

from brise_plandok import logger
from brise_plandok.annotation_process.utils.constants import (
    ANNOTATOR_DOWNLOAD_FOLDER,
    ASSIGNMENT_ADDITIONAL_HEADER,
    ASSIGNMENT_DF_HEADER_BASE,
    ASSIGNMENT_TXT,
    ASSIGNMENT_FILE_HEADER,
    ASSIGNMENT_XLSX,
    DOC_HEADER,
    PHASE_STR,
)
from brise_plandok.annotation_process.utils.sentences import sum_sens_for_docs


def get_assignment_header(phase):
    return [
        ASSIGNMENT_DF_HEADER_BASE[0],
        ASSIGNMENT_DF_HEADER_BASE[1] + "_" + PHASE_STR + "_" + str(phase),
    ]


def get_download_folder(ann_folder, annotator, phase):
    return os.path.join(ann_folder, annotator, PHASE_STR + str(phase), ANNOTATOR_DOWNLOAD_FOLDER)


def get_assignment_path(ann_folder, annotator, phase):
    return os.path.join(ann_folder, annotator, PHASE_STR + str(phase), ASSIGNMENT_TXT)


def load_assigned_docs_as_list(ann_folder, annotator, phase):
    return list(itertools.chain(*load_assigned_docs_as_df(ann_folder, annotator, phase).values))


def load_assigned_docs_as_df(ann_folder, annotator, phase):
    return pandas.read_csv(
        filepath_or_buffer=get_assignment_path(ann_folder, annotator, phase),
        dtype={ASSIGNMENT_FILE_HEADER[0]: str},
    )


def get_assignment(doc_ids, df, nr_groups):
    numbers, num_to_doc = _get_numbers(doc_ids, df)
    result = _get_partition(numbers, nr_groups)
    logger.info(f"partition created: {result}")
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
            raise ValueError(f"Some docs were not used in the partition {docs}")


def fill_assignments_with_batch(docs, cycle, assignments, partition, next_doc_ids, phase):
    assignments[ASSIGNMENT_ADDITIONAL_HEADER[0]] = None
    assignments[ASSIGNMENT_ADDITIONAL_HEADER[1]] = -1
    assignments[ASSIGNMENT_ADDITIONAL_HEADER[2]] = -1
    _enrich_docs_with_annotators(docs, cycle, partition)
    _log_for_review_tracking(docs, next_doc_ids, cycle)
    for i, group_members in enumerate(cycle.values.tolist()):
        _fill_for_group(assignments, group_members, partition[i], docs, phase)


def _log_for_review_tracking(docs, next_doc_ids, cycle):
    next_docs = docs.loc[docs[DOC_HEADER[1]].isin(next_doc_ids)].iloc[
        :, [1, 4] + [5 + i for i in range(len(cycle.columns))]
    ]
    view = next_docs.to_csv(sep=";", index=False)
    logger.info(f"print new assignment for review tracking:\n\n{view}")


def _enrich_docs_with_annotators(docs, cycle, partition):
    for i, doc_ids in enumerate(partition):
        for doc_id in doc_ids:
            mask = docs[DOC_HEADER[1]] == doc_id
            for cycle_header in cycle.columns:
                docs.loc[mask, cycle_header] = cycle.iloc[i][cycle_header]


def _fill_for_group(assignments, group_members, partition, docs, phase):
    group_members_mask = assignments[ASSIGNMENT_DF_HEADER_BASE[0]].isin(group_members)
    assignment_header = get_assignment_header(phase)
    _fill_assigned_docs(partition, assignments, group_members_mask)
    _fill_assigned_sens(docs, partition, assignments, group_members_mask)
    _fill_sens_sum(group_members, assignments, assignment_header)


def _fill_assigned_sens(docs, partition, assignments, group_members_mask):
    assignments.loc[group_members_mask, ASSIGNMENT_ADDITIONAL_HEADER[1]] = sum_sens_for_docs(
        docs, partition
    )


def _fill_assigned_docs(partition, assignments, group_members_mask):
    assignments.loc[group_members_mask, ASSIGNMENT_ADDITIONAL_HEADER[0]] = ",".join(partition)


def _fill_sens_sum(group, assignments, assignment_header):
    for annotator in group:
        annotator_mask = assignments[assignment_header[0]] == annotator
        sentences_before = assignments.loc[annotator_mask, assignment_header[1]]
        sentences_batch = assignments.loc[annotator_mask, ASSIGNMENT_ADDITIONAL_HEADER[1]]
        assignments.loc[annotator_mask, ASSIGNMENT_ADDITIONAL_HEADER[2]] = (
            sentences_before + sentences_batch
        )


def update_assignments(doc_ids, annotator, annotator_folder, phase):
    assignment_xlsx = os.path.join(
        get_download_folder(annotator_folder, annotator, phase), ASSIGNMENT_XLSX
    )
    df = load_assigned_docs_as_df(annotator_folder, annotator, phase)
    assignment_txt = get_assignment_path(annotator_folder, annotator, phase)
    for doc_id in doc_ids:
        df = df.append(
            pandas.DataFrame([[doc_id]], columns=ASSIGNMENT_FILE_HEADER),
            ignore_index=True,
        )
    df.to_csv(path_or_buf=assignment_txt, sep=";", index=False)
    df.to_excel(assignment_xlsx, index=False)  # pylint: disable=no-member
    logger.info(f"assignment text files were updated: {assignment_txt}\t{assignment_xlsx}")
