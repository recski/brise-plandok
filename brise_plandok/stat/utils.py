import os

from numpy import dtype

from brise_plandok.constants import (
    AttributesNames,
    SenFields,
    AnnotatedAttributeFields,
    FullAnnotatedAttributeFields,
    AttributeFields,
    DocumentFields,
)
from brise_plandok.stat.constants import PLACEHOLDER, DATASET_FOLDERS
from brise_plandok.utils import load_json


def make_markdown_table(array):
    """Input: Python lists with rows of table as lists
               First element as header.
        Output: String to put into a .md file

    Ex Input:
        [["Name", "Age", "Height"],
         ["Jake", 20, 5'10],
         ["Mary", 21, 5'7]]

    Source: https://gist.github.com/m0neysha/219bad4b02d2008e0154
    """

    markdown = "\n" + str("| ")

    for e in array[0]:
        to_add = " " + str(e) + str(" |")
        markdown += to_add
    markdown += "\n"

    markdown += "|"
    for i in range(len(array[0])):
        markdown += str("-------------- | ")
    markdown += "\n"

    for entry in array[1:]:
        markdown += str("| ")
        for e in entry:
            if type(e) == int or type(e) == tuple:
                e = str(e)
            elif type(e) == float or type(e) == dtype("float64"):
                e = f"{e:.3f}"
            to_add = e + str(" | ")
            markdown += to_add
        markdown += "\n"

    return markdown + "\n"


def convert_back_post_processed(gold_attrs):
    if AttributesNames.Widmung in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.Widmung}) | {"WidmungUndZweckbestimmung"}
    if AttributesNames.Nutzungsart in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.Nutzungsart}) | {"WidmungUndZweckbestimmung"}
    if AttributesNames.BBAllgemein in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.BBAllgemein}) | {"WidmungUndZweckbestimmung"}
    if AttributesNames.BebauteFlaecheMax in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.BebauteFlaecheMax}) | {"Flaechen"}
    if AttributesNames.BebauteFlaecheMin in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.BebauteFlaecheMin}) | {"Flaechen"}
    if AttributesNames.BebauteFlaecheMaxProzentual in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.BebauteFlaecheMaxProzentual}) | {"Flaechen"}
    if AttributesNames.BebauteFlaecheMaxNebengebaeude in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.BebauteFlaecheMaxNebengebaeude}) | {"Flaechen"}
    if AttributesNames.GesamtePlangebiet in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.GesamtePlangebiet}) | {"PlangebietAllgemein"}
    if AttributesNames.GebaeudeHoeheMaxWN in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.GebaeudeHoeheMaxWN}) | {"GebaeudeHoeheMax"}
    if AttributesNames.GebaeudeHoeheMaxAbsolut in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.GebaeudeHoeheMaxAbsolut}) | {
            "GebaeudeHoeheMax"
        }
    return gold_attrs


def fill_annotated_attributes(attr_stat, doc_id, first_stage_gold_ids, sen):
    if doc_id in first_stage_gold_ids:
        for attr, annotation in sen[SenFields.ANNOTATED_ATTRIBUTES].items():
            if attr == PLACEHOLDER:
                continue
            for ann in annotation[AnnotatedAttributeFields.ANNOTATORS]:
                attr_stat[ann].add(attr)
    else:
        if FullAnnotatedAttributeFields.ATTRIBUTES in sen[SenFields.FULL_ANNOTATED_ATTRIBUTES]:
            for attr, annotation in sen[SenFields.FULL_ANNOTATED_ATTRIBUTES][
                FullAnnotatedAttributeFields.ATTRIBUTES
            ].items():
                for ann_per_value in annotation[AttributeFields.VALUE].values():
                    for ann_per_type in ann_per_value[AttributeFields.TYPE].values():
                        for ann in ann_per_type[AnnotatedAttributeFields.ANNOTATORS]:
                            attr_stat[ann].add(attr)


def get_ann_pair(doc):
    return tuple(
        sorted(
            [
                (doc[DocumentFields.FULL_ANNOTATORS][0]),
                (doc[DocumentFields.FULL_ANNOTATORS][1]),
            ]
        )
    )


def collect_all_attributes(attr_stat, annotator_pairs):
    for folder in DATASET_FOLDERS:
        for filename in os.listdir(folder):
            fn = os.path.join(folder, filename)
            doc = load_json(fn)
            ann_pair = doc[DocumentFields.FULL_ANNOTATORS]
            assert len(ann_pair) == 2
            annotator_pairs.add(tuple(sorted(ann_pair)))
            for sen in doc[DocumentFields.SENS].values():
                full_annotated_attrs = (
                    set(
                        sen[SenFields.FULL_ANNOTATED_ATTRIBUTES][
                            FullAnnotatedAttributeFields.ATTRIBUTES
                        ].keys()
                    )
                    if FullAnnotatedAttributeFields.ATTRIBUTES
                    in sen[SenFields.FULL_ANNOTATED_ATTRIBUTES]
                    else set()
                )
                all_occurring_attributes = convert_back_post_processed(
                    set(sen[SenFields.GOLD_ATTRIBUTES].keys())
                    | set(sen[SenFields.ANNOTATED_ATTRIBUTES].keys())
                    | full_annotated_attrs
                ).difference({PLACEHOLDER})
                for attr in all_occurring_attributes:
                    attr_stat[attr] += 1
    return {
        k: v
        for k, v in sorted(attr_stat.items(), key=lambda item: (item[1], item[0]), reverse=True)
    }, sorted(annotator_pairs)


def fill_up_kappa_stat(kappa_stat, attr_stat, annotator_pairs):
    for attr in attr_stat:
        kappa_stat[attr] = {}
        for ann_pair in annotator_pairs:
            kappa_stat[attr][ann_pair] = {
                ann_pair[0]: [],
                ann_pair[1]: [],
            }


def append_header_for_attr_wise_kappa(annotator_pairs, values):
    header = ["Attr", "Freq", "Macro", "Weighted"]
    for ann_pair in annotator_pairs:
        header.append(ann_pair)
    values.append(header)
