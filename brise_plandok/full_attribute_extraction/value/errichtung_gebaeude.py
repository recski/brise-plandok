import re

from brise_plandok.full_attribute_extraction.utils.constants import FALSE, TRUE

VALUES = {
    r".*(darf unmittelbar bebaut werden|sind unmittelbar bebaubar|Errichtung .* zulässig).*": TRUE,
    r".*(Errichtung .* (untersagt|unzulässig)|keine .* errichtet werden).*": FALSE,
}

class ErrichtungGebaeudeExtractor:

    def extract(self, text):
        for regex, value in VALUES.items():
            m = re.search(regex, text)
            if m is not None:
                yield value
