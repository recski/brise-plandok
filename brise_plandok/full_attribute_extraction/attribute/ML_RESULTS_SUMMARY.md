# Summary of attribute extraction models

## Task description
  
Sentence-level multi label classification.

## Data description

We use the [BRISE data](../../../data).

The data contains `371` annotated document from which `46` is reviewed by an adjudicator (a.k.a. gold). The data contains `97` different labels with a great variance in frequency. To learn more about the data, see the [this](../../../DATA.md) page.

For the following experiments we used the top 15 labels of all annotated attributes. Gold labels were used if exists, otherwise we took the (not reviewed) annotated labels.

Top 15 labels (alphabetically sorted) with frequencies in validation set:

| Attribute name | val freq |
| --- | --- |
AbschlussDachMaxBezugGebaeude | 18 |
AnFluchtlinie | 24 |
AnordnungGaertnerischeAusgestaltung | 29 |
BegruenungDach | 23 |
Dachart | 25 |
Flaechen | 43 |
GebaeudeBautyp | 21 |
GebaeudeHoeheArt | 19 |
GebaeudeHoeheMax | 22 |
Planzeichen | 16 |3
VerkehrsflaecheID | 21 |
VonBebauungFreizuhalten | 20 |
VorkehrungBepflanzung | 21 |
WidmungInMehrerenEbenen | 14 |
WidmungUndZweckbestimmung | 62 |

## Machine Learning Methods

By using our prepared train and validation data, 9 different machine Learning based algorithms are implemented and trained. Before training the models, the cleaning process is applied on both train and validation data. Then, those models are used as sklearn classifiers:
1. Nearest Neighbors  
2. Linear SVM 
3. RBF SVM  
4. SGD
5. Decision Tree
6. Random Forest 
7. Neural Network (Multi Layer Perceptron)
8. AdaBoost
9. Naive Bayes

After the training phase, the validation data is used for testing the models. So, the results for each class and models are achieved as below. Precision, recall and f1-score metrics are considered.

### Nearest Neighbors

| Nearest Neighbors | precision |    recall |  f1-score   | support |
| --- | --- | --- | --- | --- | 
| AbschlussDachMaxBezugGebaeude         | 0.95 | 1.00 | 0.97 | 18 |
| AnFluchtlinie                         | 0.77 | 0.71 | 0.74 | 24 |
| AnordnungGaertnerischeAusgestaltung   | 1.00 | 0.55 | 0.71 | 29 |
| BegruenungDach                        | 0.90 | 0.83 | 0.86 | 23 |
| Dachart                               | 0.91 | 0.80 | 0.85 | 25 |
| Flaechen                              | 0.88 | 0.33 | 0.47 | 43 |
| GebaeudeBautyp                        | 0.92 | 0.57 | 0.71 | 21 |
| GebaeudeHoeheArt                      | 0.95 | 0.95 | 0.95 | 19 |
| GebaeudeHoeheMax                      | 1.00 | 0.23 | 0.37 | 22 |
| Planzeichen                           | 0.92 | 0.45 | 0.60 | 163 |
| VerkehrsflaecheID                     | 1.00 | 0.05 | 0.09 | 21 |
| VonBebauungFreizuhalten               | 0.60 | 0.30 | 0.40 | 20 |
| VorkehrungBepflanzung                 | 1.00 | 0.38 | 0.55 | 21 |
| WidmungInMehrerenEbenen               | 1.00 | 0.50 | 0.67 | 14 |
| WidmungUndZweckbestimmung             | 0.86 | 0.19 | 0.32 | 62 |
|  |  |  |  |  | 
|    micro avg |       0.90 |      0.47 |      0.62  |       525 |
|    macro avg |       0.91 |      0.52 |      0.62  |       525 |
| weighted avg |       0.91 |      0.47 |      0.59  |       525 |
|  samples avg |       0.21 |      0.20 |      0.20  |       525 |

### Linear SVM

