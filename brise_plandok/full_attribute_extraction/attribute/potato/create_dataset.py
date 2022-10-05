import argparse
import os

import pandas as pd
from xpotato.dataset.utils import save_dataframe

from brise_plandok import logger
from brise_plandok.full_attribute_extraction.attribute.potato.utils import (
    get_data_folder_path,
    create_potato_dataset,
    add_graphs_to_dataset,
)
from brise_plandok.full_attribute_extraction.attribute.utils.load_data import load_data_to_df


def create_dataset(dirs, only_gold, dataset_name, graph_format, cache_dir):
    data = []
    for dir in dirs:
        logger.info(f"Loading data from {dir}...")
        data.append(load_data_to_df(dir, only_gold))
        logger.info(f"{dir} done, shape: {data[-1].shape}")
    all_data = pd.concat(data, ignore_index=True)
    logger.info(f"All done, shape: {all_data.shape}")

    logger.info("Creating potato dataset...")
    dataset = create_potato_dataset(all_data, cache_dir)

    logger.info(
        f"Adding {graph_format} graphs (GraphExtractor cache dir is {dataset.extractor.cache_dir})..."
    )
    add_graphs_to_dataset(dataset, graph_format)

    potato_df = dataset.to_dataframe()
    potato_df.loc[:, "sen_id"] = all_data["sen_id"]
    potato_df.loc[:, "labels"] = all_data["labels"]

    dataset_path = os.path.join(get_data_folder_path(), dataset_name)
    logger.info(f"saving potato dataset to {dataset_path}...")
    save_dataframe(potato_df, dataset_path)
    logger.info("Done.")


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--dirs", nargs="+", help="Data folders where documents are stored.")
    parser.add_argument(
        "-o",
        "--only-gold",
        action="store_true",
        help="If set, only gold documents will be considered.",
    )
    parser.add_argument("-c", "--cache-dir", default=None, help="Define cache directory.")
    parser.add_argument("-g", "--graph", help="Graph type, one of 'fourlang' or 'ud'.")
    parser.add_argument("-n", "--dataset-name", help="Name of the output dataset.")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    create_dataset(args.dirs, args.only_gold, args.dataset_name, args.graph, args.cache_dir)
