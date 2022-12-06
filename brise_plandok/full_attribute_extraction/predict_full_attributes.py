import json
import sys

from brise_plandok.constants import DocumentFields
from brise_plandok.full_attribute_extraction.full.full_predictor import FullPredictor


def predict_attributes():
    docs = []
    for line in sys.stdin:
        doc = json.loads(line)
        docs.append(doc)

    full_predictor = FullPredictor(docs)
    for doc in docs:
        for sen in doc[DocumentFields.SENS].values():
            full_predictor.get_prediction_for_sen(sen)
        sys.stdout.write(json.dumps(doc) + "\n")


if __name__ == "__main__":
    predict_attributes()
