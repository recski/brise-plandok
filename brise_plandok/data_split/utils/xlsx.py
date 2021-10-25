

from brise_plandok.constants import DocumentFields, SenFields
from brise_plandok.data_split.utils.assignments import get_download_folder, update_assignments
import logging
from brise_plandok.data_split.utils.constants import ASSIGNMENT_ADDITIONAL_HEADER, ASSIGNMENT_DF_HEADER_BASE, FullAnnotationExcelConstants
import shutil
from brise_plandok.convert import Converter
import os
from brise_plandok.data_split.utils.full_annotation_excel_generator import FullAnnotationExcelGenerator
from brise_plandok.type_extraction.type_extractor import TypeExtractor
from brise_plandok.value_extraction.value_extractor import ValueExtractor


class ConverterArgs:
    def __init__(self, output_file):
        self.input_format = "JSON"
        self.output_format = "XLSX"
        self.output_file = output_file
        self.gen_attributes = True


def genereate_xlsx_files(docs, xlsx_folder, overwrite, phase):
    for doc in docs:
        doc_id = doc[DocumentFields.ID]
        xlsx_file = os.path.join(xlsx_folder, doc_id+".xlsx")
        if not overwrite and os.path.exists(xlsx_file):
            continue
        if phase == 1:
            Converter(ConverterArgs(xlsx_file)).write_xlsx(doc, xlsx_file)
        else:
            create_full_xlsx(doc, xlsx_file)
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

def create_full_xlsx(doc, xlsx_file):
    _fill_gen_attributes_for_phase_2(doc)
    FullAnnotationExcelGenerator(xlsx_file, FullAnnotationExcelConstants()).generate_excel(doc)


def _fill_gen_attributes_for_phase_2(doc):
    is_annotated = len(doc[DocumentFields.ANNOTATORS]) > 0
    value_extractor = ValueExtractor()
    type_extractor = TypeExtractor()
    for sen in doc[DocumentFields.SENS].values():
        labels_gold = sen[SenFields.LABELS_GOLD_EXISTS]
        attribute_names = _get_attributes_names(sen, labels_gold, is_annotated)
        for attribute in attribute_names:
            value_extractor.extract_for_attr(
                sen, attribute, SenFields.GEN_ATTRIBUTES_ON_FULL_ANNOTATION, False)
            type_extractor.extract_for_attr(
                sen, attribute, SenFields.GEN_ATTRIBUTES_ON_FULL_ANNOTATION, False)


def _get_attributes_names(sen, labels_gold, is_annotated):
    if labels_gold:
        attribute_names = sen[SenFields.GOLD_ATTRIBUTES].keys()
    elif is_annotated:
        attribute_names = sen[SenFields.ANNOTATED_ATTRIBUTES].keys()
    else:
        attribute_names = sen[SenFields.GEN_ATTRIBUTES_ON_ANNOTATION].keys()
    return attribute_names
