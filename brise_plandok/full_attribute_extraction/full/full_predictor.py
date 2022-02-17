from brise_plandok.constants import SenFields
from brise_plandok.full_attribute_extraction.attribute.potato.potato_predictor import PotatoPredictor
from brise_plandok.full_attribute_extraction.type.extract_types import extract_type
from brise_plandok.full_attribute_extraction.value.extract_values import extract_value


class FullPredictor:

    def __init__(self, doc):
        self.potato_predictor = PotatoPredictor(doc)

    def get_prediction_for_sen(self, sen):
        attributes = self.potato_predictor.get_prediction_for_sen(sen)
        if SenFields.PREDICTED_ATTRIBUTES not in sen:
            sen[SenFields.PREDICTED_ATTRIBUTES] = {}
        for attribute in attributes:
            extract_type(sen, attribute, field_to_add=SenFields.PREDICTED_ATTRIBUTES, only_gold=False)
            extract_value(sen, attribute, field_to_add=SenFields.PREDICTED_ATTRIBUTES, only_gold=False)
