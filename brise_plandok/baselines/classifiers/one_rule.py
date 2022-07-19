import argparse

from imodels import OneRClassifier

from brise_plandok.baselines.classifiers.baseline_classifier import BaselineClassifier
from brise_plandok.baselines.constants import MAX_DEPTH


class OneRule(BaselineClassifier):
    def __init__(self):
        super().__init__(
            "One rule",
            OneRClassifier(max_depth=MAX_DEPTH),
        )

    def _fit(self, x, y, feature_names=None):
        self.classifier.fit(x, y, feature_names=feature_names)

    def _additional_output_for_label(self, clf, feature_names, class_names, label):
        print()
        print(self.classifier)


def get_args():
    parser = argparse.ArgumentParser(description="")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    OneRule().run({"max depth": MAX_DEPTH})
