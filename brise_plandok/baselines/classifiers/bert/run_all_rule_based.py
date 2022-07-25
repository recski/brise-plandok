import argparse

from brise_plandok.baselines.classifiers.bert.run import run_bert
from brise_plandok.baselines.constants import RULE_BASED_ATTRIBUTES


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-g",
        "--gpu",
        default=None,
        help="To set on which GPU of the machine the code should run. If None, it falls back to CPU.",
    )
    parser.add_argument("-e", "--epochs", default=None, type=int, help="Number of epochs to run.")
    parser.add_argument("-l", "--log-folder", help="The name of the folder to save the logs.")
    parser.add_argument("-lr", "--learning-rate", type=float, help="The learning rate to use.")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    for attribute in RULE_BASED_ATTRIBUTES:
        run_bert(
            log_folder=args.log_folder,
            epochs=args.epochs,
            learning_rate=args.learning_rate,
            model=None,
            weights=False,
            attribute=attribute,
        )
