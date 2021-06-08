# brise-plandok

Information extraction from text documents of the zoning plan of the City of Vienna

Work supported by [BRISE-Vienna](https://smartcity.wien.gv.at/en/brise/) (UIA04-081), a European Union Urban Innovative Actions project.


## Requirements

Install the `tuw_nlp` repository:

...

Install the brise_plandok repository:

```
pip install .
```

Create subdirectories for output and cache:

```
mkdir -p output cache
```

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

The demo can then be accessed from your web browser at [http://localhost:8501/](http://localhost:8501/)


## Full pipeline

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



## References

The rule extraction system is described in the following paper:

Gabor Recski, Björn Lellmann, Adam Kovacs, Allan Hanbury: Explainable rule extraction via semantic graphs (...)


The demo also uses the deontic logic prover described in [this paper](http://www.collegepublications.co.uk/DEON/submission%20Ciabattoni%20Lellmann.pdf)

The preprocessing pipeline relies on the [Stanza](https://stanfordnlp.github.io/stanza/#citing-stanza-in-papers) library
