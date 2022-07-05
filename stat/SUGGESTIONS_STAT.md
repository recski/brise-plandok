# Pre-filled suggestion statistics

## First stage

Only 46 documents were reviewed at this stage.
### All sentences

```bash
python stat/suggestions_stat.py -f

Number of all sentences: 1372
Number of sentences with suggestions: 676
Ratio of sentences with suggestions: 49.27%

Number of all gold attributes: 1952
Number of correct suggestions: 831
Ratio of correctly suggested gold attributes: 42.57%

Number of all suggested attributes: 1000
Number of wrong suggestions: 169
Ratio of wrong suggestions: 16.90%
```

### Only sentences that contain a rule

```bash
python stat/suggestions_stat.py -r -f

Number of all sentences: 813
Number of sentences with suggestions: 588
Ratio of sentences with suggestions: 72.32%

Number of all gold attributes: 1884
Number of correct suggestions: 791
Ratio of correctly suggested gold attributes: 41.99%

Number of all suggested attributes: 908
Number of wrong suggestions: 117
Ratio of wrong suggestions: 12.89%
```

### Only sentences that contain a rule with reverted post-processed attributes

```bash
python stat/suggestions_stat.py -r -o -f

Number of all sentences: 813
Number of sentences with suggestions: 588
Ratio of sentences with suggestions: 72.32%

Number of all gold attributes: 1884
Number of correct suggestions: 863
Ratio of correctly suggested gold attributes: 45.81%

Number of all suggested attributes: 908
Number of wrong suggestions: 45
Ratio of wrong suggestions: 4.96%
```
## Second stage

In this stage, 46 documents had been reviewed and therefore all the attributes of all the sentences of these 
documents were already gold at the time of the annotation. This means 100% correct suggestions for these 46 documents,
which is included in the statistics below.
### All sentences

```bash
python stat/suggestions_stat.py

Number of all sentences: 7049
Number of sentences with suggestions: 4706
Ratio of sentences with suggestions: 66.76%

Number of all gold attributes: 9673
Number of correct suggestions: 7392
Ratio of correctly suggested gold attributes: 76.42%

Number of all suggested attributes: 10566
Number of wrong suggestions: 3174
Ratio of wrong suggestions: 30.04%
```

### Only sentences that contain a rule

```bash
python stat/suggestions_stat.py -r

Number of all sentences: 3994
Number of sentences with suggestions: 3925
Ratio of sentences with suggestions: 98.27%

Number of all gold attributes: 9221
Number of correct suggestions: 7121
Ratio of correctly suggested gold attributes: 77.23%

Number of all suggested attributes: 9604
Number of wrong suggestions: 2483
Ratio of wrong suggestions: 25.85%
```

### Only sentences that contain a rule with reverted post-processed attributes

```bash
python stat/suggestions_stat.py -r -o

Number of all sentences: 3994
Number of sentences with suggestions: 3925
Ratio of sentences with suggestions: 98.27%

Number of all gold attributes: 9221
Number of correct suggestions: 8148
Ratio of correctly suggested gold attributes: 88.36%

Number of all suggested attributes: 9604
Number of wrong suggestions: 1456
Ratio of wrong suggestions: 15.16%
```
## Combined

For the 46 documents already gold after the first stage, the first stage statistics is taken, whereas for 
all other documents the second stage statistics is taken.
### All sentences

```bash
python stat/suggestions_stat.py -c

Number of all sentences: 7049
Number of sentences with suggestions: 4528
Ratio of sentences with suggestions: 64.24%

Number of all gold attributes: 9673
Number of correct suggestions: 6657
Ratio of correctly suggested gold attributes: 68.82%

Number of all suggested attributes: 9643
Number of wrong suggestions: 2986
Ratio of wrong suggestions: 30.97%
```

### Only sentences that contain a rule

```bash
python stat/suggestions_stat.py -r -c

Number of all sentences: 3994
Number of sentences with suggestions: 3719
Ratio of sentences with suggestions: 93.11%

Number of all gold attributes: 9221
Number of correct suggestions: 6395
Ratio of correctly suggested gold attributes: 69.35%

Number of all suggested attributes: 8664
Number of wrong suggestions: 2269
Ratio of wrong suggestions: 26.19%
```

### Only sentences that contain a rule with reverted post-processed attributes

```bash
python stat/suggestions_stat.py -r -o -c

Number of all sentences: 3994
Number of sentences with suggestions: 3719
Ratio of sentences with suggestions: 93.11%

Number of all gold attributes: 9221
Number of correct suggestions: 7276
Ratio of correctly suggested gold attributes: 78.91%

Number of all suggested attributes: 8664
Number of wrong suggestions: 1388
Ratio of wrong suggestions: 16.02%
```
