import re

from brise_plandok.constants import AttributeTypes

VALUES = {
    r".*bis zu einer (Dachn|N)eigung von.*": AttributeTypes.CONDITION,
    r".*mit einer (Dachn|N)eigung bis.*": AttributeTypes.CONDITION,
}

class DachneigungMaxExtractor:

    def extract(self, text):
        for regex, type in VALUES.items():
            m = re.match(regex, text)
            if m is not None:
                return type
