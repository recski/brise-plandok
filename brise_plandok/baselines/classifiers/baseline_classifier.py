from sklearn.metrics import classification_report
from tuw_nlp.common.eval import get_cat_stats, print_cat_stats

from brise_plandok.baselines.constants import NOT, ALL_LABELS_SORTED, TOP
from brise_plandok.baselines.utils import get_x_y_dataframes, filter_gold
from brise_plandok.constants import TRAIN, VALID


class BaselineClassifier:
    def __init__(self, name, classifier):
        self.name = name
        self.classifier = classifier

    def run(self, hyperparams):
        print(f"# {self.name} classifier - report")
        print(f"Run for the top {TOP} attributes with hyperparams: {hyperparams}.")
        x_train_df, y_train_df, x_train = get_x_y_dataframes(TRAIN)
        x_valid_df, y_valid_df, x_valid = get_x_y_dataframes(VALID)
        golds = y_valid_df.Labels.tolist()
        golds = filter_gold(golds, TOP)
        preds = [set() for _ in range(len(golds))]
        for label in ALL_LABELS_SORTED[:TOP]:
            print(f"## {label}")
            print("```bash")
            y_train = y_train_df.loc[:, [label]]
            y_valid = y_valid_df.loc[:, [label]]
            clf = self.classifier.fit(x_train, y_train)
            y_pred = clf.predict(x_valid)
            for i, pred in enumerate(y_pred):
                if pred > 0.5:
                    preds[i].add(label)
            print(classification_report(y_valid[label], y_pred, target_names=[NOT, label]))
            print("```")
            self._additional_output_for_label(clf, x_train.columns.tolist(), [NOT, label], label)
        print("## Summary")
        print_cat_stats(get_cat_stats(preds, golds))

    def _additional_output_for_label(self, clf, feature_names, class_names, label):
        pass
