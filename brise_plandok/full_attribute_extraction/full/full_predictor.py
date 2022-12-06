from brise_plandok.constants import SenFields
from brise_plandok.full_attribute_extraction.attribute.potato.potato_predictor import (
    PotatoPredictor,
)
from brise_plandok.full_attribute_extraction.type.extract_types import extract_type
from brise_plandok.full_attribute_extraction.value.extract_values import extract_value
from brise_plandok.full_attribute_extraction.modality.predict_modalities import (
    predict_modality_for_sen,
)


class FullPredictor:
    def __init__(self, docs):
        self.potato_predictor = PotatoPredictor(docs)

    def get_prediction_for_sen(self, sen):
        attributes = self.potato_predictor.get_prediction_for_sen(sen)
        sen[SenFields.PREDICTED_ATTRIBUTES] = {}
        for attribute in attributes:
            extract_type(
                sen,
                attribute,
                field_to_add=SenFields.PREDICTED_ATTRIBUTES,
                only_gold=False,
            )
            extract_value(
                sen,
                attribute,
                field_to_add=SenFields.PREDICTED_ATTRIBUTES,
                only_gold=False,
            )

        predict_modality_for_sen(sen, pred_only=True)
