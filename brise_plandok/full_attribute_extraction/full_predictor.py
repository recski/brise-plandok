from brise_plandok.constants import SenFields
from brise_plandok.full_attribute_extraction.attribute.potato.potato_predictor import PotatoPredictor
from brise_plandok.full_attribute_extraction.type.type_extractor import TypeExtractor
from brise_plandok.full_attribute_extraction.value.value_extractor import ValueExtractor


class FullPredictor:

    def __init__(self, doc):
        self.potato_predictor = PotatoPredictor(doc)
        self.value_extractor = ValueExtractor()
        self.type_extractor = TypeExtractor()

    def get_prediction_for_sen(self, sen):
        attributes = self.potato_predictor.get_prediction_for_sen(sen)
        if SenFields.PREDICTED_ATTRIBUTES not in sen:
            sen[SenFields.PREDICTED_ATTRIBUTES] = {}
        for attribute in attributes:
            self.value_extractor.extract_for_attr(sen, attribute, field_to_add=SenFields.PREDICTED_ATTRIBUTES,
                                                  only_if_gold=False)
            self.type_extractor.extract_for_attr(sen, attribute, field_to_add=SenFields.PREDICTED_ATTRIBUTES,
                                                 only_if_gold=False)
