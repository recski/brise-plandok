import re

from brise_plandok.constants import AttributeTypes

VALUES = {
    r".* (mit|bis zu) einer Gebäudehöhe von( bis zu)? \d\d m.*": AttributeTypes.CONDITION,
}

class GebaeudeHoeheMaxExtractor:

    def extract(self, text):
        for regex, type in VALUES.items():
            m = re.match(regex, text)
            if m is not None:
                return type
