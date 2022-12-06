# Rule extraction evaluation


## Run extraction

### end-to-end rule extraction on full dataset (attribute extraction, detection of types, values, modality)

```
awk  1 ../../data/*/*.json | python predict_full_attributes.py > eval/pred_attrs_types_values_modality.jsonl
```

### type and value extraction on gold attributes
```
cat eval/pred_attrs_types_values_modality.jsonl | python extract_types_and_values.py -t -v -g > eval/gold_attrs_pred_types_values.jsonl
```

### modality extraction on gold attributes

```
cat eval/gold_attrs_pred_types_values.jsonl | python modality/predict_modalities.py > eval/gold_attrs_pred_types_values_modalities.jsonl
```

## Evaluate


### end-to-end eval with gold attributes

```
cat eval/gold_attrs_pred_types_values_modality.jsonl | python eval_rules.py
```

### end-to-end eval with predicted attributes (all attrs)

```
cat eval/pred_attrs_types_values_modality.jsonl | python eval_rules.py -p
```

### end-to-end eval with predicted attributes (40 attrs)

```
cat eval/pred_attrs_types_values_modality.jsonl | python eval_rules.py -p -40
```
