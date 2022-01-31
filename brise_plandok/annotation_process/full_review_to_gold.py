import argparse
import logging

from brise_plandok.annotation_process.utils.constants import ATTRIBUTES_TO_IGNORE, FullReviewExcelConstants
from brise_plandok.annotation_process.utils.review_converter import ReviewConverter
from brise_plandok.attrs_from_gold import SenToAttrMap
from brise_plandok.constants import AttributeFields, DocumentFields, SenFields


class FullReviewConverter(ReviewConverter):

    def __init__(self, data_file, gold_folder):
        super().__init__(data_file)
        self.sen_to_gold_attrs = SenToAttrMap(gold_dir=gold_folder, fuzzy=False, full=True)
        self.SEN_GOLD = SenFields.FULL_GOLD_EXISTS
        self.DOC_GOLD = DocumentFields.FULL_GOLD
        self.CONSTANTS = FullReviewExcelConstants

    def _generate_attributes(self, review_sheet, row_id):
        for col in range(FullReviewExcelConstants.ATTRIBUTE_OFFSET, review_sheet.max_column,
                         FullReviewExcelConstants.ATTRIBUTE_STEP):
            label = review_sheet.cell(
                row=row_id, column=col + FullReviewExcelConstants.LABEL_OFFSET).value
            if label is None:
                continue
            value = review_sheet.cell(
                row=row_id, column=col + FullReviewExcelConstants.VALUE_OFFSET).value
            ann_type = review_sheet.cell(
                row=row_id, column=col + FullReviewExcelConstants.TYPE_ANN_REV_OFFSET).value
            if label not in ATTRIBUTES_TO_IGNORE:
                yield {
                    AttributeFields.NAME: label,
                    AttributeFields.VALUE: value,
                    AttributeFields.TYPE: ann_type,
                }

    def _get_gold_candidate(self, sen_id, attributes):
        gold_candidate = {}
        for attr in attributes:
            attr_name = attr[AttributeFields.NAME]
            if attr_name not in gold_candidate:
                gold_candidate[attr_name] = {
                    AttributeFields.NAME: attr_name,
                    AttributeFields.VALUE: [],
                    AttributeFields.TYPE: [],
                }

            self.__append_values(attr, attr_name, gold_candidate, sen_id)
            self.__append_type(attr, attr_name, gold_candidate, sen_id)

        self.__warn_on_multiple_types(gold_candidate, sen_id)
        return gold_candidate

    def __warn_on_multiple_types(self, gold_candidate, sen_id):
        for attr_name in gold_candidate.keys():
            if len(set(gold_candidate[attr_name][AttributeFields.TYPE])) > 1:
                logging.warning(
                    f"\n\nPlease prove validity:\nSame attribute has different reviewed_type in {sen_id}: {gold_candidate}.\n")

    def __append_type(self, attr, attr_name, gold_candidate, sen_id):
        reviewed_type = attr[AttributeFields.TYPE]
        if reviewed_type is None:
            raise ValueError(
                "Reviewed type is missing for " + str(sen_id))
        gold_candidate[attr_name][AttributeFields.TYPE].append(reviewed_type)

    def __append_values(self, attr, attr_name, gold_candidate, sen_id):
        values = attr[AttributeFields.VALUE]
        if values is None:
            raise ValueError(
                "Value is missing for " + str(sen_id))
        gold_candidate[attr_name][AttributeFields.VALUE].append(values)

    def _get_modality(self, review_sheet, row_id, attributes):
        modality = review_sheet.cell(row=row_id, column=FullReviewExcelConstants.MODALITY_ANN_REV_COL).value
        if len(attributes) > 0 and not self._is_error(attributes) and modality is None:
            logging.warning("Modality is missing for row " + str(row_id))
        return modality


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-r", "--review", default=None)
    parser.add_argument("-d", "--data-file", default=None)
    parser.add_argument("-g", "--gold-folder", default=None)
    parser.add_argument("-o", "--override", action="store_true")
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " +
               "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()
    converter = FullReviewConverter(args.data_file, args.gold_folder)
    converter.convert(args.review, args.override)


if __name__ == "__main__":
    main()
