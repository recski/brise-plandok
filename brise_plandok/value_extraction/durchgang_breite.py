import re

VALUES = {
    r".*(B|b)reite von( mindestens)? (\d\d*( ?, ?\d\d*)? ?m).*": 3,
    r".* (\d\d*( ?, ?\d\d*)? ?m) (B|b)reite.*": 1,
}

class DurchgangBreiteExtractor:

    def extract(self, text):
        for regex, group in VALUES.items():
            m = re.match(regex, text)
            if m is not None:
                yield m.group(group)
