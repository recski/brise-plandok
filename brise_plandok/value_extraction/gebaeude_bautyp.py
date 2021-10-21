import re

VALUES = [
    # Haupt
    r".*(Hauptgebäude).*",
    # Neben
    r".*(Nebengebäude).*",
    # Glas
    r".*(Glashaus|Glashäuser).*",
    # Kleingarten
    r".*(Kleingartenhäuser).*",
    # Kleingarten wohn
    r".*(Kleingartenwohnhäuser).*",
]

class GebaeudeBautypExtractor:

    def extract(self, text):
        for regex in VALUES:
            m = re.match(regex, text)
            if m is not None:
                yield m.group(1)
