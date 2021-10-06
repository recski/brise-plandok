import re

VALUES = [
    # all
    r".*((Erhaltung|Pflanzung|Pflanzen|Herstellung) .* (ermöglichen|ermöglicht|zu treffen|vorhanden bleiben|möglich|geschaffen werden können)).*",
]

class VorkehrungBepflanzungExtractor:

    def extract(self, text):
        for regex in VALUES:
            m = re.match(regex, text)
            if m is not None:
                yield m.group(1)
