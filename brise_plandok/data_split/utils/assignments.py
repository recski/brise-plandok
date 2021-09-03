
from brise_plandok.data_split.utils.constants import ASSIGNMENT_ADDITIONAL_HEADER, ASSIGNMENT_DF_HEADER
from brise_plandok.data_split.utils.sentences import sum_sens_for_docs

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