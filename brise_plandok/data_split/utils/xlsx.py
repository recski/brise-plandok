

from brise_plandok.constants import DocumentFields
from brise_plandok.data_split.utils.assignments import get_assignment_path, get_download_folder, update_assignments
import logging
from brise_plandok.data_split.utils.constants import ANNOTATOR_DOWNLOAD_FOLDER, ASSIGNMENT_ADDITIONAL_HEADER, ASSIGNMENT_DF_HEADER_BASE, ASSIGNMENT_XLSX
import shutil
from brise_plandok.convert import Converter
import os


class ConverterArgs:
    def __init__(self, output_file):
        self.input_format = "JSON"
        self.output_format = "XLSX"
        self.output_file = output_file
        self.gen_attributes = True


def genereate_xlsx_files(docs, xlsx_folder, overwrite):
    for doc in docs:
        doc_id = doc[DocumentFields.ID]
        xlsx_file = os.path.join(xlsx_folder, doc_id+".xlsx")
        if not overwrite and os.path.exists(xlsx_file):
            continue
        Converter(ConverterArgs(xlsx_file)).write_xlsx(doc, xlsx_file)
    logging.info("xlsx files have been generated from json files")


def distribute_xlsx_files(xlsx_folder, df, annotators_folder, update, phase):
    for _, assignment in df.iterrows():
        annotator = assignment[ASSIGNMENT_DF_HEADER_BASE[0]]
        doc_ids_for_annotator = assignment[ASSIGNMENT_ADDITIONAL_HEADER[0]].split(
            ',')
        for doc_id in doc_ids_for_annotator:
            _copy_xlsx_files_to_annotators(
                doc_id, xlsx_folder, annotators_folder, annotator, phase)
        if update:
            update_assignments(doc_ids_for_annotator,
                               annotator, annotators_folder, phase)
    logging.info("xlsx files have been distributed to annotators")


def _copy_xlsx_files_to_annotators(doc_id, xlsx_folder, annotators_folder, annotator, phase):
    xlsx_file = os.path.join(xlsx_folder, doc_id + ".xlsx")
    dest = os.path.join(get_download_folder(
        annotators_folder, annotator, phase), os.path.basename(xlsx_file))
    shutil.copy2(xlsx_file, dest)
