import sys
from brise_plandok.constants import DataFields
import json
import os
from tqdm import tqdm

DATASET_SHEET_NAME = "Dataset"
FIRST_DATA_ROW = 3
ATTRIBUTE_OFFSET = 2
ATTRIBUTE_STEP = 2
LABEL_OFFSET = 1

ID_COL = 1
TEXT_COL = 2

ATTRIBUTES_TO_IGNORE = "DON'T ANNOTATE THIS SENTENCE"

DATA = "/home/eszter/research/brise-nlp/annotation/2021_09/full_data"

GOLD_COLOR = "00FFD700"

class FullDataConverter:

    def convert_to_full(self, line):
        old_doc = json.loads(line.strip())
        doc_id = old_doc["id"]
        doc = {
            "id": doc_id,
            "sens": {},
        }
        for sen in old_doc["sens"]:
            try:
                sen_id = sen["id"]
            except:
                sen_id = sen["sen_id"]
            assert sen_id not in doc["sens"]
            doc["sens"][sen_id] = self._get_sens(sen, sen_id)
        self._save(doc_id, doc)

    def _get_sens(self, sen, sen_id):
        return {
            DataFields.ID: sen_id,
            DataFields.TEXT: sen["text"],
            DataFields.MODALITY: None,
            DataFields.ALREADY_GOLD_ON_ANNOTATION: False,
            DataFields.GOLD_EXISTS: True,
            DataFields.GOLD_ATTRIBUTES: sen["attributes"],
            DataFields.GEN_ATTRIBUTES_ON_ANNOTATION: [],
            DataFields.ANNOTATED_ATTRIBUTES: [],
            DataFields.GEN_ATTRIBUTES: [],
        }

    def _save(self, doc_id, doc):
        data_file = os.path.join(DATA, doc_id + ".json")
        with open(data_file, "w") as f:
            json.dump(doc, f)


def main():
    converter = FullDataConverter()
    for line in tqdm(sys.stdin):
        converter.convert_to_full(line)


if __name__ == "__main__":
    main()
