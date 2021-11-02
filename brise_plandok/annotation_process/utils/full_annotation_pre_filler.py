

import os
from brise_plandok.attrs_from_gold import SenToAttrMap, full_attrs_from_gold_sen
from brise_plandok.constants import DocumentFields
from brise_plandok.utils import dump_json, load_json


class FullAnnotationPreFiller:

    def generate_for_full_annotation(self, doc_ids, data_folder):
        sen_to_gold_attrs = SenToAttrMap(
            gold_dir=data_folder, fuzzy=True) if data_folder else None
        for doc_id in doc_ids:
            full_data_file = os.path.join(data_folder, doc_id +".json")
            doc = load_json(full_data_file)
            if not doc[DocumentFields.FULL_GOLD]:
                self._pre_fill_gold(doc, sen_to_gold_attrs)
                dump_json(doc, full_data_file)
            yield doc


    def _pre_fill_gold(self, doc, sen_to_gold_attrs):
        for sen in doc[DocumentFields.SENS].values():
            full_attrs_from_gold_sen(sen, sen_to_gold_attrs, False)
