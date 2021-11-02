import argparse
import json
import sys

from brise_plandok.constants import AttributeFields, AttributesNames, DocumentFields, SenFields
from brise_plandok.full_attribute_extraction.type.anordnung_gaertnerisch import AnordnungGaertnerischeAusgestaltungExtractor
from brise_plandok.full_attribute_extraction.type.dachart import DachartExtractor
from brise_plandok.full_attribute_extraction.type.dachneigung_max import DachneigungMaxExtractor
from brise_plandok.full_attribute_extraction.type.flaechen import FlaechenExtractor
from brise_plandok.full_attribute_extraction.type.gebaeude_hoehe_max import GebaeudeHoeheMaxExtractor
from brise_plandok.full_attribute_extraction.type.planzeichen import PlanzeichenExtractor
from brise_plandok.full_attribute_extraction.utils.utils import contains_attr


class TypeExtractor:

    def __init__(self, attributes=[]):
        self.attributes = attributes
        self.dachart = DachartExtractor()
        self.anordnung_gaertnerisch = AnordnungGaertnerischeAusgestaltungExtractor()
        self.gebaeude_hoehe_max = GebaeudeHoeheMaxExtractor()
        self.dachneigung_max = DachneigungMaxExtractor()
        self.flaechen = FlaechenExtractor()
        self.planzeichen = PlanzeichenExtractor()

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

    def extract_for_attr(self, sen, attribute, field_to_add = SenFields.GEN_ATTRIBUTES,  only_if_gold=True):
        att_type = None
        if not only_if_gold or contains_attr(sen, attribute):
            if attribute == AttributesNames.DACHART:
                att_type = self.dachart.extract(sen[SenFields.TEXT])
            elif attribute == AttributesNames.ANORDNUNG_GAERTNERISCH:
                att_type = self.anordnung_gaertnerisch.extract(sen[SenFields.TEXT])
            elif attribute == AttributesNames.GEBAEUDE_HOEHE_MAX:
                att_type = self.gebaeude_hoehe_max.extract(sen[SenFields.TEXT])
            elif attribute == AttributesNames.DACHNEIGUNG_MAX:
                att_type = self.dachneigung_max.extract(sen[SenFields.TEXT])
            elif attribute == AttributesNames.FLAECHEN:
                att_type = self.flaechen.extract(sen[SenFields.TEXT])
            elif attribute == AttributesNames.PLANZEICHEN:
                att_type = self.planzeichen.extract(sen[SenFields.TEXT])
            self._add_to_gen_values(sen, attribute, att_type, field_to_add)


    def _add_to_gen_values(self, sen, attribute, attr_type, field_to_add):
        if attribute not in sen[field_to_add]:
            sen[field_to_add][attribute] = {
                AttributeFields.VALUE: [],
                AttributeFields.TYPE: None,
                AttributeFields.NAME: attribute,
            }
        sen[field_to_add][attribute][AttributeFields.TYPE] = attr_type

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-a", "--attributes", nargs="+", default=None)
    return parser.parse_args()

def main():
    args = get_args()
    value_extractor = TypeExtractor(args.attributes)
    for line in sys.stdin:
        doc = json.loads(line)
        value_extractor.extract(doc)


if __name__ == "__main__":
    main()