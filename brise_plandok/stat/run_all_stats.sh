#!/bin/bash

./brise_plandok/stat/distribution_attr.sh > brise_plandok/stat/docs/DISTRIBUTION_ATTR.md
./brise_plandok/stat/distribution_mod.sh > brise_plandok/stat/docs/DISTRIBUTION_MOD.md
./brise_plandok/stat/distribution_type.sh > brise_plandok/stat/docs/DISTRIBUTION_TYPE.md
python brise_plandok/stat/types_and_values_per_attr.py > brise_plandok/stat/docs/TYEPES_AND_VALUES_PER_ATTR.md
./brise_plandok/stat/rule_stat.sh > brise_plandok/stat/docs/RULE_STAT.md
./brise_plandok/stat/suggestion_stat.sh > brise_plandok/stat/docs/SUGGESTIONS_STAT.md
python brise_plandok/stat/annotator_performance_attr.py > brise_plandok/stat/docs/ANNOTATOR_PERFORMANCE_ATTR.md
python brise_plandok/stat/annotator_performance_mod.py > brise_plandok/stat/docs/ANNOTATOR_PERFORMANCE_MOD.md
python brise_plandok/stat/annotator_performance_type.py > brise_plandok/stat/docs/ANNOTATOR_PERFORMANCE_TYPE.md
python brise_plandok/stat/agreement_attr.py > brise_plandok/stat/docs/AGREEMENT_ATTR.md
python brise_plandok/stat/agreement_mod.py > brise_plandok/stat/docs/AGREEMENT_MOD.md
python brise_plandok/stat/agreement_type.py > brise_plandok/stat/docs/AGREEMENT_TYPE.md
./brise_plandok/stat/segmentation_error_rate.sh > brise_plandok/stat/docs/SEGMENTATION_ERROR_RATE.md
