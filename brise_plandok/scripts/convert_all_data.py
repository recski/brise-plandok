import argparse
import os

from brise_plandok.constants import DocumentFields, SenFields, AttributeFields
from brise_plandok.utils import dump_json, load_json

DOC_ID_FILTER = [
    "7377",
]


def convert_sens(data_folder, doc_map, sen_map, doc_id_filter=None):
    for data_file in os.listdir(data_folder):
        data_path = os.path.join(data_folder, data_file)
        assert os.path.isfile(data_path)
        assert data_file.split(".")[-1] == "json"
        doc = load_json(data_path)
        if doc_id_filter is None or doc[DocumentFields.ID] in doc_id_filter:
            doc = doc_map(doc)
            for sen_id, sen in doc[DocumentFields.SENS].items():
                doc[DocumentFields.SENS][sen_id] = sen_map(sen)
            dump_json(doc, data_path)


def doc_mapping_fn(doc):
    doc[DocumentFields.FULL_GOLD] = False
    return doc


def _flatten_gold_attributes(old, sen):
    new = {}
    for attr_name, attr in old.items():
        new[attr_name] = []
        if attr[AttributeFields.VALUE] is not None:
            for i, value in enumerate(attr[AttributeFields.VALUE]):
                for split_value in value.split("\n"):
                    new[attr_name].append(
                        {
                            AttributeFields.NAME: attr_name,
                            AttributeFields.VALUE: split_value.strip(),
                            AttributeFields.TYPE: attr[AttributeFields.TYPE][i],
                        }
                    )
            sen[SenFields.FULL_GOLD_EXISTS] = True
        else:
            new[attr_name].append(
                {
                    AttributeFields.NAME: attr_name,
                    AttributeFields.VALUE: None,
                    AttributeFields.TYPE: None,
                }
            )
    return new


def sen_mapping_fn(sen):
    if not sen[SenFields.FULL_GOLD_EXISTS]:
        print(sen[SenFields.ID])
        old = sen[SenFields.GOLD_ATTRIBUTES]
        new = _flatten_gold_attributes(old, sen)
        sen[SenFields.GOLD_ATTRIBUTES] = new
    return sen


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--data-folder")
    return parser.parse_args()


def main():
    args = get_args()
    convert_sens(args.data_folder, lambda x: x, lambda x: sen_mapping_fn(x), DOC_ID_FILTER)


if __name__ == "__main__":
    main()
