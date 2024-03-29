# Annotation process 

## Create folder structure

A specific folder structure is expected for the following scripts to work. Generate a sample structure by calling:

```
./scripts/TEST_gen_structure_for_annotation_process.sh
```

You can find the generated folders [here](./example).

## Shuffle data

This step is already done by the previous script!

First, we create a single file to track assignments and other stats for all documents. The dataset will also be shuffled at this step.

To execute this step separately, run:

```
python brise_plandok/annotation_process/shuffle_dataset.py -d sample_data/txt > brise_plandok/annotation_process/example/shuffled_dataset.csv
```

## Parse text data to json

Parsing all txt files at once might take some time, so let just parse those we want to assign next.

```
./scripts/TEST_text_to_jsonl.sh 7181 7272 7408 7443 7531 7545 7702 7774 7799 8159
```

The generated files can be found in the [json](./example/json) folder.

## Generate attributes with rule-based system

We want to pre-fill attributes suggested by our rule-based system to ease the work of the annotators.

```
./scripts/TEST_gen_attributes.sh 7181 7272 7408 7443 7531 7545 7702 7774 7799 8159
```

The generated files can be found in the [json_attr](./example/json_attr) folder. The generated attributes are contained in the `gen_attributes` field.

## Get a grasp of sentence counts in the next batch

In order to get a good feeling about the next batch size, we should check how many sentences are contained in each doc. 

```
python brise_plandok/annotation_process/sentence_stat.py \
    -d brise_plandok/annotation_process/example/shuffled_dataset.csv \
    -s 6 \
    -jf brise_plandok/annotation_process/example/json_attr \
    -p 1
```

The `assigned` and `assigned_2 ` columns show whether the document is already assigned for the first phase and the second phase, respectively. 

## Check existing assignments

We might want to check which assignments for each annotator already exist.

```
python brise_plandok/annotation_process/assignment_loader.py \
    -d brise_plandok/annotation_process/example/shuffled_dataset.csv \
    -af brise_plandok/annotation_process/example/annotators \
    -p 1
```

For phase 2:
```
python brise_plandok/annotation_process/assignment_loader.py \
    -d brise_plandok/annotation_process/example/shuffled_dataset.csv \
    -af brise_plandok/annotation_process/example/annotators \
    -p 2
```

## Generate a new batch

If `--phase` option is not specified, it defaults to phase number 1.

### Dry-run

You can run this script in dry-run mode (default). It will print out how the next batch would look line without updating the doc-tracking file and the assignment files.

```
python brise_plandok/annotation_process/generate_batch.py \
    -d brise_plandok/annotation_process/example/shuffled_dataset.csv \
    -s 6 \
    -jf brise_plandok/annotation_process/example/json_attr \
    -c 0 \
    -af brise_plandok/annotation_process/example/annotators
```

### Generate and distribute xlsx files

If you like the output, you can still use the script in dry-run mode, but let it generate the excels. It will also copy the xlsx file to the download folder of the annotators.

```
python brise_plandok/annotation_process/generate_batch.py \
    -d brise_plandok/annotation_process/example/shuffled_dataset.csv \
    -s 6 \
    -jf brise_plandok/annotation_process/example/json_attr \
    -c 0 \
    -af brise_plandok/annotation_process/example/annotators \
    -xf brise_plandok/annotation_process/example/xlsx \
    -df brise_plandok/annotation_process/example/full_data \
    -g
```

You can find the generated xlsx files in the [xlsx](./example/xlsx) folder.  

Additionally, you can find for each annotator in their download folder (e.g. for annotator [01](./example/annotators/01/phase1/download)) the relevant xlsx files that they have to annotate.

Pre-filled gold data in the excel sheets comes from gold json files provided by the `--data-folder` option.

#### Overwrite existing xlsx files

The generated files can be found in [xlsx](./example/xlsx) folder. If the files already exist, no new sheets will be generated. If you want to overwrite the existing ones, use the `-o` flag.

```
python brise_plandok/annotation_process/generate_batch.py \
    -d brise_plandok/annotation_process/example/shuffled_dataset.csv \
    -s 6 \
    -jf brise_plandok/annotation_process/example/json_attr \
    -c 0 \
    -af brise_plandok/annotation_process/example/annotators \
    -xf brise_plandok/annotation_process/example/xlsx \
    -df brise_plandok/annotation_process/example/full_data \
    -g \
    -o
```

### Run with update

To make the assignments final, use the `--update` flag. This will update the document tracking file, as well as all the assignment files of the annotators.

```
python brise_plandok/annotation_process/generate_batch.py \
    -d brise_plandok/annotation_process/example/shuffled_dataset.csv \
    -s 6 \
    -jf brise_plandok/annotation_process/example/json_attr \
    -c 0 \
    -af brise_plandok/annotation_process/example/annotators \
    -xf brise_plandok/annotation_process/example/xlsx \
    -df brise_plandok/annotation_process/example/full_data \
    -g \
    -o \
    -u \
    -p 1
```

For phase 2:
```
python brise_plandok/annotation_process/generate_batch.py \
    -d brise_plandok/annotation_process/example/shuffled_dataset.csv \
    -s 6 \
    -jf brise_plandok/annotation_process/example/json_attr \
    -c 0 \
    -af brise_plandok/annotation_process/example/annotators \
    -xf brise_plandok/annotation_process/example/xlsx \
    -df brise_plandok/annotation_process/example/full_data \
    -g \
    -o \
    -u \
    -p 2
```

