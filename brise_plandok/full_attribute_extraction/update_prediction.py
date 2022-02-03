import argparse
import logging

from brise_plandok.constants import DocumentFields
from brise_plandok.full_attribute_extraction.full_predictor import FullPredictor
from brise_plandok.utils import load_json, dump_json


def update_predictions(doc_file):
    doc = load_json(doc_file)
    full_predictor = FullPredictor(doc)
    for sen in doc[DocumentFields.SENS].values():
        full_predictor.get_prediction_for_sen(sen)
    dump_json(doc, doc_file)


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--doc-file")
    return parser.parse_args()


if __name__ == '__main__':
    logging.getLogger('penman').setLevel(logging.WARNING)
    logging.getLogger('stanza').setLevel(logging.WARNING)
    logging.getLogger('tuw_nlp').setLevel(logging.WARNING)
    args = get_args()
    update_predictions(args.doc_file)
