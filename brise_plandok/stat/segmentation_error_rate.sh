#!/bin/bash

echo "# Segmentation error rate"
echo ""
echo "\`\`\`bash"

echo "total"

echo "Number of sentences"
cat data/*/*.json | jq '.sens[].id' | wc -l

echo "Number of sentences with segmentation error"
cat data/*/*.json | jq '.sens[] | select(.segmentation_error == true) | .id' | wc -l

echo ""

datasets=("train" "valid" "test")

for dataset_name in "${datasets[@]}"; do
    
    echo "$dataset_name"
    
    echo "Number of sentences"
    cat data/"$dataset_name"/*.json | jq '.sens[].id' | wc -l
    
    echo "Number of sentences with segmentation error"
    cat data/"$dataset_name"/*.json | jq '.sens[] | select(.segmentation_error == true) | .id' | wc -l
    
    echo ""
    
done

echo "\`\`\`"
echo ""