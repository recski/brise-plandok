# Rules statistics

## Total

```bash
python brise_plandok/stat/rule_stat.py -d data/train data/valid data/test

Number of all rules: 3994
Mean number of rules per document: 15.976
Median number of rules per document: 14
Stdev of rules per document: 11.9304975204028
Mean number of sens per document: 28.196
Median number of sens per document: 26
Stdev of sens per document: 14.548547174876205
Number of all attributes: 9221
Average number of attributes per rule: 2.309
Median of number of attributes per rule: 2
```

## Train

```bash
python brise_plandok/stat/rule_stat.py -d data/train

Number of all rules: 3154
Mean number of rules per document: 15.77
Median number of rules per document: 13
Stdev of rules per document: 12.559290541048581
Mean number of sens per document: 27.455
Median number of sens per document: 25
Stdev of sens per document: 14.528709232405989
Number of all attributes: 7397
Average number of attributes per rule: 2.345
Median of number of attributes per rule: 2
```

## Valid

```bash
python brise_plandok/stat/rule_stat.py -d data/valid

Number of all rules: 465
Mean number of rules per document: 18.6
Median number of rules per document: 18
Stdev of rules per document: 9.840392946083673
Mean number of sens per document: 35
Median number of sens per document: 32
Stdev of sens per document: 17.141567411801446
Number of all attributes: 981
Average number of attributes per rule: 2.110
Median of number of attributes per rule: 2
```

## Test

```bash
python brise_plandok/stat/rule_stat.py -d data/test

Number of all rules: 375
Mean number of rules per document: 15
Median number of rules per document: 16
Stdev of rules per document: 7.968688725254614
Mean number of sens per document: 27.32
Median number of sens per document: 28
Stdev of sens per document: 9.915139938498095
Number of all attributes: 843
Average number of attributes per rule: 2.248
Median of number of attributes per rule: 2
```

