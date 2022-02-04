import os
import unittest

from brise_plandok.constants import DocumentFields, SenFields
from brise_plandok.full_attribute_extraction.full_predictor import FullPredictor
from brise_plandok.utils import load_json


class TestFullPredictor(unittest.TestCase):
    def test_get_prediction_for_sen(self):
        doc = load_json(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "../..", "data", "train", "8228.json"))
        predictor = FullPredictor(doc)

        for sen in doc[DocumentFields.SENS].values():
            predictor.get_prediction_for_sen(sen)

        self.assertTrue(SenFields.PREDICTED_ATTRIBUTES in doc[DocumentFields.SENS]["8228_0_0"])
