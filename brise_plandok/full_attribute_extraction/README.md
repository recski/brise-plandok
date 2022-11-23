# Full attribute extraction

## Extract values and types

To extract `values` and `types`. 

The extracted values and types are stored in the `gen_attributes` field.

```bash
# Extract values and types for one attribute, only if attribute is among gold
cat data/train/8228.json |  python brise_plandok/full_attribute_extraction/extract_types_and_values.py -t -v -a Planzeichen -g  | jq '.sens[] | .id, .text, .gen_attributes'

# Extract values and types for one attribute, for all sentences
cat data/train/8228.json |  python brise_plandok/full_attribute_extraction/extract_types_and_values.py -t -v -a Planzeichen  | jq '.sens[] | .id, .text, .gen_attributes'

# Extract for multiple attributes, only if attributes are among gold
cat data/train/8228.json |  python brise_plandok/full_attribute_extraction/extract_types_and_values.py -t -v -a Planzeichen ErrichtungGebaeude -g | jq '.sens[] | .id, .text, .gen_attributes'
```

## Predict full attributes

To predict `attributes` and extract their `values` and `types`. 

The extracted values and types are stored in the `predicted_attributes` field.

```bash
 python brise_plandok/full_attribute_extraction/predict_full_attributes.py -d data/train/8228.json -c |  jq '.sens[] | .id, .text, .predicted_attributes'
```

## [DEV] Migration scripts

For migration scripts, see [here](./migration/README.md).
