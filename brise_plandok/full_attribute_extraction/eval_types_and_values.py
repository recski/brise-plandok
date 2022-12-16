import argparse
import json
import sys
from collections import Counter

from tuw_nlp.common.eval import get_cat_stats, print_cat_stats

from brise_plandok.constants import DocumentFields, SenFields


def eval_doc(doc, field, type_stats, value_stats):
    for sen in doc[DocumentFields.SENS].values():
        gold_attr = sen[SenFields.GOLD_ATTRIBUTES]
        pred_attr = sen[field]
        for attr_name, attr in gold_attr.items():
            g_type = attr[0]["type"]
            g_value = attr[0]["value"]
            value_stats["gold"] += 1

            if attr_name not in pred_attr:
                p_type = []
            else:
                p_type = [pred_attr[attr_name]["type"]]
                if p_type[0] is None:
                    p_type = []
                p_value = pred_attr[attr_name]["value"]
                if len(p_value) > 0:
                    value_stats["pred"] += 1
                    if p_value[0] == g_value:
                        value_stats["corr"] += 1

            type_stats["preds"].append(p_type)
            type_stats["golds"].append([g_type])


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-f", "--field_to_evaluate")
    parser.add_argument("-t", "--type", default=False, action="store_true")
    parser.add_argument("-v", "--value", default=False, action="store_true")
    return parser.parse_args()


def main():
    args = get_args()
    type_stats = {"preds": [], "golds": []}
    value_stats = Counter()
    for line in sys.stdin:
        doc = json.loads(line)
        eval_doc(doc, args.field_to_evaluate, type_stats, value_stats)

    if args.type:
        print_cat_stats(
            get_cat_stats(type_stats["preds"], type_stats["golds"]), tablefmt="latex_booktabs"
        )
    if args.value:
        print()
        stats = {
            "values": {
                "TP": value_stats["corr"],
                "FP": value_stats["pred"] - value_stats["corr"],
                "FN": value_stats["gold"] - value_stats["corr"],
            }
        }

        print_cat_stats(stats, tablefmt="latex_booktabs")


if __name__ == "__main__":
    main()
