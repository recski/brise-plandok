

import logging
from brise_plandok.data_split.utils.constants import ANNOTATOR_DOWNLOAD_FOLDER, ASSIGNMENT_ADDITIONAL_HEADER, ASSIGNMENT_DF_HEADER
import json
import shutil
from brise_plandok.convert import Converter
import os

class ConverterArgs:
    def __init__(self, output_file):
        self.input_format = "JSON"
        self.output_format = "XLSX"
        self.output_file = output_file
        self.gen_attributes = True


def genereate_xlsx_files(doc_ids, json_folder, xlsx_folder, override):
    for doc_id in doc_ids:
        xlsx_file = os.path.join(xlsx_folder, doc_id+".xlsx")
        if not override and os.path.exists(xlsx_file):
            continue
        json_file = os.path.join(json_folder, doc_id+".jsonl")
        converter = Converter(ConverterArgs(xlsx_file))
        with open(json_file) as f:
            lines = f.readlines()
            assert len(lines) == 1
            doc = json.loads(lines[0].strip())
            converter.write_xlsx(doc, xlsx_file)


def distribute_xlsx_files(xlsx_folder, df, annotators_folder):
    for _, assignment in df.iterrows():
        annotator = assignment[ASSIGNMENT_DF_HEADER[0]]
        doc_ids_for_annotator = assignment[ASSIGNMENT_ADDITIONAL_HEADER[0]].split(',')
        for doc_id in doc_ids_for_annotator:
            _copy_xlsx_files_to_annotators(doc_id, xlsx_folder, annotators_folder, annotator)


def _copy_xlsx_files_to_annotators(doc_id, xlsx_folder, annotators_folder, annotator):
    xlsx_file = os.path.join(xlsx_folder, doc_id+".xlsx")
    dest = os.path.join(annotators_folder, annotator, ANNOTATOR_DOWNLOAD_FOLDER, os.path.basename(xlsx_file))
    shutil.copy2(xlsx_file, dest)
    logging.info(f"copied {xlsx_file} to {dest}")