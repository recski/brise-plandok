import argparse
import json
import sys

from brise_plandok.constants import AttributeFields, DocumentFields, SenFields
from brise_plandok.full_attribute_extraction.utils.utils import contains_attr, extract_values


class ValueExtractor:

    def __init__(self, attributes=[]):
        self.attributes = attributes

    def extract(self, doc):
        items = []
        if DocumentFields.SENS in doc:
            items = doc[DocumentFields.SENS].values()
        else:
            items = [doc]
        for sen in items:
            for attribute in self.attributes:
                self.extract_for_attr(sen, attribute)
        sys.stdout.write(json.dumps(doc) + "\n")

    def extract_for_attr(self, sen, attribute, field_to_add=SenFields.GEN_ATTRIBUTES, only_if_gold=True):
        if not only_if_gold or contains_attr(sen, attribute):
            values = list(set([value for value in extract_values(
                attribute, sen[SenFields.TEXT])]))
            self._add_to_gen_values(sen, attribute, values, field_to_add)

    def _add_to_gen_values(self, sen, attribute, values, field_to_add):
        if attribute not in sen[field_to_add]:
            sen[field_to_add][attribute] = {
                AttributeFields.VALUE: [],
                AttributeFields.TYPE: None,
                AttributeFields.NAME: attribute,
            }
        sen[field_to_add][attribute][AttributeFields.VALUE] = values


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-a", "--attributes", nargs="+", default=None)
    return parser.parse_args()


def main():
    args = get_args()
    value_extractor = ValueExtractor(args.attributes)
    for line in sys.stdin:
        doc = json.loads(line)
        value_extractor.extract(doc)


if __name__ == "__main__":
    main()
