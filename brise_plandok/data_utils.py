import logging

from brise_plandok.constants import (
    SenFields,
    ATTRIBUTE_NORM_MAP,
    AttributeFields,
)


def create_sen(
    sen_id,
    text,
    gold_modality=None,
    already_gold_on_annotation=False,
    labels_gold_exists=False,
    full_gold_exists=False,
    gold_attributes=None,
    gen_attributes_on_annotation=None,
    gen_attributes_on_full_annotation=None,
    annotated_attributes=None,
    gen_attributes=None,
    segmentation_error=False,
):
    if gen_attributes is None:
        gen_attributes = {}
    if annotated_attributes is None:
        annotated_attributes = {}
    if gen_attributes_on_full_annotation is None:
        gen_attributes_on_full_annotation = {}
    if gen_attributes_on_annotation is None:
        gen_attributes_on_annotation = {}
    if gold_attributes is None:
        gold_attributes = {}
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


def normalize_attribute_name(attribute_name):
    if attribute_name in ATTRIBUTE_NORM_MAP:
        return ATTRIBUTE_NORM_MAP[attribute_name]
    return attribute_name


def add_attribute(
    old_attributes,
    attr_name,
    attr_value,
    attr_type,
):
    if attr_name not in old_attributes:
        _add_new_attribute(attr_name, attr_type, attr_value, old_attributes)
    else:
        _append_new_value(attr_name, attr_type, attr_value, old_attributes)
    logging.info(f"Updated attributes:\n{old_attributes}")


def _add_new_attribute(attr_name, attr_type, attr_value, old_attributes):
    old_attributes[attr_name] = [
        {
            AttributeFields.NAME: attr_name,
            AttributeFields.VALUE: attr_value,
            AttributeFields.TYPE: attr_type,
        }
    ]


def _append_new_value(attr_name, attr_type, attr_value, old_attributes):
    for old_instance in old_attributes[attr_name]:
        if old_instance[AttributeFields.VALUE] == attr_value:
            if old_instance[AttributeFields.TYPE] == attr_type:
                logging.info(
                    f"Attribute with given value and type is already present:\n{old_attributes}\n- no changes done"
                )
            else:
                logging.warning(
                    f"Attribute with same value but different type is present\n{old_attributes}\n- please check"
                )
                raise ValueError(f"Conflict in {old_attributes}")
        else:
            old_attributes[attr_name].append(
                {
                    AttributeFields.NAME: attr_name,
                    AttributeFields.VALUE: attr_value,
                    AttributeFields.TYPE: attr_type,
                }
            )
            return
