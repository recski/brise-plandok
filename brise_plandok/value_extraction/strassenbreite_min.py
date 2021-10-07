import re

VALUES = [
    r".*Straßen(breiten?)? (ab|von mehr als|von über) (\d\d*( ?, ?\d\d*)? ?m).*",
]

class StrassenbreiteMinExtractor:

    def extract(self, text):
        for regex in VALUES:
            m = re.match(regex, text)
            if m is not None:
                yield m.group(3)