| Linear SVM  | precision |    recall |  f1-score   | support |
| --- | --- | --- | --- | --- | 
| AbschlussDachMaxBezugGebaeude         | 1.00 |      1.00 |      1.00 |        18 |
| AnFluchtlinie                         | 1.00 |      0.42 |      0.59 |        24 |
| AnordnungGaertnerischeAusgestaltung   | 0.89 |      0.28 |      0.42 |        29 |
| BegruenungDach                        | 0.86 |      0.83 |      0.84 |        23 |
| Dachart                               | 0.95 |      0.72 |      0.82 |        25 |
| Flaechen                              | 1.00 |      0.19 |      0.31 |        43 |
| GebaeudeBautyp                        | 1.00 |      0.05 |      0.09 |        21 |
| GebaeudeHoeheArt                      | 0.94 |      0.89 |      0.92 |        19 |
| GebaeudeHoeheMax                      | 0.00 |      0.00 |      0.00 |        22 |
| Planzeichen                           | 0.94 |      0.83 |      0.88 |       163 |
| VerkehrsflaecheID                     | 1.00 |      0.10 |      0.17 |        21 |
| VonBebauungFreizuhalten               | 0.00 |      0.00 |      0.00 |        20 |
| VorkehrungBepflanzung                 | 1.00 |      0.29 |      0.44 |        21 |
| WidmungInMehrerenEbenen               | 1.00 |      0.64 |      0.78 |        14 |
| WidmungUndZweckbestimmung             | 0.00 |      0.00 |      0.00 |        62 |
|  |  |  |  |  | 
|    micro avg |       0.94 |     0.48 |     0.64 |      525 |
|    macro avg |       0.77 |     0.42 |     0.49 |      525 |
| weighted avg |       0.77 |     0.48 |     0.54 |      525 |
|  samples avg |       0.27 |     0.20 |     0.22 |      525 |

### RBF SVM

| RBF SVM  | precision |    recall |  f1-score   | support |
| --- | --- | --- | --- | --- | 
| AbschlussDachMaxBezugGebaeude         | 1.00 |     1.00 |      1.00 |        18 |
| AnFluchtlinie                         | 0.85 |     0.92 |      0.88 |        24 |
| AnordnungGaertnerischeAusgestaltung   | 0.89 |     0.86 |      0.88 |        29 |
| BegruenungDach                        | 0.88 |     0.91 |      0.89 |        23 |
| Dachart                               | 0.88 |     0.84 |      0.86 |        25 |
| Flaechen                              | 0.80 |     0.77 |      0.79 |        43 |
| GebaeudeBautyp                        | 1.00 |     0.67 |      0.80 |        21 |
| GebaeudeHoeheArt                      | 0.86 |     0.95 |      0.90 |        19 |
| GebaeudeHoeheMax                      | 0.85 |     0.77 |      0.81 |        22 |
| Planzeichen                           | 0.91 |     0.95 |      0.93 |       163 |
| VerkehrsflaecheID                     | 1.00 |     0.81 |      0.89 |        21 |
| VonBebauungFreizuhalten               | 0.79 |     0.75 |      0.77 |        20 |
| VorkehrungBepflanzung                 | 1.00 |     0.95 |      0.98 |        21 |
| WidmungInMehrerenEbenen               | 0.83 |     0.71 |      0.77 |        14 |
| WidmungUndZweckbestimmung             | 0.79 |     0.77 |      0.78 |        62 |
|  |  |  |  |  | 
|    micro avg |      0.88 |      0.86 |     0.87 |      525 |
|    macro avg |      0.89 |      0.84 |     0.86 |      525 |
| weighted avg |      0.88 |      0.86 |     0.87 |      525 |
|  samples avg |      0.36 |      0.35 |     0.35 |      525 |

### SGD

| SGD  | precision |    recall |  f1-score   | support |
| --- | --- | --- | --- | --- | 
| AbschlussDachMaxBezugGebaeude         | 1.00 |      1.00 |      1.00 |        18 |
| AnFluchtlinie                         | 0.79 |      0.79 |      0.79 |        24 |
| AnordnungGaertnerischeAusgestaltung   | 0.87 |      0.93 |      0.90 |        29 |
| BegruenungDach                        | 0.83 |      0.83 |      0.83 |        23 |
| Dachart                               | 0.88 |      0.84 |      0.86 |        25 |
| Flaechen                              | 1.00 |      0.47 |      0.63 |        43 |
| GebaeudeBautyp                        | 1.00 |      0.62 |      0.76 |        21 |
| GebaeudeHoeheArt                      | 0.95 |      0.95 |      0.95 |        19 |
| GebaeudeHoeheMax                      | 0.93 |      0.59 |      0.72 |        22 |
| Planzeichen                           | 0.94 |      0.93 |      0.94 |       163 |
| VerkehrsflaecheID                     | 1.00 |      0.67 |      0.80 |        21 |
| VonBebauungFreizuhalten               | 0.80 |      0.40 |      0.53 |        20 |
| VorkehrungBepflanzung                 | 1.00 |      0.95 |      0.98 |        21 |
| WidmungInMehrerenEbenen               | 0.92 |      0.79 |      0.85 |        14 |
| WidmungUndZweckbestimmung             | 0.81 |      0.27 |      0.41 |        62 |
|  |  |  |  |  | 
|    micro avg |     0.92  |    0.74  |      0.82  |     525 |
|    macro avg |     0.91  |    0.73  |      0.80  |     525 |
| weighted avg |     0.91  |    0.74  |      0.80  |     525 |
|  samples avg |     0.35  |    0.31  |      0.32  |     525 |

