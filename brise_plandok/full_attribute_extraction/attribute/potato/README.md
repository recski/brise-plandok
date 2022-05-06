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
      -hr features/manual/Planzeichen.json \
      -l Planzeichen
```

## Evalutate for specific attribute

First, you have to create `data/gold.csv` as written above (if haven't already done).

```bash
python  $POTATO_DIR/scripts/evaluate.py \
    -t fourlang \
    -f features/manual \
    -d data/gold.csv \
    -m report \
    -l Planzeichen
```

## Manual rules evaluation (old)

| Manual rules                        | precision | recall | f1-score | support |
|-------------------------------------|-----------|--------|----------|---------| 
| AbschlussDachMaxBezugGebaeude       | 1.00      | 0.89   | 0.94     | 18      |
| AnFluchtlinie                       | 0.90      | 0.71   | 0.79     | 24      |
| AnordnungGaertnerischeAusgestaltung | 0.93      | 0.90   | 0.91     | 29      |
| BegruenungDach                      | 0.88      | 0.91   | 0.89     | 23      |
| Dachart                             | 0.96      | 0.84   | 0.89     | 25      |
| Flaechen                            | 1.00      | 0.19   | 0.31     | 43      |
| GebaeudeBautyp                      | 1.00      | 0.67   | 0.80     | 21      |
| GebaeudeHoeheArt                    | 1.00      | 0.47   | 0.64     | 19      |
| GebaeudeHoeheMax                    | 1.00      | 0.55   | 0.71     | 22      |
| Planzeichen                         | 0.88      | 0.23   | 0.36     | 163     |
| VerkehrsflaecheID                   | 0.26      | 0.33   | 0.29     | 21      |
| VonBebauungFreizuhalten             | 0.82      | 0.45   | 0.58     | 20      |
| VorkehrungBepflanzung               | 1.00      | 0.91   | 0.95     | 21      |
| WidmungInMehrerenEbenen             | 0.90      | 0.64   | 0.75     | 14      |
| WidmungUndZweckbestimmung           | 0.93      | 0.21   | 0.34     | 62      |
|                                     |           |        |          |         | 
| micro avg                           | 0.90      | 0.45   | 0.55     | 525     |
| macro avg                           | 0.90      | 0.59   | 0.68     | 525     |
| weighted avg                        | -         | -      | -        | 525     |
| samples avg                         | -         | -      | -        | 525     |
