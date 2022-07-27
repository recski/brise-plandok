#!/bin/bash

while getopts 'a:j::' flag; do
    case "${flag}" in
    a) attr_log=${OPTARG} ;;
    j) joint_log=${OPTARG} ;;
    *)
        print_usage
        exit 1
        ;;
    esac
done


echo "# BERT Report"

echo "## Train all rule based attributes simultaneously"

echo ""
echo "TODO $joint_log"
echo ""

echo "## Train all rule based attributes separately"

echo ""
echo "~ 4 hours / attribute, 40 attributes -> 160 hours (~ 1 week)"
echo ""

python classifiers/bert/evaluate.py -l "$attr_log" -d valid
