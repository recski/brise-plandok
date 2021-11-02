import re

VALUES = [
    # BB
    r".*(BB\d?).*",
    # G
    r".*\s(G)\s.*",
    r".*\s\((G)\)\s.*",
    # L
    r".*\s(L)\s.*",
    r".*\s\((L)\)\s.*",
    # Esp
    r".*\s(Esp)\s.*",
    # öDg
    r".*\s(öDg)\s.*",
    # Str
    r".*\s(StrG)\s.*",
]

class PlanzeichenExtractor:

    def extract(self, text):
        for regex in VALUES:
            m = re.search(regex, text)
            if m is not None:
                yield m.group(1)
