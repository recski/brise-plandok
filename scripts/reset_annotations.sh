

annotators_folder="brise_plandok/data_split/example/annotators"
download_folder="download"
assignment_file="assignment.txt"

for ann in 01 02 03 04 05 06
do
  rm $annotators_folder/$ann/$download_folder/*
  echo "document_id" > $annotators_folder/$ann/$assignment_file
done

python brise_plandok/data_split/shuffle_dataset.py -d sample_data/txt > brise_plandok/data_split/example/shuffled_dataset.csv