import argparse
import json
from utils import dump_json, load_json
from brise_plandok.constants import ANNOTATOR_NAME_INDEX, AnnotatedAttributeFields, AttributeFields, DocumentFields, OldDocumentFields, OldSectionFields, OldSenFields, SenFields
import os
from brise_plandok.review.excel_generator import ExcelGenerator
import logging
from brise_plandok.convert import Converter
from brise_plandok.attrs_from_gold import SenToAttrMap


class AnnotationConverter(Converter):

    def convert(self, annotated_xlsx_files, output_file, data_file):
        annotations = self._read_annotations(annotated_xlsx_files)
        assert data_file is not None
        data = load_json(data_file)
        self._fill_annotated_attributes(annotations, data)
        dump_json(data, data_file)
        self._generate_review_excel(data, output_file)

    def _read_annotations(self, annotated_xlsx_files):
        annotations = {}
        for annotated_xlsx in annotated_xlsx_files:
            annotator = os.path.normpath(annotated_xlsx).split(
                os.path.sep)[ANNOTATOR_NAME_INDEX]
            for doc in self.read(annotated_xlsx):
                annotations[annotator] = doc
        return annotations

    def _fill_annotated_attributes(self, annotations, data):
        self._clear_previous_annotation_info(data)
        for annotator, annotation in annotations.items():
            self._add_annotator(data, annotator)
            for section in annotation[OldDocumentFields.SECTIONS]:
                self._fill_for_section(section, data, annotator)

    def _clear_previous_annotation_info(self, data):
        data[DocumentFields.ANNOTATORS] = []
        for sen in data[DocumentFields.SENS].values():
            sen[SenFields.ANNOTATED_ATTRIBUTES] = {}

    def _add_annotator(self, data, annotator):
        if annotator in data[DocumentFields.ANNOTATORS]:
            raise ValueError(f"annotator {annotator} already added to document")
        data[DocumentFields.ANNOTATORS].append(annotator)

    def _fill_for_section(self, section, data, annotator):
        for sen in section[OldSectionFields.SENS]:
            self._fill_for_sen(sen, data, annotator)

    def _fill_for_sen(self, sen, data, annotator):
        sen_id = sen[OldSenFields.ID]
        annotated_attributes = data[DocumentFields.SENS][sen_id][SenFields.ANNOTATED_ATTRIBUTES]
        for attribute in sen[OldSenFields.ATTRIBUTES]:
            self._fill_for_attr(sen_id, data, attribute,
                                annotated_attributes, annotator)

    def _fill_for_attr(self, sen_id, data, attribute, annotated_attributes, annotator):
        assert sen_id in data[DocumentFields.SENS]
        attr_name = attribute[AttributeFields.NAME]
        if attr_name not in annotated_attributes:
            annotated_attributes[attr_name] = {
                AnnotatedAttributeFields.ANNOTATORS: [annotator]
            }
            return
        annotators = annotated_attributes[attr_name][AnnotatedAttributeFields.ANNOTATORS]
        if annotator not in annotators:
            annotators.append(annotator)

    def _generate_review_excel(self, data, output_file):
        generator = ExcelGenerator(output_file)
        generator.generate_review_excel(data)



def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-of", "--output-file", type=str)
    parser.add_argument("-a", "--annotations", nargs="+", default=None)
    parser.add_argument("-d", "--data-file", type=str, default=None)
    parser.set_defaults(input_format="XLSX", output_format="XLSX",
                        output_file="brise_plandok/review/output/review.xlsx",
                        gen_attributes=False)
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " +
               "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()
    converter = AnnotationConverter(args)
    converter.convert(args.annotations, args.output_file, args.data_file)


if __name__ == "__main__":
    main()
