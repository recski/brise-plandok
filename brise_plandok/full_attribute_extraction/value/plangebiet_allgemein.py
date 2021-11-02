import re

VALUES = {
    r".*": True,
}

class PlangebietAllgemeinExtractor:

    def extract(self, text):
        for regex, value in VALUES.items():
            m = re.search(regex, text)
            if m is not None:
                yield value
