import json
import sys

from collections import Counter

from brise_nlp.plandok.plandok import PlanDok


def main():
    stats = Counter()
    vocab = Counter()
    for line in sys.stdin:
        d = PlanDok.from_dict(json.loads(line))
        stats["docs"] += 1
        for num, section in d.sections:
            stats["sections"] += 1
            for sen in section:
                stats["sens"] += 1
                for tok in sen:
                    stats["toks"] += 1
                    vocab[(tok[0], tok[2])] += 1

    for key, value in stats.items():
        if key == "docs":
            print(f"total docs: {value}")
        else:
            avg = value / stats["docs"]
            print(f"total {key}: {value}, avg: {avg}")

    cutoff = int(sys.argv[2])
    with open(sys.argv[1], "w") as vf:
        for word, count in vocab.most_common():
            if count < cutoff:
                break
            vf.write(f"{word}\t{count}\n")


if __name__ == "__main__":
    main()
