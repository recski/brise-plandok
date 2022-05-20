# Use POTATO for attribute extraction

Official website of [POTATO](https://github.com/adaamko/POTATO).

Only [top 15 attributes](constants.py) are considered.

You can find some manually defined features [here](./features/manual).

## Create dataset for 🥔

### For the complete gold dataset
__Temporary, until dataset is moved to its final location in brise-plandok__
The environment variable `BRISE_NLP` should point to the location of the [brise-nlp]
repository

```bash
python create_dataset.py -d $BRISE_NLP/annotation/2021_09/full_data -g fourlang -o -n gold.csv
```

## Start GUI for specific attribute

_The environment variable `POTATO_DIR` should point to the location of the POTATO
repository_

```bash
# Start for Planzeichen
streamlit run $POTATO_DIR/frontend/app.py -- \
      -t data/gold.csv \
      -v data/gold.csv \
      -g fourlang \
      -hr features/manual/Widmung.tsv \
      -l Widmung \
      -cs
```

## Evalutate attribute extraction

First, you have to create `data/gold.csv` as written above (if haven't already done).

### For a specific attribute
```bash
python  $POTATO_DIR/scripts/evaluate.py \
    -t fourlang \
    -f features/manual \
    -d data/gold.csv \
    -m report \
    -l Widmung \
    -cs
```

### For all attributes
Takses around 3 minutes to calculate.
```bash
python  $POTATO_DIR/scripts/evaluate.py \
    -t fourlang \
    -f features/manual \
    -d data/gold.csv \
    -m report \
    -cs \
    -a
```

|Attribute                                    | Gold  | Predicted  | Precision  | Recall  | F-score  | Rank  |
|---------------------------------------------|-------|------------|------------|---------|----------|-------|
|total                                        | 9665  | 6595       | 93.13%     | 63.55%  | 75.55%   |       |
|Planzeichen                                  | 1844  | 1855       | 94.82%     | 95.39%  | 95.11%   | 1     |
|Widmung                                      | 641   | 745        | 80.40%     | 93.45%  | 86.44%   | 2     |
|AnordnungGaertnerischeAusgestaltung          | 292   | 273        | 97.44%     | 91.10%  | 94.16%   | 3     |
|Dachart                                      | 282   | 266        | 99.25%     | 93.62%  | 96.35%   | 4     |
|AnFluchtlinie                                | 276   | 261        | 96.17%     | 90.94%  | 93.48%   | 5     |
|VerkehrsflaecheID                            | 400   | 0          | 100.00%    | 0.00%   | 0.00%    | 6     |
|VorkehrungBepflanzung                        | 274   | 222        | 100.00%    | 81.02%  | 89.52%   | 7     |
|GebaeudeHoeheArt                             | 242   | 210        | 94.29%     | 81.82%  | 87.61%   | 8     |
|BBAllgemein                                  | 217   | 228        | 87.28%     | 91.71%  | 89.44%   | 9     |
|BegruenungDach                               | 220   | 211        | 96.68%     | 92.73%  | 94.66%   | 10    |
|AbschlussDachMaxBezugGebaeude                | 219   | 191        | 98.43%     | 85.84%  | 91.71%   | 11    |
|GebaeudeHoeheMaxAbsolut                      | 200   | 164        | 87.20%     | 71.50%  | 78.57%   | 12    |
|GehsteigbreiteMin                            | 207   | 168        | 100.00%    | 81.16%  | 89.60%   | 13    |
|WidmungInMehrerenEbenen                      | 219   | 107        | 82.24%     | 40.18%  | 53.99%   | 14    |
|GebaeudeBautyp                               | 175   | 167        | 95.81%     | 91.43%  | 93.57%   | 15    |
|UnterbrechungGeschlosseneBauweise            | 154   | 154        | 100.00%    | 100.00% | 100.00%  | 16    |
|Nutzungsart                                  | 157   | 117        | 79.49%     | 59.24%  | 67.88%   | 17    |
|AufbautenZulaessig                           | 152   | 132        | 98.48%     | 85.53%  | 91.55%   | 18    |
|ErrichtungGebaeude                           | 213   | 0          | 100.00%    | 0.00%   | 0.00%    | 19    |
|GesamtePlangebiet                            | 189   | 0          | 100.00%    | 0.00%   | 0.00%    | 20    |
|VonBebauungFreizuhalten                      | 144   | 58         | 86.21%     | 34.72%  | 49.50%   | 21    |
|StrassenbreiteMin                            | 177   | 0          | 100.00%    | 0.00%   | 0.00%    | 22    |
|DurchgangBreite                              | 109   | 94         | 100.00%    | 86.24%  | 92.61%   | 23    |
|DachneigungMax                               | 132   | 45         | 100.00%    | 34.09%  | 50.85%   | 24    |
|BebauteFlaecheMaxProzentual                  | 107   | 84         | 95.24%     | 74.77%  | 83.77%   | 25    |
|DurchgangHoehe                               | 96    | 90         | 93.33%     | 87.50%  | 90.32%   | 26    |
|AusnahmeGaertnerischAuszugestaltende         | 103   | 55         | 100.00%    | 53.40%  | 69.62%   | 27    |
|BauweiseID                                   | 97    | 56         | 98.21%     | 56.70%  | 71.90%   | 28    |
|VolumenUndUmbaubarerRaum                     | 91    | 54         | 100.00%    | 59.34%  | 74.48%   | 29    |
|Bauklasse                                    | 116   | 0          | 100.00%    | 0.00%   | 0.00%    | 30    |
|EinfriedungAusgestaltung                     | 115   | 0          | 100.00%    | 0.00%   | 0.00%    | 31    |
|Stockwerk                                    | 80    | 63         | 93.65%     | 73.75%  | 82.52%   | 32    |
|BebauteFlaecheMaxNebengebaeude               | 65    | 71         | 81.69%     | 89.23%  | 85.29%   | 33    |
|StrassenbreiteMax                            | 100   | 0          | 100.00%    | 0.00%   | 0.00%    | 34    |
|BebauteFlaecheMax                            | 69    | 57         | 98.25%     | 81.16%  | 88.89%   | 35    |
|VerbotFensterZuOeffentlichenVerkehrsflaechen | 67    | 57         | 100.00%    | 85.07%  | 91.94%   | 36    |
|DachflaecheMin                               | 71    | 48         | 100.00%    | 67.61%  | 80.67%   | 37    |
|VerbotWohnung                                | 61    | 50         | 100.00%    | 81.97%  | 90.09%   | 38    |
|UnterirdischeBaulichkeiten                   | 85    | 0          | 100.00%    | 0.00%   | 0.00%    | 39    |
|BebauteFlaecheMin                            | 48    | 55         | 76.36%     | 87.50%  | 81.55%   | 40    |
|Struktureinheit                              | 81    | 0          | 100.00%    | 0.00%   | 0.00%    | 41    |
|EinfriedungHoeheGesamt                       | 77    | 0          | 100.00%    | 0.00%   | 0.00%    | 42    |
|AnordnungGaertnerischeAusgestaltungProzentual| 50    | 35         | 94.29%     | 66.00%  | 77.65%   | 43    |
|AnOeffentlichenVerkehrsflaechen              | 54    | 25         | 100.00%    | 46.30%  | 63.29%   | 44    |
|OeffentlicheVerkehrsflaecheBreiteMin         | 51    | 27         | 100.00%    | 52.94%  | 69.23%   | 45    |
|VorstehendeBauelementeAusladungMax           | 61    | 0          | 100.00%    | 0.00%   | 0.00%    | 46    |
|EinfriedungLage                              | 56    | 0          | 100.00%    | 0.00%   | 0.00%    | 47    |
|GebaeudeHoeheMaxWN                           | 32    | 29         | 82.76%     | 75.00%  | 78.69%   | 48    |
|AnteilDachbegruenung                         | 36    | 24         | 91.67%     | 61.11%  | 73.33%   | 49    |
|StrassenbreiteVonBis                         | 49    | 0          | 100.00%    | 0.00%   | 0.00%    | 50    |
|EinfriedungZulaessig                         | 48    | 0          | 100.00%    | 0.00%   | 0.00%    | 51    |
|VorbautenVerbot                              | 46    | 0          | 100.00%    | 0.00%   | 0.00%    | 52    |
|AnlageZumEinstellenVorhanden                 | 44    | 0          | 100.00%    | 0.00%   | 0.00%    | 53    |
|FBOKMinimumWohnungen                         | 20    | 24         | 70.83%     | 85.00%  | 77.27%   | 54    |
|EinleitungNiederschlagswaesser               | 36    | 0          | 100.00%    | 0.00%   | 0.00%    | 55    |
|VerbotStaffelung                             | 32    | 0          | 100.00%    | 0.00%   | 0.00%    | 56    |
|StellplatzregulativUmfangMinimumRelativ      | 18    | 19         | 94.74%     | 100.00% | 97.30%   | 57    |
|ArkadeHoehe                                  | 27    | 0          | 100.00%    | 0.00%   | 0.00%    | 58    |
|StellplatzImNiveauZulaessig                  | 27    | 0          | 100.00%    | 0.00%   | 0.00%    | 59    |
|MaxAnzahlGeschosseOberirdisch                | 19    | 0          | 100.00%    | 0.00%   | 0.00%    | 60    |
|AnzahlGebaeudeMax                            | 19    | 0          | 100.00%    | 0.00%   | 0.00%    | 61    |
|InSchutzzone                                 | 18    | 0          | 100.00%    | 0.00%   | 0.00%    | 62    |
|Massengliederung                             | 17    | 0          | 100.00%    | 0.00%   | 0.00%    | 63    |
|BauklasseVIHoeheMax                          | 16    | 0          | 100.00%    | 0.00%   | 0.00%    | 64    |
|StellplatzMax                                | 15    | 0          | 100.00%    | 0.00%   | 0.00%    | 65    |
|AbschlussDachMaxBezugGelaende                | 14    | 0          | 100.00%    | 0.00%   | 0.00%    | 66    |
|BauklasseVIHoeheMin                          | 14    | 0          | 100.00%    | 0.00%   | 0.00%    | 67    |
|StellplatzregulativUmfangMaximumRelativ      | 11    | 4          | 75.00%     | 27.27%  | 40.00%   | 68    |
|Kleinhaeuser                                 | 13    | 0          | 100.00%    | 0.00%   | 0.00%    | 69    |
|DachneigungMin                               | 13    | 0          | 100.00%    | 0.00%   | 0.00%    | 70    |
|TechnischeAufbautenHoeheMax                  | 11    | 0          | 100.00%    | 0.00%   | 0.00%    | 71    |
|OberflaecheBestimmungP                       | 11    | 0          | 100.00%    | 0.00%   | 0.00%    | 72    |
|DurchfahrtHoehe                              | 11    | 0          | 100.00%    | 0.00%   | 0.00%    | 73    |
|MaxAnzahlDachgeschosse                       | 11    | 0          | 100.00%    | 0.00%   | 0.00%    | 74    |
|VerbotBueroGeschaeftsgebaeude                | 10    | 0          | 100.00%    | 0.00%   | 0.00%    | 75    |
|VorbautenBeschraenkung                       | 10    | 0          | 100.00%    | 0.00%   | 0.00%    | 76    |
|GaragengebaeudeAusfuehrung                   | 9     | 0          | 100.00%    | 0.00%   | 0.00%    | 77    |
|StellplatzregulativUmfangMaximumAbsolut      | 8     | 0          | 100.00%    | 0.00%   | 0.00%    | 78    |
|GebaeudeHoeheMin                             | 8     | 0          | 100.00%    | 0.00%   | 0.00%    | 79    |
|MindestraumhoeheEG                           | 7     | 0          | 100.00%    | 0.00%   | 0.00%    | 80    |
|BestimmmungenFuerHochhausUndGrossbauvorhaben | 7     | 0          | 100.00%    | 0.00%   | 0.00%    | 81    |
|Geschaeftsstrassen                           | 6     | 0          | 100.00%    | 0.00%   | 0.00%    | 82    |
|DurchfahrtBreite                             | 6     | 0          | 100.00%    | 0.00%   | 0.00%    | 83    |
|HoehenlageGrundflaeche                       | 6     | 0          | 100.00%    | 0.00%   | 0.00%    | 84    |
|GebaeudeEinschraenkungP                      | 5     | 0          | 100.00%    | 0.00%   | 0.00%    | 85    |
|AusnahmeVonWohnungenUnzulaessig              | 5     | 0          | 100.00%    | 0.00%   | 0.00%    | 86    |
|HochhausZulaessigGemaessBB                   | 4     | 0          | 100.00%    | 0.00%   | 0.00%    | 87    |
|MaxAnzahlGeschosseOberirdischOhneDachgeschoss| 3     | 0          | 100.00%    | 0.00%   | 0.00%    | 88    |
|Einbautrasse                                 | 2     | 0          | 100.00%    | 0.00%   | 0.00%    | 89    |
|ZulaessigeGeschossanzahlEinkaufszentrum      | 2     | 0          | 100.00%    | 0.00%   | 0.00%    | 90    |
|VerbotAufenthaltsraum                        | 1     | 0          | 100.00%    | 0.00%   | 0.00%    | 91    |
|AnteilBaumbepflanzung                        | 1     | 0          | 100.00%    | 0.00%   | 0.00%    | 92    |
|VerbotStellplaetzeUndParkgebaeude            | 1     | 0          | 100.00%    | 0.00%   | 0.00%    | 93    |

