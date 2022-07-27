# BERT Report

## Train all rule based attributes simultaneously

| label                                         |   gold |   predicted |   precision |   recall |      F1 |
|-----------------------------------------------|--------|-------------|-------------|----------|---------|
| total                                         |    837 |         714 |      89.50% |   76.34% |  82.40% |
| Planzeichen                                   |    228 |         223 |      95.52% |   93.42% |  94.46% |
| Widmung                                       |     59 |          44 |      65.91% |   49.15% |  56.31% |
| AnordnungGaertnerischeAusgestaltung           |     42 |          35 |     100.00% |   83.33% |  90.91% |
| GebaeudeHoeheArt                              |     34 |          26 |      96.15% |   73.53% |  83.33% |
| VorkehrungBepflanzung                         |     33 |          31 |     100.00% |   93.94% |  96.88% |
| AbschlussDachMaxBezugGebaeude                 |     28 |          24 |      91.67% |   78.57% |  84.62% |
| AnFluchtlinie                                 |     26 |          25 |      92.00% |   88.46% |  90.20% |
| Dachart                                       |     25 |          22 |      90.91% |   80.00% |  85.11% |
| GebaeudeBautyp                                |     23 |          13 |      84.62% |   47.83% |  61.11% |
| BegruenungDach                                |     23 |          25 |      84.00% |   91.30% |  87.50% |
| VolumenUndUmbaubarerRaum                      |     23 |          12 |     100.00% |   52.17% |  68.57% |
| GehsteigbreiteMin                             |     21 |          21 |     100.00% |  100.00% | 100.00% |
| Nutzungsart                                   |     21 |           8 |      87.50% |   33.33% |  48.28% |
| WidmungInMehrerenEbenen                       |     20 |          20 |      85.00% |   85.00% |  85.00% |
| VonBebauungFreizuhalten                       |     19 |          16 |     100.00% |   84.21% |  91.43% |
| GebaeudeHoeheMaxAbsolut                       |     19 |          18 |      66.67% |   63.16% |  64.86% |
| BBAllgemein                                   |     19 |          17 |      76.47% |   68.42% |  72.22% |
| DurchgangBreite                               |     14 |          15 |      80.00% |   85.71% |  82.76% |
| DachneigungMax                                |     13 |          12 |      91.67% |   84.62% |  88.00% |
| UnterbrechungGeschlosseneBauweise             |     12 |          12 |     100.00% |  100.00% | 100.00% |
| DurchgangHoehe                                |     12 |          12 |      50.00% |   50.00% |  50.00% |
| BebauteFlaecheMax                             |     11 |           0 |     100.00% |    0.00% |   0.00% |
| BauweiseID                                    |     11 |           5 |     100.00% |   45.45% |  62.50% |
| BebauteFlaecheMin                             |     10 |          11 |      81.82% |   90.00% |  85.71% |
| BebauteFlaecheMaxProzentual                   |     10 |           6 |      66.67% |   40.00% |  50.00% |
| AusnahmeGaertnerischAuszugestaltende          |     10 |           8 |      87.50% |   70.00% |  77.78% |
| BebauteFlaecheMaxNebengebaeude                |      8 |           8 |      50.00% |   50.00% |  50.00% |
| AufbautenZulaessig                            |      8 |           6 |     100.00% |   75.00% |  85.71% |
| Stockwerk                                     |      8 |           4 |     100.00% |   50.00% |  66.67% |
| OeffentlicheVerkehrsflaecheBreiteMin          |      7 |           9 |      77.78% |  100.00% |  87.50% |
| VerbotFensterZuOeffentlichenVerkehrsflaechen  |      7 |           4 |     100.00% |   57.14% |  72.73% |
| AnOeffentlichenVerkehrsflaechen               |      6 |           2 |     100.00% |   33.33% |  50.00% |
| DachflaecheMin                                |      6 |           3 |     100.00% |   50.00% |  66.67% |
| VerbotWohnung                                 |      5 |           2 |     100.00% |   40.00% |  57.14% |
| StellplatzregulativUmfangMinimumRelativ       |      5 |           6 |      83.33% |  100.00% |  90.91% |
| AnordnungGaertnerischeAusgestaltungProzentual |      4 |           4 |      75.00% |   75.00% |  75.00% |
| StellplatzregulativUmfangMaximumRelativ       |      4 |           3 |     100.00% |   75.00% |  85.71% |
| FBOKMinimumWohnungen                          |      2 |           2 |     100.00% |  100.00% | 100.00% |
| AnteilDachbegruenung                          |      1 |           0 |     100.00% |    0.00% |   0.00% |

## Train all rule based attributes separately

~ 4 hours / attribute, 40 attributes -> 160 hours (~ 1 week)

| label                                         |   gold |   predicted |   precision |   recall |     F1 |
|-----------------------------------------------|--------|-------------|-------------|----------|--------|
| total                                         |    174 |         144 |      89.58% |   74.14% | 81.13% |
| AnordnungGaertnerischeAusgestaltung           |     42 |          36 |     100.00% |   85.71% | 92.31% |
| AbschlussDachMaxBezugGebaeude                 |     28 |          25 |      92.00% |   82.14% | 86.79% |
| AnFluchtlinie                                 |     26 |          25 |      92.00% |   88.46% | 90.20% |
| BBAllgemein                                   |     19 |          17 |      76.47% |   68.42% | 72.22% |
| BebauteFlaecheMax                             |     11 |           3 |     100.00% |   27.27% | 42.86% |
| BauweiseID                                    |     11 |           9 |      88.89% |   72.73% | 80.00% |
| AusnahmeGaertnerischAuszugestaltende          |     10 |           8 |      87.50% |   70.00% | 77.78% |
| BebauteFlaecheMaxNebengebaeude                |      8 |           9 |      55.56% |   62.50% | 58.82% |
| AufbautenZulaessig                            |      8 |           6 |     100.00% |   75.00% | 85.71% |
| AnOeffentlichenVerkehrsflaechen               |      6 |           2 |     100.00% |   33.33% | 50.00% |
| AnordnungGaertnerischeAusgestaltungProzentual |      4 |           4 |      75.00% |   75.00% | 75.00% |
| AnteilDachbegruenung                          |      1 |           0 |     100.00% |    0.00% |  0.00% |
