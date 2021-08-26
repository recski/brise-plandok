import logging
import os

import openpyxl
from openpyxl.utils.cell import get_column_letter
from openpyxl.styles import Alignment, Font
from openpyxl.worksheet.datavalidation import DataValidation
from brise_plandok.annotation.attributes import ATTR_TO_CAT

review_sheet_name = "Review"
attribute_named_range = "Attribute"
attribute_review_named_range = "Attribute_Review"
sentence_review_named_range = "Sentence_Review"

class ExcelGenerator:

    def __init__(self) -> None:
        self.output = os.path.join(os.path.dirname(__file__), "review.xlsx")
        self.attribute_offset = 5
        self.first_attribute_column = 4

    def generate_review_excel(self, merged_annotations):
        excel_template = os.path.join(
            os.path.dirname(__file__), "BRISE_review.xlsx")
        workbook = openpyxl.load_workbook(excel_template)
        self._fill_workbook(workbook, merged_annotations)
        self._save_workbook(workbook)

    def _fill_workbook(self, workbook, merged_annotations):
        review_sheet = workbook[review_sheet_name]
        row = 2
        for sen_id, annotation in merged_annotations.items():
            self.__fill_sentences(sen_id, review_sheet, row, annotation)
            self.__fill_attributes(annotation, review_sheet, row)
            row += 1
        self.__add_validation(review_sheet)

    def __fill_sentences(self, sen_id, review_sheet, row, annotation):
        review_sheet.cell(row=row, column=1).value = sen_id
        review_sheet.cell(row=row, column=3).value = annotation["text"]
        review_sheet.cell(row=row, column=3).alignment = Alignment(wrapText=True)
        review_sheet.cell(row=row, column=3).font = Font(size=12)

    def __fill_attributes(self, annotation, review_sheet, row):
        col = self.first_attribute_column
        for attribute_name, attribute_props in annotation["attributes"].items():
            attribute_name = self.__normalize_attr_names(attribute_name)
            if attribute_name not in ATTR_TO_CAT:
                logging.warn(
                    f"\"{attribute_name}\" does not belong to any category - will be ignored")
            else:
                self.__fill_attribute(
                    attribute_name, attribute_props, review_sheet, col, row)
                col += self.attribute_offset

    def __fill_attribute(self, attribute_name, attribute_props, review_sheet, col, row):
        review_sheet.cell(row=row, column=col).value = ATTR_TO_CAT[attribute_name]
        review_sheet.cell(row=row, column=col+1).value = attribute_name
        review_sheet.cell(row=row, column=col+2).value = attribute_props["count"]
        review_sheet.cell(row=row, column=col+3).value = "\n".join(attribute_props["annotators"])
        review_sheet.cell(row=row, column=col+4).value = "OK"

    def __normalize_attr_names(self, attribute_name):
        if attribute_name == "Verkehrsflaeche_ID":
            return "VerkehrsflaecheID"
        return attribute_name

    def __add_validation(self, review_sheet):
        data_val = DataValidation(type="list", formula1=f"={attribute_named_range}")
        review_sheet.add_data_validation(data_val)
        review_val = DataValidation(type="list", formula1=f"={attribute_review_named_range}")
        review_sheet.add_data_validation(review_val)
        sen_review_val = DataValidation(type="list", formula1=f"={sentence_review_named_range}")
        review_sheet.add_data_validation(sen_review_val)
        for row in range(2, review_sheet.max_row):
            self.__add_validation_for_row(
                review_sheet, row, data_val, review_val, sen_review_val)

    def __add_validation_for_row(self, review_sheet, row, data_val, review_val, sen_review_val):
        for cell in review_sheet[str(row)]:
            col = cell.column
            if self.__is_sentence_review_cell(col):
                self.__add_validation_for_sentence_review(review_sheet, row, col, sen_review_val)
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
        sub_data_val.add(review_sheet.cell(row=row, column=col+1))
        review_val.add(
            review_sheet.cell(row=row, column=col+3))

    def __is_sentence_review_cell(self, col):
        return col == 2

    def __is_category_cell(self, col):
        return (col - self.first_attribute_column) % self.attribute_offset == 0

    def _save_workbook(self, workbook):
        workbook.save(self.output)
