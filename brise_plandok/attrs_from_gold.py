import argparse
import json
import logging
import os
import re
import sys

from tqdm import tqdm

from brise_plandok.constants import DocumentFields, SenFields, SenToAttrFields, AttributeFields


class SenToAttrMap:
    fuzzy_patt = re.compile("[0-9]+")

    def __init__(
        self,
        gold_dir,
        fuzzy,
        full=False,
        attributes=None,
        text_pattern=None,
        only_for_values=None,
        except_for_values=None,
    ):
        if only_for_values is not None and except_for_values is not None:
            raise ValueError(f"Either 'only_for_values' or 'except_for_values' can be given")
        self.sen_to_attr = None
        self.fuzzy = fuzzy
        self.build_map(
            gold_dir, full, attributes, text_pattern, only_for_values, except_for_values
        )

    def gen_sens_mod_attrs(self, gold_dir, full):
        if not os.path.exists(gold_dir):
            raise ValueError(f"path does not exist: {gold_dir}")
        for fn in os.listdir(gold_dir):
            if not (fn.endswith("json") or fn.endswith("jsonl")):
                logging.warning(f"skipping file not ending in json(l): {fn}")
                continue
            with open(os.path.join(gold_dir, fn)) as f:
                for line in f:
                    doc = json.loads(line)
                    if (full and doc[DocumentFields.FULL_GOLD]) or (
                        not full and doc[DocumentFields.LABELS_GOLD]
                    ):
                        for sen_id, sen in doc[DocumentFields.SENS].items():
                            yield sen, fn

    def sen_to_key(self, sen):
        if not self.fuzzy:
            return sen
        else:
            return SenToAttrMap.fuzzy_patt.sub("", sen)

    def build_map(
        self,
        gold_dir,
        full,
        attributes=None,
        text_pattern=None,
        only_for_values=None,
        except_for_values=None,
    ):
        self.sen_to_attr = {}
        for sen, fn in self.gen_sens_mod_attrs(gold_dir, full):
            sen_key = self.sen_to_key(sen[SenFields.TEXT])
            if text_pattern is None or re.search(text_pattern, sen_key) is not None:
                attr, mod = None, None
                if SenFields.GOLD_ATTRIBUTES in sen:
                    attr = sen[SenFields.GOLD_ATTRIBUTES]
                if SenFields.GOLD_MODALITY in sen:
                    mod = sen[SenFields.GOLD_MODALITY]
                sen_id = sen[SenFields.ID]
                if sen_key in self.sen_to_attr:
                    if full:
                        self._check_conflict_for_full(attr, mod, sen, sen_id, sen_key)
                    else:
                        self._check_conflict_for_label(attr, sen, sen_id, sen_key)
                else:
                    if self._contains_attribute_to_add(
                        attr, attributes, only_for_values, except_for_values
                    ):
                        self.sen_to_attr[sen_key] = {
                            SenToAttrFields.ATTR: attr,
                            SenToAttrFields.SENS: [sen_id],
                            SenToAttrFields.MOD: mod,
                        }

    def _contains_attribute_to_add(
        self, full_gold_attrs, attributes_to_select, only_for_values=None, except_for_values=None
    ):
        relevant_attributes_present = attributes_to_select is None
        if attributes_to_select is not None:
            for gold_attr_name in full_gold_attrs.keys():
                if gold_attr_name in attributes_to_select:
                    relevant_attributes_present = True
        if not relevant_attributes_present:
            return False

        for gold_attr_name, gold_attrs in full_gold_attrs.items():
            for gold_attr in gold_attrs:
                if only_for_values is not None:
                    if (
                        gold_attr_name not in only_for_values
                        or gold_attr[AttributeFields.VALUE] == only_for_values[gold_attr_name]
                    ):
                        return True
                if except_for_values is not None:
                    if (
                        gold_attr_name in except_for_values
                        and gold_attr[AttributeFields.VALUE] == except_for_values[gold_attr_name]
                    ):
                        return False
                else:
                    return True
        if only_for_values is not None:
            return False
        if except_for_values is not None:
            return True

    def _check_conflict_for_label(self, attr, sen, sen_id, sen_key):
        if set(self.sen_to_attr[sen_key][SenToAttrFields.ATTR].keys()) == set(attr.keys()):
            self.sen_to_attr[sen_key][SenToAttrFields.SENS].append(sen_id)
        else:
            self.log_conflict(sen, sen_key, attr=True)
            raise ValueError("full gold conflict with attributes")

    def _check_conflict_for_full(self, attr, mod, sen, sen_id, sen_key):
        if self.sen_to_attr[sen_key][SenToAttrFields.ATTR] == attr:
            if self.sen_to_attr[sen_key][SenToAttrFields.MOD] == mod:
                self.sen_to_attr[sen_key][SenToAttrFields.SENS].append(sen_id)
            else:
                self.log_conflict(sen, sen_key, attr=False)
                raise ValueError("full gold conflict with modalities")
        else:
            self.log_conflict(sen, sen_key, attr=True)
            raise ValueError("full gold conflict with attributes")

    def get_attrs(self, sen):
        sen_key = self.sen_to_key(sen)
        full_attr = self.sen_to_attr.get(sen_key)
        if full_attr is None:
            return None
        return full_attr[SenToAttrFields.ATTR]

    def set_attrs(self, sen, attributes):
        sen_key = self.sen_to_key(sen)
        self.sen_to_attr[sen_key][SenToAttrFields.ATTR] = attributes

    def get_mod(self, sen):
        sen_key = self.sen_to_key(sen)
        full_attr = self.sen_to_attr.get(sen_key)
        if full_attr is None:
            return None
        return full_attr[SenToAttrFields.MOD]

    def set_mod(self, sen, mod):
        sen_key = self.sen_to_key(sen)
        self.sen_to_attr[sen_key][SenToAttrFields.MOD] = mod

    def get_sens(self, sen):
        sen_key = self.sen_to_key(sen)
        full_attr = self.sen_to_attr.get(sen_key)
        if full_attr is None:
            return None
        return full_attr[SenToAttrFields.SENS]

    def log_conflict(self, sen, sen_key=None, attr=True):
        if sen_key is None:
            sen_key = self.sen_to_key(sen[SenFields.TEXT])
        old_sens = self.sen_to_attr[sen_key][SenToAttrFields.SENS]
        new_sen = sen[SenFields.ID]
        if attr:
            old_attrs = json.dumps(self.sen_to_attr[sen_key][SenToAttrFields.ATTR], indent=2)
            new_attrs = json.dumps(sen[SenFields.GOLD_ATTRIBUTES], indent=2)
            logging.error(
                "matching sens in gold with different attrs:\n"
                + f"\nold attrs {old_sens}:\n{old_attrs}\n\nnew attrs {new_sen}:\n{new_attrs}\n"
            )
        else:
            old_mod = json.dumps(self.sen_to_attr[sen_key][SenToAttrFields.MOD], indent=2)
            new_mod = json.dumps(sen[SenFields.GOLD_MODALITY], indent=2)
            logging.error(
                "matching sens in gold with different attrs:\n"
                + f"\nold attrs {old_sens}:\n{old_mod}\n\nnew attrs {new_sen}:\n{new_mod}\n"
            )


