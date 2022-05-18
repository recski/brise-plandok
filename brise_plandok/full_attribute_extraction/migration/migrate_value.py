import argparse
import logging
import os

from brise_plandok.constants import AttributeFields, DocumentFields, SenFields
from brise_plandok.data_utils import add_attribute
from brise_plandok.utils import load_json, dump_json


def migrate_value(gold_folder, input_value, output_value, input_attribute, split):
    for doc_fn in os.listdir(gold_folder):
        if not (doc_fn.endswith("json") or doc_fn.endswith("jsonl")):
            logging.warning(f"skipping file not ending in json(l): {doc_fn}")
            continue
        doc_path = os.path.join(gold_folder, doc_fn)
        doc = load_json(doc_path)
        doc_changed = False
        for sen in doc[DocumentFields.SENS].values():
            if sen[SenFields.FULL_GOLD_EXISTS]:
                gold_attributes = sen[SenFields.GOLD_ATTRIBUTES]
                sen_changed = False
                for attr_name in gold_attributes.keys():
                    if input_attribute is None or attr_name == input_attribute:
                        for attribute in gold_attributes[attr_name]:
                            attr_value = attribute[AttributeFields.VALUE]
                            if (
                                split is not None
                                and attr_value is not None
                                and split in attr_value
                            ):
                                values = attr_value.split(split)
                                for value in values:
                                    add_attribute(
                                        gold_attributes,
                                        attribute[AttributeFields.NAME],
                                        value,
                                        attribute[AttributeFields.TYPE],
                                    )
                                doc_changed, sen_changed = True, True
                            elif attribute[AttributeFields.VALUE] == input_value:
                                attribute[AttributeFields.VALUE] = output_value
                                doc_changed, sen_changed = True, True
                if sen_changed:
                    if split is not None:
                        print(f"{sen[SenFields.ID]}")
                        print(f"Gold attributes before:\n{gold_attributes}")
                        gold_attributes[input_attribute] = [
                            attr
                            for attr in gold_attributes[input_attribute]
                            if attr[AttributeFields.VALUE] is None
                            or split not in attr[AttributeFields.VALUE]
                        ]
                        print(f"Gold attributes after:\n{gold_attributes}\n")
            if doc_changed:
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
