import argparse
import logging

from brise_plandok.attrs_from_gold import SenToAttrMap
from brise_plandok.constants import AttributeFields, SenToAttrFields
from brise_plandok.utils import update_gold_docs


def rename_attribute(gold_folder, input_attribute, output_attribute):
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
    return parser.parse_args()


if __name__ == "__main__":
    logging.getLogger("penman").setLevel(logging.WARNING)
    logging.getLogger("stanza").setLevel(logging.WARNING)
    logging.getLogger("tuw_nlp").setLevel(logging.WARNING)
    args = get_args()
    rename_attribute(args.gold_dir, args.input_attribute, args.output_attribute)
