import torch

from brise_plandok.baselines.classifiers.bert.brise_bert_base import BriseBertBase


class BriseBertEvaluator(BriseBertBase):
    def __init__(self, attribute, test_dataset, model_checkpoint):
        super().__init__(attribute, test_dataset)
        self.model.load_state_dict(torch.load(model_checkpoint, map_location=self.device))
        _ = self.model.to(self.device)
