# BERT Report

## Train all rule based attributes simultaneously

| label                                         |   gold |   predicted |   precision |   recall |      F1 |
|-----------------------------------------------|--------|-------------|-------------|----------|---------|
| total                                         |    837 |         741 |      90.42% |   80.05% |  84.92% |
| macro average                                 |    837 |         741 |      89.61% |   74.08% |  78.51% |
| Planzeichen                                   |    228 |         228 |      95.61% |   95.61% |  95.61% |
| Widmung                                       |     59 |          42 |      76.19% |   54.24% |  63.37% |
| AnordnungGaertnerischeAusgestaltung           |     42 |          36 |     100.00% |   85.71% |  92.31% |
| GebaeudeHoeheArt                              |     34 |          26 |      96.15% |   73.53% |  83.33% |
| VorkehrungBepflanzung                         |     33 |          32 |     100.00% |   96.97% |  98.46% |
| AbschlussDachMaxBezugGebaeude                 |     28 |          25 |      92.00% |   82.14% |  86.79% |
| AnFluchtlinie                                 |     26 |          26 |      92.31% |   92.31% |  92.31% |
| Dachart                                       |     25 |          22 |      90.91% |   80.00% |  85.11% |
| BegruenungDach                                |     23 |          23 |      95.65% |   95.65% |  95.65% |
| GebaeudeBautyp                                |     23 |          14 |      78.57% |   47.83% |  59.46% |
| VolumenUndUmbaubarerRaum                      |     23 |          16 |      93.75% |   65.22% |  76.92% |
| GehsteigbreiteMin                             |     21 |          22 |      95.45% |  100.00% |  97.67% |
| Nutzungsart                                   |     21 |           8 |      87.50% |   33.33% |  48.28% |
| WidmungInMehrerenEbenen                       |     20 |          20 |      85.00% |   85.00% |  85.00% |
| BBAllgemein                                   |     19 |          17 |      76.47% |   68.42% |  72.22% |
| GebaeudeHoeheMaxAbsolut                       |     19 |          19 |      68.42% |   68.42% |  68.42% |
| VonBebauungFreizuhalten                       |     19 |          17 |      94.12% |   84.21% |  88.89% |
| DurchgangBreite                               |     14 |          15 |      80.00% |   85.71% |  82.76% |
| DachneigungMax                                |     13 |          12 |      91.67% |   84.62% |  88.00% |
| DurchgangHoehe                                |     12 |          14 |      57.14% |   66.67% |  61.54% |
| UnterbrechungGeschlosseneBauweise             |     12 |          12 |     100.00% |  100.00% | 100.00% |
| BauweiseID                                    |     11 |           8 |      87.50% |   63.64% |  73.68% |
| BebauteFlaecheMax                             |     11 |           3 |     100.00% |   27.27% |  42.86% |
| AusnahmeGaertnerischAuszugestaltende          |     10 |           8 |      87.50% |   70.00% |  77.78% |
| BebauteFlaecheMaxProzentual                   |     10 |           6 |      83.33% |   50.00% |  62.50% |
| BebauteFlaecheMin                             |     10 |          11 |      81.82% |   90.00% |  85.71% |
| AufbautenZulaessig                            |      8 |           6 |     100.00% |   75.00% |  85.71% |
| BebauteFlaecheMaxNebengebaeude                |      8 |           9 |      55.56% |   62.50% |  58.82% |
| Stockwerk                                     |      8 |           4 |     100.00% |   50.00% |  66.67% |
| OeffentlicheVerkehrsflaecheBreiteMin          |      7 |           9 |      77.78% |  100.00% |  87.50% |
| VerbotFensterZuOeffentlichenVerkehrsflaechen  |      7 |           5 |     100.00% |   71.43% |  83.33% |
| AnOeffentlichenVerkehrsflaechen               |      6 |           3 |     100.00% |   50.00% |  66.67% |
| DachflaecheMin                                |      6 |           4 |     100.00% |   66.67% |  80.00% |
| StellplatzregulativUmfangMinimumRelativ       |      5 |           6 |      83.33% |  100.00% |  90.91% |
| VerbotWohnung                                 |      5 |           3 |     100.00% |   60.00% |  75.00% |
| AnordnungGaertnerischeAusgestaltungProzentual |      4 |           5 |      80.00% |  100.00% |  88.89% |
| StellplatzregulativUmfangMaximumRelativ       |      4 |           3 |     100.00% |   75.00% |  85.71% |
| FBOKMinimumWohnungen                          |      2 |           2 |     100.00% |  100.00% | 100.00% |
| AnteilDachbegruenung                          |      1 |           0 |     100.00% |    0.00% |   0.00% |
| GebaeudeHoeheMaxWN                            |      0 |           0 |     100.00% |  100.00% | 100.00% |

