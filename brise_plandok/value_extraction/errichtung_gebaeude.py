import re

VALUES = {
    r".*(darf unmittelbar bebaut werden|sind unmittelbar bebaubar|Errichtung .* zulässig).*": True,
    r".*(Errichtung .* (untersagt|unzulässig)|keine .* errichtet werden).*": False,
}

class ErrichtungGebaeudeExtractor:

    def extract(self, text):
        for regex, value in VALUES.items():
            m = re.match(regex, text)
            if m is not None:
                yield value