### Decision Tree

| Decision Tree  | precision |    recall |  f1-score   | support |
| --- | --- | --- | --- | --- | 
| AbschlussDachMaxBezugGebaeude         | 0.95 |     1.00 |     0.97 |        18 |
| AnFluchtlinie                         | 0.76 |     0.92 |     0.83 |        24 |
| AnordnungGaertnerischeAusgestaltung   | 0.86 |     0.86 |     0.86 |        29 |
| BegruenungDach                        | 0.88 |     1.00 |     0.94 |        23 |
| Dachart                               | 0.85 |     0.88 |     0.86 |        25 |
| Flaechen                              | 0.76 |     0.60 |     0.68 |        43 |
| GebaeudeBautyp                        | 1.00 |     0.71 |     0.83 |        21 |
| GebaeudeHoeheArt                      | 0.90 |     0.95 |     0.92 |        19 |
| GebaeudeHoeheMax                      | 0.77 |     0.77 |     0.77 |        22 |
| Planzeichen                           | 0.86 |     0.94 |     0.90 |       163 |
| VerkehrsflaecheID                     | 0.93 |     0.62 |     0.74 |        21 |
| VonBebauungFreizuhalten               | 0.65 |     0.75 |     0.70 |        20 |
| VorkehrungBepflanzung                 | 1.00 |     1.00 |     1.00 |        21 |
| WidmungInMehrerenEbenen               | 1.00 |     0.71 |     0.83 |        14 |
| WidmungUndZweckbestimmung             | 0.76 |     0.47 |     0.58 |        62 |
|  |  |  |  |  | 
|    micro avg |    0.85 |     0.82 |      0.83 |      525 |
|    macro avg |    0.86 |     0.81 |      0.83 |      525 |
| weighted avg |    0.85 |     0.82 |      0.82 |      525 |
|  samples avg |    0.35 |     0.33 |      0.33 |      525 |

### Random Forest

| Random Forest  | precision |    recall |  f1-score   | support |
| --- | --- | --- | --- | --- | 
| AbschlussDachMaxBezugGebaeude         | 0.00 |      0.00 |      0.00 |        18 |
| AnFluchtlinie                         | 0.00 |      0.00 |      0.00 |        24 |
| AnordnungGaertnerischeAusgestaltung   | 0.00 |      0.00 |      0.00 |        29 |
| BegruenungDach                        | 0.00 |      0.00 |      0.00 |        23 |
| Dachart                               | 0.00 |      0.00 |      0.00 |        25 |
| Flaechen                              | 0.00 |      0.00 |      0.00 |        43 |
| GebaeudeBautyp                        | 0.00 |      0.00 |      0.00 |        21 |
| GebaeudeHoeheArt                      | 0.00 |      0.00 |      0.00 |        19 |
| GebaeudeHoeheMax                      | 0.00 |      0.00 |      0.00 |        22 |
| Planzeichen                           | 0.00 |      0.00 |      0.00 |       163 |
| VerkehrsflaecheID                     | 0.00 |      0.00 |      0.00 |        21 |
| VonBebauungFreizuhalten               | 0.00 |      0.00 |      0.00 |        20 |
| VorkehrungBepflanzung                 | 0.00 |      0.00 |      0.00 |        21 |
| WidmungInMehrerenEbenen               | 0.00 |      0.00 |      0.00 |        14 |
| WidmungUndZweckbestimmung             | 0.00 |      0.00 |      0.00 |        62 |
|  |  |  |  |  | 
|    micro avg |   0.00  |      0.00 |    0.00 |      525 |
|    macro avg |   0.00  |      0.00 |    0.00 |      525 |
| weighted avg |   0.00  |      0.00 |    0.00 |      525 |
|  samples avg |   0.00  |      0.00 |    0.00 |      525 |

