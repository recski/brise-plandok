import argparse
from brise_plandok.constants import ANNOTATOR_NAME_INDEX
import os
from brise_plandok.review.excel_generator import ExcelGenerator
import logging
from brise_plandok.convert import Converter
from brise_plandok.attrs_from_gold import SenToAttrMap

class AnnotationConverter(Converter):

    def convert(self, annotated_xlsx_files, output_file, sen_to_gold_attrs):
        annotations = self.__read_annotations(annotated_xlsx_files)
        merged_annotations = self.__merge_annotations(annotations)
        self.__generate_review_excel(merged_annotations, output_file, sen_to_gold_attrs)

    def __read_annotations(self, annotated_xlsx_files):
        annotations = {}
        for annotated_xlsx in annotated_xlsx_files:
            annotator = os.path.normpath(annotated_xlsx).split(os.path.sep)[ANNOTATOR_NAME_INDEX]
            for doc in self.read(annotated_xlsx):
                annotations[annotator] = doc
        return annotations

    def __merge_annotations(self, annotations):
        merged_annotations = {}
        for annotator, annotation in annotations.items():
            if merged_annotations is None:
                merged_annotations = annotation
            for section in annotation["sections"]:
                for sen in section["sens"]:
                    self.__parse_sen(sen, merged_annotations, annotator)
        return merged_annotations

    def __parse_sen(self, sen, merged_annotations, annotator):
        if sen["sen_id"] not in merged_annotations:
            merged_annotations[sen["sen_id"]] = {
                "text": sen["text"], "attributes": {}}
        for attribute in sen["attributes"]:
            merged_attributes = merged_annotations[sen["sen_id"]]["attributes"]
            if attribute["name"] not in merged_attributes:
                merged_attributes[attribute["name"]] = {
                    "count": 1, "annotators": [annotator]}
            else:
                merged_attributes[attribute["name"]]["count"] += 1
                merged_attributes[attribute["name"]
                                  ]["annotators"].append(annotator)

    def __generate_review_excel(self, merged_annotations, output_file, sen_to_gold_attrs):
        generator = ExcelGenerator(output_file, sen_to_gold_attrs)
        generator.generate_review_excel(merged_annotations)


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-of", "--output-file", type=str)
    parser.add_argument("-a", "--annotations", nargs="+", default=None)
    parser.add_argument("-g", "--gold", type=str, default=None)
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
    sen_to_gold_attrs = SenToAttrMap(gold_dir=args.gold, fuzzy=True)
    converter.convert(args.annotations, args.output_file, sen_to_gold_attrs)


if __name__ == "__main__":
    main()
