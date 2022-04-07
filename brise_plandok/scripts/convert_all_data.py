import json
import os

from brise_plandok.constants import DocumentFields, SenFields, AttributeFields
from brise_plandok.utils import dump_json, load_json

# DATA_FOLDER = "/home/eszter/research/brise-nlp/annotation/2021_09/full_data"
# DATA_FOLDER = "/home/eszter/research/brise-plandok/brise_plandok/annotation_process/example/full_data/"
DATA_FOLDER = "/home/eszter/research/brise-plandok/sample_data/annotation/full_data/"

DOC_ID_FILTER = [
    "7377",
]


class FullDataConverter:
    def convert_sens(self, doc_map, sen_map, doc_id_filter=None):
        for data_file in os.listdir(DATA_FOLDER):
            data_path = os.path.join(DATA_FOLDER, data_file)
            assert os.path.isfile(data_path)
            assert data_file.split(".")[-1] == "json"
            doc = load_json(data_path)
            if doc_id_filter is None or doc[DocumentFields.ID] in doc_id_filter:
                doc = doc_map(doc)
                for sen_id, sen in doc[DocumentFields.SENS].items():
                    doc[DocumentFields.SENS][sen_id] = sen_map(sen)
                dump_json(doc, data_path)

    def _save(self, doc_id, doc):
        data_file = os.path.join(DATA_FOLDER, doc_id + ".json")
        with open(data_file, "w") as f:
            json.dump(doc, f)


def doc_mapping_fn(doc):
    doc[DocumentFields.FULL_GOLD] = False
    return doc


def _flatten_gold_attributes(old):
    new = {}
    for attr_name, attr in old.items():
        new[attr_name] = []
        for i, value in enumerate(attr[AttributeFields.VALUE]):
            for split_value in value.split("\n"):
                new[attr_name].append(
                    {
                        AttributeFields.NAME: attr_name,
                        AttributeFields.VALUE: split_value.strip(),
                        AttributeFields.TYPE: attr[AttributeFields.TYPE][i],
                    }
                )
    return new


def sen_mapping_fn(sen):
    if sen[SenFields.FULL_GOLD_EXISTS]:
        print(sen[SenFields.ID])
        old = sen[SenFields.GOLD_ATTRIBUTES]
        new = _flatten_gold_attributes(old)
        sen[SenFields.GOLD_ATTRIBUTES] = new
    return sen


def main():
    converter = FullDataConverter()
    converter.convert_sens(lambda x: x, lambda x: x)


if __name__ == "__main__":
    main()
