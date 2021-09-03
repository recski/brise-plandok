json_folder="sample_data/data_split/json"
attr_folder="sample_data/data_split/json_attr"

for doc in "$@"
do
    cat $json_folder/$doc.jsonl | python brise_plandok/extractor.py > $attr_folder/$doc.jsonl
done