import argparse
import json

from brise_plandok.attrs_from_gold import SenToAttrMap
from brise_plandok.constants import SenToAttrFields
from brise_plandok.utils import update_gold_docs


def update_sentence(gold_folder, text, new_attribute_json):
    sen_to_gold_attrs = SenToAttrMap(
        gold_dir=gold_folder, fuzzy=False, full=True, text_pattern=text
    )
    assert len(sen_to_gold_attrs.sen_to_attr.keys()) == 1
    print(f"\n\nCurrent map:\n{json.dumps(sen_to_gold_attrs.sen_to_attr, indent=4)}\n")
    entry = sen_to_gold_attrs.sen_to_attr[text]
    new_attributes = json.loads(new_attribute_json)

    print(f"\nNew attributes:\n{json.dumps(new_attributes, indent=2)}\n")
    input()
    update_gold_docs(
        gold_attr_candidate=new_attributes,
        gold_mod_candidate=entry[SenToAttrFields.MOD],
        current_gold_sens=entry[SenToAttrFields.SENS],
        gold_folder=gold_folder,
    )


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-g", "--gold-dir")
    parser.add_argument("-t", "--text")
    parser.add_argument("-a", "--new-attributes")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    update_sentence(args.gold_dir, args.text, args.new_attributes)
