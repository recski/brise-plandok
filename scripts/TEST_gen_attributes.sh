json_folder="brise_plandok/data_split/example/json"
attr_folder="brise_plandok/data_split/example/json_attr"

for doc in "$@"
do
    cat $json_folder/$doc.jsonl | python brise_plandok/extractor.py > $attr_folder/$doc.jsonl
done