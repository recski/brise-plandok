import re

from brise_plandok.constants import AttributeTypes

VALUES = {
    r".*sind [^ ]*(dach|dächer).*": AttributeTypes.CONDITION,
    r".*(dach|dächer) dürfen.*": AttributeTypes.CONDITION,
    r".*(dach|dächer) bis zu.*": AttributeTypes.CONDITION,
    r".*(dach|dächer), die.*": AttributeTypes.CONDITION,
    r".*(dach|dächer)(flächen)? sind.*": AttributeTypes.CONDITION,
    r".*Errichtung gelangende .*(dach|dächer).*": AttributeTypes.CONDITION,
    r".*als( begrünte)? .*(dach|dächer).*": AttributeTypes.CONTENT,
    r".*mit .*(dach|dächern) auszu.*": AttributeTypes.CONTENT,
    r".*(dach|dächern) zulässig.*": AttributeTypes.CONTENT,
}

class DachartExtractor:

    def extract(self, text):
        for regex, type in VALUES.items():
            m = re.search(regex, text)
            if m is not None:
                return type
