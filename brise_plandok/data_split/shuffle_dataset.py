import argparse
from brise_plandok.data_split.constants import GOLD, ORDER_HEADER
import logging
import os
import sys
import random

def shuffle_dir(dir):
    files = os.listdir(dir)
    random.seed(10)
    random.shuffle(files)
    docs_to_annotate = [file.split('.')[0] for file in files if file.split('.')[0] not in GOLD]
    for i, doc_id in enumerate(docs_to_annotate):
        sys.stdout.write(f"{i};{doc_id};{False};{False};{-1}\n")


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--directory", type=str)
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " +
               "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()
    sys.stdout.write(f'{";".join(ORDER_HEADER)}\n')
    shuffle_dir(args.directory)
    

if __name__ == "__main__":
    main()