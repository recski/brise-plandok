import json
import logging
import os
from brise_plandok.attrs_from_gold import SenToAttrMap, attrs_from_gold_sen
from brise_plandok.constants import (
    AttributeFields,
    DocumentFields,
    OldDocumentFields,
    OldSectionFields,
    OldSenFields,
    SenFields,
)
from brise_plandok.utils import dump_json, load_json
from brise_plandok.data_utils import create_sen


class LabelAnnotationPreFiller:
    def generate_for_label_annotation(self, doc_ids, gen_attr_folder, data_folder):
        sen_to_gold_attrs = (
            SenToAttrMap(gold_dir=data_folder, fuzzy=True) if data_folder else None
        )
        for doc_id in doc_ids:
            full_data_file = os.path.join(data_folder, doc_id + ".json")
            json_file = os.path.join(gen_attr_folder, doc_id + ".jsonl")
            yield self._get_doc(json_file, full_data_file, doc_id, sen_to_gold_attrs)

    def _get_doc(self, json_file, full_data_file, doc_id, sen_to_gold_attrs):
        full_data = load_json(full_data_file)
        if full_data is not None:
            logging.info(
                f"Full data json already exists. The content of this file will be used w/o any modification: {full_data_file}"
            )
            return full_data
        gen_attrs = self._get_gen_attrs(json_file)
        return self._create_data_for_doc(
            doc_id, gen_attrs, sen_to_gold_attrs, full_data_file
        )

    def _get_gen_attrs(self, json_file):
        with open(json_file) as f:
            lines = f.readlines()
            assert len(lines) == 1
            return json.loads(lines[0].strip())

    def _create_data_for_doc(self, doc_id, get_attr, sen_to_gold_attrs, full_data_file):
        doc = {
            DocumentFields.ID: doc_id,
            DocumentFields.SENS: {},
            DocumentFields.ANNOTATORS: {},
            DocumentFields.LABELS_GOLD: False,
            DocumentFields.FULL_GOLD: False,
        }
        for section in get_attr[OldDocumentFields.SECTIONS]:
            for sen in section[OldSectionFields.SENS]:
                (
                    already_gold,
                    labels_gold_exists,
                    gold_attrs,
                ) = self._get_gold_related_attrs(sen_to_gold_attrs, sen)
                sen_id = sen[OldSenFields.ID]
                gen_attrs = self.attr_list_to_dict(sen[OldSenFields.GEN_ATTRIBUTES])
                doc[DocumentFields.SENS][sen_id] = create_sen(
                    sen_id,
                    sen[OldSenFields.TEXT],
                    gen_attributes_on_annotation=gen_attrs,
                    already_gold_on_annotation=already_gold,
                    labels_gold_exists=labels_gold_exists,
                    gold_attributes=gold_attrs,
                )
        dump_json(doc, full_data_file)
        return doc

    def attr_list_to_dict(self, attr_list):
        attr_dict = dict()
        for attr in attr_list:
            attr_name = attr[AttributeFields.NAME]
            if attr_name in attr_dict:
                logging.warning(f"Attribute '{attr_name}' was generated twice")
            attr_dict[attr_name] = attr
        return attr_dict

    def _get_gold_related_attrs(self, sen_to_gold_attrs, sen):
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
