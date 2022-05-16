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

### For all attributes
Takses around 3 minutes to calculate.
```bash
python  $POTATO_DIR/scripts/evaluate.py \
    -t fourlang \
    -f features/manual \
    -d data/gold.csv \
    -m report \
    -cs
```

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

## Manual rules evaluation (2022-05-13)

| Attributes                                | gold | predicted | precision | recall  | f1 | rank |
|-----------------------------------------------|------|-----------|-----------|---------|---------|------|
| total                                         | 8066 | 7531      | 83.06%    | 77.55%  | 80.21%  |      |
| Planzeichen                                   | 1700 | 1585      | 97.16%    | 90.59%  | 93.76%  | 1    | 
| Widmung                                       | 538  | 745       | 66.98%    | 92.75%  | 77.79%  | 2    |
| VerkehrsflaecheID                             | 400  | 342       | 64.33%    | 55.00%  | 59.30%  | 3    |
| GesamtePlangebiet                             | 189  | 358       | 47.49%    | 89.95%  | 62.16%  | 4    |
| AnordnungGaertnerischeAusgestaltung           | 292  | 273       | 97.44%    | 91.10%  | 94.16%  | 5    |
| Dachart                                       | 282  | 266       | 99.25%    | 93.62%  | 96.35%  | 6    |
| AnFluchtlinie                                 | 276  | 261       | 96.17%    | 90.94%  | 93.48%  | 7    |
| VorkehrungBepflanzung                         | 274  | 222       | 100.00%   | 81.02%  | 89.52%  | 8    |
| GebaeudeHoeheArt                              | 242  | 210       | 94.29%    | 81.82%  | 87.61%  | 9    |
| WidmungUndZweckbestimmung                     | 0    | 332       | 0.00%     | 100.00% | 0.00%   | 10   |
| BegruenungDach                                | 220  | 211       | 96.68%    | 92.73%  | 94.66%  | 11   |
| AbschlussDachMaxBezugGebaeude                 | 219  | 191       | 98.43%    | 85.84%  | 91.71%  | 12   |
| BBAllgemein                                   | 179  | 202       | 87.28%    | 91.71%  | 89.44%  | 13   |
| GebaeudeHoeheMaxAbsolut                       | 200  | 166       | 87.35%    | 72.50%  | 79.23%  | 14   |
| GehsteigbreiteMin                             | 207  | 168       | 100.00%   | 81.16%  | 89.60%  | 15   |
| WidmungInMehrerenEbenen                       | 219  | 107       | 82.24%    | 40.18%  | 53.99%  | 16   |
| GebaeudeBautyp                                | 175  | 167       | 95.81%    | 91.43%  | 93.57%  | 17   |
| Nutzungsart                                   | 157  | 151       | 79.49%    | 59.24%  | 67.88%  | 18   |
| ErrichtungGebaeude                            | 213  | 53        | 43.40%    | 10.80%  | 17.29%  | 19   |
| UnterbrechungGeschlosseneBauweise             | 154  | 154       | 100.00%   | 100.00% | 100.00% | 20   |
| AufbautenZulaessig                            | 152  | 132       | 98.48%    | 85.53%  | 91.55%  | 21   |
| UnterirdischeBaulichkeiten                    | 85   | 140       | 50.00%    | 82.35%  | 62.22%  | 22   |
| VonBebauungFreizuhalten                       | 144  | 58        | 86.21%    | 34.72%  | 49.50%  | 23   |
| DurchgangBreite                               | 109  | 94        | 100.00%   | 86.24%  | 92.61%  | 24   |
| DachneigungMax                                | 132  | 45        | 100.00%   | 34.09%  | 50.85%  | 25   |
| BebauteFlaecheMaxProzentual                   | 107  | 84        | 95.24%    | 74.77%  | 83.77%  | 26   |
| DurchgangHoehe                                | 96   | 90        | 93.33%    | 87.50%  | 90.32%  | 27   |
| AusnahmeGaertnerischAuszugestaltende          | 103  | 55        | 100.00%   | 53.40%  | 69.62%  | 28   |
| BauweiseID                                    | 97   | 56        | 98.21%    | 56.70%  | 71.90%  | 29   |
| Struktureinheit                               | 81   | 56        | 58.93%    | 40.74%  | 48.18%  | 30   |
| VolumenUndUmbaubarerRaum                      | 91   | 54        | 100.00%   | 59.34%  | 74.48%  | 31   |
| Stockwerk                                     | 80   | 63        | 93.65%    | 73.75%  | 82.52%  | 32   |
| BebauteFlaecheMaxNebengebaeude                | 65   | 71        | 81.69%    | 89.23%  | 85.29%  | 33   |
| BebauteFlaecheMax                             | 69   | 59        | 94.92%    | 81.16%  | 87.50%  | 34   |
| VerbotFensterZuOeffentlichenVerkehrsflaechen  | 67   | 57        | 100.00%   | 85.07%  | 91.94%  | 35   |
| VerbotWohnung                                 | 61   | 50        | 100.00%   | 81.97%  | 90.09%  | 36   |
| BebauteFlaecheMin                             | 48   | 55        | 76.36%    | 87.50%  | 81.55%  | 37   |
| DachflaecheMin                                | 71   | 0         | 100.00%   | 0.00%   | 0.00%   | 38   |
| AnordnungGaertnerischeAusgestaltungProzentual | 50   | 35        | 94.29%    | 66.00%  | 77.65%  | 39   |
| AnOeffentlichenVerkehrsflaechen               | 54   | 25        | 100.00%   | 46.30%  | 63.29%  | 40   |
| OeffentlicheVerkehrsflaecheBreiteMin          | 51   | 27        | 100.00%   | 52.94%  | 69.23%  | 41   |
| GebaeudeHoeheMaxWN                            | 32   | 29        | 82.76%    | 75.00%  | 78.69%  | 42   |
| AnteilDachbegruenung                          | 36   | 24        | 91.67%    | 61.11%  | 73.33%  | 43   |
| StellplatzregulativUmfangMinimumRelativ       | 18   | 19        | 94.74%    | 100.00% | 97.30%  | 44   |
| FBOKMinimumWohnungen                          | 20   | 0         | 100.00%   | 0.00%   | 0.00%   | 45   |
| StellplatzregulativUmfangMaximumRelativ       | 11   | 4         | 75.00%    | 27.27%  | 40.00%  | 46   |
