import argparse
import json
import sys

from brise_plandok.constants import AttributeFields, AttributesNames, DocumentFields, SenFields
from brise_plandok.value_extraction.abschuss_gebaeude import AbschlussDachMaxBezugGebaeudeExtractor
from brise_plandok.value_extraction.ausnahme_gaertnerisch import AusnahmeGaertnerischAuszugestaltendeExtractor
from brise_plandok.value_extraction.dachart import DachartExtractor
from brise_plandok.value_extraction.dachneigung_max import DachneigungMaxExtractor
from brise_plandok.value_extraction.durchgang_breite import DurchgangBreiteExtractor
from brise_plandok.value_extraction.durchgang_hoehe import DurchgangHoeheExtractor
from brise_plandok.value_extraction.errichtung_gebaeude import ErrichtungGebaeudeExtractor
from brise_plandok.value_extraction.flaechen import FlaechenExtractor
from brise_plandok.value_extraction.gebaeude_bautyp import GebaeudeBautypExtractor
from brise_plandok.value_extraction.gebaeude_hoehe_art import GebaeudeHoeheArtExtractor
from brise_plandok.value_extraction.gebaeude_hoehe_max import GebaeudeHoeheMaxExtractor
from brise_plandok.value_extraction.gehsteig_breite_min import GehsteigBreiteMinExtractor
from brise_plandok.value_extraction.planzeichen import PlanzeichenExtractor
from brise_plandok.value_extraction.strassenbreite_min import StrassenbreiteMinExtractor
from brise_plandok.value_extraction.utils import contains_attr
from brise_plandok.value_extraction.von_bebauung import VonBebauungFreizuhaltenExtractor
from brise_plandok.value_extraction.vorkehrung_bepflanzung import VorkehrungBepflanzungExtractor
from brise_plandok.value_extraction.wuz import WidmungUndZweckbestimmungExtractor
from brise_plandok.value_extraction.wuz_mehrere import WidmungInMehrerenEbenenExtractor

class ValueExtractor:

    def __init__(self, attributes=[]):
        self.attributes = attributes
        self.planzeichen = PlanzeichenExtractor()
        self.dachart = DachartExtractor()
        self.gehsteig = GehsteigBreiteMinExtractor()
        self.vorkehrung = VorkehrungBepflanzungExtractor()
        self.vonbebauung = VonBebauungFreizuhaltenExtractor()
        self.gebaeude_bautyp = GebaeudeBautypExtractor()
        self.gebaeude_hoehe_art = GebaeudeHoeheArtExtractor()
        self.gebaeude_hoehe_max = GebaeudeHoeheMaxExtractor()
        self.strassenbreite_min = StrassenbreiteMinExtractor()
        self.abschuss_geb = AbschlussDachMaxBezugGebaeudeExtractor()
        self.durchgang_breite = DurchgangBreiteExtractor()
        self.durchgang_hoehe = DurchgangHoeheExtractor()
        self.errichtung_gebaeude = ErrichtungGebaeudeExtractor()
        self.ausnahme_gaertnerisch = AusnahmeGaertnerischAuszugestaltendeExtractor()
        self.dachneigung_max = DachneigungMaxExtractor()
        self.wuz = WidmungUndZweckbestimmungExtractor()
        self.wuz_mehrere = WidmungInMehrerenEbenenExtractor()
        self.flaechen = FlaechenExtractor()

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

    def extract_for_attr(self, sen, attribute, field_to_add = SenFields.GEN_ATTRIBUTES, only_if_gold=True):
        values = []
        if not only_if_gold or contains_attr(sen, attribute):
            if attribute == AttributesNames.PLANZEICHEN:
                values = [value for value in self.planzeichen.extract(sen[SenFields.TEXT])]
            elif attribute == AttributesNames.DACHART:
                values = [value for value in self.dachart.extract(sen[SenFields.TEXT])]
            elif attribute == AttributesNames.GEHSTEIG_BREITE_MIN:
                values = [value for value in self.gehsteig.extract(sen[SenFields.TEXT])]
            elif attribute == AttributesNames.VORKEHRUNG_BEPFLANZUNG:
                values = [value for value in self.vorkehrung.extract(sen[SenFields.TEXT])]
            elif attribute == AttributesNames.VON_BEBAUUNG_FREIZUHALTEN:
                values = [value for value in self.vonbebauung.extract(sen[SenFields.TEXT])]
            elif attribute == AttributesNames.GEBAEUDE_BAUTYP:
                values = [value for value in self.gebaeude_bautyp.extract(sen[SenFields.TEXT])]
            elif attribute == AttributesNames.GEBAEUDE_HOEHE_ART:
                values = [value for value in self.gebaeude_hoehe_art.extract(sen[SenFields.TEXT])]
            elif attribute == AttributesNames.GEBAEUDE_HOEHE_MAX:
                values = [value for value in self.gebaeude_hoehe_max.extract(sen[SenFields.TEXT])]
            elif attribute == AttributesNames.STRASSENBREITE_MIN:
                values = [value for value in self.strassenbreite_min.extract(sen[SenFields.TEXT])]
            elif attribute == AttributesNames.ABSCHUSS_GEBAEUDE:
                values = [value for value in self.abschuss_geb.extract(sen[SenFields.TEXT])]
            elif attribute == AttributesNames.DURCHGANG_BREITE:
                values = [value for value in self.durchgang_breite.extract(sen[SenFields.TEXT])]
            elif attribute == AttributesNames.DURCHGANG_HOEHE:
                values = [value for value in self.durchgang_hoehe.extract(sen[SenFields.TEXT])]
            elif attribute == AttributesNames.ERRICHTUNG_GEBAEUDE:
                values = [value for value in self.errichtung_gebaeude.extract(sen[SenFields.TEXT])]
            elif attribute == AttributesNames.AUSNAHME_GAERTNERISCH:
                values = [value for value in self.ausnahme_gaertnerisch.extract(sen[SenFields.TEXT])]
            elif attribute == AttributesNames.DACHNEIGUNG_MAX:
                values = [value for value in self.dachneigung_max.extract(sen[SenFields.TEXT])]
            elif attribute == AttributesNames.WuZ:
                values = [value for value in self.wuz.extract(sen[SenFields.TEXT])]
            elif attribute == AttributesNames.WIDMUNG_IN_MEHREREN_EBENEN:
                values = [value for value in self.wuz_mehrere.extract(sen[SenFields.TEXT])]
            elif attribute == AttributesNames.FLAECHEN:
                values = [value for value in self.flaechen.extract(sen[SenFields.TEXT])]
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