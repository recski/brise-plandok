#!/bin/bash

echo "# Rules statistics" 
echo ""

##########################################################

echo "## Total"
echo ""
echo "\`\`\`bash"
echo "python brise_plandok/stat/rule_stat.py -d data/train data/valid data/test"
echo ""
python brise_plandok/stat/rule_stat.py -d data/train data/valid data/test
echo "\`\`\`"
echo ""


echo "## Train"
echo ""
echo "\`\`\`bash"
echo "python brise_plandok/stat/rule_stat.py -d data/train"
echo ""
python brise_plandok/stat/rule_stat.py -d data/train
echo "\`\`\`"
echo ""


echo "## Valid"
echo ""
echo "\`\`\`bash"
echo "python brise_plandok/stat/rule_stat.py -d data/valid"
echo ""
python brise_plandok/stat/rule_stat.py -d data/valid
echo "\`\`\`"
echo ""


echo "## Test"
echo ""
echo "\`\`\`bash"
echo "python brise_plandok/stat/rule_stat.py -d data/test"
echo ""
python brise_plandok/stat/rule_stat.py -d data/test
echo "\`\`\`"
echo ""


