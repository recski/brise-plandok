doc_tracking="$BRISE_NLP/annotation/2021_09/shuffled_dataset.csv"
attr_folder="$CLOUD_DIR/Shared/BRISE/data/plandok/ana/2021_09/json_attr"

if [ -d "$attr_folder" ] && [ -f "$doc_tracking" ]; then
  python brise_plandok/data_split/sentence_stat.py \
    -d $doc_tracking \
    -s $1 \
    -jf $attr_folder
fi