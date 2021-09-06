txt_folder="$CLOUD_DIR/Shared/BRISE/data/plandok/txt"
json_folder="$CLOUD_DIR/Shared/BRISE/data/plandok/ana/2021_09/json"

for doc in "$@"
do
    # To do: use cache again when bug is fixed
    rm cache/nlp_cache.json

    python brise_plandok/plandok.py $txt_folder/$doc.txt > $json_folder/$doc.jsonl
done

