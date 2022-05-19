from xpotato.graph_extractor.extract import FeatureEvaluator

from brise_plandok.constants import SenFields
from brise_plandok.full_attribute_extraction.attribute.potato.utils import (
    load_features,
    create_potato_dataset_for_doc,
)


class PotatoPredictor:
    def __init__(self, doc):
        dataset, sen_ids = create_potato_dataset_for_doc(doc)
        self.df = dataset.to_dataframe()
        self.df["sen_id"] = sen_ids
        self.evaluator = FeatureEvaluator()
        self.features = load_features()
        self.pred_df = self.evaluator.match_features(self.df, self.features, multi=True)
        self.pred_df["sen_id"] = self.df.sen_id

    def get_prediction_for_sen(self, sen):
        if sen[SenFields.SEGMENTATION_ERROR]:
            return []
        return self.pred_df.loc[self.pred_df["sen_id"] == sen[SenFields.ID]][
            "Predicted label"
        ].to_list()[0]
