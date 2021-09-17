

from brise_plandok.data_split.utils.data import create_data
from brise_plandok.attrs_from_gold import SenToAttrMap
from brise_plandok.data_split.utils.assignments import update_assignments
import logging
from brise_plandok.data_split.utils.constants import ANNOTATOR_DOWNLOAD_FOLDER, ASSIGNMENT_ADDITIONAL_HEADER, ASSIGNMENT_DF_HEADER, ASSIGNMENT_XLSX
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


def genereate_xlsx_files(doc_ids, json_folder, xlsx_folder, overwrite, data_folder):
    sen_to_gold_attrs = SenToAttrMap(
            gold_dir=data_folder, fuzzy=True) if data_folder else None
    for doc_id in doc_ids:
        xlsx_file = os.path.join(xlsx_folder, doc_id+".xlsx")
        if not overwrite and os.path.exists(xlsx_file):
            continue

        full_data_file = os.path.join(data_folder, doc_id+".json")
        json_file = os.path.join(json_folder, doc_id+".jsonl")

        doc = _get_doc(json_file, full_data_file, doc_id, sen_to_gold_attrs)
        Converter(ConverterArgs(xlsx_file)).write_xlsx(doc, xlsx_file)
    logging.info("xlsx files have been generated from json files")


def _get_doc(json_file, full_data_file, doc_id, sen_to_gold_attrs):
    full_data = _get_full_data(full_data_file)
    if full_data is not None:
        logging.info(
            f"Full data json already exists. The content of this file will be used w/o any modification: {full_data_file}")
        return full_data
    gen_attrs = _get_gen_attrs(json_file)
    return create_data(doc_id, gen_attrs, sen_to_gold_attrs, full_data_file)


def _get_full_data(data_file):
    if os.path.exists(data_file):
        with open(data_file) as f:
            return json.load(f)
    return None


def _get_gen_attrs(json_file):
    with open(json_file) as f:
        lines = f.readlines()
        assert len(lines) == 1
        return json.loads(lines[0].strip())


def distribute_xlsx_files(xlsx_folder, df, annotators_folder, update):
    for _, assignment in df.iterrows():
        annotator = assignment[ASSIGNMENT_DF_HEADER[0]]
        doc_ids_for_annotator = assignment[ASSIGNMENT_ADDITIONAL_HEADER[0]].split(
            ',')
        for doc_id in doc_ids_for_annotator:
            _copy_xlsx_files_to_annotators(
                doc_id, xlsx_folder, annotators_folder, annotator)
        if update:
            update_assignments(doc_ids_for_annotator,
                               annotator, annotators_folder)
    logging.info("xlsx files have been distributed to annotators")


def _copy_xlsx_files_to_annotators(doc_id, xlsx_folder, annotators_folder, annotator):
    xlsx_file = os.path.join(xlsx_folder, doc_id+".xlsx")
    dest = os.path.join(annotators_folder, annotator,
                        ANNOTATOR_DOWNLOAD_FOLDER, os.path.basename(xlsx_file))
    shutil.copy2(xlsx_file, dest)