import os
import shutil

from brise_plandok import logger
from brise_plandok.annotation_process.utils.assignments import (
    get_download_folder,
    update_assignments,
)
from brise_plandok.annotation_process.utils.constants import (
    ASSIGNMENT_ADDITIONAL_HEADER,
    ASSIGNMENT_DF_HEADER_BASE,
    FullAnnotationExcelConstants,
)
from brise_plandok.annotation_process.utils.full_annotation_excel_generator import (
    FullAnnotationExcelGenerator,
)
from brise_plandok.constants import DocumentFields
from brise_plandok.convert import Converter


class ConverterArgs:
    def __init__(self, output_file):
        self.input_format = "JSON"
        self.output_format = "XLSX"
        self.output_file = output_file
        self.gen_attributes = True


def genereate_xlsx_files(docs, xlsx_folder, overwrite, phase):
    for doc in docs:
        doc_id = doc[DocumentFields.ID]
        xlsx_file = os.path.join(xlsx_folder, doc_id + ".xlsx")
        if not overwrite and os.path.exists(xlsx_file):
            continue
        if phase == 1:
            Converter(ConverterArgs(xlsx_file)).write_xlsx(doc, xlsx_file)
        else:
            FullAnnotationExcelGenerator(
                xlsx_file, FullAnnotationExcelConstants(), doc
            ).generate_excel()
    logger.info("xlsx files have been generated from json files")


def distribute_xlsx_files(xlsx_folder, df, annotators_folder, update, phase):
    for _, assignment in df.iterrows():
        annotator = assignment[ASSIGNMENT_DF_HEADER_BASE[0]]
        doc_ids_for_annotator = assignment[ASSIGNMENT_ADDITIONAL_HEADER[0]].split(",")
        for doc_id in doc_ids_for_annotator:
            _copy_xlsx_files_to_annotators(
                doc_id, xlsx_folder, annotators_folder, annotator, phase
            )
        if update:
            update_assignments(doc_ids_for_annotator, annotator, annotators_folder, phase)
    logger.info("xlsx files have been distributed to annotators")


def _copy_xlsx_files_to_annotators(doc_id, xlsx_folder, annotators_folder, annotator, phase):
    xlsx_file = os.path.join(xlsx_folder, doc_id + ".xlsx")
    dest = os.path.join(
        get_download_folder(annotators_folder, annotator, phase),
        os.path.basename(xlsx_file),
    )
    shutil.copy2(xlsx_file, dest)
