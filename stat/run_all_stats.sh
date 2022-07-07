#!/bin/bash

./stat/attribute_distribution.sh > stat/docs/ATTRIBUTE_DISTRIBUTION.md
./stat/type_distribution.sh > stat/docs/TYPE_DISTRIBUTION.md
python stat/types_and_values_per_attr.py > stat/docs/TYEPES_AND_VALUES_PER_ATTR.md
./stat/modality_distribution.sh > stat/docs/MODALITY_DISTRIBUTION.md
./stat/rule_stat.sh > stat/docs/RULE_STAT.md
./stat/suggestion_stat.sh > stat/docs/SUGGESTIONS_STAT.md
python stat/annotator_mod_stat.py > stat/docs/ANNOTATOR_MOD_STAT.md
python stat/annotator_attr_stat.py > stat/docs/ANNOTATOR_ATTR_STAT.md
