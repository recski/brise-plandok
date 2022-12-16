import json
import sys
from collections import Counter, defaultdict

from tabulate import tabulate


def main():
    attr_to_mod = defaultdict(Counter)
    attr_counter = Counter()
    for line in sys.stdin:
        d = json.loads(line)
        for sen in d["sens"].values():
            if sen["segmentation_error"]:
                continue
            mod = sen["gold_modality"]
            if mod is None:
                continue
            for attr in sen["gold_attributes"].keys():
                attr_to_mod[attr][mod] += 1
                attr_to_mod["total"][mod] += 1
                attr_counter[attr] += 1
                attr_counter["total"] += 1

    print_counts(attr_counter, attr_to_mod)
    print_ratios(attr_counter, attr_to_mod)


def print_counts(attr_counter, attr_to_mod):
    table = []
    for attr, count in attr_counter.most_common():
        table.append(
            [attr, count]
            + [attr_to_mod[attr][mod] for mod in ["obligation", "permission", "prohibition"]]
        )

    sys.stdout.write(
        tabulate(
            table,
            headers=["attribute", "total", "obligation", "permission", "prohibition"],
            tablefmt="latex_booktabs",
            floatfmt=["s", "d", "d", "d", "d"],
        )
    )
    sys.stdout.write("\n")


def print_ratios(attr_counter, attr_to_mod):
    table = []
    for attr, count in attr_counter.most_common():
        table.append(
            [attr, count]
            + [
                attr_to_mod[attr][mod] / count
                for mod in ["obligation", "permission", "prohibition"]
            ]
        )

    sys.stdout.write(
        tabulate(
            table,
            headers=["attribute", "total", "obligation", "permission", "prohibition"],
            tablefmt="latex_booktabs",
            floatfmt=["s", "d", ".2%", ".2%", ".2%"],
        )
    )
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
