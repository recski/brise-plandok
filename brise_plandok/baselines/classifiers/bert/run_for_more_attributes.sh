#!/bin/bash

declare -a attrs

while getopts 'a:e:l:r:g:' flag; do
    case "${flag}" in
    a) attrs+=("$OPTARG") ;;
    e) epoch=${OPTARG} ;;
    l) log_folder=${OPTARG} ;;
    r) lr=${OPTARG} ;;
    g) gpu=${OPTARG} ;;
    *)
        print_usage
        exit 1
        ;;
    esac
done

for attr in "${attrs[@]}";
do
    echo "Train for $attr"
    CUDA_VISIBLE_DEVICES=$gpu python classifiers/bert/run.py -l $log_folder -lr $lr -e $epoch -a $attr
done