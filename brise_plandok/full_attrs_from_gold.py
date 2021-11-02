import argparse
from brise_plandok.constants import DocumentFields, SenFields
import json
import logging
import os
import re
import sys

from tqdm import tqdm


class SenToFullAttrMap():
    fuzzy_patt = re.compile('[0-9]+')

    def __init__(self, gold_dir, fuzzy):
        self.fuzzy = fuzzy
        self.build_map(gold_dir)

    def gen_sens_attrs(self, gold_dir):
        if not os.path.exists(gold_dir):
            raise ValueError(f'path does not exist: {gold_dir}')
        for fn in os.listdir(gold_dir):
            if not (fn.endswith('json') or fn.endswith('jsonl')):
                logging.warning(f'skipping file not ending in json(l): {fn}')
                continue
            with open(os.path.join(gold_dir, fn)) as f:
                for line in f:
                    doc = json.loads(line)
                    if doc[DocumentFields.FULL_GOLD]:
                        for sen_id, sen in doc[DocumentFields.SENS].items():
                            gold_attrs = sen.get(SenFields.GOLD_ATTRIBUTES)
                            sen_id = sen.get(SenFields.ID)
                            yield sen_id, sen[SenFields.TEXT], gold_attrs, fn

    def sen_to_key(self, sen):
        if not self.fuzzy:
            return sen
        else:
            return SenToFullAttrMap.fuzzy_patt.sub('', sen)

    def build_map(self, gold_dir):
        self.sen_to_attr = {}
        for sen_id, sen, attr, fn in self.gen_sens_attrs(gold_dir):
            sen_key = self.sen_to_key(sen)
            if sen_key in self.sen_to_attr:
                if self.sen_to_attr[sen_key]["attr"] == attr:
                    self.sen_to_attr[sen_key]["sens"].append(sen_id)
                    continue
                else:
                    self.log_conflict(sen, sen_key)
                    raise ValueError(f'gold conflict')

            self.sen_to_attr[sen_key] = {
                "attr": attr, 
                "sens": [
                    sen_id
                ]
            }

    def get_attrs(self, sen):
        sen_key = self.sen_to_key(sen)
        full_attr = self.sen_to_attr.get(sen_key)
        if full_attr is None:
            return None
        return full_attr["attr"]

    def get_sens(self, sen):
        sen_key = self.sen_to_key(sen)
        full_attr = self.sen_to_attr.get(sen_key)
        if full_attr is None:
            return None
        return full_attr["sens"]

    def log_conflict(self, sen, sen_key=None):
        if sen_key is None:
            sen_key = self.sen_to_key(sen[SenFields.TEXT])
        old_attrs = json.dumps(self.sen_to_attr[sen_key]["attr"], indent=2)
        old_sens = self.sen_to_attr[sen_key]["sens"]
        new_attrs = json.dumps(sen[SenFields.GOLD_ATTRIBUTES], indent=2)
        new_sen = sen[SenFields.ID]
        logging.error(f"matching sens in gold with different attrs:\n" + 
            f"\nold attrs {old_sens}:\n{old_attrs}\n\nnew attrs {new_sen}:\n{new_attrs}\n")


def attrs_from_gold_sen(sen, sen_to_attr, overwrite):
    attrs = sen_to_attr.get_attrs(sen['text'])

    if SenFields.LABELS_GOLD_EXISTS in sen and sen[SenFields.LABELS_GOLD_EXISTS]:
        if overwrite:
            if sen[SenFields.LABELS_GOLD_EXISTS]:
                del sen[SenFields.GEN_ATTRIBUTES]
                sen[SenFields.LABELS_GOLD_EXISTS] = False
        else:
            if sen[SenFields.GOLD_ATTRIBUTES] != attrs:
                sen_to_attr.log_conflict(sen)
                raise ValueError(
                    'field "labels_gold_exists" already present in input and'
                    '--overwrite not set')
    else:
        sen[SenFields.LABELS_GOLD_EXISTS] = False

    if attrs is not None:
        sen[SenFields.LABELS_GOLD_EXISTS] = True
        sen[SenFields.GOLD_ATTRIBUTES] = attrs


def attrs_from_gold(args):
    logging.info('building map...')
    sen_to_attr = SenToAttrMap(gold_dir=args.gold_dir, fuzzy=args.fuzzy)
    logging.info('done, processing docs...')
    for line in tqdm(sys.stdin):
        doc = json.loads(line)
        for section in doc['sections']:
            for sen in section['sens']:
                attrs_from_gold_sen(sen, sen_to_attr, args.overwrite)
        sys.stdout.write(json.dumps(doc))
        sys.stdout.write('\n')


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-g", "--gold-dir", type=str)
    parser.add_argument("-f", "--fuzzy", default=False, action='store_true')
    parser.add_argument(
        "-o", "--overwrite", default=False, action='store_true')
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " +
        "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()

    attrs_from_gold(args)


if __name__ == "__main__":
    main()
