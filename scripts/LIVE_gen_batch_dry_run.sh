doc_tracking="$BRISE_NLP/annotation/2021_09/shuffled_dataset.csv"
attr_folder="$CLOUD_DIR/Shared/BRISE/data/plandok/ana/2021_09/json_attr"
ann_folder="$CLOUD_DIR/Shared/BRISE/annotation/data"

python brise_plandok/data_split/generate_batch.py \
    -d $doc_tracking \
    -s $1 \
    -jf $attr_folder \
    -c $2 \
    -af $ann_folder