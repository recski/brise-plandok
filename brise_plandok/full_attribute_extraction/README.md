# Full attribute extraction

## Extract values and types

To extract `values` and `types`. 

The extracted values and types are stored in the `gen_attributes` field.

```bash
# Extract for one attribute, only if gold
cat data/train/8228.json |  python brise_plandok/full_attribute_extraction/extract_types_and_values.py -t -v -a Planzeichen -g  | jq '.sens[] | .id, .text, .gen_attributes'

# Extract for one attribute, not only if gold
cat data/train/8228.json |  python brise_plandok/full_attribute_extraction/extract_types_and_values.py -t -v -a WidmungUndZweckbestimmung  | jq '.sens[] | .id, .text, .gen_attributes'

# Extract for multiple attributes, only if gold
cat data/train/8228.json |  python brise_plandok/full_attribute_extraction/extract_types_and_values.py -t -v -a Planzeichen WidmungUndZweckbestimmung -g | jq '.sens[] | .id, .text, .gen_attributes'
```

## Predict full attributes

To predict `attributes` and extract their `values` and `types`. 

The extracted values and types are stored in the `predicted_attributes` field.

```bash
 python brise_plandok/full_attribute_extraction/predict_full_attributes.py -d data/train/8228.json -c |  jq '.sens[] | .id, .text, .predicted_attributes'
```

## Migrate attributes

```bash
# Flachen -> 
# BebauteFlaecheMax BebauteFlaecheMaxNebengebaeude BebauteFlaecheMaxProzentual BebauteFlaecheMin
python brise_plandok/full_attribute_extraction/migrate_attribute.py -g GOLD_DIR -i Flaechen -o BebauteFlaecheMax BebauteFlaecheMaxNebengebaeude BebauteFlaecheMaxProzentual BebauteFlaecheMin
```
