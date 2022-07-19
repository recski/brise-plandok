import argparse
import os.path

from graphviz import Source
from sklearn import tree

from brise_plandok.baselines.classifiers.baseline_classifier import BaselineClassifier
from brise_plandok.baselines.constants import RANDOM_STATE
from brise_plandok.baselines.utils import get_output_dir

MAX_DEPTH = 5


class DTClassifier(BaselineClassifier):
    def __init__(self):
        super().__init__(
            "Decision tree",
            tree.DecisionTreeClassifier(max_depth=MAX_DEPTH, random_state=RANDOM_STATE),
        )

    def _additional_output_for_label(self, clf, feature_names, class_names, label):
        graph = Source(
            tree.export_graphviz(
                clf,
                out_file=None,
                feature_names=feature_names,
                class_names=class_names,
            )
        )
        graph.render(
            os.path.join(get_output_dir("decision_tree"), label), view=False, format="pdf"
        )


def get_args():
    parser = argparse.ArgumentParser(description="")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    DTClassifier().run({"max depth": MAX_DEPTH})
