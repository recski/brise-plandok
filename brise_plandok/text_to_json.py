import argparse
import logging
import os.path

from tqdm import tqdm
from tuw_nlp.text.pipeline import CachedStanzaPipeline, CustomStanzaPipeline

from brise_plandok.attrs_from_gold import SenToAttrMap
from brise_plandok.plandok import parse_txt
from brise_plandok.utils import dump_json
from brise_plandok.data_utils import fill_json


def text_to_json(text_dir, json_dir, doc_ids):
    assert os.path.exists(text_dir)
    assert os.path.exists(json_dir)
    sen_to_gold_attrs = SenToAttrMap(gold_dir=json_dir, fuzzy=True, full=False) if json_dir else None
    sen_to_full_gold_attrs = SenToAttrMap(gold_dir=json_dir, fuzzy=False, full=True) if json_dir else None

    with CachedStanzaPipeline(CustomStanzaPipeline(), 'cache/nlp_cache.json') as nlp:
        for doc_id in tqdm(doc_ids):
            txt_path = os.path.join(text_dir, doc_id + ".txt")
            assert os.path.exists(txt_path)
            json_path = os.path.join(json_dir, doc_id + ".json")
            if os.path.exists(json_path):
                logging.info(f"Json {json_path} already exists - skipping document")
            else:
                doc = parse_txt(txt_path, nlp)
                filled_json = fill_json(doc, sen_to_gold_attrs, sen_to_full_gold_attrs, old_doc=True)
                dump_json(filled_json, json_path)


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-t", "--text-dir", type=str)
    parser.add_argument("-j", "--json-dir", type=str)
    parser.add_argument("-d", "--doc-ids", type=str, nargs="+")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    text_to_json(args.text_dir, args.json_dir, args.doc_ids)
