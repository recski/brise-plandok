import re

from brise_plandok.full_attribute_extraction.utils.constants import TRUE

VALUES = {
    r".*": TRUE,
}

class PlangebietAllgemeinExtractor:

    def extract(self, text):
        for regex, value in VALUES.items():
            m = re.search(regex, text)
            if m is not None:
                yield value
