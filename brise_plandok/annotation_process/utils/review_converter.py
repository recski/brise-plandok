import logging

import openpyxl

from brise_plandok.constants import DocumentFields, SenFields
from brise_plandok.utils import dump_json, load_json


class ReviewConverter:

    def __init__(self, data_file):
        self.data = load_json(data_file)
        self.data_file = data_file
        self.SEN_GOLD = None
        self.DOC_GOLD = None
        self.CONSTANTS = None
        self.sen_to_gold_attrs = None

    def convert(self, reviewed_xlsx_file):
        self._fill_gold_attrs(reviewed_xlsx_file)
        self._save_gold_json()

    def _save_gold_json(self):
        dump_json(self.data, self.data_file)
        logging.info(f"DONE. Gold json was created to: {self.data_file}")

    def _fill_gold_attrs(self, fn):
        workbook = openpyxl.load_workbook(fn)
        review_sheet = workbook[self.CONSTANTS.MAIN_SHEET_NAME]

        for row_id in range(self.CONSTANTS.FIRST_DATA_ROW, review_sheet.max_row + 1):
            sen_id = review_sheet.cell(row=row_id, column=self.CONSTANTS.SEN_ID_COL).value
            attributes = [attribute for attribute in self._generate_attributes(review_sheet, row_id)]

            if self._is_error(attributes):
                self.data[DocumentFields.SENS][sen_id][SenFields.SEGMENTATION_ERROR] = True
                logging.info(f"error row found '{sen_id}' - skipping from gold")
                continue

            gold_candidate = self._get_gold_candidate(sen_id, attributes)
            self._raise_error_on_internal_conflict(sen_id, gold_candidate)
            self._raise_error_on_external_conflict(sen_id, gold_candidate)

            self.data[DocumentFields.SENS][sen_id][self.SEN_GOLD] = True
            self.data[DocumentFields.SENS][sen_id][SenFields.GOLD_ATTRIBUTES] = gold_candidate

        self.data[self.DOC_GOLD] = True

    def _generate_attributes(self, review_sheet, row_id):
        raise NotImplementedError()

    def _get_gold_candidate(self, sen_id, attributes):
        raise NotImplementedError()

    def _raise_error_on_internal_conflict(self, sen_id, gold_candidate):
        if self.data[DocumentFields.SENS][sen_id][self.SEN_GOLD]:
            current_gold = self.data[DocumentFields.SENS][sen_id][SenFields.GOLD_ATTRIBUTES]
            if set(gold_candidate.keys()) != set(current_gold.keys()):
                logging.error(
                    f"Conflict within already gold sentence {sen_id}:\nCurrent ({sen_id}):\n{current_gold}\nNew:\n{gold_candidate}")
                raise ValueError("Gold conflict")

    def _raise_error_on_external_conflict(self, sen_id, gold_candidate):
        text = self.data[DocumentFields.SENS][sen_id][SenFields.TEXT]
        current_gold = self.sen_to_gold_attrs.get_attrs(text)
        if current_gold is not None:
            current_gold_sens = self.sen_to_gold_attrs.get_sens(text)
            if set(gold_candidate.keys()) != set(current_gold.keys()):
                logging.error(
                    f"Conflict with current gold value of {sen_id}:\nCurrent ({current_gold_sens}):\n{current_gold}\nNew:\n{gold_candidate}")
                raise ValueError("Gold conflict")

    def _is_error(self, attributes):
        return self.CONSTANTS.ERROR_LABEL in set([attr["name"] for attr in attributes])
