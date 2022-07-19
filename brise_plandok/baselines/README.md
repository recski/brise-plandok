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

### Logistic Regression 

For the results see [this report file](output/logistic_regression/REPORT.md).

You can recreate the results by calling:

```bash
python classifiers/logistic_regression.py > output/logistic_regression/REPORT.md
```

### Greedy Rule List 

For the results see [this report file](output/greedy_rule_list/REPORT.md).

You can recreate the results by calling:

```bash
python classifiers/greedy_rule_list.py > output/greedy_rule_list/REPORT.md
```

### One Rule 

For the results see [this report file](output/one_rule/REPORT.md).

You can recreate the results by calling:

```bash
python classifiers/one_rule.py > output/one_rule/REPORT.md
```
