import json
import sys

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


def main():
    preds, golds = [], []
    for line in sys.stdin:
        doc = json.loads(line)
        for sen in doc[DocumentFields.SENS].values():
            g_mod = sen.get("gold_modality")
            if not g_mod:
                continue

            golds.append([g_mod])

            p_mod = sen["predicted_modality"]
            if p_mod is None:
                preds.append([])
            else:
                preds.append([p_mod])

    print("always obl baseline:")
    print_cat_stats(get_cat_stats(len(golds) * [["obligation"]], golds), tablefmt="latex_booktabs")
    print()
    print("predictions:")
    print_cat_stats(get_cat_stats(preds, golds), tablefmt="latex_booktabs")


if __name__ == "__main__":
    main()
