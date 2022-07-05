#!/bin/bash

echo "# Attribute distribution"
echo ""
echo "\`\`\`bash"

echo "total"

echo "Number of docs"
cat data/*/*.json | jq '.id' | wc -l

echo "Number of sentences"
cat data/*/*.json | jq '.sens[].id' | wc -l

echo "Number of sentences with gold attributes (w/o segmentation_error, counted once per sentence)"
cat data/*/*.json | jq ".sens[] | select(.segmentation_error == false) | select(.gold_attributes != {}) | .id" | wc -l

echo "Sum of all gold attributes (w/o segmentation_error, counted once per sentence)"
cat data/*/*.json | jq '.sens[] | select(.segmentation_error == false) | .gold_attributes | keys[]' | wc -l

echo "Gold attribute distribution (w/o segmentation_error, counted once per sentence)"
cat data/*/*.json | jq '.sens[] | select(.segmentation_error == false) | .gold_attributes | keys[]' | sort | uniq -c | sort -nr

echo ""

datasets=("train" "valid" "test")

for dataset_name in "${datasets[@]}"; do
    
    echo "$dataset_name"
    
    echo "Number of docs"
    cat data/"$dataset_name"/*.json | jq '.id' | wc -l
    
    echo "Number of sentences"
    cat data/"$dataset_name"/*.json | jq '.sens[].id' | wc -l
    
    echo "Number of sentences with gold attributes (w/o segmentation_error, counted once per sentence)"
    cat data/"$dataset_name"/*.json | jq ".sens[] | select(.segmentation_error == false) | select(.gold_attributes != {}) | .id" | wc -l
    
    echo "Sum of all gold attributes (w/o segmentation_error, counted once per sentence)"
    cat data/"$dataset_name"/*.json | jq '.sens[] | select(.segmentation_error == false) | .gold_attributes | keys[]' | wc -l
    
    echo "Gold attribute distribution (w/o segmentation_error, counted once per sentence)"
    cat data/"$dataset_name"/*.json | jq '.sens[] | select(.segmentation_error == false) | .gold_attributes | keys[]' | sort | uniq -c | sort -nr
    
    echo ""
done

echo "\`\`\`"
echo ""