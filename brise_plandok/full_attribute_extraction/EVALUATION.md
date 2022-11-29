## Evaluation of full rule extraction

### type and value extraction of gold attributes

```
awk 1 ../../data/*/*.json | python extract_types_and_values.py -t -v -g > eval/brise_types_values.jsonl
```

```
at eval/brise_types_values.jsonl | python eval_types_and_values.py -f gen_attributes -t -v
```

### type and value extraction on predicted attributes

```
awk 1 ../../data/*/*.json | python eval_types_and_values.py -f predicted_attributes -t -v
```


### predict modalities

```
cat eval/brise_types_values.jsonl | python predict_modalities.py > eval/types_values_modality.jsonl
```

```
cat eval/types_values_modality.jsonl | python eval_modalities.py
```

### end-to-end eval with gold attributes

```
cat eval/types_values_modality.jsonl | python eval_rules.py
```

### end-to-end eval with predicted attributes

```
cat eval/types_values_modality.jsonl | python eval_rules.py -p
```