## Train all rule based attributes separately

~ 4 hours / attribute, 40 attributes -> 160 hours (~ 1 week)

| label                                         |   gold |   predicted |   precision |   recall |      F1 |
|-----------------------------------------------|--------|-------------|-------------|----------|---------|
| total                                         |    837 |         728 |      91.07% |   79.21% |  84.73% |
| Planzeichen                                   |    228 |         228 |      95.61% |   95.61% |  95.61% |
| Widmung                                       |     59 |          43 |      69.77% |   50.85% |  58.82% |
| AnordnungGaertnerischeAusgestaltung           |     42 |          36 |     100.00% |   85.71% |  92.31% |
| GebaeudeHoeheArt                              |     34 |          27 |      96.30% |   76.47% |  85.25% |
| VorkehrungBepflanzung                         |     33 |          32 |     100.00% |   96.97% |  98.46% |
| AbschlussDachMaxBezugGebaeude                 |     28 |          25 |      92.00% |   82.14% |  86.79% |
| AnFluchtlinie                                 |     26 |          25 |      92.00% |   88.46% |  90.20% |
| Dachart                                       |     25 |          22 |      90.91% |   80.00% |  85.11% |
| BegruenungDach                                |     23 |          22 |      95.45% |   91.30% |  93.33% |
| GebaeudeBautyp                                |     23 |          14 |      78.57% |   47.83% |  59.46% |
| VolumenUndUmbaubarerRaum                      |     23 |          21 |      90.48% |   82.61% |  86.36% |
| GehsteigbreiteMin                             |     21 |          21 |     100.00% |  100.00% | 100.00% |
| Nutzungsart                                   |     21 |           9 |      77.78% |   33.33% |  46.67% |
| WidmungInMehrerenEbenen                       |     20 |          20 |      85.00% |   85.00% |  85.00% |
| BBAllgemein                                   |     19 |          17 |      76.47% |   68.42% |  72.22% |
| GebaeudeHoeheMaxAbsolut                       |     19 |          18 |      66.67% |   63.16% |  64.86% |
| VonBebauungFreizuhalten                       |     19 |          16 |     100.00% |   84.21% |  91.43% |
| DurchgangBreite                               |     14 |          14 |      85.71% |   85.71% |  85.71% |
| DachneigungMax                                |     13 |          12 |      91.67% |   84.62% |  88.00% |
| DurchgangHoehe                                |     12 |           6 |      83.33% |   41.67% |  55.56% |
| UnterbrechungGeschlosseneBauweise             |     12 |          12 |     100.00% |  100.00% | 100.00% |
| BauweiseID                                    |     11 |           9 |      88.89% |   72.73% |  80.00% |
| BebauteFlaecheMax                             |     11 |           3 |     100.00% |   27.27% |  42.86% |
| AusnahmeGaertnerischAuszugestaltende          |     10 |           8 |      87.50% |   70.00% |  77.78% |
| BebauteFlaecheMaxProzentual                   |     10 |           4 |     100.00% |   40.00% |  57.14% |
| BebauteFlaecheMin                             |     10 |          11 |      81.82% |   90.00% |  85.71% |
| AufbautenZulaessig                            |      8 |           6 |     100.00% |   75.00% |  85.71% |
| BebauteFlaecheMaxNebengebaeude                |      8 |           9 |      55.56% |   62.50% |  58.82% |
| Stockwerk                                     |      8 |           4 |     100.00% |   50.00% |  66.67% |
| OeffentlicheVerkehrsflaecheBreiteMin          |      7 |           8 |      87.50% |  100.00% |  93.33% |
| VerbotFensterZuOeffentlichenVerkehrsflaechen  |      7 |           4 |     100.00% |   57.14% |  72.73% |
| AnOeffentlichenVerkehrsflaechen               |      6 |           2 |     100.00% |   33.33% |  50.00% |
| DachflaecheMin                                |      6 |           3 |     100.00% |   50.00% |  66.67% |
| StellplatzregulativUmfangMinimumRelativ       |      5 |           5 |     100.00% |  100.00% | 100.00% |
| VerbotWohnung                                 |      5 |           3 |     100.00% |   60.00% |  75.00% |
| AnordnungGaertnerischeAusgestaltungProzentual |      4 |           4 |      75.00% |   75.00% |  75.00% |
| StellplatzregulativUmfangMaximumRelativ       |      4 |           3 |     100.00% |   75.00% |  85.71% |
| FBOKMinimumWohnungen                          |      2 |           2 |     100.00% |  100.00% | 100.00% |
| AnteilDachbegruenung                          |      1 |           0 |     100.00% |    0.00% |   0.00% |
