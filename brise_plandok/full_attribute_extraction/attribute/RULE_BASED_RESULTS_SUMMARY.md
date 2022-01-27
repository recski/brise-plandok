# Rule-based methods

## Task description

Sentence-level multi label classification.

We rated the tried methods:

- ➕➕➕ Great tool with promising results. It would be useful for further research.
- ➕➕ Tool and its results are promising, but if we wanted to work with it, it definitely would require some, but
  foreseeable amount of debugging.
- ➕ Tool provides an interpretable output, but the results are either not promising or they are difficult to interpret.
  For further work an unseeable amount of debugging is estimated.
- ➖ Tool's output is hardly interpretable.
- ➖➖ Tool provides useless or unbelievable results.
- ➖➖➖ Tool does not work (e.g. error).

## [POTATO](https://github.com/adaamko/POTATO)

➕➕➕

(Eszter Iklódi)

We tried to analyze the data with POTATO. Since we already had some rules on 4lang graphs for attribute
extraction ([ASAIL paper](http://ceur-ws.org/Vol-2888/paper3.pdf)), we just converted those rules to a compatible form.

#### Example rule

```json
{
    "VonBebauungFreizuhalten": [
        [
            [
                "(u_0 / Bebauung)"
                // positive
            ],
            [
                "(u_1 / von  :2 (u_3 / Bebauung) :1 (u_2 / freibleibend))"
                // negative
            ],
            "VonBebauungFreizuhalten"
        ]
    ]
}
```

#### Results

| POTATO with improved ASAIL rules    | precision | recall | f1-score | support |
|-------------------------------------|-----------|--------|----------|---------| 
| AbschlussDachMaxBezugGebaeude       | 1.00      | 0.89   | 0.94     | 18      |
| AnFluchtlinie                       | 0.90      | 0.71   | 0.79     | 24      |
| AnordnungGaertnerischeAusgestaltung | 0.93      | 0.90   | 0.91     | 29      |
| BegruenungDach                      | 0.88      | 0.91   | 0.89     | 23      |
| Dachart                             | 0.96      | 0.84   | 0.89     | 25      |
| Flaechen                            | 1.00      | 0.19   | 0.31     | 43      |
| GebaeudeBautyp                      | 1.00      | 0.67   | 0.80     | 21      |
| GebaeudeHoeheArt                    | 1.00      | 0.47   | 0.64     | 19      |
| GebaeudeHoeheMax                    | 1.00      | 0.55   | 0.71     | 22      |
| Planzeichen                         | 0.88      | 0.23   | 0.36     | 163     |
| VerkehrsflaecheID                   | 0.26      | 0.33   | 0.29     | 21      |
| VonBebauungFreizuhalten             | 0.82      | 0.45   | 0.58     | 20      |
| VorkehrungBepflanzung               | 1.00      | 0.91   | 0.95     | 21      |
| WidmungInMehrerenEbenen             | 0.90      | 0.64   | 0.75     | 14      |
| WidmungUndZweckbestimmung           | 0.93      | 0.21   | 0.34     | 62      |

### Notes

➕ Explainable rules.

➕ Great GUI for exploration. You can browse TP, FP and FN examples.

➗ We need a graph representation.

➖ The default algorithm (decision tree) might not find the best rules.

## [imodels](https://github.com/csinva/imodels)

(Eszter Iklódi)

This library has a wide collection of interpretable models.  
The input for this experiment is the BoW representation of the sentences.

### [RuleFitClassifier](https://csinva.io/imodels/rule_set/rule_fit.html#imodels.rule_set.rule_fit.RuleFitClassifier)

➕➕

#### Example rule

```text
AbschlussDachMaxBezugGebaeude
RuleFit:
                                                                                                      rule  coef
                                                                                                      darf  0.19
                                                                                                gebaudehoh  0.91
                                                 abschluss <= 0.5 and ausgefuhrt <= 0.5 and uberrag <= 0.5 -0.72
                                                                            oberst <= 0.5 and punkt <= 0.5 -0.61
                                                                         abschluss <= 0.5 and punkt <= 0.5 -0.83
                                    abschluss <= 0.5 and hoch <= 0.5 and tatsach <= 0.5 and uberrag <= 0.5 -0.81
                                 abschluss <= 0.5 and hoch <= 0.5 and hochstzulass <= 0.5 and punkt <= 0.5 -0.02
zuzufuhr <= 0.5 and der <= 0.5 and hoch <= 0.5 and hochstzulass <= 0.5 and punkt <= 0.5 and uberrag <= 0.5 -1.10
                                                              dach <= 0.5 and konstruktionsoberkant <= 0.5 -0.92
                                                                                         gebaudehoh <= 0.5 -0.53
                                                 gebaudehoh <= 0.5 and hoch <= 0.5 and unterschreit <= 0.5 -0.75
                                                                                          gebaudehoh > 0.5  0.31
                                                                    bezeichnet <= 0.5 and gebaudehoh > 0.5  0.09
                                                          dach > 0.5 and flach <= 0.5 and gebaudehoh > 0.5  0.28
                                                                                 dach > 0.5 and darf > 0.5  0.86
```

#### Results

| RuleFitClassifier (default setup)   | precision | recall | f1-score | support |
|-------------------------------------|-----------|--------|----------|---------| 
| AbschlussDachMaxBezugGebaeude       |  1.00      | 1.00   | 1.00     | 18      |
| AnFluchtlinie                       |  0.83      | 0.83   | 0.83     | 24      |
| AnordnungGaertnerischeAusgestaltung |  0.87      | 0.93   | 0.90     | 29      |
| BegruenungDach                      |  0.91      | 0.91   | 0.91     | 23      |
| Dachart                             |  0.92      | 0.96   | 0.94     | 25      |
| Flaechen                            |  0.90      | 0.60   | 0.72     | 43      |
| GebaeudeBautyp                      |  1.00      | 0.67   | 0.80     | 21      |
| GebaeudeHoeheArt                    |  0.95      | 0.95   | 0.95     | 19      |
| GebaeudeHoeheMax                    |  0.79      | 0.68   | 0.73     | 22      |
| Planzeichen                         |  0.93      | 0.93   | 0.93     | 163     |
| VerkehrsflaecheID                   |  0.94      | 0.71   | 0.81     | 21      |
| VonBebauungFreizuhalten             |  0.75      | 0.60   | 0.67     | 20      |
| VorkehrungBepflanzung               |  1.00      | 1.00   | 1.00     | 21      |
| WidmungInMehrerenEbenen             |  0.92      | 0.79   | 0.85     | 14      |
| WidmungUndZweckbestimmung           |  0.82      | 0.53   | 0.65     | 62      |

➕ Explainable rules.

➕ Apparently quite good results out of the box.

➗ We need a vector representation.

➖ Rules are a bit complicated and not so straightforward.

➖ Lots of complicated negated rules, instead of simpler not-negated rules.

### [BoostedRulesClassifier](https://csinva.io/imodels/rule_set/boosted_rules.html#imodels.rule_set.boosted_rules.BoostedRulesClassifier)

➕➕

#### Example rule

```text
AbschlussDachMaxBezugGebaeude
BoostedRules:
Rule → predicted probability (final prediction is weighted sum of all predictions)
  If hoch <= 0.5 → 0.04 (weight: 2.24)
  If hoch > 0.5 → 0.07 (weight: 0.95)
  If gebaudehoh <= 0.5 → 0.01 (weight: 1.32)
  If gebaudehoh > 0.5 → 0.07 (weight: 0.52)
  If abschluss <= 0.5 → 0.96 (weight: 0.67)
  If abschluss > 0.5 → 0.07 (weight: 0.54)
  If dach <= 0.5 → 0.02 (weight: 0.49)
  If dach > 0.5 → 0.12 (weight: 0.44)
  If hoch <= 0.5 → 0.88 (weight: 0.38)
  If hoch > 0.5 → 0.00 (weight: 0.24)
```

#### Results

| BoostedRulesClassifier (default setup)   | precision | recall | f1-score | support |
|-------------------------------------|-----------|--------|----------|---------| 
| AbschlussDachMaxBezugGebaeude       | 1.00      | 1.00   | 1.00     | 18      |
| AnFluchtlinie                       | 0.88      | 0.62   | 0.73     | 24      |
| AnordnungGaertnerischeAusgestaltung | 0.84      | 0.93   | 0.89     | 29      |
| BegruenungDach                      | 0.87      | 0.87   | 0.87     | 23      |
| Dachart                             | 0.92      | 0.88   | 0.90     | 25      |
| Flaechen                            | 0.75      | 0.42   | 0.54     | 43      |
| GebaeudeBautyp                      | 1.00      | 0.67   | 0.80     | 21      |
| GebaeudeHoeheArt                    | 0.95      | 0.95   | 0.95     | 19      |
| GebaeudeHoeheMax                    | 0.41      | 0.73   | 0.52     | 22      |
| Planzeichen                         | 0.94      | 0.91   | 0.92     | 163     |
| VerkehrsflaecheID                   | 1.00      | 0.57   | 0.73     | 21      |
| VonBebauungFreizuhalten             | 0.75      | 0.45   | 0.56     | 20      |
| VorkehrungBepflanzung               | 1.00      | 0.57   | 0.73     | 21      |
| WidmungInMehrerenEbenen             | 0.91      | 0.71   | 0.80     | 14      |
| WidmungUndZweckbestimmung           | 0.72      | 0.21   | 0.33     | 62      |

➕ Clear rule output format.

➗ We need a vector representation.

➗ Always rule-negated rule pair.

➖ Quite doubtful rules. Strong suspicion that rules have to be inverted.

➖ Repeated rules.

### [SkopeRulesClassifier](https://csinva.io/imodels/rule_set/slipper.html#imodels.rule_set.slipper.SlipperClassifier)

➖ ➖

#### Example rule

```text
// no output
```

#### Results

| SkopeRulesClassifier (default setup)   | precision | recall | f1-score | support |
|-------------------------------------|-----------|--------|----------|---------| 
| AbschlussDachMaxBezugGebaeude       | 0.00      | 0.00   |  0.00     | 18      |
| AnFluchtlinie                       | 0.00      | 0.00   |  0.00     | 24      |
| AnordnungGaertnerischeAusgestaltung | 0.88      | 0.48   |  0.62     | 29      |
| BegruenungDach                      | 0.00      | 0.00   |  0.00     | 23      |
| Dachart                             | 0.00      | 0.00   |  0.00     | 25      |
| Flaechen                            | 0.00      | 0.00   |  0.00     | 43      |
| GebaeudeBautyp                      | 0.00      | 0.00   |  0.00     | 21      |
| GebaeudeHoeheArt                    | 0.00      | 0.00   |  0.00     | 19      |
| GebaeudeHoeheMax                    | 0.00      | 0.00   |  0.00     | 22      |
| Planzeichen                         | 0.00      | 0.00   |  0.00     | 163     |
| VerkehrsflaecheID                   | 0.00      | 0.00   |  0.00     | 21      |
| VonBebauungFreizuhalten             | 0.00      | 0.00   |  0.00     | 20      |
| VorkehrungBepflanzung               | 0.00      | 0.00   |  0.00     | 21      |
| WidmungInMehrerenEbenen             | 0.00      | 0.00   |  0.00     | 14      |
| WidmungUndZweckbestimmung           | 0.00      | 0.00   |  0.00     | 62      |

➗ We need a vector representation.

➖ No rules are shown.

➖ One has non 0.0 result for one (!) attribute.

### [GreedyRuleListClassifier](https://csinva.io/imodels/rule_list/greedy_rule_list.html#imodels.rule_list.greedy_rule_list.GreedyRuleListClassifier)

➕➕➕

#### Example rule

```text
VorkehrungBepflanzung
mean 0.04 (8946 pts)
if baumreih >= 1 then 0.993 (273 pts)
mean 0.01 (8673 pts)
if baum >= 1 then 0.98 (49 pts)
mean 0.005 (8624 pts)
if cm >= 1 then 0.765 (17 pts)
mean 0.003 (8607 pts)
if machtig >= 1 then 0.714 (14 pts)
mean 0.002 (8593 pts)
if baumpflanz >= 1 then 0.8 (5 pts)
```

#### Results

| GreedyRuleListClassifier  (default setup) | precision | recall | f1-score | support |
|-------------------------------------------|-----------|--------|----------|---------| 
| AbschlussDachMaxBezugGebaeude             | 0.90      | 1.00   |  0.95     | 18      |
| AnFluchtlinie                             | 0.73      | 0.92   |  0.81     | 24      |
| AnordnungGaertnerischeAusgestaltung       | 0.84      | 0.93   |  0.89     | 29      |
| BegruenungDach                            | 0.85      | 0.96   |  0.90     | 23      |
| Dachart                                   | 0.83      | 0.96   |  0.89     | 25      |
| Flaechen                                  | 0.69      | 0.72   |  0.70     | 43      |
| GebaeudeBautyp                            | 1.00      | 0.81   |  0.89     | 21      |
| GebaeudeHoeheArt                          | 0.86      | 0.95   |  0.90     | 19      |
| GebaeudeHoeheMax                          | 0.00      | 0.00   |  0.00     | 22      |
| Planzeichen                               | 0.82      | 0.92   |  0.86     | 163     |
| VerkehrsflaecheID                         | 0.80      | 0.57   |  0.67     | 21      |
| VonBebauungFreizuhalten                   | 0.75      | 0.45   |  0.56     | 20      |
| VorkehrungBepflanzung                     | 1.00      | 1.00   |  1.00     | 21      |
| WidmungInMehrerenEbenen                   | 0.87      | 0.93   |  0.90     | 14      |
| WidmungUndZweckbestimmung                 | 0.74      | 0.52   |  0.61     | 62      |

➕ Explainable rules.

➕ Clear rule output format.

➕ Quite good and reasonable results.

➗ Only positive rules.

➗ We need a vector representation.

➖ Probably a bug for `GebaeudeHoeheMax`?

### [OneRClassifier](https://csinva.io/imodels/rule_list/one_r.html#imodels.rule_list.one_r.OneRClassifier)

➕➕➕

#### Example rule

```text
AbschlussDachMaxBezugGebaeude
mean 0.034 (8946 pts)
if hoch >= 1 then 0.815 (319 pts)
mean 0.005 (8627 pts)
if hoch >= 0 then 0.005 (8627 pts)
```

#### Results

| OneRClassifier (default setup)      | precision | recall | f1-score | support |
|-------------------------------------|-----------|--------|----------|---------| 
| AbschlussDachMaxBezugGebaeude       | 0.90      |  1.00   |   0.95     | 18      |
| AnFluchtlinie                       | 0.88      |  0.58   |   0.70     | 24      |
| AnordnungGaertnerischeAusgestaltung | 0.84      |  0.93   |   0.89     | 29      |
| BegruenungDach                      | 0.87      |  0.87   |   0.87     | 23      |
| Dachart                             | 0.92      |  0.88   |   0.90     | 25      |
| Flaechen                            | 0.74      |  0.40   |   0.52     | 43      |
| GebaeudeBautyp                      | 1.00      |  0.67   |   0.80     | 21      |
| GebaeudeHoeheArt                    | 1.00      |  0.42   |   0.59     | 19      |
| GebaeudeHoeheMax                    | 0.00      |  0.00   |   0.00     | 22      |
| Planzeichen                         | 0.82      |  0.82   |   0.82     | 163     |
| VerkehrsflaecheID                   | 1.00      |  0.57   |   0.73     | 21      |
| VonBebauungFreizuhalten             | 0.75      |  0.45   |   0.56     | 20      |
| VorkehrungBepflanzung               | 1.00      |  0.57   |   0.73     | 21      |
| WidmungInMehrerenEbenen             | 0.91      |  0.71   |   0.80     | 14      |
| WidmungUndZweckbestimmung           | 0.72      |  0.21   |   0.33     | 62      |

➕ Explainable rules.

➕ Clear rule output format.

➕ Quite good and reasonable results. (Better results, than Greedy!)

➕ Fast, since classifies on the basis of one attribute.

➗ Always rule-negated rule pair.

➗ We need a vector representation.

➖ Probably a bug for `GebaeudeHoeheMax`?

### [GreedyTreeClassifier](https://csinva.io/imodels/tree/cart_wrapper.html#imodels.tree.cart_wrapper.GreedyTreeClassifier)

➕➕

#### Example rule

```text
AbschlussDachMaxBezugGebaeude
GreedyTree:
|--- X616 <= 0.50
|   |--- X124 <= 0.50
|   |   |--- X620 <= 0.50
|   |   |   |--- X965 <= 0.50
|   |   |   |   |--- X777 <= 0.50
|   |   |   |   |   |--- X354 <= 0.50
|   |   |   |   |   |   |--- weights: [8370.00, 0.00] class: 0
|   |   |   |   |   |--- X354 >  0.50
|   |   |   |   |   |   |--- X461 <= 0.50
|   |   |   |   |   |   |   |--- weights: [45.00, 0.00] class: 0
|   |   |   |   |   |   |--- X461 >  0.50
|   |   |   |   |   |   |   |--- X256 <= 0.50
|   |   |   |   |   |   |   |   |--- weights: [0.00, 3.00] class: 1
|   |   |   |   |   |   |   |--- X256 >  0.50
|   |   |   |   |   |   |   |   |--- weights: [2.00, 0.00] class: 0
...
```

#### Results

| GreedyTreeClassifier (default setup)    | precision  | recall   | f1-score  | support |
|-----------------------------------------|------------|----------|-----------|---------| 
| AbschlussDachMaxBezugGebaeude           | 0.95       | 1.00     | 0.97      | 18      |
| AnFluchtlinie                           | 0.73       | 0.92     | 0.81      | 24      |
| AnordnungGaertnerischeAusgestaltung     | 0.96       | 0.86     | 0.91      | 29      |
| BegruenungDach                          | 0.92       | 1.00     | 0.96      | 23      |
| Dachart                                 | 0.88       | 0.92     | 0.90      | 25      |
| Flaechen                                | 0.72       | 0.72     | 0.72      | 43      |
| GebaeudeBautyp                          | 0.94       | 0.76     | 0.84      | 21      |
| GebaeudeHoeheArt                        | 0.95       | 0.95     | 0.95      | 19      |
| GebaeudeHoeheMax                        | 0.76       | 0.73     | 0.74      | 22      |
| Planzeichen                             | 0.89       | 0.93     | 0.91      | 163     |
| VerkehrsflaecheID                       | 0.77       | 0.81     | 0.79      | 21      |
| VonBebauungFreizuhalten                 | 0.56       | 0.75     | 0.64      | 20      |
| VorkehrungBepflanzung                   | 1.00       | 0.95     | 0.98      | 21      |
| WidmungInMehrerenEbenen                 | 0.88       | 1.00     | 0.93      | 14      |
| WidmungUndZweckbestimmung               | 0.67       | 0.71     | 0.69      | 62      |

➕ Explainable rules.

➕ Quite good results.

➗ We need a vector representation.

➖ Too complicated rules.

➖ Error if feature_names are defined. Hard to interpret.

### [SLIMClassifier](https://csinva.io/imodels/algebraic/slim.html#imodels.algebraic.slim.SLIMClassifier)

➕

#### Example rule

```text
// no rules
```

#### Results

| SLIMClassifier (default setup)      | precision  | recall   | f1-score  | support |
|-------------------------------------|------------|----------|-----------|---------| 
| AbschlussDachMaxBezugGebaeude       |  0.95       |  1.00     |  0.97      | 18      |
| AnFluchtlinie                       |  0.79       |  0.79     |  0.79      | 24      |
| AnordnungGaertnerischeAusgestaltung |  0.90       |  0.93     |  0.92      | 29      |
| BegruenungDach                      |  0.88       |  0.91     |  0.89      | 23      |
| Dachart                             |  0.89       |  0.96     |  0.92      | 25      |
| Flaechen                            |  0.76       |  0.86     |  0.80      | 43      |
| GebaeudeBautyp                      |  1.00       |  0.71     |  0.83      | 21      |
| GebaeudeHoeheArt                    |  0.95       |  0.95     |  0.95      | 19      |
| GebaeudeHoeheMax                    |  0.94       |  0.68     |  0.79      | 22      |
| Planzeichen                         |  0.93       |  0.94     |  0.94      | 163     |
| VerkehrsflaecheID                   |  0.90       |  0.86     |  0.88      | 21      |
| VonBebauungFreizuhalten             |  0.78       |  0.70     |  0.74      | 20      |
| VorkehrungBepflanzung               |  1.00       |  0.95     |  0.98      | 21      |
| WidmungInMehrerenEbenen             |  0.83       |  0.71     |  0.77      | 14      |
| WidmungUndZweckbestimmung           |  0.83       |  0.63     |  0.72      | 62      |

➕ Quite good results.

➗ We need a vector representation.

➖ No rules.

## Summary of rule-based tools

| Tool                          | Evaluation | Note                                                           |
|-------------------------------|------------|----------------------------------------------------------------|
| POTATO                        | ➕➕➕        | Discover more!                                                 | 
| RuleFitClassifier             | ➕➕         | Duplicates? Reduce number of rules                             |
| BoostedRulesClassifier        | ➕➕         | Inverted  rules?                                               |
| SkopeRulesClassifier          | ➖ ➖        | No results (0.0)                                               |
| SlipperClassifier             | ➖ ➖ ➖      | Long run, fails to provide results                             |
| BayesianRuleSetClassifier     | ➖ ➖ ➖      | Works with DNF (!), but fails to produce results.              | 
| GreedyRuleListClassifier      | ➕➕➕        | Discover more! `GebaeudeHoeheMax` bug?                         |
| OneRClassifier                | ➕➕➕        | Discover more! `GebaeudeHoeheMax` bug? So simple!              |
| GreedyTreeClassifier          | ➕➕         | Show feature names?                                            |
| C45TreeClassifier             | ➖ ➖ ➖      | Long run, fails to provide results                             |
| IRFClassifier                 | ➖ ➖ ➖      | Unexpected keyword argument 'min_impurity_split'               |
| SLIMClassifier                | ➕          | No rules, probably only LogReg.                                |
| SaplingSumClassifier          | ➖ ➖ ➖      | TypeError: '(slice(None, None, None), 615)' is an invalid key  |

