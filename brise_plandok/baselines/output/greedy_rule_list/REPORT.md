# Greedy rule list classifier - report
Run for the top 40 attributes with hyperparams: {'max depth': 5}.
## Planzeichen
```bash
              precision    recall  f1-score   support

         NOT       0.96      0.99      0.98       573
 Planzeichen       0.97      0.90      0.94       228

    accuracy                           0.97       801
   macro avg       0.97      0.95      0.96       801
weighted avg       0.97      0.97      0.96       801


mean 0.268 (5368 pts)
if bb >= 1 then 0.972 (1199 pts)
mean 0.066 (4169 pts)
if bezeichnet >= 1 then 0.404 (329 pts)
mean 0.037 (3840 pts)
if stre >= 1 then 1.0 (34 pts)
mean 0.029 (3806 pts)
if punken >= 1 then 0.931 (29 pts)
mean 0.022 (3777 pts)
if spkbb >= 1 then 1.0 (15 pts)

```
## Widmung
```bash
              precision    recall  f1-score   support

         NOT       0.97      1.00      0.98       742
     Widmung       0.97      0.56      0.71        59

    accuracy                           0.97       801
   macro avg       0.97      0.78      0.85       801
weighted avg       0.97      0.97      0.96       801


mean 0.101 (5368 pts)
if bauland >= 1 then 0.825 (120 pts)
mean 0.084 (5248 pts)
if baulandflächen >= 1 then 0.983 (59 pts)
mean 0.074 (5189 pts)
if gewidmet >= 1 then 0.966 (59 pts)
mean 0.064 (5130 pts)
if gb >= 1 then 1.0 (29 pts)
mean 0.059 (5101 pts)
if ausgewiesen >= 1 then 0.638 (58 pts)

```
## VerkehrsflaecheID
```bash
                   precision    recall  f1-score   support

              NOT       0.99      0.99      0.99       769
VerkehrsflaecheID       0.71      0.75      0.73        32

         accuracy                           0.98       801
        macro avg       0.85      0.87      0.86       801
     weighted avg       0.98      0.98      0.98       801


mean 0.063 (5368 pts)
if pflanzung >= 1 then 0.904 (136 pts)
mean 0.041 (5232 pts)
if straße >= 1 then 0.65 (157 pts)
mean 0.022 (5075 pts)
if gurt >= 1 then 0.889 (9 pts)
mean 0.021 (5066 pts)
if baumreihe >= 1 then 0.647 (17 pts)
mean 0.018 (5049 pts)
if zwischen >= 1 then 0.209 (148 pts)

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
if verbleibend >= 1 then 0.167 (12 pts)
mean 0.0 (5102 pts)
if code >= 1 then 0.027 (37 pts)
mean 0 (5065 pts)

```
## Dachart
```bash
              precision    recall  f1-score   support

         NOT       1.00      1.00      1.00       776
     Dachart       0.92      0.92      0.92        25

    accuracy                           1.00       801
   macro avg       0.96      0.96      0.96       801
weighted avg       1.00      1.00      1.00       801


mean 0.042 (5368 pts)
if flachdäch >= 1 then 1.0 (181 pts)
mean 0.009 (5187 pts)
if flachdächern >= 1 then 1.0 (10 pts)
mean 0.007 (5177 pts)
if begehbar >= 1 then 0.75 (16 pts)
mean 0.005 (5161 pts)
if flugdäch >= 1 then 1.0 (6 pts)
mean 0.003 (5155 pts)
if seitlich >= 2 then 1.0 (1 pts)

```
## AnFluchtlinie
```bash
               precision    recall  f1-score   support

          NOT       0.99      1.00      1.00       775
AnFluchtlinie       0.88      0.85      0.86        26

     accuracy                           0.99       801
    macro avg       0.94      0.92      0.93       801
 weighted avg       0.99      0.99      0.99       801


mean 0.041 (5368 pts)
if entlang >= 1 then 0.894 (180 pts)
mean 0.012 (5188 pts)
if erkern >= 1 then 0.872 (39 pts)
mean 0.005 (5149 pts)
if baulinien >= 1 then 0.3 (30 pts)
mean 0.003 (5119 pts)
if baulinie >= 1 then 0.192 (52 pts)
mean 0.001 (5067 pts)
if lärmschutzwand >= 1 then 1.0 (1 pts)

```
## VorkehrungBepflanzung
```bash
                       precision    recall  f1-score   support

                  NOT       1.00      1.00      1.00       768
VorkehrungBepflanzung       0.97      0.91      0.94        33

             accuracy                           1.00       801
            macro avg       0.98      0.95      0.97       801
         weighted avg       0.99      1.00      0.99       801


mean 0.04 (5368 pts)
if pflanzung >= 1 then 1.0 (136 pts)
mean 0.015 (5232 pts)
if vorkehrung >= 1 then 0.865 (37 pts)
mean 0.009 (5195 pts)
if so >= 1 then 0.738 (42 pts)
mean 0.003 (5153 pts)
if mächtigkeit >= 1 then 1.0 (5 pts)
mean 0.002 (5148 pts)
if baumreihe >= 1 then 1.0 (3 pts)

```
## GebaeudeHoeheArt
```bash
                  precision    recall  f1-score   support

             NOT       0.99      0.99      0.99       767
GebaeudeHoeheArt       0.71      0.74      0.72        34

        accuracy                           0.98       801
       macro avg       0.85      0.86      0.86       801
    weighted avg       0.98      0.98      0.98       801


mean 0.034 (5368 pts)
if punkt >= 1 then 0.77 (187 pts)
mean 0.008 (5181 pts)
if abschlussen >= 1 then 0.415 (41 pts)
mean 0.005 (5140 pts)
if tatsächlich >= 1 then 0.571 (14 pts)
mean 0.003 (5126 pts)
if ausgeführt >= 1 then 1.0 (2 pts)
mean 0.003 (5124 pts)
if hochöchst >= 1 then 0.5 (6 pts)

```
## BegruenungDach
```bash
                precision    recall  f1-score   support

           NOT       1.00      0.99      1.00       778
BegruenungDach       0.81      0.96      0.88        23

      accuracy                           0.99       801
     macro avg       0.91      0.98      0.94       801
  weighted avg       0.99      0.99      0.99       801


mean 0.032 (5368 pts)
if stehen >= 1 then 0.869 (175 pts)
mean 0.004 (5193 pts)
if begrünen >= 1 then 0.929 (14 pts)
mean 0.001 (5179 pts)
if begrün >= 1 then 0.5 (6 pts)
mean 0.001 (5173 pts)
if ausgenommen >= 1 then 0.095 (21 pts)
mean 0.0 (5152 pts)
if flachdächern >= 1 then 0.1 (10 pts)
mean 0 (5142 pts)

```
## WidmungInMehrerenEbenen
```bash
                         precision    recall  f1-score   support

                    NOT       1.00      0.99      1.00       781
WidmungInMehrerenEbenen       0.83      0.95      0.88        20

               accuracy                           0.99       801
              macro avg       0.91      0.97      0.94       801
           weighted avg       0.99      0.99      0.99       801


mean 0.032 (5368 pts)
if raum >= 2 then 0.977 (131 pts)
mean 0.009 (5237 pts)
if zuordnen >= 1 then 0.531 (64 pts)
mean 0.002 (5173 pts)
if darüberliegende >= 1 then 0.75 (4 pts)
mean 0.002 (5169 pts)
if brückenkonstruktionsunterkante >= 1 then 0.75 (4 pts)
mean 0.001 (5165 pts)
if konstruktionsoberkante >= 1 then 0.667 (3 pts)

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
if ausgeführt >= 1 then 0.5 (10 pts)
mean 0.003 (5171 pts)
if abschlussen >= 1 then 0.205 (39 pts)
mean 0.001 (5132 pts)
if um >= 1 then 0.086 (70 pts)
mean 0.0 (5062 pts)
if als >= 3 then 0.125 (8 pts)
mean 0 (5054 pts)

```
## BBAllgemein
```bash
              precision    recall  f1-score   support

         NOT       0.99      0.99      0.99       782
 BBAllgemein       0.76      0.68      0.72        19

    accuracy                           0.99       801
   macro avg       0.88      0.84      0.86       801
weighted avg       0.99      0.99      0.99       801


mean 0.035 (5368 pts)
if stre >= 1 then 0.84 (50 pts)
mean 0.027 (5318 pts)
if strgen >= 1 then 0.969 (32 pts)
mean 0.021 (5286 pts)
if ekz >= 1 then 0.969 (32 pts)
mean 0.016 (5254 pts)
if p >= 1 then 0.842 (38 pts)
mean 0.01 (5216 pts)
if ödg >= 1 then 0.906 (32 pts)

```
## ErrichtungGebaeude
```bash
                    precision    recall  f1-score   support

               NOT       0.98      1.00      0.99       777
ErrichtungGebaeude       0.91      0.42      0.57        24

          accuracy                           0.98       801
         macro avg       0.95      0.71      0.78       801
      weighted avg       0.98      0.98      0.98       801


mean 0.033 (5368 pts)
if unmittelbar >= 1 then 0.83 (53 pts)
mean 0.025 (5315 pts)
if bauen >= 1 then 0.203 (212 pts)
mean 0.017 (5103 pts)
if zusammenhang >= 1 then 0.6 (15 pts)
mean 0.016 (5088 pts)
if errichten >= 1 then 0.192 (125 pts)
mean 0.011 (4963 pts)
if grenzlinien >= 1 then 1.0 (2 pts)

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
if gehsteig >= 1 then 0.714 (7 pts)
mean 0.0 (5191 pts)
if gehen >= 1 then 0.143 (7 pts)
mean 0.0 (5184 pts)
if code >= 1 then 0.027 (37 pts)
mean 0 (5147 pts)

```
## GebaeudeHoeheMaxAbsolut
```bash
                         precision    recall  f1-score   support

                    NOT       0.98      1.00      0.99       782
GebaeudeHoeheMaxAbsolut       0.00      0.00      0.00        19

               accuracy                           0.98       801
              macro avg       0.49      0.50      0.49       801
           weighted avg       0.95      0.98      0.96       801


mean 0.032 (5368 pts)
if gebäudehöh >= 1 then 0.418 (368 pts)
mean 0.004 (5000 pts)
if oberirdisch >= 2 then 1.0 (2 pts)
mean 0.003 (4998 pts)
if spkbb >= 2 then 1.0 (1 pts)
mean 0.003 (4997 pts)
if sonderbieten >= 1 then 0.5 (4 pts)
mean 0.003 (4993 pts)
if abschlussen >= 1 then 0.222 (18 pts)

```
## GesamtePlangebiet
```bash
                   precision    recall  f1-score   support

              NOT       1.00      0.99      0.99       783
GesamtePlangebiet       0.67      0.89      0.76        18

         accuracy                           0.99       801
        macro avg       0.83      0.94      0.88       801
     weighted avg       0.99      0.99      0.99       801


mean 0.028 (5368 pts)
if gesamt >= 1 then 0.714 (161 pts)
mean 0.007 (5207 pts)
if gesamtbreite >= 1 then 0.542 (24 pts)
mean 0.004 (5183 pts)
if plangebiets >= 1 then 0.179 (39 pts)
mean 0.003 (5144 pts)
if plangebiet >= 1 then 0.051 (235 pts)
mean 0.001 (4909 pts)
if gebäudehöh >= 3 then 0.5 (2 pts)

```
## StrassenbreiteMin
```bash
                   precision    recall  f1-score   support

              NOT       1.00      1.00      1.00       791
StrassenbreiteMin       0.91      1.00      0.95        10

         accuracy                           1.00       801
        macro avg       0.95      1.00      0.98       801
     weighted avg       1.00      1.00      1.00       801


mean 0.028 (5368 pts)
if straßenbreite >= 1 then 0.867 (128 pts)
mean 0.008 (5240 pts)
if bauelement >= 1 then 0.809 (47 pts)
mean 0.0 (5193 pts)
if zweier >= 1 then 0.1 (10 pts)
mean 0.0 (5183 pts)
if möglich >= 1 then 0.018 (57 pts)
mean 0 (5126 pts)

```
## GebaeudeBautyp
```bash
                precision    recall  f1-score   support

           NOT       1.00      1.00      1.00       778
GebaeudeBautyp       0.87      0.87      0.87        23

      accuracy                           0.99       801
     macro avg       0.93      0.93      0.93       801
  weighted avg       0.99      0.99      0.99       801


mean 0.025 (5368 pts)
if nebengebäude >= 1 then 0.973 (75 pts)
mean 0.012 (5293 pts)
if nebengebäuden >= 1 then 0.957 (47 pts)
mean 0.003 (5246 pts)
if nur >= 2 then 1.0 (1 pts)
mean 0.003 (5245 pts)
if bebauen >= 2 then 0.5 (2 pts)
mean 0.003 (5243 pts)
if wintergart >= 1 then 0.333 (3 pts)

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
if wohngebäude >= 1 then 0.941 (17 pts)
mean 0.019 (5351 pts)
if sozial >= 1 then 0.941 (17 pts)
mean 0.016 (5334 pts)
if bildungs >= 1 then 1.0 (7 pts)
mean 0.015 (5327 pts)
if zweckbestimmung >= 1 then 1.0 (6 pts)
mean 0.014 (5321 pts)
if landwirtschaftlich >= 1 then 1.0 (6 pts)

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
if zufahrtsflächen >= 1 then 0.115 (26 pts)
mean 0.001 (5210 pts)
if hinaus >= 1 then 0.167 (6 pts)
mean 0.0 (5204 pts)
if stütz >= 1 then 0.125 (8 pts)
mean 0.0 (5196 pts)
if überbauung >= 1 then 0.05 (20 pts)
mean 0 (5176 pts)

```
## VonBebauungFreizuhalten
```bash
                         precision    recall  f1-score   support

                    NOT       0.98      1.00      0.99       782
VonBebauungFreizuhalten       0.00      0.00      0.00        19

               accuracy                           0.98       801
              macro avg       0.49      0.50      0.49       801
           weighted avg       0.95      0.98      0.96       801


mean 0.02 (5368 pts)
if unterirdisch >= 1 then 0.431 (116 pts)
mean 0.011 (5252 pts)
if bebauung >= 1 then 0.386 (83 pts)
mean 0.005 (5169 pts)
if oberirdisch >= 1 then 0.344 (64 pts)
mean 0.001 (5105 pts)
if halten >= 1 then 0.5 (2 pts)
mean 0.001 (5103 pts)
if durchganges >= 1 then 0.08 (25 pts)

```
## DachneigungMax
```bash
                precision    recall  f1-score   support

           NOT       1.00      1.00      1.00       788
DachneigungMax       0.81      1.00      0.90        13

      accuracy                           1.00       801
     macro avg       0.91      1.00      0.95       801
  weighted avg       1.00      1.00      1.00       801


mean 0.019 (5368 pts)
if grad >= 1 then 0.973 (74 pts)
mean 0.006 (5294 pts)
if dachneigung >= 1 then 0.96 (25 pts)
mean 0.001 (5269 pts)
if neigung >= 1 then 1.0 (5 pts)
mean 0.0 (5264 pts)
if straßenniveau >= 1 then 0.083 (12 pts)
mean 0.0 (5252 pts)
if baufluchtlinie >= 1 then 0.077 (13 pts)
mean 0 (5239 pts)

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
if gv >= 1 then 0.308 (26 pts)
mean 0.002 (5262 pts)
if iv >= 1 then 0.6 (5 pts)
mean 0.001 (5257 pts)
if iii >= 1 then 0.5 (2 pts)
mean 0.001 (5255 pts)
if gbgv >= 1 then 0.25 (8 pts)

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
if vollflächig >= 1 then 0.781 (32 pts)
mean 0.002 (5280 pts)
if vogelschutz >= 1 then 0.833 (6 pts)
mean 0.002 (5274 pts)
if hindern >= 1 then 1.0 (2 pts)
mean 0.001 (5272 pts)
if lärmschutzeinrichtung >= 1 then 0.667 (3 pts)

```
## DurchgangBreite
```bash
                 precision    recall  f1-score   support

            NOT       0.99      0.99      0.99       787
DurchgangBreite       0.50      0.57      0.53        14

       accuracy                           0.98       801
      macro avg       0.75      0.78      0.76       801
   weighted avg       0.98      0.98      0.98       801


mean 0.016 (5368 pts)
if freizuhalten >= 1 then 0.508 (124 pts)
mean 0.004 (5244 pts)
if durchgang >= 1 then 0.429 (35 pts)
mean 0.002 (5209 pts)
if durchganges >= 1 then 0.364 (11 pts)
mean 0.001 (5198 pts)
if durchgangs >= 1 then 0.4 (5 pts)
mean 0.0 (5193 pts)
if lichte >= 1 then 0.5 (2 pts)

```
## BebauteFlaecheMaxProzentual
```bash
                             precision    recall  f1-score   support

                        NOT       1.00      0.99      0.99       791
BebauteFlaecheMaxProzentual       0.58      0.70      0.64        10

                   accuracy                           0.99       801
                  macro avg       0.79      0.85      0.82       801
               weighted avg       0.99      0.99      0.99       801


mean 0.016 (5368 pts)
if bauplatzes >= 1 then 0.646 (48 pts)
mean 0.01 (5320 pts)
if bauplatzfläche >= 1 then 0.615 (13 pts)
mean 0.009 (5307 pts)
if jeweilig >= 1 then 0.324 (34 pts)
mean 0.007 (5273 pts)
if bebauen >= 1 then 0.119 (177 pts)
mean 0.003 (5096 pts)
if trennstück >= 1 then 1.0 (2 pts)

```
## AusnahmeGaertnerischAuszugestaltende
```bash
                                      precision    recall  f1-score   support

                                 NOT       0.99      1.00      0.99       791
AusnahmeGaertnerischAuszugestaltende       0.00      0.00      0.00        10

                            accuracy                           0.99       801
                           macro avg       0.49      0.50      0.50       801
                        weighted avg       0.98      0.99      0.98       801


mean 0.016 (5368 pts)
if auszugestalt >= 1 then 0.413 (184 pts)
mean 0.002 (5184 pts)
if bleibend >= 1 then 1.0 (2 pts)
mean 0.002 (5182 pts)
if benötigt >= 1 then 1.0 (2 pts)
mean 0.001 (5180 pts)
if unterirdisch >= 2 then 1.0 (1 pts)
mean 0.001 (5179 pts)
if freibleibend >= 1 then 1.0 (1 pts)

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
if fahrbahn >= 1 then 0.812 (16 pts)
mean 0.001 (5264 pts)
if straßenbreiten >= 2 then 1.0 (1 pts)
mean 0.001 (5263 pts)
if ragen >= 1 then 1.0 (1 pts)
mean 0.0 (5262 pts)
if vorragen >= 1 then 0.167 (6 pts)

```
## BauweiseID
```bash
              precision    recall  f1-score   support

         NOT       1.00      0.99      1.00       790
  BauweiseID       0.69      0.82      0.75        11

    accuracy                           0.99       801
   macro avg       0.84      0.91      0.87       801
weighted avg       0.99      0.99      0.99       801


mean 0.015 (5368 pts)
if bauklasse >= 1 then 0.738 (80 pts)
mean 0.004 (5288 pts)
if gb >= 1 then 0.242 (33 pts)
mean 0.002 (5255 pts)
if bb >= 3 then 0.667 (3 pts)
mean 0.002 (5252 pts)
if gbgv >= 1 then 0.25 (8 pts)
mean 0.001 (5244 pts)
if gv >= 1 then 0.2 (5 pts)

```
## DurchgangHoehe
```bash
                precision    recall  f1-score   support

           NOT       0.99      0.99      0.99       789
DurchgangHoehe       0.55      0.50      0.52        12

      accuracy                           0.99       801
     macro avg       0.77      0.75      0.76       801
  weighted avg       0.99      0.99      0.99       801


mean 0.014 (5368 pts)
if durchgang >= 1 then 0.672 (67 pts)
mean 0.006 (5301 pts)
if durchganges >= 1 then 0.5 (44 pts)
mean 0.002 (5257 pts)
if duldung >= 1 then 0.5 (12 pts)
mean 0.001 (5245 pts)
if lichte >= 1 then 0.75 (4 pts)
mean 0.0 (5241 pts)
if durchgangs >= 1 then 0.167 (6 pts)
mean 0 (5235 pts)

```
## VolumenUndUmbaubarerRaum
```bash
                          precision    recall  f1-score   support

                     NOT       1.00      1.00      1.00       778
VolumenUndUmbaubarerRaum       1.00      1.00      1.00        23

                accuracy                           1.00       801
               macro avg       1.00      1.00      1.00       801
            weighted avg       1.00      1.00      1.00       801


mean 0.011 (5368 pts)
if m³ >= 1 then 1.0 (45 pts)
mean 0.003 (5323 pts)
if umbaut >= 1 then 0.75 (16 pts)
mean 0.001 (5307 pts)
if umbaubar >= 1 then 1.0 (3 pts)
mean 0.0 (5304 pts)
if kubatur >= 1 then 0.333 (3 pts)
mean 0 (5301 pts)

```
## UnterirdischeBaulichkeiten
```bash
                            precision    recall  f1-score   support

                       NOT       0.98      1.00      0.99       785
UnterirdischeBaulichkeiten       0.00      0.00      0.00        16

                  accuracy                           0.98       801
                 macro avg       0.49      0.50      0.49       801
              weighted avg       0.96      0.98      0.97       801


mean 0.011 (5368 pts)
if unterirdisch >= 1 then 0.483 (116 pts)
mean 0.0 (5252 pts)
if erdkern >= 1 then 0.5 (2 pts)
mean 0 (5250 pts)

```
## Struktureinheit
```bash
                 precision    recall  f1-score   support

            NOT       1.00      0.99      0.99       787
Struktureinheit       0.67      0.86      0.75        14

       accuracy                           0.99       801
      macro avg       0.83      0.92      0.87       801
   weighted avg       0.99      0.99      0.99       801


mean 0.012 (5368 pts)
if struktureinheit >= 1 then 0.674 (43 pts)
mean 0.006 (5325 pts)
if strukturgebiet >= 1 then 0.645 (31 pts)
mean 0.002 (5294 pts)
if struktur >= 1 then 0.778 (9 pts)
mean 0.001 (5285 pts)
if strukturgebietes >= 1 then 0.5 (6 pts)
mean 0.001 (5279 pts)
if etc >= 1 then 0.167 (6 pts)

```
## Stockwerk
```bash
              precision    recall  f1-score   support

         NOT       1.00      1.00      1.00       793
   Stockwerk       0.88      0.88      0.88         8

    accuracy                           1.00       801
   macro avg       0.94      0.94      0.94       801
weighted avg       1.00      1.00      1.00       801


mean 0.012 (5368 pts)
if erdgeschoß >= 1 then 0.923 (39 pts)
mean 0.006 (5329 pts)
if erdgeschoss >= 1 then 1.0 (15 pts)
mean 0.003 (5314 pts)
if ausschlussen >= 1 then 1.0 (4 pts)
mean 0.002 (5310 pts)
if dachgeschoß >= 1 then 0.444 (9 pts)
mean 0.002 (5301 pts)
if hauptgeschoß >= 1 then 1.0 (1 pts)

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
if vollflächig >= 1 then 0.656 (32 pts)
mean 0.002 (5298 pts)
if lärmschutzwand >= 1 then 1.0 (2 pts)
mean 0.002 (5296 pts)
if durchblick >= 1 then 0.269 (26 pts)
mean 0.001 (5270 pts)
if lärmschutzeinrichtung >= 1 then 0.333 (3 pts)

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
if technik >= 1 then 0.062 (48 pts)
mean 0.0 (5232 pts)
if begrünen >= 1 then 0.038 (26 pts)
mean 0.0 (5206 pts)
if wissenschaft >= 1 then 0.017 (58 pts)
mean 0 (5148 pts)

```
## BebauteFlaecheMax
```bash
                   precision    recall  f1-score   support

              NOT       0.99      1.00      0.99       790
BebauteFlaecheMax       0.80      0.36      0.50        11

         accuracy                           0.99       801
        macro avg       0.90      0.68      0.75       801
     weighted avg       0.99      0.99      0.99       801


mean 0.01 (5368 pts)
if maximal >= 2 then 0.611 (18 pts)
mean 0.008 (5350 pts)
if ² >= 1 then 0.127 (237 pts)
mean 0.002 (5113 pts)
if baulos >= 1 then 0.667 (3 pts)
mean 0.002 (5110 pts)
if insgesamt >= 1 then 0.071 (56 pts)
mean 0.001 (5054 pts)
if kleingartengebiet >= 1 then 0.25 (4 pts)

```
## VerbotFensterZuOeffentlichenVerkehrsflaechen
```bash
                                              precision    recall  f1-score   support

                                         NOT       1.00      1.00      1.00       794
VerbotFensterZuOeffentlichenVerkehrsflaechen       1.00      1.00      1.00         7

                                    accuracy                           1.00       801
                                   macro avg       1.00      1.00      1.00       801
                                weighted avg       1.00      1.00      1.00       801


mean 0.01 (5368 pts)
if aufenthaltsräumen >= 1 then 1.0 (38 pts)
mean 0.003 (5330 pts)
if richten >= 1 then 1.0 (9 pts)
mean 0.001 (5321 pts)
if hauptfenster >= 1 then 1.0 (5 pts)
mean 0.0 (5316 pts)
if errichtung >= 2 then 0.2 (5 pts)
mean 0.0 (5311 pts)
if hütteldorfer >= 1 then 0.111 (9 pts)
mean 0 (5302 pts)

```
## BebauteFlaecheMaxNebengebaeude
```bash
                                precision    recall  f1-score   support

                           NOT       0.99      1.00      0.99       793
BebauteFlaecheMaxNebengebaeude       0.00      0.00      0.00         8

                      accuracy                           0.99       801
                     macro avg       0.50      0.50      0.50       801
                  weighted avg       0.98      0.99      0.99       801


mean 0.01 (5368 pts)
if bauplatz >= 1 then 0.361 (133 pts)
mean 0.001 (5235 pts)
if nebengebäude >= 1 then 0.065 (46 pts)
mean 0 (5189 pts)

```
## Summary
| label                                        |   gold |   predicted |   precision |   recall |      F1 |
|----------------------------------------------|--------|-------------|-------------|----------|---------|
| total                                        |    940 |         828 |      85.87% |   75.64% |  80.43% |
| Planzeichen                                  |    228 |         212 |      97.17% |   90.35% |  93.64% |
| Widmung                                      |     59 |          34 |      97.06% |   55.93% |  70.97% |
| AnordnungGaertnerischeAusgestaltung          |     42 |          46 |      91.30% |  100.00% |  95.45% |
| GebaeudeHoeheArt                             |     34 |          35 |      71.43% |   73.53% |  72.46% |
| VorkehrungBepflanzung                        |     33 |          31 |      96.77% |   90.91% |  93.75% |
| VerkehrsflaecheID                            |     32 |          34 |      70.59% |   75.00% |  72.73% |
| AbschlussDachMaxBezugGebaeude                |     28 |          31 |      67.74% |   75.00% |  71.19% |
| AnFluchtlinie                                |     26 |          25 |      88.00% |   84.62% |  86.27% |
| Dachart                                      |     25 |          25 |      92.00% |   92.00% |  92.00% |
| ErrichtungGebaeude                           |     24 |          11 |      90.91% |   41.67% |  57.14% |
| BegruenungDach                               |     23 |          27 |      81.48% |   95.65% |  88.00% |
| GebaeudeBautyp                               |     23 |          23 |      86.96% |   86.96% |  86.96% |
| VolumenUndUmbaubarerRaum                     |     23 |          23 |     100.00% |  100.00% | 100.00% |
| GehsteigbreiteMin                            |     21 |          21 |     100.00% |  100.00% | 100.00% |
| Nutzungsart                                  |     21 |           3 |     100.00% |   14.29% |  25.00% |
| WidmungInMehrerenEbenen                      |     20 |          23 |      82.61% |   95.00% |  88.37% |
| BBAllgemein                                  |     19 |          17 |      76.47% |   68.42% |  72.22% |
| GebaeudeHoeheMaxAbsolut                      |     19 |           0 |     100.00% |    0.00% |   0.00% |
| VonBebauungFreizuhalten                      |     19 |           0 |     100.00% |    0.00% |   0.00% |
| GesamtePlangebiet                            |     18 |          24 |      66.67% |   88.89% |  76.19% |
| UnterirdischeBaulichkeiten                   |     16 |           0 |     100.00% |    0.00% |   0.00% |
| DurchgangBreite                              |     14 |          16 |      50.00% |   57.14% |  53.33% |
| Struktureinheit                              |     14 |          18 |      66.67% |   85.71% |  75.00% |
| DachneigungMax                               |     13 |          16 |      81.25% |  100.00% |  89.66% |
| Bauklasse                                    |     12 |          12 |     100.00% |  100.00% | 100.00% |
| DurchgangHoehe                               |     12 |          11 |      54.55% |   50.00% |  52.17% |
| UnterbrechungGeschlosseneBauweise            |     12 |          12 |     100.00% |  100.00% | 100.00% |
| BauweiseID                                   |     11 |          13 |      69.23% |   81.82% |  75.00% |
| BebauteFlaecheMax                            |     11 |           5 |      80.00% |   36.36% |  50.00% |
| AusnahmeGaertnerischAuszugestaltende         |     10 |           0 |     100.00% |    0.00% |   0.00% |
| BebauteFlaecheMaxProzentual                  |     10 |          12 |      58.33% |   70.00% |  63.64% |
| StrassenbreiteMin                            |     10 |          11 |      90.91% |  100.00% |  95.24% |
| EinfriedungAusgestaltung                     |      9 |           8 |     100.00% |   88.89% |  94.12% |
| AufbautenZulaessig                           |      8 |           8 |     100.00% |  100.00% | 100.00% |
| BebauteFlaecheMaxNebengebaeude               |      8 |           0 |     100.00% |    0.00% |   0.00% |
| Stockwerk                                    |      8 |           8 |      87.50% |   87.50% |  87.50% |
| StrassenbreiteMax                            |      7 |           6 |     100.00% |   85.71% |  92.31% |
| VerbotFensterZuOeffentlichenVerkehrsflaechen |      7 |           7 |     100.00% |  100.00% | 100.00% |
| DachflaecheMin                               |      6 |          14 |      28.57% |   66.67% |  40.00% |
| EinfriedungHoeheGesamt                       |      5 |           6 |      83.33% |  100.00% |  90.91% |
