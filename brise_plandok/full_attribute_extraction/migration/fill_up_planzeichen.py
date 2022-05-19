import argparse
import logging
import os
import re

from brise_plandok.constants import (
    AttributeFields,
    DocumentFields,
    SenFields,
    AttributesNames,
)
from brise_plandok.data_utils import add_attribute
from brise_plandok.utils import load_json, dump_json

PATTERN = r"Ekz|EKZ|O[eE]Z|[öÖ]Z|StrG|StrE.*|öDg|oeDg|P|GBcv|GV|GBGF|GBFB|GBBG|GBF|IG|IGBS|IGSI|SOLL|SOSI|GSLASH.*|L|G|E|Epk|Ekl|[Ee]klw|Esp|Ebd|Ebh|Sww|SwwL|Spk|F|SN|VB|W|WGV|WGF|WFB|GS|GSGM|GB|GBGV|SO"

INPUT_ATTRIBUTES = [AttributesNames.BBAllgemein, AttributesNames.Widmung]

OUTPUT_ATTRIBUTE = AttributesNames.Planzeichen


def copy_to_output_attr(gold_folder, input_attributes, output_attribute, pattern):
    for doc_fn in os.listdir(gold_folder):
        if not (doc_fn.endswith("json") or doc_fn.endswith("jsonl")):
            logging.warning(f"skipping file not ending in json(l): {doc_fn}")
            continue
        doc_path = os.path.join(gold_folder, doc_fn)
        doc = load_json(doc_path)
        changed = False
        for sen in doc[DocumentFields.SENS].values():
            gold_attributes = sen[SenFields.GOLD_ATTRIBUTES]
            gold_out_values = _get_gold_values_for_out_attr(
                gold_attributes, AttributesNames.Planzeichen
            )
            changed = _add_attr_if_matches_pattern(
                changed,
                gold_attributes,
                gold_out_values,
                input_attributes,
                output_attribute,
                pattern,
                sen[SenFields.ID],
            )
            if changed:
                dump_json(doc, doc_path)


def _add_attr_if_matches_pattern(
    changed,
    gold_attributes,
    gold_values_for_out_attr,
    input_attributes,
    output_attribute,
    pattern,
    sen_id,
):
    for input_attribute in input_attributes:
        if input_attribute in gold_attributes:
            for gold_values in gold_attributes[input_attribute]:
                gold_value = gold_values[AttributeFields.VALUE]
                if (
                    gold_value not in gold_values_for_out_attr
                    and re.fullmatch(pattern, gold_value) is not None
                ):
                    print(f"Changes for {sen_id}")
                    print(f"Existing {input_attribute}: {gold_attributes[input_attribute]}")
                    print(
                        f"{output_attribute} before: {gold_attributes[output_attribute] if output_attribute in gold_attributes else None}"
                    )
                    add_attribute(
                        gold_attributes,
                        output_attribute,
                        gold_value,
                        gold_values[AttributeFields.TYPE],
                    )
                    print(f"{output_attribute} after: {gold_attributes[output_attribute]}")
                    changed = True
    return changed


def _get_gold_values_for_out_attr(gold_attributes, output_attr):
    gold_values = (
        [attr_values[AttributeFields.VALUE] for attr_values in gold_attributes[output_attr]]
        if AttributesNames.Planzeichen in gold_attributes
        else []
    )
    return gold_values


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-g", "--gold-dir")
    return parser.parse_args()


if __name__ == "__main__":
    logging.getLogger("penman").setLevel(logging.WARNING)
    logging.getLogger("stanza").setLevel(logging.WARNING)
    logging.getLogger("tuw_nlp").setLevel(logging.WARNING)
    args = get_args()
    copy_to_output_attr(args.gold_dir, INPUT_ATTRIBUTES, OUTPUT_ATTRIBUTE, PATTERN)
