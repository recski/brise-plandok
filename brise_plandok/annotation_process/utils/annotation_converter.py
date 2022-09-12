import os

from brise_plandok import logger
from brise_plandok.annotation_process.utils.convert import Converter
from brise_plandok.constants import DocumentFields


class AnnotationConverter(Converter):
    def __init__(self, args):
        super().__init__(args)
        self.review = args.review

    def _fill_reviewers(self, data, output_fn, reviewers_field):
        if not self.review:
            logger.info(
                f"Review = false for {data[DocumentFields.ID]}, no labels_reviewers will be added to data."
            )
            return
        reviewer = os.path.basename(output_fn).split(".")[0].split("_")[-1]
        if reviewers_field not in data:
            data[reviewers_field] = [reviewer]
            return
        if reviewer in set(data[reviewers_field]):
            logger.warning(f"reviewer {reviewer} is already among labels_reviewers")
            return
        data[reviewers_field].append(reviewer)

    def _clear_previous_annotation_info(self, data, annotators_field, annotated_attribute_field):
        data[annotators_field] = []
        for sen in data[DocumentFields.SENS].values():
            sen[annotated_attribute_field] = {}

    def _add_annotator(self, data, annotator, annotators_field):
        if annotator in data[annotators_field]:
            raise ValueError(f"annotator {annotator} already added to document")
        data[annotators_field].append(annotator)
