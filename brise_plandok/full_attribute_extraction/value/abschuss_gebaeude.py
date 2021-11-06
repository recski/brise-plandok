import re

from brise_plandok.full_attribute_extraction.utils.constants import NUMBER_WITH_METER

VALUES = [
    r".*(nicht höher als|nicht mehr als|höchstens|maximal) " + NUMBER_WITH_METER + r" über.*",
]

class AbschlussDachMaxBezugGebaeudeExtractor:

    def extract(self, text):
        for regex in VALUES:
            m = re.search(regex, text)
            if m is not None:
                yield m.group(2)
