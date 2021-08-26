import argparse
from brise_plandok.review.excel_generator import ExcelGenerator
import logging
import sys
from brise_plandok.convert import Converter


class AnnotationConverter(Converter):

    def convert(self, annotated_xlsx_files):
        annotations = self.__read_annotations(annotated_xlsx_files)
        merged_annotations = self.__merge_annotations(annotations)
        self.__generate_review_excel(merged_annotations)

    def __read_annotations(self, annotated_xlsx_files):
        annotations = []
        for annotated_xlsx in annotated_xlsx_files:
            for doc in self.read(annotated_xlsx):
                annotations.append(doc)
        return annotations

    def __merge_annotations(self, annotations):
        merged_annotations = {}
        for annotation in annotations:
            if merged_annotations is None:
                merged_annotations = annotation
            for section in annotation["sections"]:
                for sen in section["sens"]:
                    self.__parse_sen(sen, merged_annotations)
        return merged_annotations

    def __parse_sen(self, sen, merged_annotations):
        if sen["sen_id"] not in merged_annotations:
            merged_annotations[sen["sen_id"]] = { "text" : sen["text"], "attributes": {} }
        for attribute in sen["attributes"]:
            merged_attributes = merged_annotations[sen["sen_id"]]["attributes"]
            if attribute["name"] not in merged_attributes:
                merged_attributes[attribute["name"]] = { "count" : 1 }
            else:
                merged_attributes[attribute["name"]]["count"] += 1

    def __generate_review_excel(self, merged_annotations):
        generator = ExcelGenerator()
        generator.generate_review_excel(merged_annotations)

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-of", "--output-file", type=str, default=None)
    parser.add_argument("-a", "--annotations", nargs="+", default=None)
    parser.set_defaults(input_format="XLSX", output_format="JSON")
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " +
               "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()
    converter = AnnotationConverter(args)
    converter.convert(args.annotations)

if __name__ == "__main__":
    main()