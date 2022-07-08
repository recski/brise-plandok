import argparse
import os
import statistics
import statistics as st
from collections import Counter

from tuw_nlp.common.eval import count_p_r_f

from brise_plandok.constants import (
    DocumentFields,
    SenFields,
    FullAnnotatedAttributeFields,
    AnnotatedAttributeFields,
    AttributeFields,
)
from brise_plandok.stat.constants import (
    FIRST_STAGE_IDS,
    DATASET_FOLDERS,
    CNT,
    PLACEHOLDER,
    TP,
    FN,
    FP,
    AVG,
    STD,
    MICRO,
    MACRO,
    PREC,
    REC,
)
from brise_plandok.stat.utils import make_markdown_table, convert_back_post_processed
from brise_plandok.utils import load_json


def annotator_stat():
    attr_stat = {}

    with open(FIRST_STAGE_IDS) as f:
        first_stage_gold_ids = f.read().splitlines()

    for folder in DATASET_FOLDERS:
        for filename in os.listdir(folder):
            fn = os.path.join(folder, filename)
            doc = load_json(fn)
            add_ann_to_map_if_not_present(attr_stat, doc)
            ann_1 = doc[DocumentFields.FULL_ANNOTATORS][0]
            ann_2 = doc[DocumentFields.FULL_ANNOTATORS][1]

            for sen in doc[DocumentFields.SENS].values():
                if not sen[SenFields.SEGMENTATION_ERROR]:
                    add_attribute_stat(
                        ann_1, ann_2, attr_stat, sen, doc[DocumentFields.ID], first_stage_gold_ids
                    )
    attr_stat = sort_map(attr_stat)
    print_stat(attr_stat)


def sort_map(attr_stat):
    attr_stat = {k: v for k, v in sorted(attr_stat.items(), key=lambda item: item[0])}
    for ann, stat in attr_stat.items():
        attr_stat[ann] = {
            k: v
            for k, v in sorted(
                stat.items(), key=lambda item: (item[1][CNT], item[0]), reverse=True
            )
        }
    return attr_stat


def add_ann_to_map_if_not_present(attr_stat, doc):
    assert len(doc[DocumentFields.FULL_ANNOTATORS]) == 2
    for ann in doc[DocumentFields.FULL_ANNOTATORS]:
        if ann not in attr_stat:
            attr_stat[ann] = {}


def add_attribute_stat(ann_1, ann_2, attr_stat, sen, doc_id, first_stage_gold_ids):
    gold_attrs = set(convert_back_post_processed(sen[SenFields.GOLD_ATTRIBUTES].keys()))
    ann_attrs = {
        ann_1: set(),
        ann_2: set(),
    }
    fill_annotated_attributes(ann_attrs, doc_id, first_stage_gold_ids, sen)
    add_attr_stat(gold_attrs, ann_1, ann_attrs[ann_1], attr_stat)
    add_attr_stat(gold_attrs, ann_2, ann_attrs[ann_2], attr_stat)


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


def add_attr_stat(gold_attrs, ann, ann_attrs, attr_stat):
    for attr in gold_attrs | ann_attrs:
        if attr not in attr_stat[ann]:
            attr_stat[ann][attr] = Counter()
    for attr in gold_attrs & ann_attrs:
        attr_stat[ann][attr][TP] += 1
    for attr in gold_attrs.difference(ann_attrs):
        attr_stat[ann][attr][FN] += 1
    for attr in ann_attrs.difference(gold_attrs):
        attr_stat[ann][attr][FP] += 1
    for attr in gold_attrs:
        attr_stat[ann][attr][CNT] += 1


def print_stat(attr_stat):
    agg = {}
    print("# Annotator statistics - Attributes")
    print("This statistics is calculated without the sentences with a segmentation error.  ")
    print(
        "Post-processed attributes were converted back to their version at the time of annotation."
    )
    for ann, ann_stat in attr_stat.items():
        print(f"## Annotator {ann}")
        print_attribute_stat_for_ann(ann_stat, agg)
    print_agg(agg, AVG)
    print_agg(agg, STD)


def print_attribute_stat_for_ann(ann_stat, agg):
    agg_per_ann = {
        MICRO: Counter(),
        MACRO: {
            PREC: [],
            REC: [],
        },
    }
    values = [["Name", "CNT", "TP", "FP", "FN", "Precision", "Recall"]]
    p_r_f = count_p_r_f(ann_stat)
    for attr, stat_per_attr in ann_stat.items():
        prec = p_r_f[attr]["P"]
        rec = p_r_f[attr]["R"]
        append_row_for_attr(attr, prec, rec, stat_per_attr, values)
        add_aggregated_stat_for_ann(agg_per_ann, prec, rec, stat_per_attr)
        add_global_aggregated_stat(agg, attr, prec, rec)
    micro_p_r_f = count_p_r_f({MICRO: agg_per_ann[MICRO]})
    append_row_for_micro(agg_per_ann, micro_p_r_f, values)
    append_row_for_macro(agg_per_ann, values)
    print(make_markdown_table(values))


def add_aggregated_stat_for_ann(agg_per_ann, prec, rec, stat_per_attr):
    agg_per_ann[MICRO][CNT] += stat_per_attr[CNT]
    agg_per_ann[MICRO][TP] += stat_per_attr[TP]
    agg_per_ann[MICRO][FP] += stat_per_attr[FP]
    agg_per_ann[MICRO][FN] += stat_per_attr[FN]
    agg_per_ann[MACRO][PREC].append(prec)
    agg_per_ann[MACRO][REC].append(rec)


def add_global_aggregated_stat(agg, attr, prec, rec):
    if attr not in agg:
        agg[attr] = {
            PREC: [],
            REC: [],
        }
    agg[attr][PREC].append(prec)
    agg[attr][REC].append(rec)


def append_row_for_attr(attr, prec, rec, stat_per_attr, values):
    values.append(
        [
            attr,
            stat_per_attr[CNT],
            stat_per_attr[TP],
            stat_per_attr[FP],
            stat_per_attr[FN],
            prec,
            rec,
        ]
    )


def append_row_for_micro(agg_per_ann, micro_p_r_f, values):
    values.append(
        [
            MICRO,
            agg_per_ann[MICRO][CNT],
            agg_per_ann[MICRO][TP],
            agg_per_ann[MICRO][FP],
            agg_per_ann[MICRO][FN],
            micro_p_r_f[MICRO]["P"],
            micro_p_r_f[MICRO]["R"],
        ]
    )


def append_row_for_macro(agg_per_ann, values):
    values.append(
        [
            MACRO,
            "-",
            "-",
            "-",
            "-",
            statistics.mean(agg_per_ann[MACRO][PREC]),
            statistics.mean(agg_per_ann[MACRO][REC]),
        ]
    )


def print_agg(agg, name):
    if name == AVG:
        print("## Average")
    elif name == STD:
        print("## STD")
    values = [["Name", "Precision", "Recall"]]
    for attr, attr_stat in agg.items():
        agg_prec = 0
        agg_rec = 0
        if name == AVG:
            agg_prec = st.mean(attr_stat[PREC])
            agg_rec = st.mean(attr_stat[REC])
        elif name == STD:
            agg_prec = "NA"
            agg_rec = "NA"
            if len(attr_stat[PREC]) > 1:
                agg_prec = st.stdev(attr_stat[PREC])
            if len(attr_stat[REC]) > 1:
                agg_rec = st.stdev(attr_stat[REC])
        values.append([attr, agg_prec, agg_rec])
    print(make_markdown_table(values))


def get_args():
    parser = argparse.ArgumentParser(description="")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    annotator_stat()
