#!/bin/bash

./brise_plandok/stat/attribute_distribution.sh > brise_plandok/stat/docs/ATTRIBUTE_DISTRIBUTION.md
./brise_plandok/stat/type_distribution.sh > brise_plandok/stat/docs/TYPE_DISTRIBUTION.md
python brise_plandok/stat/types_and_values_per_attr.py > brise_plandok/stat/docs/TYEPES_AND_VALUES_PER_ATTR.md
./brise_plandok/stat/modality_distribution.sh > brise_plandok/stat/docs/MODALITY_DISTRIBUTION.md
./brise_plandok/stat/rule_stat.sh > brise_plandok/stat/docs/RULE_STAT.md
./brise_plandok/stat/suggestion_stat.sh > brise_plandok/stat/docs/SUGGESTIONS_STAT.md
python brise_plandok/stat/annotator_mod_stat.py > brise_plandok/stat/docs/ANNOTATOR_MOD_STAT.md
python brise_plandok/stat/annotator_attr_stat.py > brise_plandok/stat/docs/ANNOTATOR_ATTR_STAT.md
python brise_plandok/stat/agreement_mod.py > brise_plandok/stat/docs/AGREEMENT_MOD.md
python brise_plandok/stat/agreement_attr.py > brise_plandok/stat/docs/AGREEMENT_ATTR.md
python brise_plandok/stat/agreement_type.py > brise_plandok/stat/docs/AGREEMENT_TYPE.md
python brise_plandok/stat/annotator_type_stat.py > brise_plandok/stat/docs/ANNOTATOR_TYPE_STAT.md
