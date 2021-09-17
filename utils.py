from brise_plandok.constants import ATTRIBUTE_NORM_MAP
import json

def normalize_attribute_name(attribute_name):
    if attribute_name in ATTRIBUTE_NORM_MAP:
        return ATTRIBUTE_NORM_MAP[attribute_name]
    return attribute_name

def load_json(fn):
    with open(fn) as f:
        return json.load(f)

def dump_json(obj, fn):
    with open(fn, "w") as f:
        json.dump(obj, f)