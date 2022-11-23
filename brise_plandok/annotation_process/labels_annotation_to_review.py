import argparse
import os

from brise_plandok import logger
from brise_plandok.annotation_process.attrs_from_gold import SenToAttrMap, attrs_from_gold_sen
from brise_plandok.annotation_process.utils.annotation_converter import (
    AnnotationConverter,
)
from brise_plandok.annotation_process.utils.constants import LabelReviewExcelConstants
from brise_plandok.annotation_process.utils.label_review_excel_generator import (
    LabelReviewExcelGenerator,
)
from brise_plandok.constants import (
    ANNOTATOR_NAME_INDEX,
    AnnotatedAttributeFields,
    AttributeFields,
    DocumentFields,
    OldDocumentFields,
    OldSectionFields,
    OldSenFields,
    SenFields,
)
from brise_plandok.utils import dump_json, load_json


class LabelAnnotationConverter(AnnotationConverter):
    def __init__(self, args):
        super().__init__(args)
        self.sen_to_attr = SenToAttrMap(args.gold_folder, fuzzy=False)
        self.review = args.review

    def convert(self, annotated_xlsx_files, output_file, data_file):
        annotations = self._read_annotations(annotated_xlsx_files)
        assert data_file is not None
        doc = load_json(data_file)
        self._fill_reviewers(doc, output_file, DocumentFields.LABELS_REVIEWERS)
        self._fill_annotated_attributes(annotations, doc)
        self._fill_with_gold(doc)
        dump_json(doc, data_file)
        self._generate_review_excel(doc, output_file)

    def _read_annotations(self, annotated_xlsx_files):
        annotations = {}
        for annotated_xlsx in annotated_xlsx_files:
            annotator = os.path.normpath(annotated_xlsx).split(os.path.sep)[ANNOTATOR_NAME_INDEX]
            for doc in self.read(annotated_xlsx):
                annotations[annotator] = doc
        return annotations

    def _fill_annotated_attributes(self, annotations, data):
        self._clear_previous_annotation_info(
            data, DocumentFields.ANNOTATORS, SenFields.ANNOTATED_ATTRIBUTES
        )
        for annotator, annotation in annotations.items():
            self._add_annotator(data, annotator, DocumentFields.ANNOTATORS)
            for section in annotation[OldDocumentFields.SECTIONS]:
                self._fill_for_section(section, data, annotator)

    def _fill_for_section(self, section, data, annotator):
        for sen in section[OldSectionFields.SENS]:
            self._fill_for_sen(sen, data, annotator)

    def _fill_for_sen(self, sen, data, annotator):
        sen_id = sen[OldSenFields.ID]
        annotated_attributes = data[DocumentFields.SENS][sen_id][SenFields.ANNOTATED_ATTRIBUTES]
        for attribute in sen[OldSenFields.ATTRIBUTES]:
            self._fill_for_attr(sen_id, data, attribute, annotated_attributes, annotator)

    def _fill_for_attr(self, sen_id, data, attribute, annotated_attributes, annotator):
        assert sen_id in data[DocumentFields.SENS]
        attr_name = attribute[AttributeFields.NAME]
        if attr_name not in annotated_attributes:
            annotated_attributes[attr_name] = {AnnotatedAttributeFields.ANNOTATORS: [annotator]}
            return
        annotators = annotated_attributes[attr_name][AnnotatedAttributeFields.ANNOTATORS]
        if annotator not in annotators:
            annotators.append(annotator)

    def _fill_with_gold(self, doc):
        for sen in doc[DocumentFields.SENS].values():
            attrs_from_gold_sen(sen, self.sen_to_attr, False)

    def _generate_review_excel(self, data, output_file):
        if not self.review:
            logger.info(
                f"Review = false for {data[DocumentFields.ID]}, no review excel will be generated."
            )
            return
        generator = LabelReviewExcelGenerator(output_file, LabelReviewExcelConstants(), data)
        generator.generate_excel()


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-of", "--output-file", type=str)
    parser.add_argument("-a", "--annotations", nargs="+", default=None)
    parser.add_argument("-d", "--data-file", type=str, default=None)
    parser.add_argument("-g", "--gold-folder", type=str, default=None)
    parser.add_argument("-r", "--review", default=False, action="store_true")
    parser.set_defaults(input_format="XLSX", output_format="XLSX", gen_attributes=False)
    return parser.parse_args()


def main():
    args = get_args()
    converter = LabelAnnotationConverter(args)
    converter.convert(args.annotations, args.output_file, args.data_file)


if __name__ == "__main__":
    main()