The [document tracking file](./example/shuffled_dataset.csv) and all the assignment files (e.g. for annotator [01](./example/annotators/01/phase1/assignment.txt)) have been updated.

You can check the status again by calling the script from the [Check existing assignments](#check-existing-assignments) section.

## Reset assignments

To reset the assigned documents to an empty state, simply call:

```
./scripts/TEST_gen_structure_for_annotation_process.sh
```

## Check annotator progress

Let's reset the environment and distribute all the 10 documents for both phases.

```bash
./scripts/TEST_annotator_process_setup.sh
```

Now you can check how many docuemnts have already been uploaded:

```bash
# For phase 1
python brise_plandok/annotation_process/annotator_progress.py \
    -af brise_plandok/annotation_process/example/annotators \
    -p 1

# For phase 2
python brise_plandok/annotation_process/annotator_progress.py \
    -af brise_plandok/annotation_process/example/annotators \
    -p 2
```

Let's pretend that the annotators have already done some of their work. This means that they have already uploaded some of the annotated documents to their own uploaded folder (e.g. for annotator [01](./example/annotators/01/phase1/upload)). Let's imitate this by copying some content from the download folders to the upload folders.

```bash
./scripts/TEST_populate_upload_folders.sh
```

Now we can call the `annotator_progress` scripts again to see the progress. If you define the document tracking file, you can even find out how many documents have been annotated once and twice.

```bash
# For phase 1
python brise_plandok/annotation_process/annotator_progress.py \
    -dt brise_plandok/annotation_process/example/shuffled_dataset.csv \
    -af brise_plandok/annotation_process/example/annotators \
    -p 1

# For phase 2
python brise_plandok/annotation_process/annotator_progress.py \
    -dt brise_plandok/annotation_process/example/shuffled_dataset.csv \
    -af brise_plandok/annotation_process/example/annotators \
    -p 2
```

## Overview of Excel sheet generation

Call these scripts from repository root.

### Stage 1 - Multi-label annotation

#### Excel for annotation

```bash
python brise_plandok/annotation_process/utils/label_annotation_excel_generator.py -d sample_data/annotation/full_data/8141.json -o sample_data/annotation/8141_annotation_labels.xlsx
```

The result is saved [here](../../sample_data/annotation/8141_annotation_labels.xlsx).

#### Excel for review

```bash
python brise_plandok/annotation_process/labels_annotation_to_review.py -a sample_data/annotation/01/phase1/upload/8141.xlsx sample_data/annotation/02/phase1/upload/8141.xlsx -d sample_data/annotation/full_data/8141.json -g sample_data/annotation/full_data -of sample_data/annotation/8141_labels_review_XY.xlsx -r
```

The result is saved [here](../../sample_data/annotation/8141_labels_review_XY.xlsx).

This time the [json file](../../sample_data/annotation/full_data/8141.json) is also updated with the name of the reviewer, which is in this case `XY`.

#### Generate gold after review

```bash
python brise_plandok/annotation_process/labels_review_to_gold.py -r sample_data/annotation/8141_labels_review_XY.xlsx -d sample_data/annotation/full_data/8141.json -g sample_data/annotation/full_data -i -e
```

Gold `gold_attributes` should be filled out and `labels_gold` and all `labels_gold_exists` should be set to true
in the [json file](../../sample_data/annotation/full_data/8141.json).

### Stage 2 - Full annotation

Before executing the next scripts, please revert the [json file](../../sample_data/annotation/full_data/8141.json).

#### Excel for annotation

```bash
python brise_plandok/annotation_process/utils/full_annotation_excel_generator.py -d sample_data/annotation/full_data/8141.json -df sample_data/annotation/full_data -o sample_data/annotation/8141_annotation_full.xlsx
```

The result is saved [here](../../sample_data/annotation/8141_annotation_full.xlsx).

#### Excel for review

```bash
python brise_plandok/annotation_process/full_annotation_to_review.py -a sample_data/annotation/01/phase2/upload/8141.xlsx sample_data/annotation/02/phase2/upload/8141.xlsx -d sample_data/annotation/full_data/8141.json -g sample_data/annotation/full_data -of sample_data/annotation/8141_full_review_XY.xlsx -r
```

The result is saved [here](../../sample_data/annotation/8141_full_review_XY.xlsx).

#### Generate gold after review

Before executing the following script, please revert the previously generated review sheet [file](../../sample_data/annotation/8141_full_review_XY.xlsx).

```bash
python brise_plandok/annotation_process/full_review_to_gold.py -r sample_data/annotation/8141_full_review_XY.xlsx -d sample_data/annotation/full_data/8141.json -g sample_data/annotation/full_data -i -e
```

Gold `gold_attributes` should be filled out and `Full_gold` and all `full_gold_exists` should be set to true
in the [json file](../../sample_data/annotation/full_data/8141.json).

## Notes

The partitioning of the documents can be described as a [multiway number partitioning](https://en.wikipedia.org/wiki/Multiway_number_partitioning) problem. For solving this problem the [Karmakar-Karp algorithm](https://en.wikipedia.org/wiki/Largest_differencing_method) was used. For the implementation we took the [numberpartitioning](https://github.com/fuglede/numberpartitioning) library.