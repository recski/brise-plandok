import csv
import os


BRISE_NLP_DIR = os.getenv(
    'BRISE_NLP_DIR', '/home/recski/projects/brise/brise-nlp')

ATTR_FN = os.path.join(
    BRISE_NLP_DIR, 'sample_data/plandok/merkmale_categories.csv')

with open(ATTR_FN) as f:
    for i, row in enumerate(csv.reader(f, delimiter=";", quotechar='"')):
        if i == 0:
            categories = row
            ATTRS_BY_CAT = {cat: set() for cat in categories}
            ATTR_TO_CAT = {}
            continue
        for j, attr in enumerate(row):
            if not attr:
                continue
            cat = categories[j]
            ATTRS_BY_CAT[cat].add(attr)
            ATTR_TO_CAT[attr] = cat


if __name__ == '__main__':
    print(ATTRS_BY_CAT)
    print(ATTR_TO_CAT)
