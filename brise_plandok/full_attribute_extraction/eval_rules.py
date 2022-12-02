import argparse
import json
import sys
from collections import Counter

from tabulate import tabulate
from tuw_nlp.common.eval import avg

from brise_plandok.constants import DocumentFields, SenFields


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-p", "--pred", action="store_true")
    return parser.parse_args()


def main():
    args = get_args()
    stats = Counter()
    errs = open("errs.txt", "w")
    attr_set_pairs = []
    for line in sys.stdin:
        doc = json.loads(line)
        for sen in doc[DocumentFields.SENS].values():
            g_mod = sen.get(SenFields.GOLD_MODALITY)
            if not g_mod:
                continue
            stats["all"] += 1

            g_attrs = sen[SenFields.GOLD_ATTRIBUTES]
            p_attrs = (
                sen[SenFields.PREDICTED_ATTRIBUTES] if args.pred else sen[SenFields.GEN_ATTRIBUTES]
            )

            if args.pred:
                g_attr_set = set(g_attrs.keys())
                p_attr_set = set(p_attrs.keys())
                attr_set_pairs.append((g_attr_set, p_attr_set))
                if g_attr_set != p_attr_set:
                    errs.write(f"g_attrs: {g_attr_set}, p_attrs: {p_attr_set}\n")
                    stats["wrong attr set"] += 1
                    continue

            for attr_name, p_attr in p_attrs.items():
                g_types = set(a["type"] for a in g_attrs[attr_name])
                g_values = set(a["value"] for a in g_attrs[attr_name])

                if set(p_attr["value"]) != g_values:
                    errs.write("g_values: {0}, p_values: {1}\n".format(g_values, p_attr["value"]))
                    stats["corr attrs, wrong value"] += 1
                    break

                if p_attr["type"] not in g_types:
                    errs.write("g_types: {0}, p_type: {1}\n".format(g_types, p_attr["type"]))
                    stats["corr values, wrong type"] += 1
                    break
            else:
                p_mod = sen[SenFields.PREDICTED_MODALITY]
                if p_mod != g_mod:
                    errs.write("g_mod: {0}, p_mod: {1}\n".format(g_mod, p_mod))
                    stats["only modality wrong"] += 1
                else:
                    stats["all correct"] += 1

    errs.close()

    get_overall_stats(stats)
    if args.pred:
        get_attr_stats(attr_set_pairs)


def get_attr_stats(attr_set_pairs):
    golds, preds, ps, rs, fs = [], [], [], [], []
    total_gold, total_pred, TP, FP, FN = 0, 0, 0, 0, 0
    for g_set, p_set in attr_set_pairs:
        golds.append(len(g_set))
        preds.append(len(p_set))
        total_gold += len(g_set)
        total_pred += len(p_set)
        tp = len(g_set & p_set)
        fp = len(p_set - g_set)
        fn = len(g_set - p_set)
        TP += tp
        FP += fp
        FN += fn
        p = 1 if (tp + fp) == 0 else tp / (tp + fp)
        r = 1 if (tp + fn) == 0 else tp / (tp + fn)
        ps.append(p)
        rs.append(r)
        fs.append(0 if p + r == 0 else (2 * p * r) / (p + r))

    P = TP / (TP + FP)
    R = TP / (TP + FN)
    F = 0 if P + R == 0 else (2 * P * R) / (P + R)
    print("attr extraction:")
    rows = [
        ["total", total_gold, total_pred, P, R, F],
        ["macro-avg (sens)", avg(golds), avg(preds), avg(ps), avg(rs), avg(fs)],
    ]

    print(
        tabulate(
            rows,
            tablefmt="latex_booktabs",
            headers=["", "gold", "pred", "P", "R", "F"],
            floatfmt=("s", ".2f", ".2f", ".2%", ".2%", ".2%"),
        )
    )


def get_overall_stats(stats):
    rows = []
    for stat, n in stats.most_common():
        if stat == "all":
            total = n

        rows.append([stat, n, n / total])

    print(
        tabulate(
            rows,
            tablefmt="latex_booktabs",
            floatfmt=("s", "d", ".2%"),
        )
    )


if __name__ == "__main__":
    main()