### Neural Net

| Neural Net  | precision |    recall |  f1-score   | support |
| --- | --- | --- | --- | --- | 
| AbschlussDachMaxBezugGebaeude         | 1.00 |      1.00 |      1.00 |       18 |
| AnFluchtlinie                         | 1.00 |      0.62 |      0.77 |       24 |
| AnordnungGaertnerischeAusgestaltung   | 0.90 |      0.66 |      0.76 |       29 |
| BegruenungDach                        | 0.94 |      0.70 |      0.80 |       23 |
| Dachart                               | 0.94 |      0.68 |      0.79 |       25 |
| Flaechen                              | 1.00 |      0.37 |      0.54 |       43 |
| GebaeudeBautyp                        | 1.00 |      0.48 |      0.65 |       21 |
| GebaeudeHoeheArt                      | 0.95 |      0.95 |      0.95 |       19 |
| GebaeudeHoeheMax                      | 1.00 |      0.14 |      0.24 |       22 |
| Planzeichen                           | 0.94 |      0.91 |      0.93 |      163 |
| VerkehrsflaecheID                     | 1.00 |      0.38 |      0.55 |       21 |
| VonBebauungFreizuhalten               | 1.00 |      0.05 |      0.10 |       20 |
| VorkehrungBepflanzung                 | 1.00 |      0.62 |      0.76 |       21 |
| WidmungInMehrerenEbenen               | 1.00 |      0.43 |      0.60 |       14 |
| WidmungUndZweckbestimmung             | 0.88 |      0.23 |      0.36 |       62 |
|  |  |  |  |  | 
|    micro avg |   0.95 |     0.62 |      0.75 |       525 |
|    macro avg |   0.97 |     0.55 |      0.65 |       525 |
| weighted avg |   0.96 |     0.62 |      0.70 |       525 |
|  samples avg |   0.32 |     0.26 |      0.28 |       525 |

### AdaBoost

| AdaBoost  | precision |    recall |  f1-score   | support |
| --- | --- | --- | --- | --- | 
| AbschlussDachMaxBezugGebaeude         | 1.00  |      1.00  |      1.00 |       18 |
| AnFluchtlinie                         | 0.78  |      0.75  |      0.77 |       24 |
| AnordnungGaertnerischeAusgestaltung   | 0.84  |      0.90  |      0.87 |       29 |
| BegruenungDach                        | 0.95  |      0.91  |      0.93 |       23 |
| Dachart                               | 0.89  |      0.96  |      0.92 |       25 |
| Flaechen                              | 0.81  |      0.70  |      0.75 |       43 |
| GebaeudeBautyp                        | 0.94  |      0.71  |      0.81 |       21 |
| GebaeudeHoeheArt                      | 0.78  |      0.95  |      0.86 |       19 |
| GebaeudeHoeheMax                      | 0.83  |      0.68  |      0.75 |       22 |
| Planzeichen                           | 0.92  |      0.92  |      0.92 |      163 |
| VerkehrsflaecheID                     | 0.86  |      0.57  |      0.69 |       21 |
| VonBebauungFreizuhalten               | 0.73  |      0.80  |      0.76 |       20 |
| VorkehrungBepflanzung                 | 1.00  |      1.00  |      1.00 |       21 |
| WidmungInMehrerenEbenen               | 0.77  |      0.71  |      0.74 |       14 |
| WidmungUndZweckbestimmung             | 0.78  |      0.69  |      0.74 |       62 |
|  |  |  |  |  | 
|    micro avg |   0.87 |      0.83 |      0.85 |       525 |
|    macro avg |   0.86 |      0.82 |      0.83 |       525 |
| weighted avg |   0.87 |      0.83 |      0.85 |       525 |
|  samples avg |   0.35 |      0.33 |      0.33 |       525 |

### Naive Bayes

