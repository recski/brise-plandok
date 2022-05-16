import argparse
import json
import logging
import os

from brise_plandok.constants import AttributeFields, DocumentFields, SenFields
from brise_plandok.utils import load_json, dump_json


def migrate_type(gold_folder, input_type_json, output_type_json):
    input_type = json.loads(input_type_json)
    output_type = json.loads(output_type_json)
    for doc_fn in os.listdir(gold_folder):
        if not (doc_fn.endswith("json") or doc_fn.endswith("jsonl")):
            logging.warning(f"skipping file not ending in json(l): {doc_fn}")
            continue
        doc_path = os.path.join(gold_folder, doc_fn)
        doc = load_json(doc_path)
        changed = False
        for sen in doc[DocumentFields.SENS].values():
            gold_attributes = sen[SenFields.GOLD_ATTRIBUTES]
            for attr, entry in gold_attributes.items():
                if entry[AttributeFields.TYPE] == input_type:
                    entry[AttributeFields.TYPE] = output_type
                    changed = True
        if changed:
            dump_json(doc, doc_path)


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-g", "--gold-dir")
    parser.add_argument("-i", "--input-type")
    parser.add_argument("-o", "--output-type")
    return parser.parse_args()


if __name__ == "__main__":
    logging.getLogger("penman").setLevel(logging.WARNING)
    logging.getLogger("stanza").setLevel(logging.WARNING)
    logging.getLogger("tuw_nlp").setLevel(logging.WARNING)
    args = get_args()
    migrate_type(args.gold_dir, args.input_type, args.output_type)
