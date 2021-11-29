import re
from brise_plandok.constants import SenFields
from brise_plandok.full_attribute_extraction.type.type_patterns import TYPE_PATTERNS
from brise_plandok.full_attribute_extraction.utils.constants import GROUP, TYPE, VALUE
from brise_plandok.full_attribute_extraction.value.value_patterns import VALUE_PATTERNS

def contains_attr(sen, attr_name):
    return attr_name in sen[SenFields.GOLD_ATTRIBUTES].keys()

def extract_values(attribute, text):
    if attribute in VALUE_PATTERNS:
        for pattern, resolution in VALUE_PATTERNS[attribute].items():
            matches = re.findall(pattern, text)
            for m in matches:
                if m is not None:
                    if VALUE in resolution:
                        yield resolution[VALUE]
                    elif type(m) is str:
                        yield m
                    elif GROUP in resolution:
                        yield m[resolution[GROUP]-1]

def extract_types(attribute, text):
    if attribute in TYPE_PATTERNS:
        for pattern, resolution in TYPE_PATTERNS[attribute].items():
            m = re.search(pattern, text)
            if m is not None:
                if TYPE in resolution:
                    return resolution[TYPE]
