#!/bin/bash

datasets=("train" "valid" "test")

for dataset_name in "${datasets[@]}"; do
    
    echo "$dataset_name"
    
    echo "Number of docs"
    cat data/"$dataset_name"/*.json | jq '.id' | wc -l
    
    echo "Number of sentences"
    cat data/"$dataset_name"/*.json | jq '.sens[].id' | wc -l
    
    echo "Number of sentences with attributes"
    cat data/"$dataset_name"/*.json | jq ".sens[] | select(.full_annotated_attributes.attributes != null) | select(.full_annotated_attributes != {}) | select(.full_annotated_attributes | keys | index(\"DON'T ANNOTATE THIS SENTENCE\") | not) | .id" | wc -l
    
    echo "Sum of all gold attributes"
    cat data/"$dataset_name"/*.json | jq ".sens[] | select(.full_annotated_attributes.attributes != null) | select(.full_annotated_attributes | keys | index(\"DON'T ANNOTATE THIS SENTENCE\") | not) | .full_annotated_attributes.attributes" | jq 'keys[]' | wc -l
    
    echo "Gold attribute distribution"
    cat data/"$dataset_name"/*.json | jq 'select(.full_gold == true)' | jq '.sens[].gold_attributes | keys[]' | sort | uniq -c | sort -nr
    
    echo ""
done

