import re

VALUES = {
    r".*(bis zu einer Dachneigung von|maximal|bis) ((\d\d*( ?, ?\d\d*)?|.*)(°| Grad)).*": 2,
    r".*zwischen ((\d\d*( ?, ?\d\d*)?|.*)(°| Grad)) und ((\d\d*( ?, ?\d\d*)?|.*)(°| Grad)).*": 5,
}

class DachneigungMaxExtractor:

    def extract(self, text):
        for regex, group in VALUES.items():
            m = re.match(regex, text)
            if m is not None:
                yield m.group(group)
