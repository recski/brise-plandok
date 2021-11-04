import os
from brise_plandok.constants import ATTRIBUTE_NORM_MAP, SenFields
import json
import logging


def normalize_attribute_name(attribute_name):
    if attribute_name in ATTRIBUTE_NORM_MAP:
        return ATTRIBUTE_NORM_MAP[attribute_name]
    return attribute_name


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


def create_sen(
    sen_id,
    text,
    gold_modality=None,
    already_gold_on_annotation=False,
    labels_gold_exists=False,
    full_gold_exists=False,
    gold_attributes={},
    gen_attributes_on_annotation={},
    gen_attributes_on_full_annotation={},
    annotated_attributes={},
    gen_attributes={},
    segmentation_error=False
):
    return {
        SenFields.ID: sen_id,
        SenFields.TEXT: text,
        SenFields.GOLD_MODALITY: gold_modality,
        SenFields.ALREADY_GOLD_ON_ANNOTATION: already_gold_on_annotation,
        SenFields.LABELS_GOLD_EXISTS: labels_gold_exists,
        SenFields.FULL_GOLD_EXISTS: full_gold_exists,
        SenFields.GOLD_ATTRIBUTES: gold_attributes,
        SenFields.GEN_ATTRIBUTES_ON_ANNOTATION: gen_attributes_on_annotation,
        SenFields.GEN_ATTRIBUTES_ON_FULL_ANNOTATION: gen_attributes_on_full_annotation,
        SenFields.ANNOTATED_ATTRIBUTES: annotated_attributes,
        SenFields.GEN_ATTRIBUTES: gen_attributes,
        SenFields.SEGMENTATION_ERROR: segmentation_error,
    }
