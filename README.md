# brise-plandok

Information extraction from text documents of the zoning plan of the City of Vienna

Work supported by [BRISE-Vienna](https://smartcity.wien.gv.at/en/brise/) (UIA04-081), a European Union Urban Innovative Actions project.


## Requirements

Install the brise_plandok repository:

```
pip install .
```

Installing this repository will also install the `tuw_nlp` repository, a graph-transformation framework. To get to know more, visit https://github.com/recski/tuw-nlp:

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

## References

The rule extraction system is described in the following paper:

Gabor Recski, Björn Lellmann, Adam Kovacs, Allan Hanbury: Explainable rule extraction via semantic graphs (...)


The demo also uses the deontic logic prover described in [this paper](http://www.collegepublications.co.uk/DEON/submission%20Ciabattoni%20Lellmann.pdf)

The preprocessing pipeline relies on the [Stanza](https://stanfordnlp.github.io/stanza/#citing-stanza-in-papers) library
