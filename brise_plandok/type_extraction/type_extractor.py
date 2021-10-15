import argparse
import json
import sys

from brise_plandok.constants import AttributeFields, AttributesNames, DocumentFields, SenFields
from brise_plandok.type_extraction.anordnung_gaertnerisch import AnordnungGaertnerischeAusgestaltungExtractor
from brise_plandok.type_extraction.dachart import DachartExtractor
from brise_plandok.type_extraction.dachneigung_max import DachneigungMaxExtractor
from brise_plandok.type_extraction.flaechen import FlaechenExtractor
from brise_plandok.type_extraction.gebaeude_hoehe_max import GebaeudeHoeheMaxExtractor
from brise_plandok.value_extraction.utils import contains_attr


class TypeExtractor:

    def __init__(self, args):
        self.attributes = args.attributes
        self.dachart = DachartExtractor()
        self.anordnung_gaertnerisch = AnordnungGaertnerischeAusgestaltungExtractor()
        self.gebaeude_hoehe_max = GebaeudeHoeheMaxExtractor()
        self.dachneigung_max = DachneigungMaxExtractor()
        self.flaechen = FlaechenExtractor()

    def extract(self, doc):
        items = []
        if DocumentFields.SENS in doc:
            items = doc[DocumentFields.SENS].values()
        else:
            items = [doc]
        for sen in items:
            for attribute in self.attributes:
                self._extract_for_attr(sen, attribute)
        sys.stdout.write(json.dumps(doc) + "\n")

    def _extract_for_attr(self, sen, attribute):
        att_type = None
        if contains_attr(sen, attribute):
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
            self._add_to_gen_values(sen, attribute, att_type)


    def _add_to_gen_values(self, sen, attribute, attr_type):
        if attribute not in sen[SenFields.GEN_ATTRIBUTES]:
            sen[SenFields.GEN_ATTRIBUTES][attribute] = {
                AttributeFields.VALUE: [],
                AttributeFields.TYPE: None,
                AttributeFields.NAME: attribute,
            }
        sen[SenFields.GEN_ATTRIBUTES][attribute][AttributeFields.TYPE] = attr_type

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-a", "--attributes", nargs="+", default=None)
    return parser.parse_args()

def main():
    args = get_args()
    value_extractor = TypeExtractor(args)
    for line in sys.stdin:
        doc = json.loads(line)
        value_extractor.extract(doc)


if __name__ == "__main__":
    main()