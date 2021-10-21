import re

from brise_plandok.constants import AttributeTypes

VALUES = {
    r".*für die die gärtnerische Ausgestaltung (vorgeschrieben|angeordnet) ist.*": AttributeTypes.CONDITION,
    r".*auf gärtnerisch auszugestaltenden (Grundf|F)lächen.*": AttributeTypes.CONDITION,
    r".*die angrenzende gärtnerisch auszugestaltenden.*": AttributeTypes.CONDITION,
}

class AnordnungGaertnerischeAusgestaltungExtractor:

    def extract(self, text):
        for regex, type in VALUES.items():
            m = re.match(regex, text)
            if m is not None:
                return type
