import re

AREA_SIZE = r"(\d\d*.\d*) ?(m ?(²|2)|v. ?H.?|%)"

VALUES = {
    # Bebaubarkeit
    r".*(((b|B)ebaubare,? jedoch)? unbebaut bleibenden? (Grund|Bauland)?(F|f)lächen?).*": 1,
    r".*((N|n)icht bebaute,? jedoch bebaubare (Grund|Bauland)flächen?).*": 1,
    r".*((B|b)ebaubaren?,? (aber )?von Bebauung freibleibenden? (Grund|Bauland)flächen?).*": 1,
    r".*(bebauten? Fläche).*": 1,
    # Maximum
    r".*((in Summe|in Anspruch genommene Gesamtnutzfläche) " + AREA_SIZE + r" nicht überschreiten).*": 1,
    r".*(höchstens " + AREA_SIZE + r").*": 1,
    r".*(maximal(en Grundfläche von( insgesamt)?)? " + AREA_SIZE + r").*": 1,
    r".*(bis zu einem (Flächen)?(A|a)usmaß von " + AREA_SIZE + r").*": 1,
    # Minimum
    r".*(f|F)lächen? (von mehr als " + AREA_SIZE + r").*": 2,
    r".*((m|M)indestens " + AREA_SIZE + r").*": 1,
    r".*(nicht weniger als " + AREA_SIZE + r").*": 1,
}

class FlaechenExtractor:

    def extract(self, text):
        for regex, group in VALUES.items():
            m = re.match(regex, text)
            if m is not None:
                yield m.group(group)
