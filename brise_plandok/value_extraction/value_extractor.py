import argparse
import json
import sys

from brise_plandok.constants import AttributesNames, DocumentFields, SenFields
from brise_plandok.value_extraction.planzeichen import PlanzeichenExtractor
from brise_plandok.value_extraction.utils import contains_attr

class ValueExtractor:

    def __init__(self, args):
        self.attributes = args.attributes
        self.planzeichen = PlanzeichenExtractor()

    def extract(self, doc):
        for sen in doc[DocumentFields.SENS].values():
            for attribute in self.attributes:
                self._extract_for_attr(sen, attribute)
        sys.stdout.write(json.dumps(doc) + "\n")

    def _extract_for_attr(self, sen, attribute):
        if contains_attr(sen, attribute):
            if attribute == AttributesNames.PLANZEICHEN:
                values = [value for value in self.planzeichen.extract(sen[SenFields.TEXT])]
                self._add_to_gen_values(sen, attribute, values)

    def _add_to_gen_values(self, sen, attribute, values):
        if SenFields.GEN_VALUES not in sen.keys():
            sen[SenFields.GEN_VALUES] = {}
        sen[SenFields.GEN_VALUES][attribute] = values

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-a", "--attributes", nargs="+", default=None)
    return parser.parse_args()

def main():
    args = get_args()
    value_extractor = ValueExtractor(args)
    for line in sys.stdin:
        doc = json.loads(line)
        value_extractor.extract(doc)


if __name__ == "__main__":
    main()