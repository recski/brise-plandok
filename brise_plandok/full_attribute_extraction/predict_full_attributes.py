import argparse
import json
import logging
import sys

from brise_plandok.constants import DocumentFields
from brise_plandok.full_attribute_extraction.full.full_predictor import FullPredictor
from brise_plandok.utils import load_json, dump_json


def predict_attributes(doc_file, console):
    doc = load_json(doc_file)
    full_predictor = FullPredictor(doc)
    for sen in doc[DocumentFields.SENS].values():
        full_predictor.get_prediction_for_sen(sen)
    if not console:
        dump_json(doc, doc_file)
    else:
        sys.stdout.write(json.dumps(doc) + "\n")


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--doc-file")
    parser.add_argument("-c", "--console-output", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    logging.getLogger("penman").setLevel(logging.WARNING)
    logging.getLogger("stanza").setLevel(logging.WARNING)
    logging.getLogger("tuw_nlp").setLevel(logging.WARNING)
    args = get_args()
    predict_attributes(args.doc_file, args.console_output)
