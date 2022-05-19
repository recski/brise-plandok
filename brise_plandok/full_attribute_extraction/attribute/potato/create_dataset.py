import argparse
import logging
import os

from xpotato.dataset.utils import save_dataframe

from brise_plandok.full_attribute_extraction.attribute.potato.utils import (
    get_data_folder_path,
    create_potato_dataset,
    add_graphs_to_dataset,
)
from brise_plandok.full_attribute_extraction.attribute.utils.load_data import load_data_to_df


def create_dataset(dir_path, only_gold, dataset_name, graph_format, cache_dir):
    logging.info(f"Loading data from {dir_path}...")
    df = load_data_to_df(dir_path, only_gold)
    logging.info(f"Done, shape: {df.shape}")

    logging.info("Creating potato dataset...")
    dataset = create_potato_dataset(df, cache_dir)

    logging.info(
        f"Adding {graph_format} graphs (GraphExtractor cache dir is {dataset.extractor.cache_dir})..."
    )
    add_graphs_to_dataset(dataset, graph_format)

    potato_df = dataset.to_dataframe()
    potato_df.loc[:, "sen_id"] = df["sen_id"]
    potato_df.loc[:, "labels"] = df["labels"]

    dataset_path = os.path.join(get_data_folder_path(), dataset_name)
    logging.info(f"saving potato dataset to {dataset_path}...")
    save_dataframe(potato_df, dataset_path)
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
