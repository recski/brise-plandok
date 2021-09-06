

annotators_folder="brise_plandok/data_split/example/annotators"
download_folder="download"
assignment_file="assignment.txt"

mkdir brise_plandok/data_split/example
mkdir brise_plandok/data_split/example/json
mkdir brise_plandok/data_split/example/json_attr
mkdir brise_plandok/data_split/example/xlsx
mkdir $annotators_folder

for ann in 01 02 03 04 05 06
do
  mkdir -p $annotators_folder/$ann/$download_folder
  echo "document_id" > $annotators_folder/$ann/$assignment_file
done