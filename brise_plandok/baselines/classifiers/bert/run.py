import argparse
import datetime
import logging
import os
import stat

from brise_plandok.baselines.classifiers.bert.brise_bert_trainer import BriseBertTrainer


def set_logging(log_root):
    now = datetime.datetime.now()
    timestamp = f"brise_bert_{now.year}{now.month:02d}{now.day:02d}_{now.hour:02d}{now.minute:02d}_{now.second:02d}"
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
    return parser.parse_args()


def main():
    args = get_args()
    log_folder = set_logging(args.log_folder)
    logging.info(f"Epochs: {args.epochs}")
    logging.info(f"Learning rate: {args.learning_rate}")
    trainer = BriseBertTrainer(
        args.epochs, args.model, log_folder, args.weights, args.learning_rate
    )
    trainer.train()
    remove_write_access_from_log_folder(log_folder)


if __name__ == "__main__":
    main()
