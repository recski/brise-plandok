doc_tracking="$BRISE_NLP/annotation/2021_09/shuffled_dataset.csv"
ann_folder="$CLOUD_DIR/Shared/BRISE/annotation/data"

python brise_plandok/data_split/assignment_loader.py \
    -d $doc_tracking \
    -af $ann_folder