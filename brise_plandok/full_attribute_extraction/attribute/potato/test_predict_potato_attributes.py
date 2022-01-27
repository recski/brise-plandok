import os.path
import unittest

from brise_plandok.full_attribute_extraction.attribute.potato.predict_potato_attributes import PotatoPredictor
from brise_plandok.utils import load_json


class TestPotatoPredictor(unittest.TestCase):
    def test_get_prediction_for_attributes(self):
        doc = load_json(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../..", "data", "train", "8228.json"))
        predictor = PotatoPredictor(doc)

        pred_labels = predictor.get_prediction_for_sen_id("8228_10_0")
        self.assertLess(len(pred_labels), 3)
