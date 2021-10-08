import re

VALUES = [
    r".*(nicht höher als|nicht mehr als|höchstens|maximal) (\d\d*( ?, ?\d\d*)? ?m) über.*",
]

class AbschlussDachMaxBezugGebaeudeExtractor:

    def extract(self, text):
        for regex in VALUES:
            m = re.match(regex, text)
            if m is not None:
                yield m.group(2)
