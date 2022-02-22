import json
import logging
import os

from brise_plandok.constants import SenFields


def load_json(fn):
    logging.debug(f"loading {fn}")
    if os.path.exists(fn):
        with open(fn) as f:
            return json.load(f)
    return None


def dump_json(obj, fn):
    logging.debug(f"dumping {fn}")
    with open(fn, "w") as f:
        json.dump(obj, f)


def is_gold_attribute(sen, attr_name):
    return attr_name in sen[SenFields.GOLD_ATTRIBUTES].keys()
