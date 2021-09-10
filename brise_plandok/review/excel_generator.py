from brise_plandok.constants import GOLD_COLOR
from openpyxl.styles.fills import PatternFill
from utils import normalize_attribute_name
from brise_plandok.review.constants import ANNOTATORS_OFFSET, ANNOTATOR_SEPARATOR, ATTRIBUTE_NAMED_RANGE, ATTRIBUTE_OFFSET, ATTRIBUTE_REVIEW_NAMED_RANGE, ATTRIBUTE_REVIEW_OFFSET, ATTRIBUTE_STEP, CATEGORY_OFFSET, COUNT_OFFSET, FIRST_DATA_ROW, LABEL_OFFSET, REVIEW_SHEET_NAME, SENTENCE_REVIEW_NAMED_RANGE, SEN_ID_COL, SEN_REVIEW_COL, SEN_TEXT_COL
import logging
import os

import openpyxl
from openpyxl.utils.cell import get_column_letter
from openpyxl.styles import Alignment, Font
from openpyxl.worksheet.datavalidation import DataValidation
from brise_plandok.annotation.attributes import ATTR_TO_CAT


class ExcelGenerator:

    def __init__(self, output_file):
        self.input_template = os.path.join(os.path.dirname(
            __file__), "input", "review_template.xlsx")
        self.output_file = output_file

    def generate_review_excel(self, merged_annotations, sen_to_gold_attrs):
        workbook = openpyxl.load_workbook(self.input_template)
        self._fill_workbook(workbook, merged_annotations, sen_to_gold_attrs)
        self._save_workbook(workbook)

    def _fill_workbook(self, workbook, merged_annotations, sen_to_gold_attrs):
        review_sheet = workbook[REVIEW_SHEET_NAME]
        row = FIRST_DATA_ROW
        for sen_id, annotation in merged_annotations.items():
            self.__fill_sentences(sen_id, review_sheet,
                                  row, annotation, sen_to_gold_attrs)
            self.__fill_attributes(annotation, review_sheet, row)
            row += 1
        self.__add_validation(review_sheet)

    def __fill_sentences(self, sen_id, review_sheet, row, annotation, sen_to_gold_attrs):
        review_sheet.cell(row=row, column=SEN_ID_COL).value = sen_id
        review_sheet.cell(
            row=row, column=SEN_TEXT_COL).value = annotation["text"]
        self._color_if_gold(sen_to_gold_attrs, annotation, review_sheet, row)
        review_sheet.cell(
            row=row, column=SEN_TEXT_COL).alignment = Alignment(wrapText=True)
        review_sheet.cell(row=row, column=SEN_TEXT_COL).font = Font(size=12)

    def _color_if_gold(self, sen_to_gold_attrs, annotation, review_sheet, row):
        if sen_to_gold_attrs.get_attrs(annotation['text']):
            review_sheet.cell(row=row, column=SEN_ID_COL).fill = PatternFill(
                fgColor=GOLD_COLOR, fill_type="solid")
            review_sheet.cell(row=row, column=SEN_TEXT_COL).fill = PatternFill(
                fgColor=GOLD_COLOR, fill_type="solid")

    def __fill_attributes(self, annotation, review_sheet, row):
        col = ATTRIBUTE_OFFSET
        for attribute_name, attribute_props in annotation["attributes"].items():
            attribute_name = normalize_attribute_name(attribute_name)
            if attribute_name not in ATTR_TO_CAT:
                logging.warn(
                    f"\"{attribute_name}\" does not belong to any category - will be ignored")
            else:
                self.__fill_attribute(
                    attribute_name, attribute_props, review_sheet, col, row)
                col += ATTRIBUTE_STEP

    def __fill_attribute(self, attribute_name, attribute_props, review_sheet, col, row):
        review_sheet.cell(
            row=row, column=col+CATEGORY_OFFSET).value = ATTR_TO_CAT[attribute_name]
        review_sheet.cell(row=row, column=col +
                          LABEL_OFFSET).value = attribute_name
        review_sheet.cell(row=row, column=col +
                          COUNT_OFFSET).value = attribute_props["count"]
        review_sheet.cell(row=row, column=col +
                          ANNOTATORS_OFFSET).value = ANNOTATOR_SEPARATOR.join(attribute_props["annotators"])
        review_sheet.cell(row=row, column=col +
                          ATTRIBUTE_REVIEW_OFFSET).value = "OK"

    def __add_validation(self, review_sheet):
        data_val = DataValidation(
            type="list", formula1=f"={ATTRIBUTE_NAMED_RANGE}")
        review_sheet.add_data_validation(data_val)
        review_val = DataValidation(
            type="list", formula1=f"={ATTRIBUTE_REVIEW_NAMED_RANGE}")
        review_sheet.add_data_validation(review_val)
        sen_review_val = DataValidation(
            type="list", formula1=f"={SENTENCE_REVIEW_NAMED_RANGE}")
        review_sheet.add_data_validation(sen_review_val)
        for row in range(FIRST_DATA_ROW, review_sheet.max_row):
            self.__add_validation_for_row(
                review_sheet, row, data_val, review_val, sen_review_val)

    def __add_validation_for_row(self, review_sheet, row, data_val, review_val, sen_review_val):
        for cell in review_sheet[str(row)]:
            col = cell.column
            if self.__is_sentence_review_cell(col):
                self.__add_validation_for_sentence_review(
                    review_sheet, row, col, sen_review_val)
            elif self.__is_category_cell(col):
                self.__add_validations_for_attribute(
                    review_sheet, row, col, data_val, review_val)

    def __add_validation_for_sentence_review(self, review_sheet, row, col, sentence_review_val):
        sentence_review_val.add(review_sheet.cell(row=row, column=col))

    def __add_validations_for_attribute(self, review_sheet, row, col, data_val, review_val):
        data_val.add(review_sheet.cell(row=row, column=col))
        sub_data_val = DataValidation(
            type="list", formula1='==INDIRECT(${0}${1})'.format(get_column_letter(col), str(row)))
        review_sheet.add_data_validation(sub_data_val)
        sub_data_val.add(review_sheet.cell(row=row, column=col+LABEL_OFFSET))
        review_val.add(
            review_sheet.cell(row=row, column=col+ATTRIBUTE_REVIEW_OFFSET))

    def __is_sentence_review_cell(self, col):
        return col == SEN_REVIEW_COL

    def __is_category_cell(self, col):
        return (col - ATTRIBUTE_OFFSET) % ATTRIBUTE_STEP == 0

    def _save_workbook(self, workbook):
        workbook.save(self.output_file)
        logging.info(f"DONE. Review xlsx was created to: {self.output_file}")
