import re
from brise_plandok.constants import SenFields, AttributeFields
from brise_plandok.full_attribute_extraction.constants import VALUE, GROUP
from brise_plandok.utils import is_gold_attribute
from brise_plandok.full_attribute_extraction.value.value_patterns import VALUE_PATTERNS


def extract_value(
    sen, attribute, field_to_add=SenFields.GEN_ATTRIBUTES, only_gold=True
):
    if not only_gold or is_gold_attribute(sen, attribute):
        values = list(
            set([value for value in _match_values(attribute, sen[SenFields.TEXT])])
        )
        if field_to_add is None:
            return values
        _add_to_gen_values(sen, attribute, values, field_to_add)


def _match_values(attribute, text):
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
                        yield m[resolution[GROUP] - 1]


def _add_to_gen_values(sen, attribute, values, field_to_add):
    if attribute not in sen[field_to_add]:
        sen[field_to_add][attribute] = {
            AttributeFields.VALUE: [],
            AttributeFields.TYPE: None,
            AttributeFields.NAME: attribute,
        }
    sen[field_to_add][attribute][AttributeFields.VALUE] = values
