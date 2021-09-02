import argparse
from brise_plandok.data_split.count_sentences import count_sentences_in_doc
import json
from brise_plandok.data_split.constants import ORDER_HEADER
import logging
import pandas
import os

def generate_batch(dataset, batch_size, json_folder):
    docs = read_dataset_order(dataset)
    next_docs = get_next_batch(docs, batch_size)
    logging.info(f"next documents to assign: {next_docs}")
    calculate_sentence_counts(docs, next_docs, json_folder)
    logging.info(f"number of sentences are updates:\n {docs[docs[ORDER_HEADER[1]].isin(next_docs)]}")
    # update sentence count
    # get cycle
    # check if all annotators are in the cycle
    # assign docs to annotators
    # print assignments
    # print sentence stat before & after
    # break if --dry-run
    # generate excels to xls folder
    # copy excels to annotator folders
    # update assigments
    # update dataset
    pass
    # To do
    # - error handling
    # - documentation

def read_dataset_order(file):
    return pandas.read_csv(filepath_or_buffer=file, sep=";")

def get_next_batch(df, batch_size):
    first = _get_first_not_assigned(df)
    _set_assigned_true(df, first, batch_size)
    return _get_next_batch_doc_ids(df, first, batch_size)

def _get_first_not_assigned(df):
    order_col = ORDER_HEADER[0]
    assigned_col = ORDER_HEADER[2]
    return df[df[assigned_col] == False].iloc[0][order_col]

def _set_assigned_true(df, first, batch_size):
    order_col = ORDER_HEADER[0]
    assigned_col = ORDER_HEADER[2]
    df[assigned_col][(df[order_col] >= first) & (df[order_col] < first + batch_size)] = True

def _get_next_batch_doc_ids(df, first, batch_size):
    order_col = ORDER_HEADER[0]
    doc_id_col = ORDER_HEADER[1]
    return list(df[doc_id_col][(df[order_col] >= first) & (df[order_col] < first + batch_size)])

def calculate_sentence_counts(df, doc_ids, json_folder):
    for doc_id in doc_ids:
        if not _nr_sens_calculated(df, doc_id):
            _calculate_nr_sens_for_doc(df, doc_id, json_folder)

def _nr_sens_calculated(df, doc_id):
    doc_id_col = ORDER_HEADER[1]
    nr_sens_calculated_col = ORDER_HEADER[3]
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
    doc_id_col = ORDER_HEADER[1]
    nr_sens_col = ORDER_HEADER[4]
    df[nr_sens_col][df[doc_id_col] == doc_id] = count_sentences_in_doc(doc)

def _set_nr_sens_calculated_true(df, doc_id):
    doc_id_col = ORDER_HEADER[1]
    nr_sens_calculated_col = ORDER_HEADER[3]
    df[nr_sens_calculated_col][df[doc_id_col] == doc_id] = True




def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--dataset-file", type=str)
    parser.add_argument("-s", "--batch-size", type=int)
    parser.add_argument("-jf", "--json-folder", type=str)
    # parser.add_argument("-c", "--cycle", type=int)
    # parser.add_argument("-af", "--annotator-folder", type=str)
    # add dry-run
    # parser.add_argument("-xf", "--xlsx-folder", type=str)
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " +
               "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()
    generate_batch(args.dataset_file, args.batch_size, args.json_folder)
    

if __name__ == "__main__":
    main()