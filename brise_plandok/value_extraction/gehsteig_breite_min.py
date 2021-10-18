import re

VALUES = [
    # w/o jeweils
    r".*Gehsteige? mit mindestens (\d*,\d*|\d*) ?.*",
    # with jeweils
    r".*Gehsteige? mit (jeweils|einer Breite von) mindestens (\d*,\d*|\d*) ?.*",
]

class GehsteigBreiteMinExtractor:

    def extract(self, text):
        for regex in VALUES:
            m = re.match(regex, text)
            if m is not None:
                yield m.group(1)
