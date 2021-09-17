
import json
import logging
from brise_plandok.attrs_from_gold import attrs_from_gold_sen
from brise_plandok.constants import DocumentFields, OldDocumentFields, OldSectionFields, OldSenFields, SenFields


def create_data(doc_id, get_attr, sen_to_gold_attrs, full_data_file):
    doc = {
        DocumentFields.ID: doc_id,
        DocumentFields.SENS: {},
    }
    for section in get_attr[OldDocumentFields.SECTIONS]:
        for sen in section[OldSectionFields.SENS]:
            already_gold, gold_exists, gold_attrs = get_gold_related_attrs(sen_to_gold_attrs, sen)
            sen_id = sen[OldSenFields.ID]
            doc[DocumentFields.SENS][sen_id] = get_sen(
                sen_id,
                sen[OldSenFields.TEXT],
                gen_attributes_on_annotation=sen[OldSenFields.GEN_ATTRIBUTES],
                already_gold_on_annotation=already_gold,
                gold_exists=gold_exists,
                gold_attributes=gold_attrs
            )
    save_data(full_data_file, doc)
    return doc
            

def get_gold_related_attrs(sen_to_gold_attrs, sen):
    already_gold = False
    gold_exists = False
    gold_attrs = []
    if sen_to_gold_attrs:
        attrs_from_gold_sen(sen, sen_to_gold_attrs, False)
        gold_exists = sen[SenFields.GOLD_EXISTS]
        if gold_exists:
            gold_attrs = sen[SenFields.GOLD_ATTRIBUTES]
            already_gold = True
    return already_gold, gold_exists, gold_attrs


def get_sen(
    sen_id,
    text,
    modality=None,
    already_gold_on_annotation=False,
    gold_exists=False,
    gold_attributes=[],
    gen_attributes_on_annotation=[],
    annotated_attributes=[],
    gen_attributes=[],
    segmentation_error=False
):
    return {
        SenFields.ID: sen_id,
        SenFields.TEXT: text,
        SenFields.MODALITY: modality,
        SenFields.ALREADY_GOLD_ON_ANNOTATION: already_gold_on_annotation,
        SenFields.GOLD_EXISTS: gold_exists,
        SenFields.GOLD_ATTRIBUTES: gold_attributes,
        SenFields.GEN_ATTRIBUTES_ON_ANNOTATION: gen_attributes_on_annotation,
        SenFields.ANNOTATED_ATTRIBUTES: annotated_attributes,
        SenFields.GEN_ATTRIBUTES: gen_attributes,
        SenFields.SEGMENTATION_ERROR: segmentation_error,
    }

def save_data(full_data_file, doc):
    logging.info(f"Saving full data to: {full_data_file}")
    with open(full_data_file, "w") as f:
        json.dump(doc, f)