| Naive Bayes  | precision |    recall |  f1-score   | support |
| --- | --- | --- | --- | --- | 
| AbschlussDachMaxBezugGebaeude         | 1.00 |     0.89 |     0.94 |       18 |
| AnFluchtlinie                         | 0.72 |     0.75 |     0.73 |       24 |
| AnordnungGaertnerischeAusgestaltung   | 1.00 |     0.72 |     0.84 |       29 |
| BegruenungDach                        | 0.85 |     0.74 |     0.79 |       23 |
| Dachart                               | 0.86 |     0.72 |     0.78 |       25 |
| Flaechen                              | 0.75 |     0.63 |     0.68 |       43 |
| GebaeudeBautyp                        | 1.00 |     0.48 |     0.65 |       21 |
| GebaeudeHoeheArt                      | 0.94 |     0.89 |     0.92 |       19 |
| GebaeudeHoeheMax                      | 0.00 |     0.00 |     0.00 |       22 |
| Planzeichen                           | 0.79 |     0.90 |     0.84 |      163 |
| VerkehrsflaecheID                     | 1.00 |     0.67 |     0.80 |       21 |
| VonBebauungFreizuhalten               | 0.00 |     0.00 |     0.00 |       20 |
| VorkehrungBepflanzung                 | 1.00 |     0.95 |     0.98 |       21 |
| WidmungInMehrerenEbenen               | 1.00 |     0.64 |     0.78 |       14 |
| WidmungUndZweckbestimmung             | 0.76 |     0.35 |     0.48 |       62 |
|  |  |  |  |  | 
|    micro avg |   0.84 |     0.68 |     0.75 |      525 |
|    macro avg |   0.78 |     0.62 |     0.68 |      525 |
| weighted avg |   0.78 |     0.68 |     0.71 |      525 |
|  samples avg |   0.33 |     0.28 |     0.30 |      525 |

---------------------------------------------

### Strengths and weaknesses

According to average test results, there are some pros are cons observed:

➕ The best competitors are NN and RBF. While NN has the highest average score, RBF has well distributed general high scores. 

➗ Random Forest seems not to work for this data. This is a pain-point that should be investigated. 

➖ NN train and test time costs are quite high compare to other models. 


## Neural Networks

Beside classical machine learning models, one NN model is also applied as a multi-layer perceptron. The default settings of sklearn library is used with max 1000 iteration. For detailed information please see the code base. 

For the "basic" NN approaches we implemented both our own models as well as an adaption to the lecture code. 

Our own implementation is based on tensorflow.keras.Sequential() model. We used different Dense layers for the Initial and Initial150 model. Additionally, the Initial150 model contains a Dropout layer (10%) and is computed on 150 epochs. Both models performed pretty decent considering they were "simple" approaches for Neural Networks. Through all evaluation metrics they achieve > 80% with the Initial150 having a slight edge over the Initial model

The Initial Deep model is also a tensorflow.keras.Sequential() model but we tried adding an Embedding + Convolutional Conv1D Layers. It was an interesting idea but the approach failed miserable considering Precision and F1 Score. Here the assumption is that the model learned to "just" predict 0.

For the lecture implementation we had to switch from binary classification to a multilabel classification and also adapt to our own vectorizer which we already used in Milestone1. Some other small changes were made to the code to make it run. The results were quite pleasing but did not reach the levels of our Initial and Inital150 models. The models were computed with cuda (getting it started on the local machine was a bit rough but a great experience!). We did not experiment with the Embedding and Class Imbalance of the lecture implementation.

### Weighted results

| BERT  | Precision | Recall | F1 | Accuracy |
| --- | --- | --- | --- | --- | 
| Initial |  .88| .85| .87 |.82 |
| Initial150 | .89 | .87 | .88 |.86 |
| InitialDeep | .02 | .75 | .04 |.60 |
| Lecture | .73 | .83 | .75 | .69 | 
| LectureDeep |  .76 | .85 | .77 | .69 |

### Strengths and weaknesses (try to find some +/- points)

➕ Powerful tool if used correctly. Achieves good results on basic approaches. Can handle multi-label classification with ease. Can also handle class imbalance to a certain extent

➗ Tuning the models is an exhaustive task. Finding the right combinations can take lots of time. 

➗ Thorough preprocessing could possibly lift our models to new heights (good embeddings, class imbalance handling)

➖ Embedding step did not work as intented. Did take a lot of time without any new gains.

## BERT approach

BERT is a Transformer model trained basically for masked language model and next sentence prediction tasks. With
additional neural network layers it can also work as a classifier.

