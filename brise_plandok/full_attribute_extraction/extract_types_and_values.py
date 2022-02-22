import argparse
import json
import sys

from brise_plandok.constants import DocumentFields, SenFields
from brise_plandok.full_attribute_extraction.type.extract_types import extract_type
from brise_plandok.full_attribute_extraction.value.extract_values import extract_value


def extract(doc, attributes, attribute_type, attribute_value, only_gold):
    if DocumentFields.SENS in doc:
        items = doc[DocumentFields.SENS].values()
    else:
        items = [doc]
    for sen in items:
        sen[SenFields.GEN_ATTRIBUTES] = {}
        for attribute in attributes:
            if attribute_value:
                extract_value(sen, attribute, only_gold=only_gold)
            if attribute_type:
                extract_type(sen, attribute, only_gold=only_gold)


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-a", "--attributes", nargs="+", default=None)
    parser.add_argument("-t", "--type", default=False, action="store_true")
    parser.add_argument("-v", "--value", default=False, action="store_true")
    parser.add_argument("-g", "--only-gold", default=False, action="store_true")
    return parser.parse_args()


def main():
    args = get_args()
    for line in sys.stdin:
        doc = json.loads(line)
        extract(doc, args.attributes, args.type, args.value, args.only_gold)
        sys.stdout.write(json.dumps(doc) + "\n")


if __name__ == "__main__":
    main()
