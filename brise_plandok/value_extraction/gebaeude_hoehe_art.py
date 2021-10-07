import re

VALUES = [
    r".*(tatsächlich errichtet).*",
    r".*(ausgeführt).*",
    r".*(festgesetzt).*",
    r".*(zulässig).*",
]

class GebaeudeHoeheArtExtractor:

    def extract(self, text):
        for regex in VALUES:
            m = re.match(regex, text)
            if m is not None:
                yield m.group(1)
