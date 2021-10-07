import re

VALUES = [
    # Flach
    r".*(Flach).*",
    # Pult
    r".*(Pult).*",
    # Glas
    r".*(Glas).*",
    # Flug
    r".*(Flug).*",
    # Vor
    r".*(Vor).*",
]

class DachartExtractor:

    def extract(self, text):
        for regex in VALUES:
            m = re.match(regex, text)
            if m is not None:
                yield m.group(1)
