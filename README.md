# brise-plandok

Information extraction from text documents of the zoning plan of the City of Vienna

Work supported by [BRISE-Vienna](https://smartcity.wien.gv.at/en/brise/) (UIA04-081), a European Union Urban Innovative Actions project.

__The [asail2021](https://github.com/recski/brise-plandok/tree/asail2021) tag contains the code in the state presented in our [2021 ASAIL paper](#references)__

## Requirements

Install the brise_plandok repository:

```bash
pip install .
```

Installing this repository will also install the `tuw_nlp` repository, a graph-transformation framework. To get to know more, visit https://github.com/recski/tuw-nlp.

Ensure that you have at least `Java 8` for the [alto](https://github.com/coli-saar/alto) library.


## Annotated Data Description

See [DATA.md](./DATA.md).

## Extraction service

```bash
# Start service
 python brise_plandok/services/full_extractor.py -d <DATA_DIR>
```

You can now reach the service by calling the url `http://localhost:5005/extract/<doc_id>`.

## Demo for attribute names only

To run the browser-based demo described in the paper (also available [online](https://ir-group.ec.tuwien.ac.at/brise-extract)), first start rule extraction as a service like this:

```bash
python brise_plandok/services/attribute_extractor.py
```

Then run the frontend with this command:

```bash
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

```bash
python brise_plandok/plandok.py sample_data/txt/*.txt > sample_data/json/sample.jsonl
```

## Attribute extraction with [POTATO](https://github.com/adaamko/POTATO)

For attribution extraction experiments with [POTATO](https://github.com/adaamko/POTATO), see [here](brise_plandok/full_attribute_extraction/attribute/potato/README.md).

## Annotation process

For details about annotation process, see [here](ANNOTATION.md).

## Development

For development details read more [here](./DEVELOPMENT.md).

## References

The rule extraction system is described in the following paper:

Gabor Recski, Björn Lellmann, Adam Kovacs, Allan Hanbury: Explainable rule extraction via semantic graphs (...)

The demo also uses the deontic logic prover described in [this paper](http://www.collegepublications.co.uk/DEON/submission%20Ciabattoni%20Lellmann.pdf)

The preprocessing pipeline relies on the [Stanza](https://stanfordnlp.github.io/stanza/#citing-stanza-in-papers) library
