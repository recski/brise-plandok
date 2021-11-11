import re

VALUES = {
    # all
    r".*(((die Erhaltung|die Pflanzung|das Pflanzen|die Herstellung) .*) (zu ermöglichen|ermöglicht|zu treffen|vorhanden bleiben|möglich|geschaffen werden können)).*": 2,
}

class VorkehrungBepflanzungExtractor:

    def extract(self, text):
        for regex, group in VALUES.items():
            m = re.search(regex, text)
            if m is not None:
                yield m.group(group)
