import json
import random
import sys


def print_doc(doc):
    for sec in doc["sections"]:
        if sec["num"] == "header":
            continue

        for sen in sec["sens"]:
            print(f"{sen['sen_id']}\t{sen['text']}")


def sample_ids(ids, n, seed):
    sys.stderr.write(f"using random seed {seed}\n")
    # sample of 10 docs first created on Aug 6 2020
    # random.seed(20200806)

    # sample of 100 docs created on Aug 11 2020
    # random.seed(20200811)

    random.seed(seed)
    return random.sample(ids, n)


def main():
    n = int(sys.argv[2])
    seed = int(sys.argv[3])
    with open(sys.argv[1]) as f:
        ids_to_docs = {doc["id"]: doc for doc in (json.loads(line.strip()) for line in f)}

    for i in sorted(sample_ids(ids_to_docs.keys(), n, seed)):
        print_doc(ids_to_docs[i])


if __name__ == "__main__":
    main()
