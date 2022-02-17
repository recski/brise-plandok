import re

from brise_plandok.constants import AttributeFields, SenFields
from brise_plandok.full_attribute_extraction.type.type_patterns import TYPE_PATTERNS
from brise_plandok.full_attribute_extraction.constants import TYPE
from brise_plandok.utils import is_gold_attribute


def extract_type(sen, attribute, field_to_add=SenFields.GEN_ATTRIBUTES, only_gold=True):
    if not only_gold or is_gold_attribute(sen, attribute):
        att_type = _match_types(attribute, sen[SenFields.TEXT])
        if field_to_add is None:
            return att_type
        _add_to_gen_values(sen, attribute, att_type, field_to_add)


def _match_types(attribute, text):
    if attribute in TYPE_PATTERNS:
        for pattern, resolution in TYPE_PATTERNS[attribute].items():
            m = re.search(pattern, text)
            if m is not None:
                if TYPE in resolution:
                    return resolution[TYPE]


def _add_to_gen_values(sen, attribute, attr_type, field_to_add):
    if attribute not in sen[field_to_add]:
        sen[field_to_add][attribute] = {
            AttributeFields.VALUE: [],
            AttributeFields.TYPE: None,
            AttributeFields.NAME: attribute,
        }
    sen[field_to_add][attribute][AttributeFields.TYPE] = attr_type
