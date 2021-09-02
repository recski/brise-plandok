import argparse
from brise_plandok.data_split.sentence_counter import count_sentences_in_doc
from brise_plandok.data_split.doc_tracking_utils import get_next_batch, load_doc_tracking_data, save_doc_tracking_data
import json
from brise_plandok.data_split.constants import ANNOTATORS, DOC_HEADER
import logging
import os


def calculate_sentences_for_next_batch(doc_tracking_file, batch_size, json_folder, save=False):
    docs = load_doc_tracking_data(doc_tracking_file)
    next_docs = get_next_batch(docs, batch_size, set_assigned=False)
    logging.info(f"next documents to assign: {next_docs}")
    calculate_sentence_counts(docs, next_docs, json_folder)
    if save:
        logging.info(
            f"updating doc tracking file {doc_tracking_file} with new sentence counts")
        save_doc_tracking_data(doc_tracking_file, docs)


def calculate_sentence_counts(df, doc_ids, json_folder):
    for doc_id in doc_ids:
        if not _nr_sens_calculated(df, doc_id):
            _calculate_nr_sens_for_doc(df, doc_id, json_folder)
    sum = sum_sens_for_docs(df, doc_ids)
    logging.info(
        f"number of sentences for each document in batch:\n {df[df[DOC_HEADER[1]].isin(doc_ids)]}")
    logging.info(
        f"next batch of size {len(doc_ids)} would add {sum} new sentences - ~{int(sum/len(ANNOTATORS))} sens / annotator")
    return sum


def _nr_sens_calculated(df, doc_id):
    doc_id_col = DOC_HEADER[1]
    nr_sens_calculated_col = DOC_HEADER[3]
    return df[df[doc_id_col] == doc_id].iloc[0][nr_sens_calculated_col]


def _calculate_nr_sens_for_doc(df, doc_id, json_folder):
    path = os.path.join(json_folder, doc_id + ".jsonl")
    with open(path) as f:
        lines = f.readlines()
        assert len(lines) == 1
        doc = json.loads(lines[0].strip())
        _set_nr_sens(df, doc, doc_id)
        _set_nr_sens_calculated_true(df, doc_id)


def _set_nr_sens(df, doc, doc_id):
    doc_id_col = DOC_HEADER[1]
    nr_sens_col = DOC_HEADER[4]
    df[nr_sens_col][df[doc_id_col] == doc_id] = count_sentences_in_doc(doc)


def _set_nr_sens_calculated_true(df, doc_id):
    doc_id_col = DOC_HEADER[1]
    nr_sens_calculated_col = DOC_HEADER[3]
    df[nr_sens_calculated_col][df[doc_id_col] == doc_id] = True


def sum_sens_for_docs(df, doc_ids):
    doc_id_col = DOC_HEADER[1]
    nr_sens_col = DOC_HEADER[4]
    return df[nr_sens_col][df[doc_id_col].isin(doc_ids)].sum()


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--dataset-file", type=str)
    parser.add_argument("-s", "--batch-size", type=int)
    parser.add_argument("-jf", "--json-folder", type=str)
    parser.add_argument("-o", "--override", default=False, action="store_true")
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " +
               "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()
    calculate_sentences_for_next_batch(
        args.dataset_file, args.batch_size, args.json_folder, args.override)


if __name__ == "__main__":
    main()
