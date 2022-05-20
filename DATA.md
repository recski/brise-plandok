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

Dataset was split by calling the following script:
```bash
./scripts/dataset/split_data.sh 
```

### Run dataset statistics

```bash
./scripts/dataset/dataset_stat.sh

# Answer
total
Number of docs
250
Number of sentences
7049
Number of sentences with gold attributes
4238
Sum of all gold attributes
9665
Gold attribute distribution
   1844 "Planzeichen"
    641 "Widmung"
    400 "VerkehrsflaecheID"
    292 "AnordnungGaertnerischeAusgestaltung"
    282 "Dachart"
    276 "AnFluchtlinie"
    274 "VorkehrungBepflanzung"
    242 "GebaeudeHoeheArt"
    220 "BegruenungDach"
    219 "WidmungInMehrerenEbenen"
    219 "AbschlussDachMaxBezugGebaeude"
    217 "BBAllgemein"
    213 "ErrichtungGebaeude"
    207 "GehsteigbreiteMin"
    200 "GebaeudeHoeheMaxAbsolut"
    189 "GesamtePlangebiet"
    177 "StrassenbreiteMin"
    175 "GebaeudeBautyp"
    157 "Nutzungsart"
    154 "UnterbrechungGeschlosseneBauweise"
    152 "AufbautenZulaessig"
    144 "VonBebauungFreizuhalten"
    132 "DachneigungMax"
    116 "Bauklasse"
    115 "EinfriedungAusgestaltung"
    109 "DurchgangBreite"
    107 "BebauteFlaecheMaxProzentual"
    103 "AusnahmeGaertnerischAuszugestaltende"
    100 "StrassenbreiteMax"
     97 "BauweiseID"
     96 "DurchgangHoehe"
     91 "VolumenUndUmbaubarerRaum"
     85 "UnterirdischeBaulichkeiten"
     81 "Struktureinheit"
     80 "Stockwerk"
     77 "EinfriedungHoeheGesamt"
     71 "DachflaecheMin"
     69 "BebauteFlaecheMax"
     67 "VerbotFensterZuOeffentlichenVerkehrsflaechen"
     65 "BebauteFlaecheMaxNebengebaeude"
     61 "VorstehendeBauelementeAusladungMax"
     61 "VerbotWohnung"
     56 "EinfriedungLage"
     54 "AnOeffentlichenVerkehrsflaechen"
     51 "OeffentlicheVerkehrsflaecheBreiteMin"
     50 "AnordnungGaertnerischeAusgestaltungProzentual"
     49 "StrassenbreiteVonBis"
     48 "EinfriedungZulaessig"
     48 "BebauteFlaecheMin"
     46 "VorbautenVerbot"
     44 "AnlageZumEinstellenVorhanden"
     36 "EinleitungNiederschlagswaesser"
     36 "AnteilDachbegruenung"
     32 "VerbotStaffelung"
     32 "GebaeudeHoeheMaxWN"
     27 "StellplatzImNiveauZulaessig"
     27 "ArkadeHoehe"
     20 "FBOKMinimumWohnungen"
     19 "MaxAnzahlGeschosseOberirdisch"
     19 "AnzahlGebaeudeMax"
     18 "StellplatzregulativUmfangMinimumRelativ"
     18 "InSchutzzone"
     17 "Massengliederung"
     16 "BauklasseVIHoeheMax"
     15 "StellplatzMax"
     14 "BauklasseVIHoeheMin"
     14 "AbschlussDachMaxBezugGelaende"
     13 "Kleinhaeuser"
     13 "DachneigungMin"
     11 "TechnischeAufbautenHoeheMax"
     11 "StellplatzregulativUmfangMaximumRelativ"
     11 "OberflaecheBestimmungP"
     11 "MaxAnzahlDachgeschosse"
     11 "DurchfahrtHoehe"
     10 "VorbautenBeschraenkung"
     10 "VerbotBueroGeschaeftsgebaeude"
      9 "GaragengebaeudeAusfuehrung"
      8 "StellplatzregulativUmfangMaximumAbsolut"
      8 "GebaeudeHoeheMin"
      7 "MindestraumhoeheEG"
      7 "BestimmmungenFuerHochhausUndGrossbauvorhaben"
      6 "HoehenlageGrundflaeche"
      6 "Geschaeftsstrassen"
      6 "DurchfahrtBreite"
      5 "GebaeudeEinschraenkungP"
      5 "AusnahmeVonWohnungenUnzulaessig"
      4 "HochhausZulaessigGemaessBB"
      3 "MaxAnzahlGeschosseOberirdischOhneDachgeschoss"
      2 "ZulaessigeGeschossanzahlEinkaufszentrum"
      2 "Einbautrasse"
      1 "VerbotStellplaetzeUndParkgebaeude"
      1 "VerbotAufenthaltsraum"
      1 "AnteilBaumbepflanzung"

train
Number of docs
200
Number of sentences
5491
Number of sentences with gold attributes
3318
Sum of all gold attributes
7714
Gold attribute distribution
   1441 "Planzeichen"
    542 "Widmung"
    337 "VerkehrsflaecheID"
    227 "Dachart"
    221 "AnFluchtlinie"
    213 "VorkehrungBepflanzung"
    213 "AnordnungGaertnerischeAusgestaltung"
    186 "BBAllgemein"
    185 "GebaeudeHoeheArt"
    175 "ErrichtungGebaeude"
    174 "WidmungInMehrerenEbenen"
    172 "GebaeudeHoeheMaxAbsolut"
    171 "BegruenungDach"
    168 "AbschlussDachMaxBezugGebaeude"
    164 "GehsteigbreiteMin"
    151 "StrassenbreiteMin"
    150 "GesamtePlangebiet"
    135 "GebaeudeBautyp"
    131 "AufbautenZulaessig"
    126 "UnterbrechungGeschlosseneBauweise"
    117 "Nutzungsart"
    109 "VonBebauungFreizuhalten"
    103 "DachneigungMax"
     96 "Bauklasse"
     94 "EinfriedungAusgestaltung"
     88 "StrassenbreiteMax"
     87 "AusnahmeGaertnerischAuszugestaltende"
     86 "DurchgangBreite"
     85 "BebauteFlaecheMaxProzentual"
     78 "BauweiseID"
     77 "DurchgangHoehe"
     67 "Stockwerk"
     64 "EinfriedungHoeheGesamt"
     62 "Struktureinheit"
     61 "VolumenUndUmbaubarerRaum"
     57 "UnterirdischeBaulichkeiten"
     56 "DachflaecheMin"
     54 "VorstehendeBauelementeAusladungMax"
     54 "VerbotFensterZuOeffentlichenVerkehrsflaechen"
     52 "BebauteFlaecheMax"
     51 "BebauteFlaecheMaxNebengebaeude"
     50 "VerbotWohnung"
     47 "AnOeffentlichenVerkehrsflaechen"
     45 "StrassenbreiteVonBis"
     45 "EinfriedungLage"
     43 "AnordnungGaertnerischeAusgestaltungProzentual"
     41 "VorbautenVerbot"
     39 "EinfriedungZulaessig"
     35 "AnlageZumEinstellenVorhanden"
     34 "OeffentlicheVerkehrsflaecheBreiteMin"
     31 "GebaeudeHoeheMaxWN"
     30 "AnteilDachbegruenung"
     26 "VerbotStaffelung"
     25 "BebauteFlaecheMin"
     24 "EinleitungNiederschlagswaesser"
     23 "StellplatzImNiveauZulaessig"
     18 "AnzahlGebaeudeMax"
     17 "ArkadeHoehe"
     15 "StellplatzMax"
     15 "Massengliederung"
     15 "FBOKMinimumWohnungen"
     14 "MaxAnzahlGeschosseOberirdisch"
     14 "InSchutzzone"
     13 "BauklasseVIHoeheMax"
     11 "StellplatzregulativUmfangMinimumRelativ"
     11 "DachneigungMin"
     11 "BauklasseVIHoeheMin"
     10 "TechnischeAufbautenHoeheMax"
     10 "OberflaecheBestimmungP"
     10 "AbschlussDachMaxBezugGelaende"
      9 "Kleinhaeuser"
      9 "GaragengebaeudeAusfuehrung"
      9 "DurchfahrtHoehe"
      8 "VerbotBueroGeschaeftsgebaeude"
      8 "MaxAnzahlDachgeschosse"
      8 "GebaeudeHoeheMin"
      7 "VorbautenBeschraenkung"
      6 "StellplatzregulativUmfangMaximumRelativ"
      6 "StellplatzregulativUmfangMaximumAbsolut"
      6 "Geschaeftsstrassen"
      6 "BestimmmungenFuerHochhausUndGrossbauvorhaben"
      5 "MindestraumhoeheEG"
      4 "HoehenlageGrundflaeche"
      4 "DurchfahrtBreite"
      4 "AusnahmeVonWohnungenUnzulaessig"
      3 "MaxAnzahlGeschosseOberirdischOhneDachgeschoss"
      3 "GebaeudeEinschraenkungP"
      2 "ZulaessigeGeschossanzahlEinkaufszentrum"
      2 "HochhausZulaessigGemaessBB"
      1 "VerbotStellplaetzeUndParkgebaeude"
      1 "VerbotAufenthaltsraum"
      1 "Einbautrasse"

valid
Number of docs
25
Number of sentences
875
Number of sentences with gold attributes
515
Sum of all gold attributes
1064
Gold attribute distribution
    228 "Planzeichen"
     59 "Widmung"
     42 "AnordnungGaertnerischeAusgestaltung"
     34 "GebaeudeHoeheArt"
     33 "VorkehrungBepflanzung"
     32 "VerkehrsflaecheID"
     28 "AbschlussDachMaxBezugGebaeude"
     26 "AnFluchtlinie"
     25 "Dachart"
     24 "ErrichtungGebaeude"
     23 "VolumenUndUmbaubarerRaum"
     23 "GebaeudeBautyp"
     23 "BegruenungDach"
     21 "Nutzungsart"
     21 "GehsteigbreiteMin"
     20 "WidmungInMehrerenEbenen"
     19 "VonBebauungFreizuhalten"
     19 "GebaeudeHoeheMaxAbsolut"
     19 "BBAllgemein"
     18 "GesamtePlangebiet"
     16 "UnterirdischeBaulichkeiten"
     14 "Struktureinheit"
     14 "DurchgangBreite"
     13 "DachneigungMax"
     12 "UnterbrechungGeschlosseneBauweise"
     12 "DurchgangHoehe"
     12 "Bauklasse"
     11 "BebauteFlaecheMax"
     11 "BauweiseID"
     10 "StrassenbreiteMin"
     10 "BebauteFlaecheMin"
     10 "BebauteFlaecheMaxProzentual"
     10 "AusnahmeGaertnerischAuszugestaltende"
      9 "EinfriedungAusgestaltung"
      8 "Stockwerk"
      8 "BebauteFlaecheMaxNebengebaeude"
      8 "AufbautenZulaessig"
      7 "VerbotFensterZuOeffentlichenVerkehrsflaechen"
      7 "StrassenbreiteMax"
      7 "OeffentlicheVerkehrsflaecheBreiteMin"
      7 "EinleitungNiederschlagswaesser"
      7 "ArkadeHoehe"
      6 "EinfriedungLage"
      6 "DachflaecheMin"
      6 "AnOeffentlichenVerkehrsflaechen"
      5 "VerbotWohnung"
      5 "StellplatzregulativUmfangMinimumRelativ"
      5 "MaxAnzahlGeschosseOberirdisch"
      5 "EinfriedungZulaessig"
      5 "EinfriedungHoeheGesamt"
      4 "VorstehendeBauelementeAusladungMax"
      4 "StellplatzregulativUmfangMaximumRelativ"
      4 "InSchutzzone"
      4 "AnordnungGaertnerischeAusgestaltungProzentual"
      4 "AnlageZumEinstellenVorhanden"
      3 "StrassenbreiteVonBis"
      3 "Kleinhaeuser"
      3 "BauklasseVIHoeheMin"
      3 "BauklasseVIHoeheMax"
      3 "AbschlussDachMaxBezugGelaende"
      2 "VorbautenVerbot"
      2 "VerbotStaffelung"
      2 "StellplatzregulativUmfangMaximumAbsolut"
      2 "StellplatzImNiveauZulaessig"
      2 "MindestraumhoeheEG"
      2 "FBOKMinimumWohnungen"
      2 "DachneigungMin"
      1 "VorbautenBeschraenkung"
      1 "VerbotBueroGeschaeftsgebaeude"
      1 "TechnischeAufbautenHoeheMax"
      1 "OberflaecheBestimmungP"
      1 "Massengliederung"
      1 "HoehenlageGrundflaeche"
      1 "HochhausZulaessigGemaessBB"
      1 "Einbautrasse"
      1 "AusnahmeVonWohnungenUnzulaessig"
      1 "AnzahlGebaeudeMax"
      1 "AnteilDachbegruenung"
      1 "AnteilBaumbepflanzung"

test
Number of docs
25
Number of sentences
683
Number of sentences with gold attributes
405
Sum of all gold attributes
887
Gold attribute distribution
    175 "Planzeichen"
     40 "Widmung"
     37 "AnordnungGaertnerischeAusgestaltung"
     31 "VerkehrsflaecheID"
     30 "Dachart"
     29 "AnFluchtlinie"
     28 "VorkehrungBepflanzung"
     26 "BegruenungDach"
     25 "WidmungInMehrerenEbenen"
     23 "GebaeudeHoeheArt"
     23 "AbschlussDachMaxBezugGebaeude"
     22 "GehsteigbreiteMin"
     21 "GesamtePlangebiet"
     19 "Nutzungsart"
     17 "GebaeudeBautyp"
     16 "VonBebauungFreizuhalten"
     16 "UnterbrechungGeschlosseneBauweise"
     16 "StrassenbreiteMin"
     16 "DachneigungMax"
     14 "ErrichtungGebaeude"
     13 "BebauteFlaecheMin"
     13 "AufbautenZulaessig"
     12 "UnterirdischeBaulichkeiten"
     12 "EinfriedungAusgestaltung"
     12 "BebauteFlaecheMaxProzentual"
     12 "BBAllgemein"
     10 "OeffentlicheVerkehrsflaecheBreiteMin"
      9 "GebaeudeHoeheMaxAbsolut"
      9 "DurchgangBreite"
      9 "DachflaecheMin"
      8 "EinfriedungHoeheGesamt"
      8 "BauweiseID"
      8 "Bauklasse"
      7 "VolumenUndUmbaubarerRaum"
      7 "DurchgangHoehe"
      6 "VerbotWohnung"
      6 "VerbotFensterZuOeffentlichenVerkehrsflaechen"
      6 "BebauteFlaecheMaxNebengebaeude"
      6 "BebauteFlaecheMax"
      6 "AusnahmeGaertnerischAuszugestaltende"
      5 "Struktureinheit"
      5 "StrassenbreiteMax"
      5 "Stockwerk"
      5 "EinleitungNiederschlagswaesser"
      5 "EinfriedungLage"
      5 "AnteilDachbegruenung"
      5 "AnlageZumEinstellenVorhanden"
      4 "VerbotStaffelung"
      4 "EinfriedungZulaessig"
      3 "VorstehendeBauelementeAusladungMax"
      3 "VorbautenVerbot"
      3 "MaxAnzahlDachgeschosse"
      3 "FBOKMinimumWohnungen"
      3 "ArkadeHoehe"
      3 "AnordnungGaertnerischeAusgestaltungProzentual"
      2 "VorbautenBeschraenkung"
      2 "StellplatzregulativUmfangMinimumRelativ"
      2 "StellplatzImNiveauZulaessig"
      2 "GebaeudeEinschraenkungP"
      2 "DurchfahrtHoehe"
      2 "DurchfahrtBreite"
      1 "VerbotBueroGeschaeftsgebaeude"
      1 "StrassenbreiteVonBis"
      1 "StellplatzregulativUmfangMaximumRelativ"
      1 "Massengliederung"
      1 "Kleinhaeuser"
      1 "HoehenlageGrundflaeche"
      1 "HochhausZulaessigGemaessBB"
      1 "GebaeudeHoeheMaxWN"
      1 "BestimmmungenFuerHochhausUndGrossbauvorhaben"
      1 "AnOeffentlichenVerkehrsflaechen"
      1 "AbschlussDachMaxBezugGelaende"
```