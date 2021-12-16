# Use POTATO for attribute extraction

Official website of [POTATO](https://github.com/adaamko/POTATO).

Only [top 15 attributes](constants.py) are considered.

You can find some manually defined features [here](./features/manual).

## Create dataset for 🥔

```bash
# Train with 4lang graphs
python create_dataset.py -d ../../../../data/train -g fourlang -n train

# valid with 4lang graphs
python create_dataset.py -d ../../../../data/valid -g fourlang -n valid
```

## Start GUI for specific attribute

```bash
# Start for Planzeichen
streamlit run POTATO_DIR/frontend/app.py -- \
      -t data/train \
      -v data/valid \
      -g fourlang \
      -sr features/manual/Planzeichen.json \
      -l Planzeichen
```

## Evalutate for specific attribute

```bash
python  POTATO_DIR/scripts/evaluate.py \
    -t fourlang \
    -f features/manual/Planzeichen.json \
    -d data/valid \
    -m report \
    -l Planzeichen
```

## Manual rules evalutaion

| Manual rules                        | precision | recall | f1-score | support |
|-------------------------------------|-----------|--------|----------|---------| 
| AbschlussDachMaxBezugGebaeude       |           |        |          | 18      |
| AnFluchtlinie                       | 0.90      | 0.71   | 0.79     | 24      |
| AnordnungGaertnerischeAusgestaltung | 0.93      | 0.90   | 0.91     | 29      |
| BegruenungDach                      |           |        |          | 23      |
| Dachart                             | 0.96      | 0.84   | 0.89     | 25      |
| Flaechen                            | 1.00      | 0.19   | 0.31     | 43      |
| GebaeudeBautyp                      |           |        |          | 21      |
| GebaeudeHoeheArt                    | 1.00      | 0.47   | 0.64     | 19      |
| GebaeudeHoeheMax                    | 1.00      | 0.55   | 0.71     | 22      |
| Planzeichen                         | 0.88      | 0.23   | 0.36     | 163     |
| VerkehrsflaecheID                   | 0.26      | 0.33   | 0.29     | 21      |
| VonBebauungFreizuhalten             |           |        |          | 20      |
| VorkehrungBepflanzung               | 1.00      | 0.91   | 0.95     | 21      |
| WidmungInMehrerenEbenen             | 0.90      | 0.64   | 0.75     | 14      |
| WidmungUndZweckbestimmung           | 0.93      | 0.21   | 0.34     | 62      |
|                                     |           |        |          |         | 
| micro avg                           | -         | -      | -        | 525     |
| macro avg                           | -         | -      | -        | 525     |
| weighted avg                        | -         | -      | -        | 525     |
| samples avg                         | -         | -      | -        | 525     |
