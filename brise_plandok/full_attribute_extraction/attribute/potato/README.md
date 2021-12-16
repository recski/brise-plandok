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

## Start GUI for a specific attribute

```bash
# Start for Planzeichen
streamlit run POTATO_DIR/frontend/app.py -- -t data/train -v data/valid -g fourlang -sr features/manual/Planzeichen.json -l Planzeichen
```