For pre-trained model we took [deepset/gbert-base](https://huggingface.co/deepset/gbert-base), which is the German cased
version of BERT.

It is possible to fine tune a BERT model for a multi-labelling task by
using [BertForSequenceClassification](https://huggingface.co/docs/transformers/model_doc/bert#transformers.BertForSequenceClassification)
on `problem_type="multi_label_classification"`.

This uses [BCEWithLogitsLoss](https://pytorch.org/docs/stable/generated/torch.nn.BCEWithLogitsLoss.html) for loss
calculation, which combines a Sigmoid layer and BCELoss (Binary Cross Entropy) calculation in one single class. Since
the data exhibits very imbalanced classes, we used a slightly [modified version](./python/bert/brise_bert_model.py) of
BertForSequenceClassification.

### Results

First experiments were done in [this](milestone2/Multi_Label_BERT.ipynb) notebook.

The final training was executed using [this](./python/bert/run.py) script on troubadix, a TU machine with large GPU
power. We trained the model for 26 epochs with `learning rate=1e-03`. After that, even with a decreased learning rate
the results did not get better.

| BERT  | Precision | Recall | F1 | Support |
| --- | --- | --- | --- | --- | 
| AbschlussDachMaxBezugGebaeude         | 0.90 | 1.00 | 0.95 |  18 |
| AnFluchtlinie                         | 0.81 | 0.71 | 0.76 |  24 |
| AnordnungGaertnerischeAusgestaltung   | 1.00 | 0.79 | 0.88 |  29 |
| BegruenungDach                        | 0.90 | 0.78 | 0.84 |  23 |
| Dachart                               | 0.88 | 0.84 | 0.86 |  25 |
| Flaechen                              | 0.62 | 0.47 | 0.53 |  43 |
| GebaeudeBautyp                        | 1.00 | 0.52 | 0.69 |  21 |
| GebaeudeHoeheArt                      | 0.95 | 0.95 | 0.95 |  19 |
| GebaeudeHoeheMax                      | 1.00 | 0.18 | 0.31 |  22 |
| Planzeichen                           | 0.83 | 0.90 | 0.86 | 163 |
| VerkehrsflaecheID                     | 0.88 | 0.71 | 0.79 |  21 |
| VonBebauungFreizuhalten               | 0.60 | 0.60 | 0.60 |  20 |
| VorkehrungBepflanzung                 | 1.00 | 0.95 | 0.98 |  21 |
| WidmungInMehrerenEbenen               | 0.83 | 0.71 | 0.77 |  14 |
| WidmungUndZweckbestimmung             | 0.82 | 0.44 | 0.57 |  62 |
|  |  |  |  |  | 
|    micro avg |  0.84 | 0.73 | 0.78 | 525 |
|    macro avg |  0.87 | 0.70 | 0.76 | 525 |
| weighted avg |  0.85 | 0.73 | 0.76 | 525 |
|  samples avg |  0.34 | 0.30 | 0.31 | 525 |

### Strengths and weaknesses

➕ Apparently the model achieves pretty good scores on lots of tasks.

➖ Takes a lot of time and resources to train.  
➖ An unnecessary big model is used for this task.  
➖ Difficult to debug.  
➖ Unexplainable results.

## Weighted average summary of machine learning models

| Rank (F1) | Approach  | Precision | Recall | F1 |
| --- | --- | --- | --- | --- | 
| (1)  | NN Initial150         |   .89   | **.87** | **.88**   | 
| (2)  | RBF SVM               |   .88   |   .86   |   .87     | 
| (2)  | NN Initial            |   .88   |   .85   |   .87     | 
| (4)  | AdaBoost              |   .87   |   .83   |   .85     | 
| (5)  | Decision Tree         |   .85   |   .82   |   .82     | 
| (6)  | SGD                   |   .91   |   .74   |   .80     | 
| (7)  | NN LectureDeep        |   .76   |   .85   |   .77     | 
| (8)  | BERT                  |   .85   |   .73   |   .76     | 
| (9)  | NN Lecture            |   .73   |   .83   |   .75     | 
| (10) | Naive Bayes           |   .78   |   .68   |   .71     |  
| (11) | NN (MLP)              | **.96** |   .62   |   .70     | 
| (12) | Nearest Neighbours    |   .91   |   .47   |   .59     | 
| (13) | Linear SVM            |   .77   |   .48   |   .54     | 
| (14) | NN InitialDeep        |   .02   |   .75   |   .04     | 
| (15) | Random Forest         |   .00   |   .00   |   .00     | 
