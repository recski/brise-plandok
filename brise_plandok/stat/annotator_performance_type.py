import argparse
import os
from collections import Counter

import numpy
import numpy as np
from tabulate import tabulate
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
    F1,
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
    agg_mic_mac = {}
    print("# Annotator performance - Types")
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
    collect_micro_and_macro_averages_per_ann(agg_per_ann, TYPES, agg_mic_mac)
    collect_micro_and_macro_averages_per_ann(agg_per_ann, ATTRIBUTES, agg_mic_mac)
    print_average_details(agg_mic_mac)
    print_category_aggregation(
        agg_per_type, "Per type / annotator aggregation", agg_per_ann, TYPES
    )
    print_category_aggregation(
        agg_per_attr, "Per attribute / annotator aggregation", agg_per_ann, ATTRIBUTES
    )
    print_category_details(agg_per_ann, "Per type / annotator details", TYPES, agg_mic_mac)
    print_category_details(
        agg_per_ann, "Per attribute / annotator details", ATTRIBUTES, agg_mic_mac
    )
    print_full_details(global_stat, agg_per_ann, "Per annotator / attribute / type details")


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


def print_category_aggregation(agg, title, agg_per_ann, category):
    print()
    print("## " + title)
    values = [["Name", FREQ, TP, FP, FN, PREC, REC]]
    aggr_values = [["Attr", FREQ, PREC, REC, F1]]
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

        p, r = stat[MICRO][PREC], stat[MICRO][REC]
        f1 = 0.0 if p + r == 0 else (2 * p * r) / (p + r)

        aggr_values.append(
            [
                cat,
                stat[MICRO][FREQ],
                stat[MICRO][PREC],
                stat[MICRO][REC],
                f1,
            ]
        )

        avg_collector = numpy.zeros(shape=(6, 2))
        row = 0
        for ann, ann_stat in agg_per_ann.items():
            micro_avg_per_cat = ann_stat[category][cat]
            values.append(
                [
                    ann,
                    micro_avg_per_cat[FREQ],
                    micro_avg_per_cat[TP],
                    micro_avg_per_cat[FP],
                    micro_avg_per_cat[FN],
                    micro_avg_per_cat[PREC],
                    micro_avg_per_cat[REC],
                ]
            )
            avg_collector[row][0] = micro_avg_per_cat[PREC]
            avg_collector[row][1] = micro_avg_per_cat[REC]
            row += 1
        avg = numpy.average(avg_collector, axis=0)
        values.append(
            [
                AVG,
                "",
                "",
                "",
                "",
                avg[0],
                avg[1],
            ]
        )
        std = numpy.std(avg_collector, axis=0)
        values.append(
            [
                STD,
                "",
                "",
                "",
                "",
                std[0],
                std[1],
            ]
        )
    print(make_markdown_table(values))
    print(
        tabulate(
            aggr_values[1:],
            headers=aggr_values[0],
            tablefmt="latex_booktabs",
            floatfmt=["s", "d"] + 3 * [".2%"],
        )
    )


def collect_micro_and_macro_averages_per_ann(agg_per_ann, category, agg_mic_mac):
    for ann, ann_stat in agg_per_ann.items():
        if ann not in agg_mic_mac:
            agg_mic_mac[ann] = {}
        if category not in agg_mic_mac[ann]:
            agg_mic_mac[ann][category] = {
                MICRO: Counter(),
                MACRO: {
                    PREC: [],
                    REC: [],
                },
            }
        micro = agg_mic_mac[ann][category][MICRO]
        macro = agg_mic_mac[ann][category][MACRO]
        for cat in ann_stat[category].keys():
            micro_avg_per_cat = ann_stat[category][cat]
            micro[FREQ] += micro_avg_per_cat[FREQ]
            micro[TP] += micro_avg_per_cat[TP]
            micro[FP] += micro_avg_per_cat[FP]
            micro[FN] += micro_avg_per_cat[FN]
            macro[PREC].append(micro_avg_per_cat[PREC])
            macro[REC].append(micro_avg_per_cat[REC])
        add_p_r(micro)


