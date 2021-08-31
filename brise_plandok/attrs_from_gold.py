import argparse
import json
import logging
import os
import re
import sys

from tqdm import tqdm


class SenToAttrMap():
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
                    sens = json.loads(line)
                    for sen in sens['sens']:
                        gold_attrs = sen.get('gold_attributes')
                        if gold_attrs is None:
                            # support outputs from convert.py
                            gold_attrs = sen['attributes']
                        yield sen['text'], gold_attrs

    def sen_to_key(self, sen):
        if not self.fuzzy:
            return sen
        else:
            return SenToAttrMap.fuzzy_patt.sub('', sen)

    def build_map(self, gold_dir):
        self.sen_to_attr = {}
        for sen, attr in self.gen_sens_attrs(gold_dir):
            sen_key = self.sen_to_key(sen)
            if sen_key in self.sen_to_attr:
                if self.sen_to_attr[sen_key] == attr:
                    continue
                raise ValueError(
                    f'matching sens in gold with different attrs: {sen_key}')

            self.sen_to_attr[sen_key] = attr

    def get_attrs(self, sen):
        sen_key = self.sen_to_key(sen)
        return self.sen_to_attr.get(sen_key)


def attrs_from_gold_sen(sen, sen_to_attr, args):
    if 'gold_exists' in sen:
        if args.overwrite:
            if sen['gold_exists']:
                del sen['gold_attributes']
                sen['gold_exists'] = False
        else:
            raise ValueError(
                'field "gold_exists" already present in input and'
                '--overwrite not set')
    else:
        sen['gold_exists'] = False

    attrs = sen_to_attr.get_attrs(sen['text'])
    if attrs is not None:
        sen['gold_exists'] = True
        sen['gold_attributes'] = attrs


def attrs_from_gold(args):
    logging.info('building map...')
    sen_to_attr = SenToAttrMap(gold_dir=args.gold_dir, fuzzy=args.fuzzy)
    logging.info('done, processing docs...')
    for line in tqdm(sys.stdin):
        doc = json.loads(line)
        for section in doc['sections']:
            for sen in section['sens']:
                attrs_from_gold_sen(sen, sen_to_attr, args)
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
