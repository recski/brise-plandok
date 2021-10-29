import re

from brise_plandok.value_extraction.constants import NUMBER_WITH_METER

VALUES = {
    # w/o jeweils
    r".*Gehsteige? mit mindestens " + NUMBER_WITH_METER: 1,
    # with jeweils
    r".*Gehsteige? mit (jeweils|einer Breite von) mindestens " + NUMBER_WITH_METER: 2,
}

class GehsteigBreiteMinExtractor:

    def extract(self, text):
        for regex, group in VALUES.items():
            m = re.search(regex, text)
            if m is not None:
                yield m.group(group)
