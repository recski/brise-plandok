# Data description

The data can be found in [data](./data) folder.

## Annotation stages

The data is stored in json format. You can use [jq](https://stedolan.github.io/jq/manual/) to analyze it from the command line. 

The data was annotated in two steps:
1. **Label annotation**  
In this step the presence of attributes was labeled (_attribute names_). Multiplicity was not considered.
2. **Full annotation**  
In this step in addition to _attribute names_, _attribute values_, _attribute types_ and _sentence modalities_ were also annotated.

After the first stage, 46 documents were reviewed, while after the second stage 250. 
The task of the second stage inherently involves the task of the first stage, so the first stage is only mentioned for documentation reasons. 

## Document level attributes

```bash
# Example
cat data/train/8303.json | jq

# Answer
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
  "full_gold": true,
  "full_annotators": [
    "01",
    "02"
  ],
  "full_reviewers": [
    "eszti"
  ]
}
```

### Explanation

```bash
cat data/train/8303.json | jq '. | keys'

# Answer
[
  "annotators",
  "full_annotators",
  "full_gold",
  "full_reviewers",
  "id",
  "labels_gold",
  "labels_reviewers",
  "sens"
]
```

- `id`: id of the document
- `sens`: sentence_id - sentence map
- `labels_gold`: true if gold labels exist for this document (i.e. annotations from stage 1 were reviewed)
- `full_gold`: true if full gold labels with values, types and modalities exist for this document (i.e. annotations from step 2 were reviewed - this is true for all docuemnts)
- `annotators`: anonymized annotators of the 1st stage
- `full_annotators`: anonymized annotators of the 2nd stage (always the same as 1st stage)
- `labels_reviewers`: reviewers of the 1st stage for this document 
- `full_reviewers`: reviewers of the 2nd stage for this document 

## Sentence level attributes

```bash
# Example
cat data/train/8303.json | jq '.sens[]' | jq 'select(.id == "8303_20_0")'

# Answer
{
  "id": "8303_20_0",
  "text": "Für die mit BB1 bezeichneten Grundflächen wird bestimmt: Die Unterbrechung der geschlossenen Bauweise ist zulässig.",
  "gold_modality": "permission",
  "already_gold_on_annotation": true,
  "labels_gold_exists": true,
  "gold_attributes": {
    "Planzeichen": [
      {
        "name": "Planzeichen",
        "value": "BB1",
        "type": "condition"
      }
    ],
    "UnterbrechungGeschlosseneBauweise": [
      {
        "name": "UnterbrechungGeschlosseneBauweise",
        "value": true,
        "type": "content"
      }
    ]
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
  "gen_attributes": {
    "Planzeichen": {
      "value": [
        "BB1"
      ],
      "type": null,
      "name": "Planzeichen"
    },
    "UnterbrechungGeschlosseneBauweise": {
      "value": [
        "True"
      ],
      "type": null,
      "name": "UnterbrechungGeschlosseneBauweise"
    }
  },
  "segmentation_error": false,
  "gen_attributes_on_full_annotation": {
    "Planzeichen": {
      "value": [
        "BB1"
      ],
      "type": "condition",
      "name": "Planzeichen"
    },
    "UnterbrechungGeschlosseneBauweise": {
      "value": [],
      "type": null,
      "name": "UnterbrechungGeschlosseneBauweise"
    }
  },
  "full_gold_exists": true,
  "full_annotated_attributes": {
    "modality": {
      "permission": {
        "annotators": [
          "01",
          "02"
        ]
      }
    },
    "attributes": {
      "Planzeichen": {
        "value": {
          "BB1": {
            "type": {
              "condition": {
                "annotators": [
                  "01",
                  "02"
                ]
              }
            }
          }
        }
      },
      "UnterbrechungGeschlosseneBauweise": {
        "value": {
          "True": {
            "type": {
              "content": {
                "annotators": [
                  "01",
                  "02"
                ]
              }
            }
          }
        }
      }
    }
  },
  "predicted_attributes": {
    "Planzeichen": {
      "value": [
        "BB1"
      ],
      "type": "condition",
      "name": "Planzeichen"
    },
    "UnterbrechungGeschlosseneBauweise": {
      "value": [
        "True"
      ],
      "type": "content",
      "name": "UnterbrechungGeschlosseneBauweise"
    }
  }
}
```

### Explanation

```bash
cat data/train/8303.json | jq '.sens[]' | jq 'select(.id == "8303_20_0") | keys'

# Answer
[
  "already_gold_on_annotation",
  "annotated_attributes",
  "full_annotated_attributes",
  "full_gold_exists",
  "gen_attributes",
  "gen_attributes_on_annotation",
  "gen_attributes_on_full_annotation",
  "gold_attributes",
  "gold_modality",
  "id",
  "labels_gold_exists",
  "predicted_attributes",
  "segmentation_error",
  "text"
]
```

#### General information

- `id`: id of the sentence with format <DOC_ID>\_<SECTION_NUMBER>\_\<SENTENCE_NUMBER>
- `text`: text of the sentence

#### Gold information

- `gold_attributes`: reviewed gold attributes of the sentence
- `gold_modality`: reviwed modality of the sentence, one of {`prohibition`, `permission`, `obligation`} 
- `labels_gold_exists`: true if the sentence was reviewed during the 1st stage (true for 46 docs)
- `full_gold_exists`: true if the sentence was reviewed during the 2nd stage (this is true for all sentences)

#### Annotation information

- `annotated_attributes`: attributes given by the annotators during the 1st stage
- `full_annotated_attributes`: attributes given by the annotators during the 2nd stage
- `already_gold_on_annotation`: at the time of the annotation gold labels already existed for this sentence and therefore it was not requested to annotate again (This attribute was only used for the 1st stage.)
- `gen_attributes_on_annotation`: attribute suggestions, which were generated before the annotation using the rule-based system to make the annotation easier and faster (1st stage)
- `gen_attributes_on_full_annotation`: full attribute suggestions, which were generated before the annotation using the rule-based system to make the annotation easier and faster (2nd stage)

#### Other attributes

- `segmentation_error`: the text contains a segmentation error (this attribute is set at adjudication time)
- `predicted_attributes`: used to store the predictions of our best-performing rule-extraction system
- `gen_attributes`: placeholder for generated attributes, mostly used temporary for evaluation

## Dataset

The dataset contains 250 number of annotated and reviewed (a.k.a. gold) documents. The data was split into train-valid-test sets following the 80-10-10 rule.

### Train

```bash
# Number of docs
cat data/train/*.json | jq '.id' | wc -l
200

# Number of sentences
cat data/train/*.json | jq '.sens[].id' | wc -l
5759

# Number of sentences with attributes
cat data/train/*.json | jq ".sens[] | select(.full_annotated_attributes.attributes != null) | select(.full_annotated_attributes != {}) | select(.full_annotated_attributes | keys | index(\"DON'T ANNOTATE THIS SENTENCE\") | not) | .id" | wc -l
3629

# Sum of all gold attributes
cat data/train/*.json | jq ".sens[] | select(.full_annotated_attributes.attributes != null) | select(.full_annotated_attributes | keys | index(\"DON'T ANNOTATE THIS SENTENCE\") | not) | .full_annotated_attributes.attributes" | jq 'keys[]' | wc -l
8655
```

### Validation

```bash
# Validation data
cat data/valid/*.json | jq '.id' | wc -l
25

# Number of sentences
cat data/valid/*.json | jq '.sens[].id' | wc -l
617

# Number of sentences with attributes
cat data/valid/*.json | jq ".sens[] | select(.full_annotated_attributes.attributes != null) | select(.full_annotated_attributes != {}) | select(.full_annotated_attributes | keys | index(\"DON'T ANNOTATE THIS SENTENCE\") | not) | .id" | wc -l
368

# Sum of all gold attributes
cat data/valid/*.json | jq ".sens[] | select(.full_annotated_attributes.attributes != null) | select(.full_annotated_attributes | keys | index(\"DON'T ANNOTATE THIS SENTENCE\") | not) | .full_annotated_attributes.attributes" | jq 'keys[]' | wc -l
834
```

### Test

```bash
# Test data
cat data/test/*.json | jq '.id' | wc -l
25

# Number of sentences
cat data/test/*.json | jq '.sens[].id' | wc -l
673

# Number of sentences with attributes
cat data/test/*.json | jq ".sens[] | select(.full_annotated_attributes.attributes != null) | select(.full_annotated_attributes != {}) | select(.full_annotated_attributes | keys | index(\"DON'T ANNOTATE THIS SENTENCE\") | not) | .id" | wc -l
424

# Sum of all gold attributes
cat data/test/*.json | jq ".sens[] | select(.full_annotated_attributes.attributes != null) | select(.full_annotated_attributes | keys | index(\"DON'T ANNOTATE THIS SENTENCE\") | not) | .full_annotated_attributes.attributes" | jq 'keys[]' | wc -l
975
```