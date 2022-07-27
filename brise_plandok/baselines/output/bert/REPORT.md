# BERT Report
## Train all rule based attributes simultaneously

TODO /newstorage4/eiklodi/permanent_output/brise_bert_all/

## Train all rule based attributes separately

~ 4 hours / attribute, 40 attributes -> 160 hours (~ 1 week)

| label                                         |   gold |   predicted |   precision |   recall |     F1 |
|-----------------------------------------------|--------|-------------|-------------|----------|--------|
| total                                         |    174 |         144 |      89.58% |   74.14% | 81.13% |
| AnordnungGaertnerischeAusgestaltung           |     42 |          36 |     100.00% |   85.71% | 92.31% |
| AbschlussDachMaxBezugGebaeude                 |     28 |          25 |      92.00% |   82.14% | 86.79% |
| AnFluchtlinie                                 |     26 |          25 |      92.00% |   88.46% | 90.20% |
| BBAllgemein                                   |     19 |          17 |      76.47% |   68.42% | 72.22% |
| BauweiseID                                    |     11 |           9 |      88.89% |   72.73% | 80.00% |
| BebauteFlaecheMax                             |     11 |           3 |     100.00% |   27.27% | 42.86% |
| AusnahmeGaertnerischAuszugestaltende          |     10 |           8 |      87.50% |   70.00% | 77.78% |
| BebauteFlaecheMaxNebengebaeude                |      8 |           9 |      55.56% |   62.50% | 58.82% |
| AufbautenZulaessig                            |      8 |           6 |     100.00% |   75.00% | 85.71% |
| AnOeffentlichenVerkehrsflaechen               |      6 |           2 |     100.00% |   33.33% | 50.00% |
| AnordnungGaertnerischeAusgestaltungProzentual |      4 |           4 |      75.00% |   75.00% | 75.00% |
| AnteilDachbegruenung                          |      1 |           0 |     100.00% |    0.00% |  0.00% |
