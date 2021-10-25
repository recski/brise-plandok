from brise_plandok.constants import GOLD_COLOR, GRAY_COLOR, ROW_HEIGHT
from brise_plandok.constants import SenFields as SF
from brise_plandok.constants import DocumentFields as DF
from openpyxl.styles.fills import PatternFill
import logging
import os

import openpyxl
from openpyxl.utils.cell import get_column_letter
from openpyxl.styles import Alignment, Font
from openpyxl.worksheet.datavalidation import DataValidation


class ExcelGenerator:

    def __init__(self, output_file, CONSTANTS, sen_to_gold_attrs=None):
        self.input_template = os.path.join(os.path.dirname(
            __file__), "input", "review_template.xlsx")
        self.output_file = output_file
        self.sen_to_gold_attrs = sen_to_gold_attrs
        self.CONSTANTS = CONSTANTS

    def generate_excel(self, doc):
        workbook = openpyxl.load_workbook(self.input_template)
        self._fill_workbook(workbook, doc)
        self._save_workbook(workbook)

    def _fill_workbook(self, workbook, doc):
        main_sheet = workbook[self.CONSTANTS.MAIN_SHEET_NAME]
        row = self.CONSTANTS.FIRST_DATA_ROW
        for sen_id, sen in doc[DF.SENS].items():
            self._fill_sentences(sen_id, main_sheet, row, sen)
            self._fill_attributes(sen, main_sheet, row)
            row += 1
        self._add_validation(main_sheet)
        self._set_row_height(main_sheet)

    def _fill_sentences(self, sen_id, main_sheet, row, sen):
        main_sheet.cell(
            row=row, column=self.CONSTANTS.SEN_ID_COL).value = sen_id
        main_sheet.cell(
            row=row, column=self.CONSTANTS.SEN_TEXT_COL).value = sen[SF.TEXT]
        if self._is_gold(sen):
            self._color_gold(main_sheet, row, self.CONSTANTS.SEN_ID_COL)
            self._color_gold(main_sheet, row, self.CONSTANTS.SEN_TEXT_COL)
        main_sheet.cell(
            row=row, column=self.CONSTANTS.SEN_TEXT_COL).alignment = Alignment(wrapText=True)
        main_sheet.cell(
            row=row, column=self.CONSTANTS.SEN_TEXT_COL).font = Font(size=12)

    def _fill_attributes(self, sen, main_sheet, row):
        raise NotImplementedError()

    def _add_validation(self, main_sheet):
        raise NotImplementedError()

    def _is_gold(self, sen):
        return sen[SF.GOLD_EXISTS]

    def _color_gray(self, main_sheet, row, col):
        self._color(main_sheet, row, col, GRAY_COLOR)

    def _color_gold(self, main_sheet, row, col):
        self._color(main_sheet, row, col, GOLD_COLOR)

    def _color(self, main_sheet, row, col, color):
        main_sheet.cell(row=row, column=col).fill = PatternFill(
            fgColor=color, fill_type="solid")
        main_sheet.cell(row=row, column=col).font = Font(size=12)

    def _add_validations_for_attribute(self, main_sheet, row, col, category_val):
        category_val.add(main_sheet.cell(row=row, column=col))
        sub_data_val = DataValidation(
            type="list", formula1='==INDIRECT(${0}${1})'.format(get_column_letter(col), str(row)))
        main_sheet.add_data_validation(sub_data_val)
        sub_data_val.add(main_sheet.cell(
            row=row, column=col+self.CONSTANTS.LABEL_OFFSET))

    def _is_category_cell(self, col):
        return (col - self.CONSTANTS.ATTRIBUTE_OFFSET) % self.CONSTANTS.ATTRIBUTE_STEP == 0

    def _set_row_height(self, main_sheet):
        for row in range(self.CONSTANTS.FIRST_DATA_ROW, main_sheet.max_row + 1):
            main_sheet.row_dimensions[row].height = ROW_HEIGHT

    def _save_workbook(self, workbook):
        workbook.save(self.output_file)
        logging.info(f"DONE. Review xlsx was created to: {self.output_file}")
