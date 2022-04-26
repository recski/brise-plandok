import argparse
import os
import random
import sys

from brise_plandok.annotation_process.utils.constants import DOC_HEADER, GOLD


def shuffle_dir(dir):
    files = os.listdir(dir)
    random.seed(10)
    random.shuffle(files)
    docs_to_annotate = [file.split(".")[0] for file in files if file.split(".")[0] not in GOLD]
    for i, doc_id in enumerate(docs_to_annotate):
        sys.stdout.write(f"{i};{doc_id};{False};{False};{-1};;;{False}\n")


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--directory", type=str)
    return parser.parse_args()


def main():
    args = get_args()
    sys.stdout.write(f'{";".join(DOC_HEADER)}\n')
    shuffle_dir(args.directory)


if __name__ == "__main__":
    main()
