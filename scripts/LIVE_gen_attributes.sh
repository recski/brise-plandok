json_folder="$CLOUD_DIR/Shared/BRISE/data/plandok/ana/2021_09/json"
attr_folder="$CLOUD_DIR/Shared/BRISE/data/plandok/ana/2021_09/json_attr"

for doc in "$@"
do
    cat $json_folder/$doc.jsonl | python brise_plandok/extractor.py > $attr_folder/$doc.jsonl
done