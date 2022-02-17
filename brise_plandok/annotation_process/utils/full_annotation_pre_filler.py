import os
from brise_plandok.attrs_from_gold import (
    SenToAttrMap,
    attrs_from_gold_sen,
    full_attrs_from_gold_sen,
)
from brise_plandok.constants import DocumentFields, SenFields
from brise_plandok.full_attribute_extraction.type.extract_types import extract_type
from brise_plandok.full_attribute_extraction.value.extract_values import extract_value
from brise_plandok.utils import dump_json, load_json


class FullAnnotationPreFiller:
    def generate_for_full_annotation(self, doc_ids, data_folder):
        sen_to_full_gold_attrs = (
            SenToAttrMap(gold_dir=data_folder, fuzzy=True, full=True)
            if data_folder
            else None
        )
        sen_to_gold_attrs = (
            SenToAttrMap(gold_dir=data_folder, fuzzy=True, full=False)
            if data_folder
            else None
        )
        for doc_id in doc_ids:
            full_data_file = os.path.join(data_folder, doc_id + ".json")
            doc = load_json(full_data_file)
            self.pre_fill_gold_labels(doc, sen_to_gold_attrs)
            self.pre_fill_full_gold(doc, sen_to_full_gold_attrs)
            self.fill_gen_attributes_for_full(doc)
            dump_json(doc, full_data_file)
            yield doc

    def pre_fill_gold_labels(self, doc, sen_to_gold_attrs):
        if not doc[DocumentFields.LABELS_GOLD]:
            for sen in doc[DocumentFields.SENS].values():
                attrs_from_gold_sen(sen, sen_to_gold_attrs, False)

    def pre_fill_full_gold(self, doc, sen_to_full_gold_attrs):
        if not doc[DocumentFields.FULL_GOLD]:
            for sen in doc[DocumentFields.SENS].values():
                full_attrs_from_gold_sen(sen, sen_to_full_gold_attrs, False)

    def fill_gen_attributes_for_full(self, doc):
        is_annotated = (
            len(doc[DocumentFields.ANNOTATORS]) > 0
            if DocumentFields.ANNOTATORS in doc
            else False
        )
        for sen in doc[DocumentFields.SENS].values():
            labels_gold = sen[SenFields.LABELS_GOLD_EXISTS]
            attribute_names = self._get_attributes_names(sen, labels_gold, is_annotated)
            for attribute in attribute_names:
                extract_value(
                    sen, attribute, SenFields.GEN_ATTRIBUTES_ON_FULL_ANNOTATION, False
                )
                extract_type(
                    sen, attribute, SenFields.GEN_ATTRIBUTES_ON_FULL_ANNOTATION, False
                )

    def _get_attributes_names(self, sen, labels_gold, is_annotated):
        if labels_gold:
            attribute_names = sen[SenFields.GOLD_ATTRIBUTES].keys()
        elif is_annotated:
            attribute_names = sen[SenFields.ANNOTATED_ATTRIBUTES].keys()
        else:
            attribute_names = sen[SenFields.GEN_ATTRIBUTES_ON_ANNOTATION].keys()
        return attribute_names
