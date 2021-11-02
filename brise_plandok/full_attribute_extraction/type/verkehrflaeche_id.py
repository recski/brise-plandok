import re

from brise_plandok.constants import AttributeTypes

VALUES = {
    r".*": AttributeTypes.CONDITION,
}

class VerkehrsflaecheIDExtractor:

    def extract(self, text):
        for regex, type in VALUES.items():
            m = re.search(regex, text)
            if m is not None:
                return type