def print_average_details(agg_mic_mac):
    print()
    print("## Average summary")
    values = [
        [
            "Annotator",
            FREQ,
            TP,
            FP,
            FN,
            PREC + " (micro)",
            REC + " (micro)",
            PREC + " (macro - type)",
            REC + " (macro - type)",
            PREC + " (macro - attribute)",
            REC + " (macro - attribute)",
        ]
    ]
    global_averages_collector = numpy.zeros(shape=(len(agg_mic_mac.keys()), 6))
    row = 0
    freqs = []
    for ann, ann_averages in agg_mic_mac.items():
        micro = ann_averages[TYPES][MICRO]
        macro_type = ann_averages[TYPES][MACRO]
        macro_attributes = ann_averages[ATTRIBUTES][MACRO]
        macro_type_prec = numpy.average(macro_type[PREC])
        macro_type_rec = numpy.average(macro_type[REC])
        macro_attr_prec = numpy.average(macro_attributes[PREC])
        macro_attr_rec = numpy.average(macro_attributes[REC])
        values.append(
            [
                ann,
                micro[FREQ],
                micro[TP],
                micro[FP],
                micro[FN],
                micro[PREC],
                micro[REC],
                macro_type_prec,
                macro_type_rec,
                macro_attr_prec,
                macro_attr_rec,
            ]
        )
        global_averages_collector[row][0] = micro[PREC]
        global_averages_collector[row][1] = micro[REC]
        global_averages_collector[row][2] = macro_type_prec
        global_averages_collector[row][3] = macro_type_rec
        global_averages_collector[row][4] = macro_attr_prec
        global_averages_collector[row][5] = macro_attr_rec
        freqs.append(micro[FREQ])
        row += 1
    global_averages = np.average(global_averages_collector, axis=0)
    values.append(
        [
            AVG,
            "",
            "",
            "",
            "",
            global_averages[0],
            global_averages[1],
            global_averages[2],
            global_averages[3],
            global_averages[4],
            global_averages[5],
        ]
    )
    global_w_averages = np.average(global_averages_collector, weights=freqs, axis=0)
    values.append(
        [
            AVG + " weighted",
            "",
            "",
            "",
            "",
            global_w_averages[0],
            global_w_averages[1],
            global_w_averages[2],
            global_w_averages[3],
            global_w_averages[4],
            global_w_averages[5],
        ]
    )
    global_deviations = np.std(global_averages_collector, axis=0)
    values.append(
        [
            STD,
            "",
            "",
            "",
            "",
            global_deviations[0],
            global_deviations[1],
            global_deviations[2],
            global_deviations[3],
            global_deviations[4],
            global_deviations[5],
        ]
    )
    print(make_markdown_table(values))


def print_category_details(agg_per_ann, title, category, agg_mic_mac):
    print()
    print("## " + title)
    for ann, ann_stat in agg_per_ann.items():
        print(f"### Annotator {ann}")
        values = [["Name", FREQ, TP, FP, FN, PREC, REC]]
        for cat in ann_stat[category].keys():
            micro_avg_per_cat = ann_stat[category][cat]
            values.append(
                [
                    cat,
                    micro_avg_per_cat[FREQ],
                    micro_avg_per_cat[TP],
                    micro_avg_per_cat[FP],
                    micro_avg_per_cat[FN],
                    micro_avg_per_cat[PREC],
                    micro_avg_per_cat[REC],
                ]
            )
        micro = agg_mic_mac[ann][category][MICRO]
        values.append(
            [
                MICRO,
                micro[FREQ],
                micro[TP],
                micro[FP],
                micro[FN],
                micro[PREC],
                micro[REC],
            ]
        )
        macro = agg_mic_mac[ann][category][MACRO]
        values.append(
            [
                MACRO,
                "",
                "",
                "",
                "",
                numpy.average(macro[PREC]),
                numpy.average(macro[REC]),
            ]
        )
        print(make_markdown_table(values))


def print_full_details(global_stat, agg_per_ann, title):
    print()
    print("## " + title)
    for ann, ann_stat in global_stat.items():
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


def get_args():
    parser = argparse.ArgumentParser(description="")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    annotator_stat()
