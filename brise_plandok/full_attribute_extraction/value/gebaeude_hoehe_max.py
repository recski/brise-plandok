import re

VALUES = [
    r".*(Gebäudehöhe|Höhe) \D*(\d\d*( ?, ?\d\d*)? ?m).*",
]

class GebaeudeHoeheMaxExtractor:

    def extract(self, text):
        for regex in VALUES:
            m = re.search(regex, text)
            if m is not None:
                yield m.group(2)
