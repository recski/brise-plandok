import re

from brise_plandok.constants import AttributeTypes
from brise_plandok.full_attribute_extraction.utils.constants import AREA_SIZE

VALUES = {
    # Bebaubarkeit
    r".*(((b|B)ebaubare,? jedoch)? unbebaut bleibenden? (Grund|Bauland)?(F|f)lächen?).*": AttributeTypes.CONDITION,
    r".*((N|n)icht bebaute,? jedoch bebaubare (Grund|Bauland)flächen?).*": AttributeTypes.CONDITION,
    r".*((B|b)ebaubaren?,? (aber )?von Bebauung freibleibenden? (Grund|Bauland)flächen?).*": AttributeTypes.CONDITION,
    r".*unbebauten? Fläche.*": AttributeTypes.CONDITION,
    # Maximum
    r".*((in Summe|in Anspruch genommene Gesamtnutzfläche) " + AREA_SIZE + r" nicht überschreiten).*": AttributeTypes.CONTENT,
    r".*(höchstens " + AREA_SIZE + r").*": AttributeTypes.CONTENT,
    r".*(maximal(en Grundfläche von( insgesamt)?)? " + AREA_SIZE + r").*": AttributeTypes.CONTENT,
    r".*(bis zu einem (Flächen)?(A|a)usmaß von " + AREA_SIZE + r").*": AttributeTypes.CONTENT,
    r".*(die bebaute Fläche nicht mehr als " + AREA_SIZE + r").*": AttributeTypes.CONTENT,
    # Minimum
    r".*(f|F)lächen? (von mehr als " + AREA_SIZE + r").*": AttributeTypes.CONTENT,
    r".*((m|M)indestens " + AREA_SIZE + r").*": AttributeTypes.CONTENT,
    r".*(nicht weniger als " + AREA_SIZE + r").*": AttributeTypes.CONTENT,
}

class FlaechenExtractor:

    def extract(self, text):
        for regex, attr_type in VALUES.items():
            m = re.search(regex, text)
            if m is not None:
                return attr_type
