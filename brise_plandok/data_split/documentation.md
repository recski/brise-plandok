# Dataset createion documentation

## Create folder structure

A specific folder structure is expected for the following scripts to work. Genere a sample structure by calling:

```
./scripts/gen_structure_for_data_split.sh
```

## Shuffle data

First, create a single file to track assignments and other stats for all documents. The dataset will also be shuffled at this step.

```
python brise_plandok/data_split/shuffle_dataset.py -d sample_data/txt > brise_plandok/data_split/example/shuffled_dataset.csv
```

## Parse text data to json

Parsing all txt files at once might take some time, so let just parse those we want to assign next.

```
./scripts/text_to_jsonl.sh 7181 7272 7408 7443 7531 7545 7702 7774 7799 8159
```

The generated files can be found in `brise_plandok/data_split/example/json`.

## Generate attributes with rule-based system

We want to prefill attributes suggested by our rule-based system to ease the work of the annotators.

```
./scripts/gen_attributes.sh 7181 7272 7408 7443 7531 7545 7702 7774 7799 8159
```

The generated files can be found in `brise_plandok/data_split/example/json_attr`.

## Get a grasp of sentence counts in the next batch

In order to get a good feeling about the next batch size, we should check how may sentences are contained in each doc. 

```
python brise_plandok/data_split/sentence_stat.py \
    -d brise_plandok/data_split/example/shuffled_dataset.csv \
    -s 6 \
    -jf brise_plandok/data_split/example/json_attr
```

## Check existing assigments

We might want to check what assigments for each annotator already exist.

```
python brise_plandok/data_split/assignment_loader.py \
    -d brise_plandok/data_split/example/shuffled_dataset.csv \
    -af brise_plandok/data_split/example/annotators
```

## Generate a new batch

### Dry-run

You can run this script in dry-run mode (default). It will print out how the next batch would look line without updating the doc-tracking file, the assignment files.

```
python brise_plandok/data_split/generate_batch.py \
    -d brise_plandok/data_split/example/shuffled_dataset.csv \
    -s 6 \
    -jf brise_plandok/data_split/example/json_attr \
    -c 0 \
    -af brise_plandok/data_split/example/annotators
```

### Generate and distribute xlsx files

If you like the output, you can still use the script in dry-run mode, but let it generate the excels. It will also copy the xlsx file to the download folder of the annotators.

```
python brise_plandok/data_split/generate_batch.py \
    -d brise_plandok/data_split/example/shuffled_dataset.csv \
    -s 6 \
    -jf brise_plandok/data_split/example/json_attr \
    -c 0 \
    -af brise_plandok/data_split/example/annotators \
    -xf brise_plandok/data_split/example/xlsx \
    -g
```

#### Overwrite existing xlsx files

The generated files can be found in `brise_plandok/data_split/example/xlsx`. If the files already exist, no new sheets will be generated. If you want to override the existing ones, use the `-o` flag.

```
python brise_plandok/data_split/generate_batch.py \
    -d brise_plandok/data_split/example/shuffled_dataset.csv \
    -s 6 \
    -jf brise_plandok/data_split/example/json_attr \
    -c 0 \
    -af brise_plandok/data_split/example/annotators \
    -xf brise_plandok/data_split/example/xlsx \
    -g \
    -o
```

### Run with update

To make the assignments final, let us use the `--update` flag. This will update the document tracking file, as well as all the assignment files of the annotators.

```
python brise_plandok/data_split/generate_batch.py \
    -d brise_plandok/data_split/example/shuffled_dataset.csv \
    -s 6 \
    -jf brise_plandok/data_split/example/json_attr \
    -c 0 \
    -af brise_plandok/data_split/example/annotators \
    -xf brise_plandok/data_split/example/xlsx \
    -g \
    -o \
    -u
```
