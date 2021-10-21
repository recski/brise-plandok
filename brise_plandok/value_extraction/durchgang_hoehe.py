import re

VALUES = {
    r".*(H|h)öhe von( mindestens)? (\d\d*( ?, ?\d\d*)? ?m).*": 3,
    r".* (\d\d*( ?, ?\d\d*)? ?m) (H|h)öhe.*": 1,
}

class DurchgangHoeheExtractor:

    def extract(self, text):
        for regex, group in VALUES.items():
            m = re.match(regex, text)
            if m is not None:
                yield m.group(group)
