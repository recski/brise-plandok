txt_folder="sample_data/txt"
json_folder="sample_data/data_split/json"

for doc in "$@"
do
    # To do: use cache again when bug is fixed
    rm cache/nlp_cache.json

    python brise_plandok/plandok.py $txt_folder/$doc.txt > $json_folder/$doc.jsonl
done

