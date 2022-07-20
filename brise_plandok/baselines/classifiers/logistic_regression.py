import argparse

from sklearn.linear_model import LogisticRegression

from brise_plandok.baselines.classifiers.baseline_classifier import BaselineClassifier
from brise_plandok.baselines.constants import RANDOM_STATE


class LogRegClassifier(BaselineClassifier):
    def __init__(self):
        super().__init__(
            "Logistic regression",
            LogisticRegression(random_state=RANDOM_STATE),
        )


def get_args():
    parser = argparse.ArgumentParser(description="")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    LogRegClassifier().run()
