import argparse
import logging
import os

from brise_plandok.annotation_process.attrs_from_gold import SenToAttrMap
from brise_plandok.constants import AttributeFields, SenToAttrFields, DocumentFields, SenFields
from brise_plandok.utils import update_gold_docs, load_json, dump_json


def rename_attribute(gold_folder, input_attribute, output_attribute, all):
    if all:
        _rename_in_all_gold_sentences(gold_folder, input_attribute, output_attribute)
    else:
        _rename_only_in_gold_docs(gold_folder, input_attribute, output_attribute)


def _rename_in_all_gold_sentences(gold_folder, input_attribute, output_attribute):
    for doc_fn in os.listdir(gold_folder):
        if not (doc_fn.endswith("json") or doc_fn.endswith("jsonl")):
            logging.warning(f"skipping file not ending in json(l): {doc_fn}")
            continue
        doc_path = os.path.join(gold_folder, doc_fn)
        doc = load_json(doc_path)
        changed = False
        for sen in doc[DocumentFields.SENS].values():
            gold_attributes = sen[SenFields.GOLD_ATTRIBUTES]
            if input_attribute in gold_attributes:
                old_attributes = gold_attributes[input_attribute]
                if output_attribute != "":
                    gold_attributes[output_attribute] = {
                        AttributeFields.NAME: output_attribute,
                        AttributeFields.VALUE: old_attributes[AttributeFields.VALUE],
                        AttributeFields.TYPE: old_attributes[AttributeFields.TYPE],
                    }
                del gold_attributes[input_attribute]
                changed = True
        if changed:
            dump_json(doc, doc_path)


def _rename_only_in_gold_docs(gold_folder, input_attribute, output_attribute):
    sen_to_gold_attrs = SenToAttrMap(
        gold_dir=gold_folder, fuzzy=False, full=True, attributes=[input_attribute]
    )
    print(f"Number of different texts to update: {len(sen_to_gold_attrs.sen_to_attr.keys())}")
    for text, entry in sen_to_gold_attrs.sen_to_attr.items():
        attributes = entry[SenToAttrFields.ATTR]
        attribute_to_change = attributes[input_attribute]
        attributes[output_attribute] = {
            AttributeFields.NAME: output_attribute,
            AttributeFields.VALUE: attribute_to_change[AttributeFields.VALUE],
            AttributeFields.TYPE: attribute_to_change[AttributeFields.TYPE],
        }
        del attributes[input_attribute]
        update_gold_docs(
            gold_attr_candidate=attributes,
            gold_mod_candidate=entry[SenToAttrFields.MOD],
            current_gold_sens=entry[SenToAttrFields.SENS],
            gold_folder=gold_folder,
        )


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-g", "--gold-dir")
    parser.add_argument("-i", "--input-attribute")
    parser.add_argument("-o", "--output-attribute")
    parser.add_argument("-a", "--all", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    logging.getLogger("penman").setLevel(logging.WARNING)
    logging.getLogger("stanza").setLevel(logging.WARNING)
    logging.getLogger("tuw_nlp").setLevel(logging.WARNING)
    args = get_args()
    rename_attribute(args.gold_dir, args.input_attribute, args.output_attribute, args.all)
