# Data description

The data can be found in [data](./data) folder.

### Data representation

The data is stored in json format. You can use [jq](https://stedolan.github.io/jq/manual/) to analyze it from the command line. 

The annotation of the data is still in progress. The annotation process was split into two subtasks:
1. **Multi-label annotation**
In this step the presence of attributes was labeled. Multiplicity was not considered. This step is already finished, although the adjudication of the annotations is only done for 10% of the annotated documents. It means 51 documents - they count currently as gold.
1. **Full annotation**
In this step *values*, *types* and *modalities* are annotated. This process has not been finished yet.

#### Document level attributes

```bash
cat data/train/8303.json | jq '. | keys'
[
  "annotators",
  "full_gold",
  "id",
  "labels_gold",
  "labels_reviewers",
  "sens"
]
```

```bash
cat data/train/8303.json | jq
{
    "id": "8303",
    "sens": {
        ...
    },
    "labels_gold": true,
    "labels_reviewers": [
        "eszti"
    ],
    "annotators": [
        "01",
        "02"
    ],
    "full_gold": false
}

```

##### Explanation

- `id`: id of the document
- `sens`: sentence_id - sentence map
- `labels_gold`: true if gold labels exist for this document (i.e. annotations from step 1 were adjudicated)
- `full_gold`: true if full gold labels with values, types and modalities exist for this document (i.e. annotations from step 2 were adjudicated - currently there are no such documents)
- `annotators`: anonymized annotator information
- `labels_reviewers`: adjudicators for this document 

#### Sentence level attributes

```bash
cat data/train/8303.json | jq '.sens[]' | jq 'select(.id == "8303_20_0")'
{
  "id": "8303_20_0",
  "text": "Für die mit BB1 bezeichneten Grundflächen wird bestimmt: Die Unterbrechung der geschlossenen Bauweise ist zulässig.",
  "modality": null,
  "already_gold_on_annotation": true,
  "labels_gold_exists": true,
  "gold_attributes": {
    "Planzeichen": {
      "name": "Planzeichen",
      "type": null,
      "value": null
    },
    "UnterbrechungGeschlosseneBauweise": {
      "name": "UnterbrechungGeschlosseneBauweise",
      "type": null,
      "value": null
    }
  },
  "gen_attributes_on_annotation": {
    "Planzeichen": {
      "name": "Planzeichen",
      "value": null,
      "type": null
    },
    "UnterbrechungGeschlosseneBauweise": {
      "name": "UnterbrechungGeschlosseneBauweise",
      "value": null,
      "type": null
    }
  },
  "annotated_attributes": {
    "Planzeichen": {
      "annotators": [
        "01",
        "02"
      ]
    },
    "UnterbrechungGeschlosseneBauweise": {
      "annotators": [
        "01",
        "02"
      ]
    }
  },
  "gen_attributes": {},
  "segmentation_error": false,
  "gen_attributes_on_full_annotation": {},
  "full_gold_exists": false
}

```

##### Explanation

General attributes:

- `id`: id of the sentence with format <DOC_ID>\_<SECTION_NUMBER>\_\<SENTENCE_NUMBER>
- `text`: text of the sentence

Attributes relevant for the first annotation step:

- `already_gold_on_annotation`: at the time of the annotation gold labels already existed for this sentence and therefore it was not requested to annotate again
- `labels_gold_exists`: for this sentence gold labels exist
- `gold_attributes`: adjudicated gold attributes for the sentence
- `gen_attributes_on_annotation`: attribute suggestions, which were generated before the annotation using the rule-based system to make the annotation easier and faster
- `annotated_attributes`: attributes given by the annotators with anonymized annotator information
- `segmentation_error`: the text contains a segmentation error (this attribute is set at adjudication time)

Attributes relevant for the second annotation step (this is still an ongoing process, so the list of attributes may not be complete):

- `gen_attributes_on_full_annotation`: full attribute suggestions, which were generated before the annotation using the rule-based system to make the annotation easier and faster
- `full_gold_exists`: the sentence is fully annotated, which means *modality*, *attribute names*, *attribute values* and *attribute types* (currently there's not such sentence in the dataset)

Other attributes:

- `modality`: one of {`prohibition`, `permission`, `obligation`} - not yet annotated
- `gen_attributes`: placeholder for generated attributes, mostly used temporary for evaluation

### Dataset

The dataset contains 371 number of annotated documents, of which 46 ones are gold (adjudicated by an expert reviewer). The data was split into train-valid-test sets following the 80-10-10 rule.

#### Train

```bash
# Training data
cat data/train/*.json | jq '.id' | wc -l
295
# With gold labels
cat data/train/*.json | jq 'select(.labels_gold == true)' | jq '.id' | wc -l
36
```

#### Validation

```bash
# Validation data
cat data/valid/*.json | jq '.id' | wc -l
37
# With gold labels
cat data/valid/*.json | jq 'select(.labels_gold == true)' | jq '.id' | wc -l
5
```

#### Test

```bash
# Test data
cat data/test/*.json | jq '.id' | wc -l
39
# With gold labels
cat data/test/*.json | jq 'select(.labels_gold == true)' | jq '.id' | wc -l
5
```