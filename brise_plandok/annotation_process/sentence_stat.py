import argparse
from brise_plandok.annotation_process.utils.sentences import count_sentences_in_doc, sum_sens_for_docs
from brise_plandok.annotation_process.utils.doc_tracking import get_next_batch, load_doc_tracking_data
from brise_plandok.annotation_process.utils.constants import ANNOTATORS, DOC_HEADER

import json
import logging
import os


def calculate_sentences_for_next_batch(doc_tracking_file, batch_size, json_folder):
    docs = load_doc_tracking_data(doc_tracking_file)
    next_docs = get_next_batch(docs, batch_size, False)
    logging.info(f"next documents to assign: {next_docs}")
    calculate_sentence_counts(docs, next_docs, json_folder)


def calculate_sentence_counts(df, doc_ids, json_folder):
    for doc_id in doc_ids:
        if not _nr_sens_calculated(df, doc_id):
            _calculate_nr_sens_for_doc(df, doc_id, json_folder)
    sum = sum_sens_for_docs(df, doc_ids)
    logging.info(
        f"number of sentences for each document in batch:\n {df[df[DOC_HEADER[1]].isin(doc_ids)]}")
    logging.info(
        f"next batch of size {len(doc_ids)} would add {sum} new sentences - without overlap ~{int(sum/len(ANNOTATORS))} sens / annotator")
    return sum


def _nr_sens_calculated(df, doc_id):
    doc_id_col = DOC_HEADER[1]
    nr_sens_calculated_col = DOC_HEADER[3]
    return df[df[doc_id_col] == doc_id].iloc[0][nr_sens_calculated_col]


def _calculate_nr_sens_for_doc(df, doc_id, json_folder):
    path = os.path.join(json_folder, doc_id + ".jsonl")
    if not os.path.exists(path):
        raise ValueError(f"Path does not exist: {path}")
    with open(path) as f:
        lines = f.readlines()
        if len(lines) != 1:
            raise ValueError(f"File must contain exactly one line: {path}")
        doc = json.loads(lines[0].strip())
        _set_nr_sens(df, doc, doc_id)


def _set_nr_sens(df, doc, doc_id):
    doc_id_col = DOC_HEADER[1]
    nr_sens_calculated_col = DOC_HEADER[3]
    nr_sens_col = DOC_HEADER[4]
    mask = df[doc_id_col] == doc_id
    df.loc[mask, nr_sens_col] = count_sentences_in_doc(doc)
    df.loc[mask, nr_sens_calculated_col] = True


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--dataset-file", type=str)
    parser.add_argument("-s", "--batch-size", type=int)
    parser.add_argument("-jf", "--json-folder", type=str)
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " +
               "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()
    calculate_sentences_for_next_batch(
        args.dataset_file, args.batch_size, args.json_folder)


if __name__ == "__main__":
    main()
