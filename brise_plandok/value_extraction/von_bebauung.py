import re

VALUES = [
    # jeder Bebauung
    r".*(von( jeder)? Bebauung).*",
    # Baute
    r".*((ober|unter)irdische(n|r)? (Bauten?|Bebauung|Bauwerk(en)?)).*",
    # Gebäude
    r".*((ober- und unterirdischen|oberirdischer) Gebäude).*",
    # keine Bauwerke
    r".*(keine Bauwerke).*",
]

class VonBebauungFreizuhaltenExtractor:

    def extract(self, text):
        for regex in VALUES:
            m = re.search(regex, text)
            if m is not None:
                yield m.group(1)
