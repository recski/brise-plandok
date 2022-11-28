# BERT Report

## Train all rule based attributes simultaneously

| label                                         |   gold |   predicted |   precision |   recall |      F1 |
|-----------------------------------------------|--------|-------------|-------------|----------|---------|
| macro average                                 |    702 |         642 |      90.87% |   73.77% |  77.03% |
| total                                         |    702 |         642 |      91.12% |   83.33% |  87.05% |
| Planzeichen                                   |    175 |         180 |      95.00% |   97.71% |  96.34% |
| Widmung                                       |     40 |          32 |      65.62% |   52.50% |  58.33% |
| AnordnungGaertnerischeAusgestaltung           |     37 |          32 |      93.75% |   81.08% |  86.96% |
| Dachart                                       |     30 |          27 |      96.30% |   86.67% |  91.23% |
| AnFluchtlinie                                 |     29 |          29 |      89.66% |   89.66% |  89.66% |
| VorkehrungBepflanzung                         |     28 |          28 |      96.43% |   96.43% |  96.43% |
| BegruenungDach                                |     26 |          26 |      92.31% |   92.31% |  92.31% |
| WidmungInMehrerenEbenen                       |     25 |          24 |     100.00% |   96.00% |  97.96% |
| AbschlussDachMaxBezugGebaeude                 |     23 |          22 |      95.45% |   91.30% |  93.33% |
| GebaeudeHoeheArt                              |     23 |          22 |      95.45% |   91.30% |  93.33% |
| GehsteigbreiteMin                             |     22 |          22 |     100.00% |  100.00% | 100.00% |
| Nutzungsart                                   |     19 |           7 |      85.71% |   31.58% |  46.15% |
| GebaeudeBautyp                                |     17 |          15 |      86.67% |   76.47% |  81.25% |
| DachneigungMax                                |     16 |          12 |     100.00% |   75.00% |  85.71% |
| UnterbrechungGeschlosseneBauweise             |     16 |          16 |     100.00% |  100.00% | 100.00% |
| VonBebauungFreizuhalten                       |     16 |          18 |      72.22% |   81.25% |  76.47% |
| AufbautenZulaessig                            |     13 |          12 |      91.67% |   84.62% |  88.00% |
| BebauteFlaecheMin                             |     13 |          11 |     100.00% |   84.62% |  91.67% |
| BBAllgemein                                   |     12 |           4 |      75.00% |   25.00% |  37.50% |
| BebauteFlaecheMaxProzentual                   |     12 |          13 |      69.23% |   75.00% |  72.00% |
| OeffentlicheVerkehrsflaecheBreiteMin          |     10 |          10 |      90.00% |   90.00% |  90.00% |
| DachflaecheMin                                |      9 |           6 |     100.00% |   66.67% |  80.00% |
| DurchgangBreite                               |      9 |          10 |      80.00% |   88.89% |  84.21% |
| GebaeudeHoeheMaxAbsolut                       |      9 |           6 |     100.00% |   66.67% |  80.00% |
| BauweiseID                                    |      8 |           3 |     100.00% |   37.50% |  54.55% |
| DurchgangHoehe                                |      7 |           8 |      62.50% |   71.43% |  66.67% |
| VolumenUndUmbaubarerRaum                      |      7 |           5 |     100.00% |   71.43% |  83.33% |
| AusnahmeGaertnerischAuszugestaltende          |      6 |           6 |     100.00% |  100.00% | 100.00% |
| BebauteFlaecheMax                             |      6 |           1 |     100.00% |   16.67% |  28.57% |
| BebauteFlaecheMaxNebengebaeude                |      6 |           8 |      75.00% |  100.00% |  85.71% |
| VerbotFensterZuOeffentlichenVerkehrsflaechen  |      6 |           5 |     100.00% |   83.33% |  90.91% |
| VerbotWohnung                                 |      6 |           4 |     100.00% |   66.67% |  80.00% |
| AnteilDachbegruenung                          |      5 |           3 |     100.00% |   60.00% |  75.00% |
| Stockwerk                                     |      5 |           6 |      66.67% |   80.00% |  72.73% |
| AnordnungGaertnerischeAusgestaltungProzentual |      3 |           5 |      60.00% |  100.00% |  75.00% |
| FBOKMinimumWohnungen                          |      3 |           1 |     100.00% |   33.33% |  50.00% |
| StellplatzregulativUmfangMinimumRelativ       |      2 |           2 |     100.00% |  100.00% | 100.00% |
| AnOeffentlichenVerkehrsflaechen               |      1 |           0 |     100.00% |    0.00% |   0.00% |
| GebaeudeHoeheMaxWN                            |      1 |           0 |     100.00% |    0.00% |   0.00% |
| StellplatzregulativUmfangMaximumRelativ       |      1 |           1 |     100.00% |  100.00% | 100.00% |

