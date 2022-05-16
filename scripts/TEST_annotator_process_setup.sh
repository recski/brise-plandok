# Regenerate folder structure
./scripts/TEST_gen_structure_for_annotation_process.sh

# Distribute for phase 1
python brise_plandok/annotation_process/generate_batch.py \
    -d brise_plandok/annotation_process/example/shuffled_dataset.csv \
    -s 10 \
    -jf brise_plandok/annotation_process/example/json_attr \
    -c 0 \
    -af brise_plandok/annotation_process/example/annotators \
    -xf brise_plandok/annotation_process/example/xlsx \
    -df brise_plandok/annotation_process/example/full_data \
    -g \
    -o \
    -u \
    -p 1

# Distribute for phase 2
python brise_plandok/annotation_process/generate_batch.py \
    -d brise_plandok/annotation_process/example/shuffled_dataset.csv \
    -s 10 \
    -jf brise_plandok/annotation_process/example/json_attr \
    -c 0 \
    -af brise_plandok/annotation_process/example/annotators \
    -xf brise_plandok/annotation_process/example/xlsx \
    -df brise_plandok/annotation_process/example/full_data \
    -g \
    -o \
    -u \
    -p 2

