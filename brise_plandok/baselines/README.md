# Baseline Experiments

## Featurize

For baseline experiments we used Bag of Words features, vectorized by the [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) from sklearn.

The featurized dataframes are saved in csv format in the [input](input) folder.

You can recreate these dataframes by calling the [featurize](featurize.py) script:

```bash
python featureize.py
```

## Classifiers

### Decision Tree

For the results see [this report file](output/decision_tree/REPORT.md).

You can recreate the results by calling:

```bash
python classifiers/decistion_tree.py > output/decision_tree/REPORT.md
```