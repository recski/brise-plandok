import argparse
import os
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
    ATTRIBUTES,
    TYPES,
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


def print_stat(global_stat):
    agg_per_attr = {}
    agg_per_type = {}
    agg_per_ann = {}
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
    collect_aggregation(global_stat, agg_per_attr, agg_per_type, agg_per_ann)
    print_category_aggregation(agg_per_type, "Per type summary")
    print_category_aggregation(agg_per_attr, "Per attribute summary")
    print_category_details(agg_per_ann, "Per type details", TYPES)
    print_category_details(agg_per_ann, "Per attribute details", ATTRIBUTES)
    print_full_details(global_stat, agg_per_ann)


def collect_aggregation(global_stat, agg_per_attr, agg_per_type, agg_per_ann):
    for ann, ann_stat in global_stat.items():
        if ann not in agg_per_ann:
            agg_per_ann[ann] = {
                ATTRIBUTES: {},
                TYPES: {},
            }
        agg_attr_per_ann = agg_per_ann[ann][ATTRIBUTES]
        agg_types_per_ann = agg_per_ann[ann][TYPES]
        for attr, stat_per_attr in ann_stat.items():
            if attr not in agg_per_attr:
                agg_per_attr[attr] = {
                    MICRO: Counter(),
                    MACRO: {
                        PREC: [],
                        REC: [],
                    },
                }
            if attr not in agg_attr_per_ann:
                agg_attr_per_ann[attr] = Counter()
            for attr_type, type_stat in stat_per_attr.items():
                if attr_type not in agg_per_type:
                    agg_per_type[attr_type] = {
                        MICRO: Counter(),
                        MACRO: {
                            PREC: [],
                            REC: [],
                        },
                    }
                if attr_type not in agg_types_per_ann:
                    agg_types_per_ann[attr_type] = Counter()
                aggregate(agg_types_per_ann[attr_type], type_stat)
                aggregate(agg_per_type[attr_type][MICRO], type_stat)
                aggregate(agg_attr_per_ann[attr], type_stat)
                aggregate(agg_per_attr[attr][MICRO], type_stat)
        append_p_r_to_macro(agg_attr_per_ann, agg_per_attr)
        append_p_r_to_macro(agg_types_per_ann, agg_per_type)
    calculate_micro_avg(agg_per_type)
    calculate_micro_avg(agg_per_attr)


def append_p_r_to_macro(agg_cat_per_ann, agg_per_cat):
    for cat in agg_cat_per_ann.keys():
        add_p_r(agg_cat_per_ann[cat])
        agg_per_cat[cat][MACRO][PREC].append(agg_cat_per_ann[cat][PREC])
        agg_per_cat[cat][MACRO][REC].append(agg_cat_per_ann[cat][REC])


def calculate_micro_avg(collector):
    for category in collector.keys():
        add_p_r(collector[category][MICRO])


def add_p_r(collector):
    p_r_f_micro = count_p_r_f({"dummy": collector})
    collector[PREC] = p_r_f_micro["dummy"]["P"]
    collector[REC] = p_r_f_micro["dummy"]["R"]


def aggregate(counter, type_stat):
    counter[FREQ] += type_stat[FREQ]
    counter[TP] += type_stat[TP]
    counter[FP] += type_stat[FP]
    counter[FN] += type_stat[FN]


def print_category_aggregation(agg, title):
    print()
    print("## " + title)
    values = [["Name", FREQ, TP, FP, FN, PREC, REC]]
    for cat, stat in agg.items():
        values.append([cat, "", "", "", "", "", ""])
        values.append(
            [
                MICRO,
                stat[MICRO][FREQ],
                stat[MICRO][TP],
                stat[MICRO][FP],
                stat[MICRO][FN],
                stat[MICRO][PREC],
                stat[MICRO][REC],
            ]
        )
    print(make_markdown_table(values))


def print_category_details(agg_per_ann, title, category):
    print()
    print("## " + title)
    for ann, ann_stat in agg_per_ann.items():
        print(f"### Annotator {ann}")
        values = [["Name", FREQ, TP, FP, FN, PREC, REC]]
        for cat in ann_stat[category].keys():
            micro_avg = ann_stat[category][cat]
            values.append(
                [
                    cat,
                    micro_avg[FREQ],
                    micro_avg[TP],
                    micro_avg[FP],
                    micro_avg[FN],
                    micro_avg[PREC],
                    micro_avg[REC],
                ]
            )
        print(make_markdown_table(values))


def print_full_details(global_stat, agg_per_ann):
    for ann, ann_stat in global_stat.items():
        print()
        print("## Full details")
        print(f"### Annotator {ann}")
        values = [["Name", FREQ, TP, FP, FN, PREC, REC]]
        for attr, stat_per_attr in ann_stat.items():
            values.append([attr, agg_per_ann[ann][ATTRIBUTES][attr][FREQ], "", "", "", "", ""])
            p_r_f = count_p_r_f(stat_per_attr)
            for attr_type, type_stat in stat_per_attr.items():
                values.append(
                    [
                        attr_type,
                        type_stat[FREQ],
                        type_stat[TP],
                        type_stat[FP],
                        type_stat[FN],
                        (p_r_f[attr_type]["P"]),
                        (p_r_f[attr_type]["R"]),
                    ]
                )
            micro_stat_attr = agg_per_ann[ann][ATTRIBUTES][attr]
            values.append(
                [
                    MICRO,
                    micro_stat_attr[FREQ],
                    micro_stat_attr[TP],
                    micro_stat_attr[FP],
                    micro_stat_attr[FN],
                    micro_stat_attr[PREC],
                    micro_stat_attr[REC],
                ]
            )
        print(make_markdown_table(values))


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
