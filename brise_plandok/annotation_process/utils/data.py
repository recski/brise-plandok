
from brise_plandok.annotation_process.utils.full_annotation_pre_filler import FullAnnotationPreFiller
from brise_plandok.annotation_process.utils.label_annotation_pre_filler import LabelAnnotationPreFiller


def generate_data(doc_ids, gen_attr_folder, data_folder, phase):
    if phase == 1:
        return [doc for doc in LabelAnnotationPreFiller().generate_for_label_annotation(doc_ids, gen_attr_folder, data_folder)]
    else:
        return [doc for doc in FullAnnotationPreFiller().generate_for_full_annotation(doc_ids, data_folder)]
