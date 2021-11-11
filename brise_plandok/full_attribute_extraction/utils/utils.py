import re
from brise_plandok.constants import SenFields
from brise_plandok.full_attribute_extraction.utils.constants import GROUP, VALUE
from brise_plandok.full_attribute_extraction.value.patterns import VALUE_PATTERNS

def contains_attr(sen, attr_name):
    return attr_name in sen[SenFields.GOLD_ATTRIBUTES].keys()

def extract_values(attribute, text):
    if attribute in VALUE_PATTERNS:
        for pattern, resolution in VALUE_PATTERNS[attribute].items():
            m = re.search(pattern, text)
            if m is not None:
                if GROUP in resolution:
                    yield m.group(resolution[GROUP])
                if VALUE in resolution:
                    yield resolution[VALUE]
