import json
import logging
import os

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


def make_markdown_table(array):
    """Input: Python lists with rows of table as lists
               First element as header.
        Output: String to put into a .md file

    Ex Input:
        [["Name", "Age", "Height"],
         ["Jake", 20, 5'10],
         ["Mary", 21, 5'7]]

    Source: https://gist.github.com/m0neysha/219bad4b02d2008e0154
    """

    markdown = "\n" + str("| ")

    for e in array[0]:
        to_add = " " + str(e) + str(" |")
        markdown += to_add
    markdown += "\n"

    markdown += "|"
    for i in range(len(array[0])):
        markdown += str("-------------- | ")
    markdown += "\n"

    for entry in array[1:]:
        markdown += str("| ")
        for e in entry:
            if type(e) == int:
                e = str(e)
            elif type(e) == float:
                e = f"{e:.3f}"
            to_add = e + str(" | ")
            markdown += to_add
        markdown += "\n"

    return markdown + "\n"
