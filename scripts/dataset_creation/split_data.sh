#!/bin/bash

INPUT_DIR=$BRISE_NLP/annotation/2021_09/full_data/
OUTPUT_DIR=data
mkdir "$OUTPUT_DIR/train"
mkdir "$OUTPUT_DIR/valid"
mkdir "$OUTPUT_DIR/test"

cnt=0

while IFS= read -r line
do
    if ((cnt < 200))
    then
        cp "$INPUT_DIR/$line.json" $OUTPUT_DIR/train/
    elif ((cnt < 225))
    then
        cp "$INPUT_DIR/$line.json" $OUTPUT_DIR/valid/
    else
        cp "$INPUT_DIR/$line.json" $OUTPUT_DIR/test/
    fi
    ((cnt=cnt+1))
done < <(shuf --random-source=<(yes 42) scripts/dataset/gold_ids.txt)

