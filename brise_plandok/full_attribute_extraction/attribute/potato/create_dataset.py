import argparse
import logging
import os
import pickle

from xpotato.dataset.dataset import Dataset

from brise_plandok.full_attribute_extraction.attribute.potato.utils import load_data_to_df, \
    get_data_folder_path, get_sentences, get_vocab_for_all_attributes


def add_graphs(dataset, graph_path, graph_format):
    if not os.path.exists(graph_path):
        dataset.set_graphs(dataset.parse_graphs(graph_format=graph_format))
    else:
        logging.info(f"Graphs are already parsed. Loading graphs from {graph_path}")
        dataset.load_graphs(graph_path)
    df = dataset.to_dataframe()
    if not os.path.exists(graph_path):
        with open(graph_path, "wb") as f:
            pickle.dump(df.graph, f)
        logging.info(f"Graphs saved to {graph_path}")
    return df


def get_dataset(data, label_vocab, dataset_name, graph_format):
    dataset_path = os.path.join(get_data_folder_path(), dataset_name)
    graph_path = os.path.join(get_data_folder_path(), f"{dataset_name}_{graph_format}.pickle")
    logging.info(f"Start processing data for {dataset_path} with {graph_format} graphs...")

    dataset = Dataset(get_sentences(data), label_vocab=label_vocab, lang="de")
    potato_df = add_graphs(dataset, graph_path, graph_format)

    potato_df.loc[:, "sen_id"] = data["sen_id"]
    potato_df.loc[:, "labels"] = data["labels"]

    potato_df.to_pickle(dataset_path)
    logging.info(f"...finished processing data for {dataset_path} with {graph_format} graphs")
    return potato_df


def create_dataset(dir_path, only_gold, dataset_name, graph_format):
    data_df = load_data_to_df(dir_path, only_gold)
    logging.info(f"Data loaded to DataFrame for {dir_path}. Shape: {data_df.shape}")

    potato_df = get_dataset(data_df, get_vocab_for_all_attributes(), dataset_name, graph_format)
    logging.info("POTATO dataset is created")
    logging.info(f"\n{potato_df.head()}")


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-d", "--dir-path")
    parser.add_argument("-o", "--only-gold", action="store_true")
    parser.add_argument("-g", "--graph")
    parser.add_argument("-n", "--dataset-name")
    return parser.parse_args()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " +
               "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()
    create_dataset(args.dir_path, args.only_gold, args.dataset_name, args.graph)
