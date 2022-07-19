# One rule classifier - report
Run for the top 40 attributes with hyperparams: {'max depth': 5}.
## Planzeichen
```bash
              precision    recall  f1-score   support

         NOT       0.95      0.99      0.97       573
 Planzeichen       0.99      0.87      0.92       228

    accuracy                           0.96       801
   macro avg       0.97      0.93      0.95       801
weighted avg       0.96      0.96      0.96       801


mean 0.268 (5368 pts)
if bb >= 1 then 0.972 (1199 pts)
mean 0.066 (4169 pts)
if bb >= 0 then 0.066 (4169 pts)

```
## Widmung
```bash
              precision    recall  f1-score   support

         NOT       0.94      1.00      0.97       742
     Widmung       0.91      0.17      0.29        59

    accuracy                           0.94       801
   macro avg       0.92      0.58      0.63       801
weighted avg       0.94      0.94      0.92       801


mean 0.101 (5368 pts)
if bauland >= 1 then 0.825 (120 pts)
mean 0.084 (5248 pts)
if bauland >= 0 then 0.084 (5248 pts)

```
## VerkehrsflaecheID
```bash
                   precision    recall  f1-score   support

              NOT       0.97      1.00      0.98       769
VerkehrsflaecheID       0.86      0.19      0.31        32

         accuracy                           0.97       801
        macro avg       0.91      0.59      0.65       801
     weighted avg       0.96      0.97      0.96       801


mean 0.063 (5368 pts)
if pflanzung >= 1 then 0.904 (136 pts)
mean 0.041 (5232 pts)
if pflanzung >= 0 then 0.041 (5232 pts)

```
## AnordnungGaertnerischeAusgestaltung
```bash
                                     precision    recall  f1-score   support

                                NOT       1.00      0.99      1.00       759
AnordnungGaertnerischeAusgestaltung       0.91      1.00      0.95        42

                           accuracy                           1.00       801
                          macro avg       0.96      1.00      0.98       801
                       weighted avg       1.00      1.00      1.00       801


mean 0.04 (5368 pts)
if gärtnerisch >= 1 then 0.827 (254 pts)
mean 0.001 (5114 pts)
if gärtnerisch >= 0 then 0.001 (5114 pts)

```
## Dachart
```bash
              precision    recall  f1-score   support

         NOT       0.99      1.00      1.00       776
     Dachart       0.95      0.76      0.84        25

    accuracy                           0.99       801
   macro avg       0.97      0.88      0.92       801
weighted avg       0.99      0.99      0.99       801


mean 0.042 (5368 pts)
if flachdäch >= 1 then 1.0 (181 pts)
mean 0.009 (5187 pts)
if flachdäch >= 0 then 0.009 (5187 pts)

```
## AnFluchtlinie
```bash
               precision    recall  f1-score   support

          NOT       0.99      1.00      1.00       775
AnFluchtlinie       0.91      0.81      0.86        26

     accuracy                           0.99       801
    macro avg       0.95      0.90      0.93       801
 weighted avg       0.99      0.99      0.99       801


mean 0.041 (5368 pts)
if entlang >= 1 then 0.894 (180 pts)
mean 0.012 (5188 pts)
if entlang >= 0 then 0.012 (5188 pts)

```
## VorkehrungBepflanzung
```bash
                       precision    recall  f1-score   support

                  NOT       0.97      1.00      0.98       768
VorkehrungBepflanzung       1.00      0.21      0.35        33

             accuracy                           0.97       801
            macro avg       0.98      0.61      0.67       801
         weighted avg       0.97      0.97      0.96       801


mean 0.04 (5368 pts)
if pflanzung >= 1 then 1.0 (136 pts)
mean 0.015 (5232 pts)
if pflanzung >= 0 then 0.015 (5232 pts)

```
## GebaeudeHoeheArt
```bash
                  precision    recall  f1-score   support

             NOT       0.98      1.00      0.99       767
GebaeudeHoeheArt       1.00      0.53      0.69        34

        accuracy                           0.98       801
       macro avg       0.99      0.76      0.84       801
    weighted avg       0.98      0.98      0.98       801


mean 0.034 (5368 pts)
if ausgeführt >= 1 then 0.957 (117 pts)
mean 0.014 (5251 pts)
if ausgeführt >= 0 then 0.014 (5251 pts)

```
## BegruenungDach
```bash
                precision    recall  f1-score   support

           NOT       1.00      0.99      1.00       778
BegruenungDach       0.81      0.91      0.86        23

      accuracy                           0.99       801
     macro avg       0.90      0.95      0.93       801
  weighted avg       0.99      0.99      0.99       801


mean 0.032 (5368 pts)
if stehen >= 1 then 0.869 (175 pts)
mean 0.004 (5193 pts)
if stehen >= 0 then 0.004 (5193 pts)

```
## WidmungInMehrerenEbenen
```bash
                         precision    recall  f1-score   support

                    NOT       0.99      1.00      1.00       781
WidmungInMehrerenEbenen       1.00      0.75      0.86        20

               accuracy                           0.99       801
              macro avg       1.00      0.88      0.93       801
           weighted avg       0.99      0.99      0.99       801


mean 0.032 (5368 pts)
if raum >= 2 then 0.977 (131 pts)
mean 0.009 (5237 pts)
if raum >= 1 then 0.201 (194 pts)
mean 0.001 (5043 pts)
if raum >= 0 then 0.001 (5043 pts)

```
## AbschlussDachMaxBezugGebaeude
```bash
                               precision    recall  f1-score   support

                          NOT       0.99      0.99      0.99       773
AbschlussDachMaxBezugGebaeude       0.68      0.75      0.71        28

                     accuracy                           0.98       801
                    macro avg       0.83      0.87      0.85       801
                 weighted avg       0.98      0.98      0.98       801


mean 0.031 (5368 pts)
if punkt >= 1 then 0.791 (187 pts)
mean 0.004 (5181 pts)
if punkt >= 0 then 0.004 (5181 pts)

```
## BBAllgemein
```bash
              precision    recall  f1-score   support

         NOT       0.98      1.00      0.99       782
 BBAllgemein       0.70      0.37      0.48        19

    accuracy                           0.98       801
   macro avg       0.84      0.68      0.74       801
weighted avg       0.98      0.98      0.98       801


mean 0.035 (5368 pts)
if stre >= 1 then 0.84 (50 pts)
mean 0.027 (5318 pts)
if stre >= 0 then 0.027 (5318 pts)

```
## ErrichtungGebaeude
```bash
                    precision    recall  f1-score   support

               NOT       0.98      1.00      0.99       777
ErrichtungGebaeude       1.00      0.42      0.59        24

          accuracy                           0.98       801
         macro avg       0.99      0.71      0.79       801
      weighted avg       0.98      0.98      0.98       801


mean 0.033 (5368 pts)
if unmittelbar >= 1 then 0.83 (53 pts)
mean 0.025 (5315 pts)
if unmittelbar >= 0 then 0.025 (5315 pts)

```
## GehsteigbreiteMin
```bash
                   precision    recall  f1-score   support

              NOT       1.00      1.00      1.00       780
GehsteigbreiteMin       1.00      1.00      1.00        21

         accuracy                           1.00       801
        macro avg       1.00      1.00      1.00       801
     weighted avg       1.00      1.00      1.00       801


mean 0.031 (5368 pts)
if gehsteige >= 1 then 0.924 (170 pts)
mean 0.001 (5198 pts)
if gehsteige >= 0 then 0.001 (5198 pts)

```
## GebaeudeHoeheMaxAbsolut
```bash
                         precision    recall  f1-score   support

                    NOT       0.98      1.00      0.99       782
GebaeudeHoeheMaxAbsolut       0.60      0.16      0.25        19

               accuracy                           0.98       801
              macro avg       0.79      0.58      0.62       801
           weighted avg       0.97      0.98      0.97       801


mean 0.032 (5368 pts)
if maximal >= 2 then 1.0 (18 pts)
mean 0.029 (5350 pts)
if maximal >= 1 then 0.194 (237 pts)
mean 0.021 (5113 pts)
if maximal >= 0 then 0.021 (5113 pts)

```
## GesamtePlangebiet
```bash
                   precision    recall  f1-score   support

              NOT       0.99      0.99      0.99       783
GesamtePlangebiet       0.76      0.72      0.74        18

         accuracy                           0.99       801
        macro avg       0.88      0.86      0.87       801
     weighted avg       0.99      0.99      0.99       801


mean 0.028 (5368 pts)
if gesamt >= 1 then 0.714 (161 pts)
mean 0.007 (5207 pts)
if gesamt >= 0 then 0.007 (5207 pts)

```
## StrassenbreiteMin
```bash
                   precision    recall  f1-score   support

              NOT       1.00      1.00      1.00       791
StrassenbreiteMin       0.88      0.70      0.78        10

         accuracy                           1.00       801
        macro avg       0.94      0.85      0.89       801
     weighted avg       0.99      1.00      0.99       801


mean 0.028 (5368 pts)
if straßenbreite >= 1 then 0.867 (128 pts)
mean 0.008 (5240 pts)
if straßenbreite >= 0 then 0.008 (5240 pts)

```
## GebaeudeBautyp
```bash
                precision    recall  f1-score   support

           NOT       0.98      1.00      0.99       778
GebaeudeBautyp       0.89      0.35      0.50        23

      accuracy                           0.98       801
     macro avg       0.93      0.67      0.74       801
  weighted avg       0.98      0.98      0.98       801


mean 0.025 (5368 pts)
if nebengebäude >= 1 then 0.973 (75 pts)
mean 0.012 (5293 pts)
if nebengebäude >= 0 then 0.012 (5293 pts)

```
## Nutzungsart
```bash
              precision    recall  f1-score   support

         NOT       0.98      1.00      0.99       780
 Nutzungsart       1.00      0.14      0.25        21

    accuracy                           0.98       801
   macro avg       0.99      0.57      0.62       801
weighted avg       0.98      0.98      0.97       801


mean 0.022 (5368 pts)
if sozial >= 1 then 0.941 (17 pts)
mean 0.019 (5351 pts)
if sozial >= 0 then 0.019 (5351 pts)

```
## UnterbrechungGeschlosseneBauweise
```bash
                                   precision    recall  f1-score   support

                              NOT       1.00      1.00      1.00       789
UnterbrechungGeschlosseneBauweise       1.00      1.00      1.00        12

                         accuracy                           1.00       801
                        macro avg       1.00      1.00      1.00       801
                     weighted avg       1.00      1.00      1.00       801


mean 0.023 (5368 pts)
if unterbrechung >= 1 then 1.0 (126 pts)
mean 0 (5242 pts)

```
## AufbautenZulaessig
```bash
                    precision    recall  f1-score   support

               NOT       1.00      1.00      1.00       793
AufbautenZulaessig       1.00      1.00      1.00         8

          accuracy                           1.00       801
         macro avg       1.00      1.00      1.00       801
      weighted avg       1.00      1.00      1.00       801


mean 0.024 (5368 pts)
if aufbauen >= 1 then 0.947 (132 pts)
mean 0.001 (5236 pts)
if aufbauen >= 0 then 0.001 (5236 pts)

```
## VonBebauungFreizuhalten
```bash
                         precision    recall  f1-score   support

                    NOT       0.98      1.00      0.99       782
VonBebauungFreizuhalten       1.00      0.05      0.10        19

               accuracy                           0.98       801
              macro avg       0.99      0.53      0.54       801
           weighted avg       0.98      0.98      0.97       801


mean 0.02 (5368 pts)
if gbb >= 1 then 0.8 (10 pts)
mean 0.019 (5358 pts)
if gbb >= 0 then 0.019 (5358 pts)

```
## DachneigungMax
```bash
                precision    recall  f1-score   support

           NOT       0.99      1.00      1.00       788
DachneigungMax       0.82      0.69      0.75        13

      accuracy                           0.99       801
     macro avg       0.91      0.84      0.87       801
  weighted avg       0.99      0.99      0.99       801


mean 0.019 (5368 pts)
if grad >= 1 then 0.973 (74 pts)
mean 0.006 (5294 pts)
if grad >= 0 then 0.006 (5294 pts)

```
## Bauklasse
```bash
              precision    recall  f1-score   support

         NOT       1.00      1.00      1.00       789
   Bauklasse       1.00      1.00      1.00        12

    accuracy                           1.00       801
   macro avg       1.00      1.00      1.00       801
weighted avg       1.00      1.00      1.00       801


mean 0.018 (5368 pts)
if bauklasse >= 1 then 1.0 (80 pts)
mean 0.003 (5288 pts)
if bauklasse >= 0 then 0.003 (5288 pts)

```
## EinfriedungAusgestaltung
```bash
                          precision    recall  f1-score   support

                     NOT       1.00      1.00      1.00       792
EinfriedungAusgestaltung       1.00      0.89      0.94         9

                accuracy                           1.00       801
               macro avg       1.00      0.94      0.97       801
            weighted avg       1.00      1.00      1.00       801


mean 0.018 (5368 pts)
if durchblick >= 1 then 1.0 (56 pts)
mean 0.007 (5312 pts)
if durchblick >= 0 then 0.007 (5312 pts)

```
## DurchgangBreite
```bash
                 precision    recall  f1-score   support

            NOT       0.98      1.00      0.99       787
DurchgangBreite       1.00      0.07      0.13        14

       accuracy                           0.98       801
      macro avg       0.99      0.54      0.56       801
   weighted avg       0.98      0.98      0.98       801


mean 0.016 (5368 pts)
if dulden >= 1 then 0.825 (40 pts)
mean 0.01 (5328 pts)
if dulden >= 0 then 0.01 (5328 pts)

```
## BebauteFlaecheMaxProzentual
```bash
                             precision    recall  f1-score   support

                        NOT       0.99      0.99      0.99       791
BebauteFlaecheMaxProzentual       0.50      0.50      0.50        10

                   accuracy                           0.99       801
                  macro avg       0.75      0.75      0.75       801
               weighted avg       0.99      0.99      0.99       801


mean 0.016 (5368 pts)
if bauplatzes >= 1 then 0.646 (48 pts)
mean 0.01 (5320 pts)
if bauplatzes >= 0 then 0.01 (5320 pts)

```
## AusnahmeGaertnerischAuszugestaltende
```bash
                                      precision    recall  f1-score   support

                                 NOT       0.99      1.00      1.00       791
AusnahmeGaertnerischAuszugestaltende       1.00      0.30      0.46        10

                            accuracy                           0.99       801
                           macro avg       1.00      0.65      0.73       801
                        weighted avg       0.99      0.99      0.99       801


mean 0.016 (5368 pts)
if rangieren >= 1 then 0.81 (42 pts)
mean 0.01 (5326 pts)
if rangieren >= 0 then 0.01 (5326 pts)

```
## StrassenbreiteMax
```bash
                   precision    recall  f1-score   support

              NOT       1.00      1.00      1.00       794
StrassenbreiteMax       1.00      0.86      0.92         7

         accuracy                           1.00       801
        macro avg       1.00      0.93      0.96       801
     weighted avg       1.00      1.00      1.00       801


mean 0.016 (5368 pts)
if m >= 4 then 0.807 (88 pts)
mean 0.003 (5280 pts)
if m >= 1 then 0.013 (1343 pts)
mean 0 (3937 pts)

```
## BauweiseID
```bash
              precision    recall  f1-score   support

         NOT       1.00      1.00      1.00       790
  BauweiseID       0.75      0.82      0.78        11

    accuracy                           0.99       801
   macro avg       0.87      0.91      0.89       801
weighted avg       0.99      0.99      0.99       801


mean 0.015 (5368 pts)
if bauklasse >= 1 then 0.738 (80 pts)
mean 0.004 (5288 pts)
if bauklasse >= 0 then 0.004 (5288 pts)

```
## DurchgangHoehe
```bash
                precision    recall  f1-score   support

           NOT       0.99      0.99      0.99       789
DurchgangHoehe       0.50      0.42      0.45        12

      accuracy                           0.99       801
     macro avg       0.75      0.71      0.72       801
  weighted avg       0.98      0.99      0.98       801


mean 0.014 (5368 pts)
if durchgang >= 1 then 0.672 (67 pts)
mean 0.006 (5301 pts)
if durchgang >= 0 then 0.006 (5301 pts)

```
## VolumenUndUmbaubarerRaum
```bash
                          precision    recall  f1-score   support

                     NOT       0.98      1.00      0.99       778
VolumenUndUmbaubarerRaum       1.00      0.48      0.65        23

                accuracy                           0.99       801
               macro avg       0.99      0.74      0.82       801
            weighted avg       0.99      0.99      0.98       801


mean 0.011 (5368 pts)
if m³ >= 1 then 1.0 (45 pts)
mean 0.003 (5323 pts)
if m³ >= 0 then 0.003 (5323 pts)

```
## UnterirdischeBaulichkeiten
```bash
                            precision    recall  f1-score   support

                       NOT       0.99      1.00      0.99       785
UnterirdischeBaulichkeiten       0.83      0.31      0.45        16

                  accuracy                           0.99       801
                 macro avg       0.91      0.66      0.72       801
              weighted avg       0.98      0.99      0.98       801


mean 0.011 (5368 pts)
if ausreichend >= 1 then 1.0 (16 pts)
mean 0.008 (5352 pts)
if ausreichend >= 0 then 0.008 (5352 pts)

```
## Struktureinheit
```bash
                 precision    recall  f1-score   support

            NOT       0.99      0.99      0.99       787
Struktureinheit       0.55      0.43      0.48        14

       accuracy                           0.98       801
      macro avg       0.77      0.71      0.74       801
   weighted avg       0.98      0.98      0.98       801


mean 0.012 (5368 pts)
if struktureinheit >= 1 then 0.674 (43 pts)
mean 0.006 (5325 pts)
if struktureinheit >= 0 then 0.006 (5325 pts)

```
## Stockwerk
```bash
              precision    recall  f1-score   support

         NOT       1.00      1.00      1.00       793
   Stockwerk       1.00      0.75      0.86         8

    accuracy                           1.00       801
   macro avg       1.00      0.88      0.93       801
weighted avg       1.00      1.00      1.00       801


mean 0.012 (5368 pts)
if erdgeschoß >= 1 then 0.923 (39 pts)
mean 0.006 (5329 pts)
if erdgeschoß >= 0 then 0.006 (5329 pts)

```
## EinfriedungHoeheGesamt
```bash
                        precision    recall  f1-score   support

                   NOT       1.00      1.00      1.00       796
EinfriedungHoeheGesamt       0.83      1.00      0.91         5

              accuracy                           1.00       801
             macro avg       0.92      1.00      0.95       801
          weighted avg       1.00      1.00      1.00       801


mean 0.012 (5368 pts)
if hinter >= 1 then 0.816 (38 pts)
mean 0.006 (5330 pts)
if hinter >= 0 then 0.006 (5330 pts)

```
## DachflaecheMin
```bash
                precision    recall  f1-score   support

           NOT       1.00      0.99      0.99       795
DachflaecheMin       0.29      0.67      0.40         6

      accuracy                           0.99       801
     macro avg       0.64      0.83      0.70       801
  weighted avg       0.99      0.99      0.99       801


mean 0.01 (5368 pts)
if groß >= 1 then 0.58 (88 pts)
mean 0.001 (5280 pts)
if groß >= 0 then 0.001 (5280 pts)

```
## BebauteFlaecheMax
```bash
                   precision    recall  f1-score   support

              NOT       0.99      1.00      0.99       790
BebauteFlaecheMax       0.00      0.00      0.00        11

         accuracy                           0.99       801
        macro avg       0.49      0.50      0.50       801
     weighted avg       0.97      0.99      0.98       801


mean 0.01 (5368 pts)
if erholungsgebietsport >= 1 then 1.0 (6 pts)
mean 0.009 (5362 pts)
if erholungsgebietsport >= 0 then 0.009 (5362 pts)

```
## VerbotFensterZuOeffentlichenVerkehrsflaechen
```bash
                                              precision    recall  f1-score   support

                                         NOT       1.00      1.00      1.00       794
VerbotFensterZuOeffentlichenVerkehrsflaechen       1.00      0.86      0.92         7

                                    accuracy                           1.00       801
                                   macro avg       1.00      0.93      0.96       801
                                weighted avg       1.00      1.00      1.00       801


mean 0.01 (5368 pts)
if aufenthaltsräumen >= 1 then 1.0 (38 pts)
mean 0.003 (5330 pts)
if aufenthaltsräumen >= 0 then 0.003 (5330 pts)

```
## BebauteFlaecheMaxNebengebaeude
```bash
                                precision    recall  f1-score   support

                           NOT       0.99      0.99      0.99       793
BebauteFlaecheMaxNebengebaeude       0.22      0.25      0.24         8

                      accuracy                           0.98       801
                     macro avg       0.61      0.62      0.61       801
                  weighted avg       0.98      0.98      0.98       801


mean 0.01 (5368 pts)
if pro >= 1 then 0.605 (38 pts)
mean 0.005 (5330 pts)
if pro >= 0 then 0.005 (5330 pts)

```
## Summary
| label                                        |   gold |   predicted |   precision |   recall |      F1 |
|----------------------------------------------|--------|-------------|-------------|----------|---------|
| total                                        |    940 |         652 |      88.04% |   61.06% |  72.11% |
| Planzeichen                                  |    228 |         201 |      98.51% |   86.84% |  92.31% |
| Widmung                                      |     59 |          11 |      90.91% |   16.95% |  28.57% |
| AnordnungGaertnerischeAusgestaltung          |     42 |          46 |      91.30% |  100.00% |  95.45% |
| GebaeudeHoeheArt                             |     34 |          18 |     100.00% |   52.94% |  69.23% |
| VorkehrungBepflanzung                        |     33 |           7 |     100.00% |   21.21% |  35.00% |
| VerkehrsflaecheID                            |     32 |           7 |      85.71% |   18.75% |  30.77% |
| AbschlussDachMaxBezugGebaeude                |     28 |          31 |      67.74% |   75.00% |  71.19% |
| AnFluchtlinie                                |     26 |          23 |      91.30% |   80.77% |  85.71% |
| Dachart                                      |     25 |          20 |      95.00% |   76.00% |  84.44% |
| ErrichtungGebaeude                           |     24 |          10 |     100.00% |   41.67% |  58.82% |
| BegruenungDach                               |     23 |          26 |      80.77% |   91.30% |  85.71% |
| GebaeudeBautyp                               |     23 |           9 |      88.89% |   34.78% |  50.00% |
| VolumenUndUmbaubarerRaum                     |     23 |          11 |     100.00% |   47.83% |  64.71% |
| GehsteigbreiteMin                            |     21 |          21 |     100.00% |  100.00% | 100.00% |
| Nutzungsart                                  |     21 |           3 |     100.00% |   14.29% |  25.00% |
| WidmungInMehrerenEbenen                      |     20 |          15 |     100.00% |   75.00% |  85.71% |
| BBAllgemein                                  |     19 |          10 |      70.00% |   36.84% |  48.28% |
| GebaeudeHoeheMaxAbsolut                      |     19 |           5 |      60.00% |   15.79% |  25.00% |
| VonBebauungFreizuhalten                      |     19 |           1 |     100.00% |    5.26% |  10.00% |
| GesamtePlangebiet                            |     18 |          17 |      76.47% |   72.22% |  74.29% |
| UnterirdischeBaulichkeiten                   |     16 |           6 |      83.33% |   31.25% |  45.45% |
| DurchgangBreite                              |     14 |           1 |     100.00% |    7.14% |  13.33% |
| Struktureinheit                              |     14 |          11 |      54.55% |   42.86% |  48.00% |
| DachneigungMax                               |     13 |          11 |      81.82% |   69.23% |  75.00% |
| Bauklasse                                    |     12 |          12 |     100.00% |  100.00% | 100.00% |
| DurchgangHoehe                               |     12 |          10 |      50.00% |   41.67% |  45.45% |
| UnterbrechungGeschlosseneBauweise            |     12 |          12 |     100.00% |  100.00% | 100.00% |
| BauweiseID                                   |     11 |          12 |      75.00% |   81.82% |  78.26% |
| BebauteFlaecheMax                            |     11 |           1 |       0.00% |    0.00% |   0.00% |
| AusnahmeGaertnerischAuszugestaltende         |     10 |           3 |     100.00% |   30.00% |  46.15% |
| BebauteFlaecheMaxProzentual                  |     10 |          10 |      50.00% |   50.00% |  50.00% |
| StrassenbreiteMin                            |     10 |           8 |      87.50% |   70.00% |  77.78% |
| EinfriedungAusgestaltung                     |      9 |           8 |     100.00% |   88.89% |  94.12% |
| AufbautenZulaessig                           |      8 |           8 |     100.00% |  100.00% | 100.00% |
| BebauteFlaecheMaxNebengebaeude               |      8 |           9 |      22.22% |   25.00% |  23.53% |
| Stockwerk                                    |      8 |           6 |     100.00% |   75.00% |  85.71% |
| StrassenbreiteMax                            |      7 |           6 |     100.00% |   85.71% |  92.31% |
| VerbotFensterZuOeffentlichenVerkehrsflaechen |      7 |           6 |     100.00% |   85.71% |  92.31% |
| DachflaecheMin                               |      6 |          14 |      28.57% |   66.67% |  40.00% |
| EinfriedungHoeheGesamt                       |      5 |           6 |      83.33% |  100.00% |  90.91% |
