import argparse
import logging
import os
import sys
import random

GOLD = ["7374", "7857", "7990", "8065", "8250"]

def shuffle_dir(dir):
    files = os.listdir(dir)
    random.seed(10)
    random.shuffle(files)
    docs_to_annotate = [file.split('.')[0] for file in files if file.split('.')[0] not in GOLD]
    for i, doc_id in enumerate(docs_to_annotate):
        sys.stdout.write(f"{i};{doc_id};false\n")


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
    sys.stdout.write(f"count;doc_id;assigned\n")
    shuffle_dir(args.directory)
    

if __name__ == "__main__":
    main()