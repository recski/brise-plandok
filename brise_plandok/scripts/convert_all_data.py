from brise_plandok.data_split.utils.data import attr_list_to_dict
from brise_plandok.utils import dump_json, load_json
import sys
from brise_plandok.constants import DocumentFields, SenFields
import json
import os


DATA_FOLDER = "/home/eszter/research/brise-nlp/annotation/2021_09/full_data"

class FullDataConverter:

    def convert_to_full(self, map):
        for data_file in os.listdir(DATA_FOLDER):
            data_path = os.path.join(DATA_FOLDER, data_file)
            assert os.path.isfile(data_path)
            assert data_file.split(".")[-1] == "json"
            doc = load_json(data_path)
            for sen_id, sen in doc[DocumentFields.SENS].items():
                doc[DocumentFields.SENS][sen_id] = map(sen)
            dump_json(doc, data_path)
            

    def _save(self, doc_id, doc):
        data_file = os.path.join(DATA_FOLDER, doc_id + ".json")
        with open(data_file, "w") as f:
            json.dump(doc, f)


def mapping_fn(sen):
    old = sen[SenFields.GEN_ATTRIBUTES_ON_ANNOTATION]
    new = attr_list_to_dict(old)
    sen[SenFields.GEN_ATTRIBUTES_ON_ANNOTATION] = new
    return sen

def main():
    converter = FullDataConverter()
    converter.convert_to_full(mapping_fn)


if __name__ == "__main__":
    main()
