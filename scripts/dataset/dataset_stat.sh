#!/bin/bash

echo "total"

echo "Number of docs"
cat data/*/*.json | jq '.id' | wc -l

echo "Number of sentences"
cat data/*/*.json | jq '.sens[].id' | wc -l

echo "Number of sentences with gold attributes"
cat data/*/*.json | jq ".sens[] | select(.segmentation_error == false) | select(.gold_attributes != {}) | .id" | wc -l

echo "Sum of all gold attributes"
cat data/*/*.json | jq '.sens[] | select(.segmentation_error == false) | .gold_attributes | keys[]' | wc -l

echo "Gold attribute distribution"
cat data/*/*.json | jq '.sens[] | select(.segmentation_error == false) | .gold_attributes | keys[]' | sort | uniq -c | sort -nr

echo ""

datasets=("train" "valid" "test")

for dataset_name in "${datasets[@]}"; do
    
    echo "$dataset_name"
    
    echo "Number of docs"
    cat data/"$dataset_name"/*.json | jq '.id' | wc -l
    
    echo "Number of sentences"
    cat data/"$dataset_name"/*.json | jq '.sens[].id' | wc -l
    
    echo "Number of sentences with gold attributes"
    cat data/"$dataset_name"/*.json | jq ".sens[] | select(.segmentation_error == false) | select(.gold_attributes != {}) | .id" | wc -l
    
    echo "Sum of all gold attributes"
    cat data/"$dataset_name"/*.json | jq '.sens[] | select(.segmentation_error == false) | .gold_attributes | keys[]' | wc -l
    
    echo "Gold attribute distribution"
    cat data/"$dataset_name"/*.json | jq '.sens[] | select(.segmentation_error == false) | .gold_attributes | keys[]' | sort | uniq -c | sort -nr
    
    echo ""
done