def attrs_from_gold_sen(sen, sen_to_attr, overwrite):
    attrs = sen_to_attr.get_attrs(sen["text"])

    if SenFields.LABELS_GOLD_EXISTS in sen and sen[SenFields.LABELS_GOLD_EXISTS]:
        if overwrite:
            del sen[SenFields.GOLD_ATTRIBUTES]
            sen[SenFields.LABELS_GOLD_EXISTS] = False
        else:
            if sen[SenFields.GOLD_ATTRIBUTES] != attrs:
                sen_to_attr.log_conflict(sen)
                raise ValueError(
                    'field "labels_gold_exists" already present in input and' "--overwrite not set"
                )
    else:
        sen[SenFields.LABELS_GOLD_EXISTS] = False

    if attrs is not None:
        sen[SenFields.LABELS_GOLD_EXISTS] = True
        sen[SenFields.GOLD_ATTRIBUTES] = attrs


def full_attrs_from_gold_sen(sen, sen_to_attr, overwrite):
    attrs = sen_to_attr.get_attrs(sen["text"])
    mod = sen_to_attr.get_mod(sen["text"])

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
                    'field "full_gold_exists" already present in input and' "--overwrite not set"
                )
            if sen[SenFields.GOLD_MODALITY] != mod:
                sen_to_attr.log_conflict(sen, attr=False)
                raise ValueError(
                    'field "full_gold_exists" already present in input and' "--overwrite not set"
                )

    if attrs is not None:
        sen[SenFields.LABELS_GOLD_EXISTS] = True
        sen[SenFields.FULL_GOLD_EXISTS] = True
        sen[SenFields.GOLD_ATTRIBUTES] = attrs
        sen[SenFields.GOLD_MODALITY] = mod


def attrs_from_gold(args):
    logging.info("building map...")
    sen_to_attr = SenToAttrMap(gold_dir=args.gold_dir, fuzzy=args.fuzzy)
    logging.info("done, processing docs...")
    for line in tqdm(sys.stdin):
        doc = json.loads(line)
        for section in doc["sections"]:
            for sen in section[SenToAttrFields.SENS]:
                attrs_from_gold_sen(sen, sen_to_attr, args.overwrite)
        sys.stdout.write(json.dumps(doc))
        sys.stdout.write("\n")


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-g", "--gold-dir", type=str)
    parser.add_argument("-f", "--fuzzy", default=False, action="store_true")
    parser.add_argument("-o", "--overwrite", default=False, action="store_true")
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " + "%(module)s (%(lineno)s) - %(levelname)s - %(message)s",
    )
    args = get_args()

    attrs_from_gold(args)


if __name__ == "__main__":
    main()
