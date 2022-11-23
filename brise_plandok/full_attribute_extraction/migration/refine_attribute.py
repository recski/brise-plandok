import argparse
import logging

from brise_plandok.annotation_process.attrs_from_gold import SenToAttrMap
from brise_plandok.constants import SenToAttrFields
from brise_plandok.data_utils import add_attribute
from brise_plandok.utils import update_gold_docs

DUMMY_LABEL = "dummy"
GRAPH_FORMAT = "fourlang"


def refine_attribute(gold_folder, attr_name, attr_value, attr_type, sentence_pattern):
    sen_to_gold_attrs = SenToAttrMap(
        gold_dir=gold_folder,
        fuzzy=False,
        full=True,
        text_pattern=sentence_pattern,
        except_for_values={attr_name: attr_value},
    )
    sens_to_update = len(sen_to_gold_attrs.sen_to_attr.keys())
    print(f"Number of different texts to update: {sens_to_update}")
    for text, entry in sen_to_gold_attrs.sen_to_attr.items():
        print("================================================")
        print(f"{sens_to_update} to go")
        print(text)
        old_attributes = entry[SenToAttrFields.ATTR]

        print(f"\nOld attributes:\n{old_attributes}")
        if attr_name in old_attributes:
            print(old_attributes[attr_name])
        else:
            print(f"no entry for {attr_name}")
        add_attribute(old_attributes, attr_name, attr_value, attr_type)
        print(f"\nNew attributes:\n{old_attributes}")
        print(old_attributes[attr_name])

        print(f"\nSentences to update: {entry[SenToAttrFields.SENS]}")
        take = input("Add attribute? (Enter=yes, else no)")
        if take == "":
            update_gold_docs(
                gold_attr_candidate=old_attributes,
                gold_mod_candidate=entry[SenToAttrFields.MOD],
                current_gold_sens=entry[SenToAttrFields.SENS],
                gold_folder=gold_folder,
            )
            print(f"Updated docs: {entry[SenToAttrFields.SENS]}")
        else:
            print("No update was done")
        sens_to_update -= 1


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-g", "--gold-dir")
    parser.add_argument("-a", "--attribute-name")
    parser.add_argument("-v", "--attribute-value")
    parser.add_argument("-t", "--attribute-type")
    parser.add_argument("-p", "--sentence-pattern")
    return parser.parse_args()


if __name__ == "__main__":
    logging.getLogger("penman").setLevel(logging.WARNING)
    logging.getLogger("stanza").setLevel(logging.WARNING)
    logging.getLogger("tuw_nlp").setLevel(logging.WARNING)
    args = get_args()
    refine_attribute(
        args.gold_dir,
        args.attribute_name,
        args.attribute_value,
        args.attribute_type,
        args.sentence_pattern,
    )
