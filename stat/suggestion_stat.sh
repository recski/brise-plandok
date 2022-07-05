#!/bin/bash

echo "# Pre-filled suggestion statistics" 
echo ""

echo "## All sentences"
echo ""
echo "\`\`\`bash"
echo "python stat/suggestions_stat.py"
echo ""
python stat/suggestions_stat.py
echo "\`\`\`"
echo ""

echo "## Only sentences that contain a rule"
echo ""
echo "\`\`\`bash"
echo "python stat/suggestions_stat.py -r"
echo ""
python stat/suggestions_stat.py -r
echo "\`\`\`"
echo ""

echo "## Only sentences that contain a rule with reverted post-processed attributes"
echo ""
echo "\`\`\`bash"
echo "python stat/suggestions_stat.py -r -o"
echo ""
python stat/suggestions_stat.py -r -o
echo "\`\`\`"
