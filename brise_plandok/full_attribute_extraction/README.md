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

## Maintenance scripts

### Migrate attribute

To migrate one attribute into several new ones semi-manually. This program suggests full predictions based on our best system, but the user is asked to confirm or fix it.

This example turns `Flaechen` into `BebauteFlaecheMax`, `BebauteFlaecheMaxNebengebaeude`, `BebauteFlaecheMaxProzentual` and `BebauteFlaecheMin`.

```bash
python brise_plandok/full_attribute_extraction/migration/migrate_attribute.py \
    -g GOLD_DIR \
    -i Flaechen \
    -o BebauteFlaecheMax BebauteFlaecheMaxNebengebaeude BebauteFlaecheMaxProzentual BebauteFlaecheMin
```

You can also migrate an attribute with a specific value, even not changing the attribute itself, just the value only (e.g. migrate all the `AnFluchtlinie` attributes with a values of `['True']`):

```bash
python brise_plandok/full_attribute_extraction/migration/migrate_attribute.py \
    -g GOLD_DIR \
    -i AnFluchtlinie \
    -o AnFluchtlinie \
    -v True
```

### Update attributes of a specific sentence

To change attributes for all sentences matching a specific text.

```bash
python brise_plandok/full_attribute_extraction/migration/update_sentence.py \
    -g GOLD_DIR \
    -t "Pro Bauplatz darf nur ein Nebengebäude mit einer bebauten Fläche von maximal 30m² errichtet werden." \
    -a '{
            "AnzahlGebaeudeMax": {
              "name": "AnzahlGebaeudeMax",
              "value": [
                "ein"
              ],
              "type": [
                "content"
              ]
            },
            "GebaeudeBautyp": {
              "name": "GebaeudeBautyp",
              "value": [
                "Nebengebäude"
              ],
              "type": [
                "condition"
              ]
            },
            "BebauteFlaecheMaxNebengebaeude": {
              "name": "BebauteFlaecheMaxNebengebaeude",
              "value": [
                "30m²"
              ],
              "type": [                     
                "content"
              ]
            }
        }'
```

### Rename attribute

To rename one attribute by keeping the sames values and types.

```bash
# Rename only in gold docs
python brise_plandok/full_attribute_extraction/migration/rename_attribute.py \
    -g GOLD_DIR \
    -i PlangebietAllgemein \
    -o GesamtePlangebiet
    
# Rename in all docs (only for gold_attributes)
python brise_plandok/full_attribute_extraction/migration/rename_attribute.py \
    -g GOLD_DIR \
    -i PlangebietAllgemein \
    -o GesamtePlangebiet \
    -a
    
# Delete a specific attribute
python brise_plandok/full_attribute_extraction/migration/rename_attribute.py \
    -g GOLD_DIR \
    -i Flaechen \
    -o "" \
    -a
```


### Migrate types

To migrate one specific type to another in all gold_attributes of all docs.

```bash
# String representation to list representation
python brise_plandok/full_attribute_extraction/migration/migrate_type.py \
    -g GOLD_DIR \
    -i '"condition"' \
    -o '["condition"]'
```

