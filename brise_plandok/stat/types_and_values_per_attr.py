import argparse
import os

from brise_plandok.constants import DocumentFields, SenFields, AttributeFields
from brise_plandok.utils import load_json

DATASET_FOLDERS = ["data/train", "data/valid", "data/test"]

TYPES = "types"
VALUES = "values"
CNT = "count"


def types_and_values_per_attr():
    attr_map = {}
    for folder in DATASET_FOLDERS:
        for filename in os.listdir(folder):
            fn = os.path.join(folder, filename)
            doc = load_json(fn)
            for sen in doc[DocumentFields.SENS].values():
                for attr_list in sen[SenFields.GOLD_ATTRIBUTES].values():
                    for attr in attr_list:
                        attr_name = attr[AttributeFields.NAME]
                        attr_value = attr[AttributeFields.VALUE]
                        attr_type = attr[AttributeFields.TYPE]
                        if attr_name not in attr_map:
                            attr_map[attr_name] = {TYPES: {}, VALUES: {}, CNT: 1}
                        else:
                            attr_map[attr_name][CNT] += 1
                        if attr_type not in attr_map[attr_name][TYPES]:
                            attr_map[attr_name][TYPES][attr_type] = 1
                        else:
                            attr_map[attr_name][TYPES][attr_type] += 1
                        if attr_value not in attr_map[attr_name][VALUES]:
                            attr_map[attr_name][VALUES][attr_value] = 1
                        else:
                            attr_map[attr_name][VALUES][attr_value] += 1
    attr_map = {
        k: v for k, v in sorted(attr_map.items(), key=lambda item: item[1][CNT], reverse=True)
    }
    for attr_name, stat in attr_map.items():
        stat[TYPES] = {
            k: v for k, v in sorted(stat[TYPES].items(), key=lambda item: item[1], reverse=True)
        }
        stat[VALUES] = {
            k: v for k, v in sorted(stat[VALUES].items(), key=lambda item: (-item[1], item[0]))
        }
    print_stat(attr_map)


def print_stat(attr_map):
    print("# Types and Values per Attribute")
    print()
    for attr_name, types_and_values in attr_map.items():
        print(f"## {attr_name}")
        print(f"Count: {types_and_values[CNT]}")
        print(f"### Types")
        print("```bash")
        for attr_type, cnt in types_and_values[TYPES].items():
            print(f"{attr_type}: {cnt}")
        print("```")
        print(f"### Values")
        print("```bash")
        for attr_value, cnt in types_and_values[VALUES].items():
            print(f"{attr_value}: {cnt}")
        print("```")
        print()


def get_args():
    parser = argparse.ArgumentParser(description="")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    types_and_values_per_attr()
