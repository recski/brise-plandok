import json
import logging
import os

import pandas as pd

from brise_plandok.constants import SenFields, DocumentFields


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


def update_gold_docs(gold_attr_candidate, gold_mod_candidate, current_gold_sens, gold_folder):
    update_map = {}
    for sen_id in current_gold_sens:
        doc_id = sen_id.split("_")[0]
        if doc_id not in update_map:
            update_map[doc_id] = [sen_id]
        else:
            update_map[doc_id].append(sen_id)
    logging.info(f"The following docs and sentences will be updated: {update_map}")
    for doc_id in update_map.keys():
        fn = os.path.join(gold_folder, doc_id + ".json")
        doc = load_json(fn)
        for sen_id in update_map[doc_id]:
            doc[DocumentFields.SENS][sen_id][SenFields.GOLD_ATTRIBUTES] = gold_attr_candidate
            doc[DocumentFields.SENS][sen_id][SenFields.GOLD_MODALITY] = gold_mod_candidate
        dump_json(doc, fn)


def create_input(directory):
    ids = []
    sentences = []
    labels = []
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), "rt") as f:
            doc = json.load(f)
            for sen in doc[DocumentFields.SENS].values():
                ids.append(sen[SenFields.ID])
                sentences.append(sen[SenFields.TEXT])
                labels.append(set(sen[SenFields.GOLD_ATTRIBUTES].keys()))
    return pd.DataFrame(data=list(zip(ids, sentences, labels)), columns=["ID", "Text", "Labels"])
