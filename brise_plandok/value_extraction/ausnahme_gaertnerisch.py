import re

VALUES = {
    r".*mit Ausnahme( der| von)? ([^:]*),? gärtnerisch auszugestalten.*": 2,
    r".*mit Ausnahme( der| von)? (.*), wird bestimmt*": 2,
    r".*soweit sie nicht (für|als) (.*) benötigt werden, .*gärtnerisch.*": 2,
    r".*soweit nicht (.*) erforderlich ist, gärtnerisch auszugestalten.*": 1,
    r".*nicht von (.*) in Anspruch genommenen Bereiche,? sind gärtnerisch auszugestalten.*": 1,
    r".*(A|a)usgenommen davon sind (.*).": 2,
}

class AusnahmeGaertnerischAuszugestaltendeExtractor:

    def extract(self, text):
        for regex, group in VALUES.items():
            m = re.match(regex, text)
            if m is not None:
                yield m.group(group)
