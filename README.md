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

## Rule extraction

To run the rule extraction system described in the [2021 ASAIL paper](#references) on a small annotated sample, run:

```
cat sample_data/json/asail.jsonl | python brise_plandok/extractor.py -r > output/asail_rules.jsonl
```

### Evaluation

To perform evaluation on the same sample, run:

```
cat sample_data/json/asail.jsonl | python brise_plandok/eval_attr_ext.py -r
```

### Demo

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

## Full pipeline

### Data

All steps described below can be run on the sample documents included in this repository under `sample_data`.

The preprocessed version of all plan documents (as of December 2020) can be
downloaded as [a single JSON file](https://url.tuwien.at/ndnre). If you would like
to customize preprocessing, you can also download the [raw text documents](https://url.tuwien.at/eydmo)

### Preprocessing

Extract section structure from raw text and run NLP pipeline (sentence segmentation, tokenization, dependency parsing):

```
python brise_plandok/plandok.py sample_data/txt/*.txt > sample_data/json/sample.jsonl
```

Run attribute extraction:

```
cat sample_data/json/sample.jsonl | python brise_plandok/extractor.py > output/sample_attr.jsonl
```

To run the rule extraction system of the ASAIL paper, add the `-r` command-line switch to the above command.

### Evaluation

Evaluate attribute extraction on annotated sample of 10 documents:

```
cat sample_data/json/sample_10.jsonl | python brise_plandok/eval_attr_ext.py
```

### Annotation

To generate `xlsx` files for annotation, run the following command:

```
sed "5q;d" sample_data/json/asail.jsonl | python brise_plandok/extractor.py -r | python brise_plandok/convert.py -i JSON -o XLSX -of output/asail.xlsx
```

The generated excel sheet will be placed under output/asail.xlsx. The samples are annotated by our rule-based system and then can be used by the human annotators as well.

To generate `json` files from the annotated samples, you can run:

```
cat sample_data/csv/sample_10_annotated.csv | python brise_plandok/convert.py -i CSV_FULL > sample_10_annotated.json
```

If labels change in the `BRISE.xlsx` template file, new excel file from a fully or partially annotated excel can be generated with the command:

```
python brise_plandok/convert.py -i XLSX -if sample_data/xlsx/asail.xlsx -o XLSX -of output/asail.xlsx
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

## References

The rule extraction system is described in the following paper:

Gabor Recski, Björn Lellmann, Adam Kovacs, Allan Hanbury: Explainable rule extraction via semantic graphs (...)

The demo also uses the deontic logic prover described in [this paper](http://www.collegepublications.co.uk/DEON/submission%20Ciabattoni%20Lellmann.pdf)

The preprocessing pipeline relies on the [Stanza](https://stanfordnlp.github.io/stanza/#citing-stanza-in-papers) library
