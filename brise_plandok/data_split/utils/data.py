
import json
import logging
import os
from brise_plandok.attrs_from_gold import SenToAttrMap, attrs_from_gold_sen
from brise_plandok.constants import AttributeFields, DocumentFields, OldDocumentFields, OldSectionFields, OldSenFields, SenFields


def generate_data(doc_ids, gen_attr_folder, data_folder):
    sen_to_gold_attrs = SenToAttrMap(
        gold_dir=data_folder, fuzzy=True) if data_folder else None
    for doc_id in doc_ids:
        full_data_file = os.path.join(data_folder, doc_id +".json")
        json_file = os.path.join(gen_attr_folder, doc_id + ".jsonl")
        yield _get_doc(json_file, full_data_file, doc_id, sen_to_gold_attrs)


def _get_doc(json_file, full_data_file, doc_id, sen_to_gold_attrs):
    full_data = _get_full_data(full_data_file)
    if full_data is not None:
        logging.info(
            f"Full data json already exists. The content of this file will be used w/o any modification: {full_data_file}")
        return full_data
    gen_attrs = _get_gen_attrs(json_file)
    return _create_data_for_doc(doc_id, gen_attrs, sen_to_gold_attrs, full_data_file)


def _get_full_data(data_file):
    if os.path.exists(data_file):
        with open(data_file) as f:
            return json.load(f)
    return None


def _get_gen_attrs(json_file):
    with open(json_file) as f:
        lines = f.readlines()
        assert len(lines) == 1
        return json.loads(lines[0].strip())


def _create_data_for_doc(doc_id, get_attr, sen_to_gold_attrs, full_data_file):
    doc = {
        DocumentFields.ID: doc_id,
        DocumentFields.SENS: {},
        DocumentFields.ANNOTATORS: {},
        DocumentFields.LABELS_GOLD: False,
        DocumentFields.FULL_GOLD: False,
    }
    for section in get_attr[OldDocumentFields.SECTIONS]:
        for sen in section[OldSectionFields.SENS]:
            already_gold, labels_gold_exists, gold_attrs = _get_gold_related_attrs(
                sen_to_gold_attrs, sen)
            sen_id = sen[OldSenFields.ID]
            gen_attrs = attr_list_to_dict(sen[OldSenFields.GEN_ATTRIBUTES])
            doc[DocumentFields.SENS][sen_id] = _get_sen(
                sen_id,
                sen[OldSenFields.TEXT],
                gen_attributes_on_annotation=gen_attrs,
                already_gold_on_annotation=already_gold,
                labels_gold_exists=labels_gold_exists,
                gold_attributes=gold_attrs
            )
    _save_data(full_data_file, doc)
    return doc


def attr_list_to_dict(attr_list):
    attr_dict = dict()
    for attr in attr_list:
        attr_name = attr[AttributeFields.NAME]
        if attr_name in attr_dict:
            logging.warning(f"Attribute '{attr_name}' was generated twice")
        attr_dict[attr_name] = attr
    return attr_dict


def _get_gold_related_attrs(sen_to_gold_attrs, sen):
    already_gold = False
    labels_gold_exists = False
    gold_attrs = {}
    if sen_to_gold_attrs:
        attrs_from_gold_sen(sen, sen_to_gold_attrs, False)
        labels_gold_exists = sen[SenFields.LABELS_GOLD_EXISTS]
        if labels_gold_exists:
            gold_attrs = sen[SenFields.GOLD_ATTRIBUTES]
            already_gold = True
    return already_gold, labels_gold_exists, gold_attrs


def _get_sen(
    sen_id,
    text,
    modality=None,
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
        SenFields.MODALITY: modality,
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


def _save_data(full_data_file, doc):
    logging.info(f"Saving full data to: {full_data_file}")
    with open(full_data_file, "w") as f:
        json.dump(doc, f)
