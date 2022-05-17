import argparse
import logging
import os

from brise_plandok.constants import AttributeFields, DocumentFields, SenFields
from brise_plandok.data_utils import add_attribute
from brise_plandok.utils import load_json, dump_json


def migrate_value(gold_folder, input_value, output_value, attribute, split):
    for doc_fn in os.listdir(gold_folder):
        if not (doc_fn.endswith("json") or doc_fn.endswith("jsonl")):
            logging.warning(f"skipping file not ending in json(l): {doc_fn}")
            continue
        doc_path = os.path.join(gold_folder, doc_fn)
        doc = load_json(doc_path)
        changed = False
        for sen in doc[DocumentFields.SENS].values():
            gold_attributes = sen[SenFields.GOLD_ATTRIBUTES]
            for attr, entries in gold_attributes.items():
                if attribute is None or attr == attribute:
                    for entry in entries:
                        entry_value = entry[AttributeFields.VALUE]
                        if split is not None and entry_value is not None and split in entry_value:
                            values = entry_value.split(split)
                            for value in values:
                                add_attribute(
                                    gold_attributes,
                                    entry[AttributeFields.NAME],
                                    value,
                                    entry[AttributeFields.TYPE],
                                )
                            print(f"Before delete:\n{gold_attributes[attr]}")
                            entries.remove(entry)
                            print(f"After delete:\n{gold_attributes[attr]}")
                            changed = True
                        elif entry[AttributeFields.VALUE] == input_value:
                            entry[AttributeFields.VALUE] = output_value
                            changed = True
        if changed:
            dump_json(doc, doc_path)


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-g", "--gold-dir")
    parser.add_argument("-i", "--input-value", default=None)
    parser.add_argument("-o", "--output-value", default=None)
    parser.add_argument("-a", "--attribute", default=None)
    parser.add_argument("-s", "--split", default=None)
    return parser.parse_args()


if __name__ == "__main__":
    logging.getLogger("penman").setLevel(logging.WARNING)
    logging.getLogger("stanza").setLevel(logging.WARNING)
    logging.getLogger("tuw_nlp").setLevel(logging.WARNING)
    args = get_args()
    migrate_value(args.gold_dir, args.input_value, args.output_value, args.attribute, args.split)
