json_folder="brise_plandok/annotation_process/example/json"
attr_folder="brise_plandok/annotation_process/example/json_attr"

for doc in "$@"
do
    cat $json_folder/$doc.jsonl | python brise_plandok/asail/extractor.py > $attr_folder/$doc.jsonl
done