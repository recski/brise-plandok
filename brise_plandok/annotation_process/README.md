# Dataset creation documentation

## Create folder structure

A specific folder structure is expected for the following scripts to work. Generate a sample structure by calling:

```
./scripts/TEST_gen_structure_for_annotation_process.sh
```

## Shuffle data

This step is already done by the previous script!

First, we create a single file to track assignments and other stats for all documents. The dataset will also be shuffled at this step.

```
python brise_plandok/annotation_process/shuffle_dataset.py -d sample_data/txt > brise_plandok/annotation_process/example/shuffled_dataset.csv
```

## Parse text data to json

Parsing all txt files at once might take some time, so let just parse those we want to assign next.

```
./scripts/TEST_text_to_jsonl.sh 7181 7272 7408 7443 7531 7545 7702 7774 7799 8159
```

The generated files can be found in `brise_plandok/annotation_process/example/json`.

## Generate attributes with rule-based system

We want to pre-fill attributes suggested by our rule-based system to ease the work of the annotators.

```
./scripts/TEST_gen_attributes.sh 7181 7272 7408 7443 7531 7545 7702 7774 7799 8159
```

The generated files can be found in `brise_plandok/annotation_process/example/json_attr`.

## Get a grasp of sentence counts in the next batch

In order to get a good feeling about the next batch size, we should check how many sentences are contained in each doc. 

```
python brise_plandok/annotation_process/sentence_stat.py \
    -d brise_plandok/annotation_process/example/shuffled_dataset.csv \
    -s 6 \
    -jf brise_plandok/annotation_process/example/json_attr
```

## Check existing assignments

We might want to check which assignments for each annotator already exist.

```
python brise_plandok/annotation_process/assignment_loader.py \
    -d brise_plandok/annotation_process/example/shuffled_dataset.csv \
    -af brise_plandok/annotation_process/example/annotators
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

You can find the generated xlsx files in `brise_plandok/annotation_process/example/xlsx` folder.  

Additionally, you can find for each annotator in their download folder (e.g. `brise_plandok/annotation_process/example/annotators/01/phase1/download`) the relevant xlsx files that they have to annotate.

Pre-filled gold data in the excel sheets comes from gold json files provided by the `--data-folder` option.

#### Overwrite existing xlsx files

The generated files can be found in `brise_plandok/annotation_process/example/xlsx`. If the files already exist, no new sheets will be generated. If you want to overwrite the existing ones, use the `-o` flag.

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

To make the assignments final, let us use the `--update` flag. This will update the document tracking file, as well as all the assignment files of the annotators.

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

The document tracking file (`brise_plandok/annotation_process/shuffled_dataset.csv`) and all the assignment files (e.g. `brise_plandok/annotation_process/example/annotators/01/assignment.txt`) have been updated.

## Reset assignments

To reset the assigned documents to an empty state, simply call:

```
./scripts/TEST_gen_structure_for_annotation_process.sh
```

## Notes

The partitioning of the documents can be described as a [multiway number partitioning](https://en.wikipedia.org/wiki/Multiway_number_partitioning) problem. For solving this problem the [Karmakar-Karp algorithm](https://en.wikipedia.org/wiki/Largest_differencing_method) was used. For the implementation we took the [numberpartitioning](https://github.com/fuglede/numberpartitioning) library.