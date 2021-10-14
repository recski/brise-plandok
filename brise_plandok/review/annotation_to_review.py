import argparse
from utils import dump_json, load_json
from brise_plandok.constants import ANNOTATOR_NAME_INDEX, AnnotatedAttributeFields, AttributeFields, DocumentFields, OldDocumentFields, OldSectionFields, OldSenFields, SenFields
import os
from brise_plandok.review.excel_generator import ExcelGenerator
import logging
from brise_plandok.convert import Converter
from brise_plandok.attrs_from_gold import SenToAttrMap, attrs_from_gold_sen


class AnnotationConverter(Converter):

    def __init__(self, args):
        super().__init__(args)
        self.sen_to_attr = SenToAttrMap(args.gold_folder, fuzzy=True)
        self.review = args.review

    def convert(self, annotated_xlsx_files, output_file, data_file):
        annotations = self._read_annotations(annotated_xlsx_files)
        assert data_file is not None
        doc = load_json(data_file)
        self._fill_reviewers(doc, output_file)
        self._fill_annotated_attributes(annotations, doc)
        self._fill_with_gold(doc)
        dump_json(doc, data_file)
        self._generate_review_excel(doc, output_file)

    def _read_annotations(self, annotated_xlsx_files):
        annotations = {}
        for annotated_xlsx in annotated_xlsx_files:
            annotator = os.path.normpath(annotated_xlsx).split(
                os.path.sep)[ANNOTATOR_NAME_INDEX]
            for doc in self.read(annotated_xlsx):
                annotations[annotator] = doc
        return annotations

    def _fill_reviewers(self, data, output_fn):
        if not self.review:
            logging.info(f"Review = false for {data[DocumentFields.ID]}, no reviewers will be added to data.")
            return
        reviewer = os.path.basename(output_fn).split('.')[0].split('_')[1]
        if DocumentFields.REVIEWERS not in data:
            data[DocumentFields.REVIEWERS] = [reviewer]
            return
        if reviewer in set(data[DocumentFields.REVIEWERS]):
            logging.warning(f"reviewer {reviewer} is already among reviewers")
            return
        data[DocumentFields.REVIEWERS].append(reviewer)


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

    def _fill_with_gold(self, doc):
        for sen in doc[DocumentFields.SENS].values():
            attrs_from_gold_sen(sen, self.sen_to_attr, False)

    def _generate_review_excel(self, data, output_file):
        if not self.review:
            logging.info(f"Review = false for {data[DocumentFields.ID]}, no review excel will be generated.")
            return
        generator = ExcelGenerator(output_file)
        generator.generate_review_excel(data)



def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-of", "--output-file", type=str)
    parser.add_argument("-a", "--annotations", nargs="+", default=None)
    parser.add_argument("-d", "--data-file", type=str, default=None)
    parser.add_argument("-g", "--gold-folder", type=str, default=None)
    parser.add_argument("-r", "--review", default=False, action="store_true")
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
