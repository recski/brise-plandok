import json

from brise_plandok.constants import SenFields

def contains_attr(sen, attr_name):
    return attr_name in sen[SenFields.GOLD_ATTRIBUTES].keys()
