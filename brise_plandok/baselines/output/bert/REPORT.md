# BERT Report

## Train all rule based attributes simultaneously

Logs: brise_bert_20220722_1423_21

```bash
                                                precision    recall  f1-score   support

                AbschlussDachMaxBezugGebaeude       0.92      0.79      0.85        28
                                AnFluchtlinie       0.92      0.88      0.90        26
              AnOeffentlichenVerkehrsflaechen       1.00      0.33      0.50         6
          AnordnungGaertnerischeAusgestaltung       1.00      0.83      0.91        42
AnordnungGaertnerischeAusgestaltungProzentual       0.75      0.75      0.75         4
                         AnteilDachbegruenung       0.00      0.00      0.00         1
                           AufbautenZulaessig       1.00      0.75      0.86         8
         AusnahmeGaertnerischAuszugestaltende       0.88      0.70      0.78        10
                                  BBAllgemein       0.76      0.68      0.72        19
                                   BauweiseID       1.00      0.45      0.62        11
                            BebauteFlaecheMax       0.00      0.00      0.00        11
               BebauteFlaecheMaxNebengebaeude       0.50      0.50      0.50         8
                  BebauteFlaecheMaxProzentual       0.67      0.40      0.50        10
                            BebauteFlaecheMin       0.82      0.90      0.86        10
                               BegruenungDach       0.84      0.91      0.87        23
                                      Dachart       0.91      0.80      0.85        25
                               DachflaecheMin       1.00      0.50      0.67         6
                               DachneigungMax       0.92      0.85      0.88        13
                              DurchgangBreite       0.80      0.86      0.83        14
                               DurchgangHoehe       0.50      0.50      0.50        12
                         FBOKMinimumWohnungen       1.00      1.00      1.00         2
                               GebaeudeBautyp       0.85      0.48      0.61        23
                             GebaeudeHoeheArt       0.96      0.74      0.83        34
                      GebaeudeHoeheMaxAbsolut       0.67      0.63      0.65        19
                           GebaeudeHoeheMaxWN       0.00      0.00      0.00         0
                            GehsteigbreiteMin       1.00      1.00      1.00        21
                                  Nutzungsart       0.88      0.33      0.48        21
         OeffentlicheVerkehrsflaecheBreiteMin       0.78      1.00      0.88         7
                                  Planzeichen       0.96      0.93      0.94       228
      StellplatzregulativUmfangMaximumRelativ       1.00      0.75      0.86         4
      StellplatzregulativUmfangMinimumRelativ       0.83      1.00      0.91         5
                                    Stockwerk       1.00      0.50      0.67         8
            UnterbrechungGeschlosseneBauweise       1.00      1.00      1.00        12
 VerbotFensterZuOeffentlichenVerkehrsflaechen       1.00      0.57      0.73         7
                                VerbotWohnung       1.00      0.40      0.57         5
                     VolumenUndUmbaubarerRaum       1.00      0.52      0.69        23
                      VonBebauungFreizuhalten       1.00      0.84      0.91        19
                        VorkehrungBepflanzung       1.00      0.94      0.97        33
                                      Widmung       0.66      0.49      0.56        59
                      WidmungInMehrerenEbenen       0.85      0.85      0.85        20

                                    micro avg       0.89      0.76      0.82       837
                                    macro avg       0.82      0.66      0.71       837
                                 weighted avg       0.88      0.76      0.81       837
                                  samples avg       0.46      0.43      0.44       837
```

## Train all rule based attributes separately 

~ 4 hours / attribute, 40 attributes -> 160 hours (~ 1 week)