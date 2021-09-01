import argparse
from brise_plandok.data_split.constants import ORDER_HEADER
import logging
import csv
import pandas

def generate_batch(dataset, batch_size):
    doc_order = read_dataset_order(dataset)
    next_docs = get_next_batch(doc_order, batch_size)
    # update sentence count
    # generate excels
    # get cycle
    # assign docs to annotators
    # copy to output folder
    # update assigments with sentence count
    # update dataset
    pass

def read_dataset_order(file):
    return pandas.read_csv(filepath_or_buffer=file, sep=";")

def get_next_batch(df, batch_size):
    order_col = ORDER_HEADER[0]
    doc_id_col = ORDER_HEADER[1]
    assigned_col = ORDER_HEADER[2]
    first = df[df[assigned_col] == False].iloc[0][order_col]
    df[assigned_col][(df[order_col] >= first) & (df[order_col] < first + batch_size)] = True
    return df[doc_id_col][(df[order_col] >= first) & (df[order_col] < first + batch_size)]



def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--dataset-file", type=str)
    parser.add_argument("-s", "--batch-size", type=int)
    # parser.add_argument("-j", "--json-folder", type=str)
    # parser.add_argument("-a", "--assignment-folder", type=str)
    # parser.add_argument("-o", "--output-folder", type=str)
    # parser.add_argument("-c", "--cycle", type=int)
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " +
               "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()
    generate_batch(args.dataset_file, args.batch_size)
    

if __name__ == "__main__":
    main()