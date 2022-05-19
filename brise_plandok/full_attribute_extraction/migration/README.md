# Migration

## Migrate attribute

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

## Update attributes of a specific sentence

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

## Add attributes for sentences matching a specific patter

```bash
python brise_plandok/full_attribute_extraction/migration/refine_attribute.py \
    -g GOLD_DIR \
    -a Widmung \
    -v Bauland \
    -t condition \
    -p "im Bauland"
```

## Rename attribute

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


## Migrate types

To migrate one specific type to another in all gold_attributes of all docs.

```bash
# String representation to list representation
python brise_plandok/full_attribute_extraction/migration/migrate_type.py \
    -g GOLD_DIR \
    -i '"condition"' \
    -o '["condition"]'
```

## One-time migration

Extend `Planzeichen` with map signs from `Widmung` and `BBAllgemein`.

```bash
python brise_plandok/full_attribute_extraction/migration/fill_up_planzeichen.py \
    -g ~/research/brise-nlp/annotation/2021_09/full_data > extend_planzeichen_log.txt
```