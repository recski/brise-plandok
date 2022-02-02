# Annotation process

For details on how the dataset was split for the annotation see
the [data split documentation](brise_plandok/annotation_process/README.md).

## Step 1 - Multi-label annotation

### Excel for annotation

```bash
python brise_plandok/annotation_process/utils/label_annotation_excel_generator.py -d sample_data/annotation/full_data/8141.json -o sample_data/annotation/8141_annotation_labels.xlsx
```

### Excel for review

```bash
python brise_plandok/annotation_process/labels_annotation_to_review.py -a sample_data/annotation/01/phase1/upload/8141.xlsx sample_data/annotation/02/phase1/upload/8141.xlsx -d sample_data/annotation/full_data/8141.json -g data/train/ -of sample_data/annotation/8141_labels_review_XY.xlsx -r
```

The output is save to `sample_data/annotation/8141_labels_review_XY.xlsx`.

### Generate gold after review

```bash
python brise_plandok/annotation_process/labels_review_to_gold.py -r sample_data/annotation/8141_labels_review_XY.xlsx -d sample_data/annotation/full_data/8141.json -g data/train/
```

Gold `gold_attributes` should be filled out and `labels_gold` and all `labels_gold_exists` should be set to true
in `sample_data/annotation/full_data/8141.json`.

## Step 2 - Full annotation

### Excel for annotation

```bash
python brise_plandok/annotation_process/utils/full_annotation_excel_generator.py -d sample_data/annotation/full_data/8141.json -df data/train -o sample_data/annotation/8141_annotation_full.xlsx
```

The output is save to `sample_data/annotation/8141_annotation_full.xlsx`.

### Excel for review

```bash
python brise_plandok/annotation_process/full_annotation_to_review.py -a sample_data/annotation/01/phase2/upload/8141.xlsx sample_data/annotation/02/phase2/upload/8141.xlsx -d sample_data/annotation/full_data/8141.json -g data/train/ -of sample_data/annotation/8141_full_review_XY.xlsx -r
```

The output is save to `sample_data/annotation/8141_labels_review_XY.xlsx`.

### Generate gold after review

```bash
python brise_plandok/annotation_process/full_review_to_gold.py -r sample_data/annotation/8141_full_review_XY.xlsx -d sample_data/annotation/full_data/8141.json -g data/train/
```

Gold `gold_attributes` should be filled out and `Full_gold` and all `full_gold_exists` should be set to true
in `sample_data/annotation/full_data/8141.json`.

## Pre-fill attributes from gold

Use gold to add attributes to documents (-f enables fuzzy sentence matching, which currently ignores digits):

```bash
cat sample_data/json/sample_10.jsonl | python brise_plandok/attrs_from_gold.py -g data/train -f > sample_data/json/sample_10_prefilled.jsonl
```

## Annotation agreement

Calculates the inter-annotator agreement.

```bash
python brise_plandok/annotation/agreement.py -a sample_data/xlsx/asail_annot1.xlsx sample_data/xlsx/asail_annot2.xlsx sample_data/xlsx/asail_gold.xlsx -of output/annotation_output.tsv
```

Constraints

- File names must follow a `<doc_id>_<annotator_name>.xlsx` pattern.
- You must provide exactly one gold annotation in the form of `<doc_id>_gold.xlsx`.
- You must provide at least two non-gold annotations.

You can find a comparative summary in `output/annotation_output.tsv`.