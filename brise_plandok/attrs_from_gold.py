import argparse
from brise_plandok.constants import DocumentFields, SenFields
import json
import logging
import os
import re
import sys

from tqdm import tqdm


class SenToAttrMap():
    fuzzy_patt = re.compile('[0-9]+')

    def __init__(self, gold_dir, fuzzy, full=False):
        self.fuzzy = fuzzy
        self.build_map(gold_dir, full)

    def gen_sens_mod_attrs(self, gold_dir, full):
        if not os.path.exists(gold_dir):
            raise ValueError(f'path does not exist: {gold_dir}')
        for fn in os.listdir(gold_dir):
            if not (fn.endswith('json') or fn.endswith('jsonl')):
                logging.warning(f'skipping file not ending in json(l): {fn}')
                continue
            with open(os.path.join(gold_dir, fn)) as f:
                for line in f:
                    doc = json.loads(line)
                    if (full and doc[DocumentFields.FULL_GOLD]) or (not full and doc[DocumentFields.LABELS_GOLD]):
                        for sen_id, sen in doc[DocumentFields.SENS].items():
                            gold_attrs = sen.get(SenFields.GOLD_ATTRIBUTES)
                            if gold_attrs is None:
                                # support outputs from convert.py
                                gold_attrs = sen[SenFields.ATTRIBUTES]
                            sen_id = sen.get(SenFields.ID)
                            gold_modality = sen[SenFields.GOLD_MODALITY]
                            yield sen_id, sen[SenFields.TEXT], gold_modality, gold_attrs, fn

    def sen_to_key(self, sen):
        if not self.fuzzy:
            return sen
        else:
            return SenToAttrMap.fuzzy_patt.sub('', sen)

    def build_map(self, gold_dir, full):
        self.sen_to_attr = {}
        for sen_id, sen, mod, attr, fn in self.gen_sens_mod_attrs(gold_dir, full):
            sen_key = self.sen_to_key(sen)
            if sen_key in self.sen_to_attr:
                if self.sen_to_attr[sen_key]["attr"] == attr:
                    if self.sen_to_attr[sen_key]["mod"] == mod:
                        self.sen_to_attr[sen_key]["sens"].append(sen_id)
                        continue
                    else:
                        self.log_conflict(sen, sen_key, attr=False)
                        raise ValueError(f'gold conflict with modalities')
                else:
                    self.log_conflict(sen, sen_key, attr=True)
                    raise ValueError(f'gold conflict with attributes')

            self.sen_to_attr[sen_key] = {
                "attr": attr, 
                "sens": [
                    sen_id
                ],
                "mod": mod,
            }

    def get_attrs(self, sen):
        sen_key = self.sen_to_key(sen)
        full_attr = self.sen_to_attr.get(sen_key)
        if full_attr is None:
            return None
        return full_attr["attr"]

    def get_mod(self, sen):
        sen_key = self.sen_to_key(sen)
        full_attr = self.sen_to_attr.get(sen_key)
        if full_attr is None:
            return None
        return full_attr["mod"]

    def get_sens(self, sen):
        sen_key = self.sen_to_key(sen)
        full_attr = self.sen_to_attr.get(sen_key)
        if full_attr is None:
            return None
        return full_attr["sens"]

    def log_conflict(self, sen, sen_key=None, attr=True):
        if sen_key is None:
            sen_key = self.sen_to_key(sen[SenFields.TEXT])
        old_sens = self.sen_to_attr[sen_key]["sens"]
        new_sen = sen[SenFields.ID]
        if attr:
            old_attrs = json.dumps(self.sen_to_attr[sen_key]["attr"], indent=2)
            new_attrs = json.dumps(sen[SenFields.GOLD_ATTRIBUTES], indent=2)
            logging.error(f"matching sens in gold with different attrs:\n" +
                f"\nold attrs {old_sens}:\n{old_attrs}\n\nnew attrs {new_sen}:\n{new_attrs}\n")
        else:
            old_mod = json.dumps(self.sen_to_attr[sen_key]["mod"], indent=2)
            new_mod = json.dumps(sen[SenFields.GOLD_MODALITY], indent=2)
            logging.error(f"matching sens in gold with different attrs:\n" +
                f"\nold attrs {old_sens}:\n{old_mod}\n\nnew attrs {new_sen}:\n{new_mod}\n")


def attrs_from_gold_sen(sen, sen_to_attr, overwrite):
    attrs = sen_to_attr.get_attrs(sen['text'])

    if SenFields.LABELS_GOLD_EXISTS in sen and sen[SenFields.LABELS_GOLD_EXISTS]:
        if overwrite:
            del sen[SenFields.GOLD_ATTRIBUTES]
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


def full_attrs_from_gold_sen(sen, sen_to_attr, overwrite):
    attrs = sen_to_attr.get_attrs(sen['text'])
    mod = sen_to_attr.get_mod(sen['text'])

    if SenFields.FULL_GOLD_EXISTS in sen and sen[SenFields.FULL_GOLD_EXISTS]:
        if overwrite:
            del sen[SenFields.GOLD_ATTRIBUTES]
            del sen[SenFields.GOLD_MODALITY]
            sen[SenFields.LABELS_GOLD_EXISTS] = False
            sen[SenFields.FULL_GOLD_EXISTS] = False
        else:
            if sen[SenFields.GOLD_ATTRIBUTES] != attrs:
                sen_to_attr.log_conflict(sen)
                raise ValueError(
                    'field "full_gold_exists" already present in input and'
                    '--overwrite not set')
            if sen[SenFields.GOLD_MODALITY] != mod:
                sen_to_attr.log_conflict(sen, attr=False)
                raise ValueError(
                    'field "full_gold_exists" already present in input and'
                    '--overwrite not set')

    if attrs is not None and mod is not None:
        sen[SenFields.LABELS_GOLD_EXISTS] = True
        sen[SenFields.FULL_GOLD_EXISTS] = True
        sen[SenFields.GOLD_ATTRIBUTES] = attrs
        sen[SenFields.GOLD_MODALITY] = mod


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
