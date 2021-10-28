# brise-plandok

Information extraction from text documents of the zoning plan of the City of Vienna

Work supported by [BRISE-Vienna](https://smartcity.wien.gv.at/en/brise/) (UIA04-081), a European Union Urban Innovative Actions project.

__The ASAIL2021 branch contains the code in the state presented in our [2021 ASAIL paper](#references)__

## Requirements

Install the brise_plandok repository:

```
pip install .
```

Installing this repository will also install the `tuw_nlp` repository, a graph-transformation framework. To get to know more, visit https://github.com/recski/tuw-nlp.

Ensure that you have at least `Java 8` for the [alto](https://github.com/coli-saar/alto) library.


## Annotated Data Description

See [DATA.md](./DATA.md).

## Attribute extraction

```bash
cat sample_data/json/sample.jsonl | python brise_plandok/extractor.py > output/sample_attr.jsonl
```

### Evalutaion

```bash
cat sample_data/json/sample_10.jsonl | python brise_plandok/eval_attr_ext.py
```

## Rule extraction

To run the rule extraction system described in the [2021 ASAIL paper](#references) on a small annotated sample, run:

```bash
cat sample_data/json/asail.jsonl | python brise_plandok/extractor.py -r > output/asail_rules.jsonl
```

### Evaluation

To perform evaluation on the same sample, run:

```bash
cat sample_data/json/asail.jsonl | python brise_plandok/eval_attr_ext.py -r
```

## Demo

To run the browser-based demo described in the paper (also available [online](https://ir-group.ec.tuwien.ac.at/brise-extract)), first start rule extraction as a service like this:

```
python brise_plandok/services/attribute_extractor.py
```

Then run the frontend with this command:

```
streamlit run brise_plandok/frontend/extract.py
```

To run the prover of our system, also start the prover service from this repository: https://github.com/adaamko/BRISEprover. This will start a small Flask service on port 5007 that will be used by the demo service.

The demo can then be accessed from your web browser at [http://localhost:8501/](http://localhost:8501/)

## Preprocessing

### Input data

All steps described below can be run on the sample documents included in this repository under `sample_data`.

The preprocessed version of all plan documents (as of December 2020) can be
downloaded as [a single JSON file](https://url.tuwien.at/ndnre). If you would like
to customize preprocessing, you can also download the [raw text documents](https://url.tuwien.at/eydmo)

### NLP Pipeline

Extract section structure from raw text and run NLP pipeline (sentence segmentation, tokenization, dependency parsing):

```
python brise_plandok/plandok.py sample_data/txt/*.txt > sample_data/json/sample.jsonl
```

## Annotation process

For details on how the dataset was split for the annotation see the [data split documentation](brise_plandok/data_split/documentation.md).

### Step 1 - Multi-label annotation

#### Excel for annotation

<!-- todo -->

```bash
python brise_plandok/data_split/utils/full_annotation_excel_generator.py -d sample_data/annotation/full_data/8141.json -o sample_data/annotation/8141_annotation_phase2.xlsx
```

#### Excel for review

```bash
python brise_plandok/review/annotation_to_review.py -a sample_data/annotation/01/phase1/upload/8141.xlsx sample_data/annotation/02/phase1/upload/8141.xlsx -d sample_data/annotation/full_data/8141.json -g data/train/ -of sample_data/annotation/8141_review.xlsx -r
```
The output is save to `sample_data/annotation/8141_review.xlsx`.

#### Generate gold after review

```bash
python brise_plandok/review/review_to_gold.py -r sample_data/annotation/8141_review.xlsx -d sample_data/annotation/full_data/8141.json -g sample_data/annotation/full_data
```

Gold `gold_attributes` should be filled out and `labels_gold` and all `labels_gold_exists` should be set to true in `sample_data/annotation/full_data/8141.json`.

### Step 2 - Full annotation

#### Excel for annotation

```bash
python brise_plandok/data_split/utils/full_annotation_excel_generator.py -d sample_data/annotation/full_data/8141.json -o sample_data/annotation/8141_annotation_full.xlsx
```
The output is save to `sample_data/annotation/8141_annotation_full.xlsx`.

#### Excel for review

```bash
# TBD
```

#### Generate gold after review

```bash
# TBD
```

## Pre-fill attributes from gold

<!-- # Todo -->

Use gold to add attributes to documents (-f enables fuzzy sentence matching, which currently ignores digits):

```bash
cat sample_data/json/sample_10.jsonl | python brise_plandok/attrs_from_gold.py -g brise_plandok/review/output -f > sample_data/json/sample_10_prefilled.jsonl
```

## Annotation agreement

Calculates the inter-annotator agreement.

```bash
python brise_plandok/annotation/agreement.py sample_data/xlsx/asail_annot1.xlsx sample_data/xlsx/asail_annot2.xlsx sample_data/xlsx/asail_gold.xlsx
```
Constraints

- File names must follow a `<doc_id>_<annotator_name>.xlsx` pattern.
- You must provide exactly one gold annotation in the form of `<doc_id>_gold.xlsx`.
- You must provide at least two non-gold annotations.

## Development

For development details read more [here](./DEVELOPMENT.md).

## References

The rule extraction system is described in the following paper:

Gabor Recski, Björn Lellmann, Adam Kovacs, Allan Hanbury: Explainable rule extraction via semantic graphs (...)

The demo also uses the deontic logic prover described in [this paper](http://www.collegepublications.co.uk/DEON/submission%20Ciabattoni%20Lellmann.pdf)

The preprocessing pipeline relies on the [Stanza](https://stanfordnlp.github.io/stanza/#citing-stanza-in-papers) library
