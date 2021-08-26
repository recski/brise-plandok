import logging
import os

import openpyxl
from openpyxl.utils.cell import get_column_letter
from openpyxl.styles import Alignment, Font
from openpyxl.worksheet.datavalidation import DataValidation
from brise_plandok.annotation.attributes import ATTR_TO_CAT


class ExcelGenerator:

    def __init__(self) -> None:
        self.output = os.path.join(os.path.dirname(__file__), "review.xlsx")
        self.attribute_offset = 4

    def generate_review_excel(self, merged_annotations):
        excel_template = os.path.join(
            os.path.dirname(__file__), "BRISE_review.xlsx")
        workbook = openpyxl.load_workbook(excel_template)
        self._fill_workbook(workbook, merged_annotations)
        self._save_workbook(workbook)

    def _fill_workbook(self, workbook, merged_annotations):
        review_sheet = workbook["Review"]
        row = 2
        for sen_id, annotation in merged_annotations.items():
            self.__fill_sens(sen_id, review_sheet, row, annotation)
            base_column = ord('C')
            for attribute_name, attribute_props in annotation["attributes"].items():
                attribute_name = self.__normalize_attr_names(attribute_name)
                if attribute_name not in ATTR_TO_CAT:
                    logging.warn(
                        f"\"{attribute_name}\" does not belong to any category - will be ignored")
                else:
                    self.__fill_attributes(
                        attribute_name, attribute_props, review_sheet, base_column, row)
                    base_column += self.attribute_offset
            row += 1
        self.__add_data_validation(review_sheet)

    def __fill_sens(self, sen_id, review_sheet, row, annotation):
        sen_id_cell = "A"+str(row)
        sen_txt_cell = "B"+str(row)
        review_sheet[sen_id_cell] = sen_id
        review_sheet[sen_txt_cell] = annotation["text"]
        review_sheet[sen_id_cell].alignment = Alignment(wrapText=True)
        review_sheet[sen_txt_cell].alignment = Alignment(wrapText=True)
        review_sheet[sen_id_cell].font = Font(size=12)
        review_sheet[sen_txt_cell].font = Font(size=12)

    def __fill_attributes(self, attribute_name, attribute_props, review_sheet, base_column, row):
        review_sheet[self.__get_cell(
            base_column, 0, row)] = ATTR_TO_CAT[attribute_name]
        review_sheet[self.__get_cell(base_column, 1, row)] = attribute_name
        review_sheet[self.__get_cell(
            base_column, 2, row)] = attribute_props["count"]
        review_sheet[self.__get_cell(base_column, 3, row)] = "OK"

    def __get_cell(self, base_column, column_offset, row):
        return chr(base_column + column_offset)+str(row)

    def __normalize_attr_names(self, attribute_name):
        if attribute_name == "Verkehrsflaeche_ID":
            return "VerkehrsflaecheID"
        return attribute_name

    def __add_data_validation(self, review_sheet):
        data_val = DataValidation(type="list", formula1='=Attribute')
        review_val = DataValidation(type="list", formula1='=Review')
        review_sheet.add_data_validation(data_val)
        review_sheet.add_data_validation(review_val)
        for row in range(2, review_sheet.max_row):
            self.__add_data_validation_for_row(
                review_sheet, row, data_val, review_val)

    def __add_data_validation_for_row(self, review_sheet, row, data_val, review_val):
        sub_data_val = None
        for cell in review_sheet[str(row)]:
            col = cell.column
            if self.__not_attribute(col):
                continue
            if self.__is_category_cell(col):
                data_val.add(review_sheet.cell(row=row, column=col))
                sub_data_val = DataValidation(
                    type="list", formula1='==INDIRECT(${0}${1})'.format(get_column_letter(col), str(row)))
                review_sheet.add_data_validation(sub_data_val)
            elif self.__is_label_cell(col):
                sub_data_val.add(review_sheet.cell(row=row, column=col))
            elif self.__is_review_cell(col):
                review_val.add(
                    review_sheet.cell(row=row, column=col))

    def __not_attribute(self, col):
        return col < 3

    def __is_category_cell(self, col):
        return (col - 3) % self.attribute_offset == 0

    def __is_label_cell(self, col):
        return (col-3) % self.attribute_offset == 1

    def __is_review_cell(self, col):
        return (col-3) % self.attribute_offset == 3

    def _save_workbook(self, workbook):
        workbook.save(self.output)
