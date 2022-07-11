import argparse
import os
import statistics
import statistics as st
from collections import Counter

from tuw_nlp.common.eval import count_p_r_f

from brise_plandok.constants import (
    DocumentFields,
    SenFields,
    EMPTY,
    AttributeFields,
    FullAnnotatedAttributeFields,
    AnnotatedAttributeFields,
    AttributeTypes,
)
from brise_plandok.stat.constants import (
    DATASET_FOLDERS,
    FREQ,
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
from brise_plandok.stat.utils import (
    make_markdown_table,
    convert_back_post_processed,
    collect_all_attributes,
)
from brise_plandok.utils import load_json


def annotator_stat():
    type_stat = {}
    attr_stat = Counter()
    annotators = set()
    attr_stat, _, annotators = collect_all_attributes(attr_stat, set(), annotators)
    fill_up_type_stat(type_stat, attr_stat, annotators)

    for folder in DATASET_FOLDERS:
        for filename in os.listdir(folder):
            fn = os.path.join(folder, filename)
            doc = load_json(fn)
            add_ann_to_map_if_not_present(type_stat, doc)
            ann_1 = doc[DocumentFields.FULL_ANNOTATORS][0]
            ann_2 = doc[DocumentFields.FULL_ANNOTATORS][1]

            for sen in doc[DocumentFields.SENS].values():
                if not sen[SenFields.SEGMENTATION_ERROR]:
                    add_type_stat(
                        sen,
                        ann_1,
                        ann_2,
                        type_stat,
                    )
    print_stat(type_stat)


def fill_up_type_stat(type_stat, attr_stat, annotators):
    for ann in annotators:
        type_stat[ann] = {}
        for attr in attr_stat:
            type_stat[ann][attr] = {
                AttributeTypes.CONDITION: Counter(),
                AttributeTypes.CONTENT: Counter(),
                AttributeTypes.CONDITION_EXCEPTION: Counter(),
                AttributeTypes.CONTENT_EXCEPTION: Counter(),
            }


def add_ann_to_map_if_not_present(attr_stat, doc):
    assert len(doc[DocumentFields.FULL_ANNOTATORS]) == 2
    for ann in doc[DocumentFields.FULL_ANNOTATORS]:
        if ann not in attr_stat:
            attr_stat[ann] = {}


def add_type_stat(sen, ann1, ann2, type_stat):
    for attr_name, attr in sen[SenFields.GOLD_ATTRIBUTES].items():
        if len(attr) != 1:
            continue
        ann_types = {
            ann1: EMPTY,
            ann2: EMPTY,
        }
        gold_attr = list(convert_back_post_processed({attr_name}))[0]
        gold_type = attr[0][AttributeFields.TYPE]
        if (
            FullAnnotatedAttributeFields.ATTRIBUTES in sen[SenFields.FULL_ANNOTATED_ATTRIBUTES]
            and gold_attr
            in sen[SenFields.FULL_ANNOTATED_ATTRIBUTES][FullAnnotatedAttributeFields.ATTRIBUTES]
        ):
            annotation = sen[SenFields.FULL_ANNOTATED_ATTRIBUTES][
                FullAnnotatedAttributeFields.ATTRIBUTES
            ][gold_attr]
            for ann_per_value in annotation[AttributeFields.VALUE].values():
                for ann_type, ann_per_type in ann_per_value[AttributeFields.TYPE].items():
                    for ann in ann_per_type[AnnotatedAttributeFields.ANNOTATORS]:
                        if ann_types[ann] == EMPTY or ann_type == gold_type:
                            ann_types[ann] = ann_type
        fill_type_stat(gold_attr, gold_type, ann1, ann_types[ann1], type_stat)
        fill_type_stat(gold_attr, gold_type, ann2, ann_types[ann2], type_stat)


def fill_type_stat(attr, gold_type, ann, ann_type, type_stat):
    if ann_type == gold_type:
        type_stat[ann][attr][gold_type][TP] += 1
    else:
        type_stat[ann][attr][gold_type][FN] += 1
        if ann_type != EMPTY:
            type_stat[ann][attr][ann_type][FP] += 1
    type_stat[ann][attr][gold_type][FREQ] += 1


def print_stat(type_stat):
    agg_per_attr = {}
    agg_per_type = {}
    print("# Annotator statistics - Types")
    print(
        "This statistics is calculated without the sentences with a segmentation error.  \n"
        "Post-processed attributes were converted back to their version at the time of annotation.  \n\n"
        "For complexity reasons, agreement is only calculated for cases, where the attribute occurs in gold exactly "
        "once, and where the annotator gave at least one annotation for the attribute. "
        "In case the annotator labeled the attribute within the same sentence multiple times, "
        "the most beneficial type annotation is taken into account, i.e. if the annotator labeled both gold and "
        "non-gold types, then we regard the gold one."
    )
    for ann, ann_stat in type_stat.items():
        print(f"## Annotator {ann}")
        print_attribute_stat_for_ann(ann_stat, agg_per_attr, agg_per_type)
    # print_agg(agg, AVG)
    # print_agg(agg, STD)


def print_attribute_stat_for_ann(ann_stat, agg_per_attr, agg_per_tpe):
    # agg_per_ann = {}
    values = [["Name", FREQ, TP, FP, FN, PREC, REC]]
    for attr, stat_per_attr in ann_stat.items():
        if attr not in agg_per_attr:
            agg_per_attr[attr] = {
                MICRO: Counter(),
                MACRO: {
                    PREC: [],
                    REC: [],
                },
            }
        attr_cnt = get_attr_cnt(stat_per_attr)
        values.append([attr, attr_cnt, "", "", "", "", ""])
        p_r_f = count_p_r_f(stat_per_attr)
        for attr_type, type_stat in stat_per_attr.items():
            if attr_type not in agg_per_tpe:
                agg_per_tpe[attr_type] = {
                    MICRO: Counter(),
                    MACRO: {
                        PREC: [],
                        REC: [],
                    },
                }
            prec = p_r_f[attr_type]["P"]
            rec = p_r_f[attr_type]["R"]
            append_row_for_attr(attr_type, prec, rec, type_stat, values)
            # add_aggregated_stat_for_ann(agg_per_ann, prec, rec, stat_per_attr)
            # add_global_aggregated_stat(agg, attr, prec, rec)
    # micro_p_r_f = count_p_r_f({MICRO: agg_per_ann[MICRO]})
    # append_row_for_micro(agg_per_ann, micro_p_r_f, values)
    # append_row_for_macro(agg_per_ann, values)
    print(make_markdown_table(values))


def get_attr_cnt(stat_per_attr):
    attr_cnt = (
        stat_per_attr[AttributeTypes.CONDITION][FREQ]
        + stat_per_attr[AttributeTypes.CONTENT][FREQ]
        + stat_per_attr[AttributeTypes.CONDITION_EXCEPTION][FREQ]
        + stat_per_attr[AttributeTypes.CONTENT_EXCEPTION][FREQ]
    )
    return attr_cnt


def add_aggregated_stat_for_ann(agg_per_ann, prec, rec, stat_per_attr):
    agg_per_ann[MICRO][FREQ] += stat_per_attr[FREQ]
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


def append_row_for_attr(attr_type, prec, rec, stat_per_type, values):
    values.append(
        [
            attr_type,
            stat_per_type[FREQ],
            stat_per_type[TP],
            stat_per_type[FP],
            stat_per_type[FN],
            prec,
            rec,
        ]
    )


def append_row_for_micro(agg_per_ann, micro_p_r_f, values):
    values.append(
        [
            MICRO,
            agg_per_ann[MICRO][FREQ],
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
    values = [["Name", PREC, REC]]
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
