import argparse
import json
import sys
from collections import Counter

from brise_plandok.constants import DocumentFields, SenFields


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-p", "--pred", action="store_true")
    return parser.parse_args()


def main():
    args = get_args()
    stats = Counter()
    errs = open("errs.txt", "w")
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

            if args.pred and not set(g_attrs.keys()) == set(p_attrs.keys()):
                errs.write(
                    "g_attrs: {0}, p_attrs: {1}\n".format(set(g_attrs.keys()), set(p_attrs.keys()))
                )
                stats["wrong attr set"] += 1
                continue

            corr_attrs = True
            for attr_name, p_attr in p_attrs.items():
                g_types = set(a["type"] for a in g_attrs[attr_name])
                g_values = set(a["value"] for a in g_attrs[attr_name])

                if p_attr["type"] not in g_types:
                    errs.write("g_types: {0}, p_type: {1}\n".format(g_types, p_attr["type"]))
                    stats["wrong type"] += 1
                    corr_attrs = False
                if set(p_attr["value"]) != g_values:
                    errs.write("g_values: {0}, p_values: {1}\n".format(g_values, p_attr["value"]))
                    stats["wrong values"] += 1
                    corr_attrs = False

            if not corr_attrs:
                stats["wrong attr property"] += 1
                continue

            p_mod = sen[SenFields.PREDICTED_MODALITY]
            if p_mod != g_mod:
                errs.write("g_mod: {0}, p_mod: {1}\n".format(g_mod, p_mod))
                stats["wrong_modality"] += 1
                continue

            stats["all correct"] += 1

    errs.close()
    print(stats.most_common())


if __name__ == "__main__":
    main()
