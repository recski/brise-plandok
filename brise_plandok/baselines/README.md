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
python classifiers/decision_tree.py > output/decision_tree/REPORT.md
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

### BERT

For the results see [this report file](output/bert/REPORT.md).

To call a test run for BERT:

```bash
python classifiers/bert/run.py -e 1 -l output/bert -lr 0.01
```

To train a BERT model for multiple attributes:

```bash
./classifiers/bert/run_for_more_attributes.sh -g 2 -l output/bert/ -r 0.001 -e 200 -a Planzeichen -a Widmung
```

To run evaluation on trained BERT models:

```bash
./classifiers/bert/evaluate.sh -a ATTR_LOG_FOLDER -j JOINT_LOG_FOLDER > output/bert/REPORT.md
```
