txt_folder="sample_data/txt"
shuffled_dataset_file="brise_plandok/annotation_process/example/shuffled_dataset.csv"
annotators_folder="brise_plandok/annotation_process/example/annotators"
download_folder="download"
assignment_txt="assignment.txt"
assignment_xlsx="assignment.xlsx"

rm -r brise_plandok/annotation_process/example/xlsx/

mkdir brise_plandok/annotation_process/example
mkdir brise_plandok/annotation_process/example/json
mkdir brise_plandok/annotation_process/example/json_attr
mkdir brise_plandok/annotation_process/example/xlsx
mkdir brise_plandok/annotation_process/example/full_data
mkdir $annotators_folder


for ann in 01 02 03 04 05 06
do
  for phase in phase1 phase2
  do
    rm -r $annotators_folder/$ann/$phase/$download_folder
    mkdir -p $annotators_folder/$ann/$phase/$download_folder
    echo "doc_id" > $annotators_folder/$ann/$phase/$assignment_txt
    ssconvert $annotators_folder/$ann/$phase/$assignment_txt $annotators_folder/$ann/$phase/$download_folder/$assignment_xlsx
  done
done

python brise_plandok/annotation_process/shuffle_dataset.py -d $txt_folder > $shuffled_dataset_file