# Pre-filled suggestion statistics

## All sentences

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

## Only sentences that contain a rule

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

## Only sentences that contain a rule with reverted post-processed attributes

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
