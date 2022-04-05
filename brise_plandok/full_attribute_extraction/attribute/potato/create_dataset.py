import argparse
import logging
import os
import pickle

from xpotato.dataset.dataset import Dataset
from xpotato.dataset.utils import save_dataframe

from brise_plandok.full_attribute_extraction.attribute.potato.utils import (
    load_data_to_df,
    get_data_folder_path,
    get_sentences,
    get_vocab_for_all_attributes,
)


def create_dataset(dir_path, only_gold, dataset_name, graph_format, cache_dir):
    logging.info(f"Loading data from {dir_path}...")
    data_df = load_data_to_df(dir_path, only_gold)
    logging.info(f"Done, shape: {data_df.shape}")

    logging.info("Creating potato dataset...")
    dataset = Dataset(
        get_sentences(data_df),
        label_vocab=get_vocab_for_all_attributes(),
        lang="de",
        cache_dir=cache_dir,
    )

    logging.info(
        f"Adding {graph_format} graphs (GraphExtractor cache dir is {dataset.extractor.cache_dir})..."
    )
    dataset.set_graphs(dataset.parse_graphs(graph_format=graph_format))

    df = dataset.to_dataframe()
    df.loc[:, "sen_id"] = data_df["sen_id"]
    df.loc[:, "labels"] = data_df["labels"]

    dataset_path = os.path.join(get_data_folder_path(), dataset_name)
    logging.info(f"saving potato dataset to {dataset_path}...")
    save_dataframe(df, dataset_path)
    logging.info("Done.")


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--dir-path")
    parser.add_argument("-o", "--only-gold", action="store_true")
    parser.add_argument("-c", "--cache-dir", default=None)
    parser.add_argument("-g", "--graph")
    parser.add_argument("-n", "--dataset-name")
    return parser.parse_args()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " + "%(module)s (%(lineno)s) - %(levelname)s - %(message)s",
    )
    args = get_args()
    create_dataset(args.dir_path, args.only_gold, args.dataset_name, args.graph, args.cache_dir)
