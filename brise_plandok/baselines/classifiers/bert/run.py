import argparse
import datetime
import logging
import os
import stat

from brise_plandok.baselines.classifiers.bert.brise_bert_trainer import BriseBertTrainer


def set_logging(log_root, attribute):
    if attribute is None:
        attribute = "all"
    now = datetime.datetime.now()
    timestamp = (
        f"brise_bert_"
        f"{now.year}{now.month:02d}{now.day:02d}_{now.hour:02d}{now.minute:02d}_{now.second:02d}_"
        f"{attribute}"
    )
    timestamp_folder = os.path.join(log_root, timestamp)
    os.mkdir(timestamp_folder)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : %(module)s (%(lineno)s) - %(levelname)s - %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        handlers=[
            logging.FileHandler(f"{timestamp_folder}/{timestamp}.log"),
            logging.StreamHandler(),
        ],
    )

    return timestamp_folder


def remove_write_access_from_log_folder(log_folder):
    current = stat.S_IMODE(os.lstat(log_folder).st_mode)
    os.chmod(log_folder, current & ~stat.S_IWRITE)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-g",
        "--gpu",
        default=None,
        help="To set on which GPU of the machine the code should run. If None, it falls back to CPU.",
    )
    parser.add_argument("-e", "--epochs", default=None, type=int, help="Number of epochs to run.")
    parser.add_argument("-m", "--model", default=None, help="Path to model to continue from.")
    parser.add_argument("-l", "--log-folder", help="The name of the folder to save the logs.")
    parser.add_argument(
        "-w", "--weights", action="store_true", help="Set weights for BCEWithLogitsLoss."
    )
    parser.add_argument("-lr", "--learning-rate", type=float, help="The learning rate to use.")
    parser.add_argument(
        "-a",
        "--attribute",
        help="Specific attribute to learn. If left empty, all attributes will be trained simultaneously.",
    )
    return parser.parse_args()


def run_bert(log_folder, epochs, learning_rate, model, weights, attribute):
    timestamped_log_folder = set_logging(log_folder, attribute)
    logging.info(f"Epochs: {epochs}")
    logging.info(f"Learning rate: {learning_rate}")
    trainer = BriseBertTrainer(
        epochs, model, timestamped_log_folder, weights, learning_rate, attribute
    )
    trainer.train()
    remove_write_access_from_log_folder(timestamped_log_folder)


if __name__ == "__main__":
    args = get_args()
    run_bert(
        args.log_foler, args.epochs, args.learning_rate, args.model, args.weights, args.attribute
    )
