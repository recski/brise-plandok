from brise_plandok.constants import ATTRIBUTE_NORM_MAP


def normalize_attribute_name(attribute_name):
    if attribute_name in ATTRIBUTE_NORM_MAP:
        return ATTRIBUTE_NORM_MAP[attribute_name]
    return attribute_name