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

<<<<<<< HEAD
## Manual rules evaluation (old)
=======
## Manual rules evaluation (2022-05-18)
>>>>>>> 8499d321a49781be8e5bf5e733005cc3cfdfcff5

| Attributes                                | gold | predicted | precision | recall   | f1       | rank |
|-----------------------------------------------|------|-----------|-----------|----------|----------|------|
| total                                         | 8351 | 7472      | 88.24%    | 78.95%   | 83.33%   |      |
| Planzeichen                                   | 1844 | 1855      | 94.82%    | 95.39%   | 95.11%   | 1    | 
| Widmung                                       | 641  | 745       | 80.40%    | 93.45%   | 86.44%   | 2    |
| VerkehrsflaecheID                             | 400  | 342       | 64.33%    | 55.00%   | 59.30%   | 3    |
| GesamtePlangebiet                             | 189  | 358       | 47.49%    | 89.95%   | 62.16%   | 4    |
| AnordnungGaertnerischeAusgestaltung           | 292  | 273       | 97.44%    | 91.10%   | 94.16%   | 5    |
| Dachart                                       | 282  | 266       | 99.25%    | 93.62%   | 96.35%   | 6    |
| AnFluchtlinie                                 | 276  | 261       | 96.17%    | 90.94%   | 93.48%   | 7    |
| VorkehrungBepflanzung                         | 274  | 222       | 100.00%   | 81.02%   | 89.52%   | 8    |
| GebaeudeHoeheArt                              | 242  | 210       | 94.29%    | 81.82%   | 87.61%   | 9    |
| BegruenungDach                                | 220  | 211       | 96.68%    | 92.73%   | 94.66%   | 10   |
| AbschlussDachMaxBezugGebaeude                 | 219  | 191       | 98.43%    | 85.84%   | 91.71%   | 11   |
| BBAllgemein                                   | 179  | 202       | 87.28%    | 91.71%   | 89.44%   | 12   |
| GebaeudeHoeheMaxAbsolut                       | 200  | 166       | 87.35%    | 72.50%   | 79.23%   | 13   |
| GehsteigbreiteMin                             | 207  | 168       | 100.00%   | 81.16%   | 89.60%   | 14   |
| WidmungInMehrerenEbenen                       | 219  | 107       | 82.24%    | 40.18%   | 53.99%   | 15   |
| GebaeudeBautyp                                | 175  | 167       | 95.81%    | 91.43%   | 93.57%   | 16   |
| Nutzungsart                                   | 157  | 151       | 79.49%    | 59.24%   | 67.88%   | 17   |
| ErrichtungGebaeude                            | 213  | 53        | 43.40%    | 10.80%   | 17.29%   | 18   |
| UnterbrechungGeschlosseneBauweise             | 154  | 154       | 100.00%   | 100.00%  | 100.00%  | 19   |
| AufbautenZulaessig                            | 152  | 132       | 98.48%    | 85.53%   | 91.55%   | 20   |
| UnterirdischeBaulichkeiten                    | 85   | 140       | 50.00%    | 82.35%   | 62.22%   | 21   |
| VonBebauungFreizuhalten                       | 144  | 58        | 86.21%    | 34.72%   | 49.50%   | 22   |
| DurchgangBreite                               | 109  | 94        | 100.00%   | 86.24%   | 92.61%   | 23   |
| DachneigungMax                                | 132  | 45        | 100.00%   | 34.09%   | 50.85%   | 24   |
| BebauteFlaecheMaxProzentual                   | 107  | 84        | 95.24%    | 74.77%   | 83.77%   | 25   |
| DurchgangHoehe                                | 96   | 90        | 93.33%    | 87.50%   | 90.32%   | 26   |
| AusnahmeGaertnerischAuszugestaltende          | 103  | 55        | 100.00%   | 53.40%   | 69.62%   | 27   |
| BauweiseID                                    | 97   | 56        | 98.21%    | 56.70%   | 71.90%   | 28   |
| Struktureinheit                               | 81   | 56        | 58.93%    | 40.74%   | 48.18%   | 29   |
| VolumenUndUmbaubarerRaum                      | 91   | 54        | 100.00%   | 59.34%   | 74.48%   | 30   |
| Stockwerk                                     | 80   | 63        | 93.65%    | 73.75%   | 82.52%   | 31   |
| BebauteFlaecheMaxNebengebaeude                | 65   | 71        | 81.69%    | 89.23%   | 85.29%   | 32   |
| BebauteFlaecheMax                             | 69   | 59        | 94.92%    | 81.16%   | 87.50%   | 33   |
| VerbotFensterZuOeffentlichenVerkehrsflaechen  | 67   | 57        | 100.00%   | 85.07%   | 91.94%   | 34   |
| VerbotWohnung                                 | 61   | 50        | 100.00%   | 81.97%   | 90.09%   | 35   |
| BebauteFlaecheMin                             | 48   | 55        | 76.36%    | 87.50%   | 81.55%   | 36   |
| DachflaecheMin                                | 71   | 0         | 100.00%   | 0.00%    | 0.00%    | 37   |
| AnordnungGaertnerischeAusgestaltungProzentual | 50   | 35        | 94.29%    | 66.00%   | 77.65%   | 38   |
| AnOeffentlichenVerkehrsflaechen               | 54   | 25        | 100.00%   | 46.30%   | 63.29%   | 39   |
| OeffentlicheVerkehrsflaecheBreiteMin          | 51   | 27        | 100.00%   | 52.94%   | 69.23%   | 40   |
| GebaeudeHoeheMaxWN                            | 32   | 29        | 82.76%    | 75.00%   | 78.69%   | 41   |
| AnteilDachbegruenung                          | 36   | 24        | 91.67%    | 61.11%   | 73.33%   | 42   |
| StellplatzregulativUmfangMinimumRelativ       | 18   | 19        | 94.74%    | 100.00%  | 97.30%   | 43   |
| FBOKMinimumWohnungen                          | 20   | 0         | 100.00%   | 0.00%    | 0.00%    | 44   |
| StellplatzregulativUmfangMaximumRelativ       | 11   | 4         | 75.00%    | 27.27%   | 40.00%   | 45   |
