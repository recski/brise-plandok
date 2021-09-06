from brise_plandok.constants import ATTRIBUTE_NORMALIZE_MAP


def normalize_attribute_name(attribute_name):
    if attribute_name in ATTRIBUTE_NORMALIZE_MAP:
        return ATTRIBUTE_NORMALIZE_MAP[attribute_name]
    return attribute_name