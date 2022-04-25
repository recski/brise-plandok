import argparse

from brise_plandok.annotation_process.utils.xlsx import ConverterArgs
from brise_plandok.convert import Converter
from brise_plandok.utils import load_json


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-o", "--output-file", type=str)
    parser.add_argument("-d", "--data-file", type=str, default=None)
    return parser.parse_args()


def main():
    args = get_args()
    doc = load_json(args.data_file)
    xlsx_file = args.output_file
    Converter(ConverterArgs(xlsx_file)).write_xlsx(doc, xlsx_file)


if __name__ == "__main__":
    main()
