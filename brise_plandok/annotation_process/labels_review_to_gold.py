import argparse
import logging

from brise_plandok.annotation_process.utils.constants import ATTRIBUTES_TO_IGNORE, LabelReviewExcelConstants
from brise_plandok.annotation_process.utils.review_converter import ReviewConverter
from brise_plandok.attrs_from_gold import SenToAttrMap
from brise_plandok.constants import AttributeFields, DocumentFields, SenFields


def _labels_gold(review):
    return review == "OK" or review == "MISSING"


def _generate_gold_attrs(attributes):
    for attr in attributes:
        if attr["gold"]:
            yield attr["name"], {
                AttributeFields.NAME: attr["name"],
                AttributeFields.TYPE: None,
                AttributeFields.VALUE: None,
            }


class LabelReviewConverter(ReviewConverter):

    def __init__(self, data_file, gold_folder):
        super().__init__(data_file)
        self.sen_to_gold_attrs = SenToAttrMap(gold_dir=gold_folder, fuzzy=True)
        self.SEN_GOLD = SenFields.LABELS_GOLD_EXISTS
        self.DOC_GOLD = DocumentFields.LABELS_GOLD
        self.CONSTANTS = LabelReviewExcelConstants

    def _get_gold_candidate(self, sen_id, attributes):
        gold_candidate = {}
        for attr_name, attr in _generate_gold_attrs(attributes):
            if attr_name in gold_candidate:
                logging.warning(f"In {sen_id}: {attr_name} is already in gold candidates: {gold_candidate}")
            gold_candidate[attr_name] = attr
        return gold_candidate

    def _generate_attributes(self, review_sheet, row_id):
        for col in range(LabelReviewExcelConstants.ATTRIBUTE_OFFSET, review_sheet.max_column,
                         LabelReviewExcelConstants.ATTRIBUTE_STEP):
            label = review_sheet.cell(
                row=row_id, column=col + LabelReviewExcelConstants.LABEL_OFFSET).value
            if label is None:
                continue
            review = review_sheet.cell(
                row=row_id, column=col + LabelReviewExcelConstants.ATTRIBUTE_REVIEW_OFFSET).value
            if review is None:
                raise ValueError(
                    "Review field is not filled out for row " + str(row_id))
            if label not in ATTRIBUTES_TO_IGNORE:
                yield {
                    "name": label,
                    "gold": _labels_gold(review),
                }


def get_args():
    parser = argparse.ArgumentParser(description="Convert label review to gold data")
    parser.add_argument("-r", "--review", default=None)
    parser.add_argument("-d", "--data-file", default=None)
    parser.add_argument("-g", "--gold-folder", default=None)
    parser.set_defaults(input_format="XLSX", output_format="JSON")
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " +
               "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()
    converter = LabelReviewConverter(args.data_file, args.gold_folder)
    converter.convert(args.review)


if __name__ == "__main__":
    main()
