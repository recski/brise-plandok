#!/bin/bash

echo "# Pre-filled suggestion statistics" 
echo ""

##########################################################

echo "## First stage"
echo ""
echo "Only 46 documents were reviewed at this stage."

echo "### All sentences"
echo ""
echo "\`\`\`bash"
echo "python stat/suggestions_stat.py -f"
echo ""
python stat/suggestions_stat.py -f
echo "\`\`\`"
echo ""

echo "### Only sentences that contain a rule"
echo ""
echo "\`\`\`bash"
echo "python stat/suggestions_stat.py -r -f"
echo ""
python stat/suggestions_stat.py -r -f
echo "\`\`\`"
echo ""

echo "### Only sentences that contain a rule with reverted post-processed attributes"
echo ""
echo "\`\`\`bash"
echo "python stat/suggestions_stat.py -r -o -f"
echo ""
python stat/suggestions_stat.py -r -o -f
echo "\`\`\`"

##########################################################

echo "## Second stage"
echo ""
echo "In this stage, 46 documents had been reviewed and therefore all the attributes of all the sentences of these 
documents were already gold at the time of the annotation. This means 100% correct suggestions for these 46 documents,
which is included in the statistics below."

echo "### All sentences"
echo ""
echo "\`\`\`bash"
echo "python stat/suggestions_stat.py"
echo ""
python stat/suggestions_stat.py
echo "\`\`\`"
echo ""

echo "### Only sentences that contain a rule"
echo ""
echo "\`\`\`bash"
echo "python stat/suggestions_stat.py -r"
echo ""
python stat/suggestions_stat.py -r
echo "\`\`\`"
echo ""

echo "### Only sentences that contain a rule with reverted post-processed attributes"
echo ""
echo "\`\`\`bash"
echo "python stat/suggestions_stat.py -r -o"
echo ""
python stat/suggestions_stat.py -r -o
echo "\`\`\`"

##########################################################

echo "## Combined"
echo ""
echo "For the 46 documents already gold after the first stage, the first stage statistics is taken, whereas for 
all other documents the second stage statistics is taken."

echo "### All sentences"
echo ""
echo "\`\`\`bash"
echo "python stat/suggestions_stat.py -c"
echo ""
python stat/suggestions_stat.py -c
echo "\`\`\`"
echo ""

echo "### Only sentences that contain a rule"
echo ""
echo "\`\`\`bash"
echo "python stat/suggestions_stat.py -r -c"
echo ""
python stat/suggestions_stat.py -r -c
echo "\`\`\`"
echo ""

echo "### Only sentences that contain a rule with reverted post-processed attributes"
echo ""
echo "\`\`\`bash"
echo "python stat/suggestions_stat.py -r -o -c"
echo ""
python stat/suggestions_stat.py -r -o -c
echo "\`\`\`"
