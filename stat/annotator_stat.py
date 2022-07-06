import argparse
import os
import statistics as st

from brise_plandok.constants import (
    DocumentFields,
    SenFields,
    FullAnnotatedAttributeFields,
    AnnotatedAttributeFields,
)
from brise_plandok.utils import load_json, make_markdown_table

DATASET_FOLDERS = ["data/train", "data/valid", "data/test"]
FIRST_STAGE_IDS = "stat/first_stage_gold_ids.txt"

TYPES = "types"
MOD = "modality"
ATTR = "attributes"
TP = "TP"
FP = "FP"
FN = "FN"
CNT_ALL = "cnt_all"
CNT_RULE = "cnt_rule"
EMPTY = "_empty"
PREC = "prec"
REC = "rec"
CORR_ALL_RATIO = "corr_all_ratio"
CORR_RULE_RATIO = "corr_rule_ratio"
AVG = "avg"
STD = "std"


def annotator_stat():
    ann_map = {}

    # first_stage_gold_ids = None
    # with open(FIRST_STAGE_IDS) as f:
    #     first_stage_gold_ids = f.read().splitlines()
    for folder in DATASET_FOLDERS:
        for filename in os.listdir(folder):
            fn = os.path.join(folder, filename)
            doc = load_json(fn)
            add_ann_to_map_if_not_present(ann_map, doc)
            ann_1 = doc[DocumentFields.FULL_ANNOTATORS][0]
            ann_2 = doc[DocumentFields.FULL_ANNOTATORS][1]

            for sen in doc[DocumentFields.SENS].values():
                if not sen[SenFields.SEGMENTATION_ERROR]:
                    add_modality_stat(ann_1, ann_2, ann_map, sen)
    ann_map = {k: v for k, v in sorted(ann_map.items(), key=lambda item: item[0])}
    for ann, stat in ann_map.items():
        stat[MOD] = {
            k: v for k, v in sorted(stat[MOD].items(), key=lambda item: item[0], reverse=True)
        }
    print_stat(ann_map)


def add_modality_stat(ann_1, ann_2, ann_map, sen):
    ann_map[ann_1][MOD][CNT_ALL] += 1
    ann_map[ann_2][MOD][CNT_ALL] += 1
    ann_modalities = {
        ann_1: EMPTY,
        ann_2: EMPTY,
    }
    gold_mod = sen[SenFields.GOLD_MODALITY]
    if gold_mod is None:
        gold_mod = EMPTY
        # if FullAnnotatedAttributeFields.MODALITY in sen[SenFields.FULL_ANNOTATED_ATTRIBUTES]:
        #     print(sen[SenFields.ID])
    else:
        ann_map[ann_1][MOD][CNT_RULE] += 1
        ann_map[ann_2][MOD][CNT_RULE] += 1
    if FullAnnotatedAttributeFields.MODALITY in sen[SenFields.FULL_ANNOTATED_ATTRIBUTES]:
        for mod, annotators in sen[SenFields.FULL_ANNOTATED_ATTRIBUTES][
            FullAnnotatedAttributeFields.MODALITY
        ].items():
            for ann in annotators[AnnotatedAttributeFields.ANNOTATORS]:
                assert ann_modalities[ann] == EMPTY
                ann_modalities[ann] = mod
    for ann, mod in ann_modalities.items():
        assert mod is not None
        if gold_mod not in ann_map[ann][MOD]:
            ann_map[ann][MOD][gold_mod] = {
                TP: 0,
                FP: 0,
                FN: 0,
            }
        if mod not in ann_map[ann][MOD]:
            ann_map[ann][MOD][mod] = {
                TP: 0,
                FP: 0,
                FN: 0,
            }
        if gold_mod == mod:
            ann_map[ann][MOD][gold_mod][TP] += 1
        else:
            ann_map[ann][MOD][gold_mod][FN] += 1
            ann_map[ann][MOD][mod][FP] += 1


def add_ann_to_map_if_not_present(ann_map, doc):
    assert len(doc[DocumentFields.FULL_ANNOTATORS]) == 2
    for ann in doc[DocumentFields.FULL_ANNOTATORS]:
        if ann not in ann_map:
            ann_map[ann] = {
                MOD: {
                    CNT_ALL: 0,
                    CNT_RULE: 0,
                },
                ATTR: {},
                TYPES: {},
            }


def print_stat(ann_map):
    print("# Annotator statistics")
    print()
    print("This statistics is calculated without the sentences with a segmentation error.")
    agg = {
        MOD: {
            CORR_ALL_RATIO: [],
            CORR_RULE_RATIO: [],
        }
    }
    for ann, ann_stat in ann_map.items():
        print(f"## Annotator {ann}")
        print_modality(ann_stat, agg)
    print_agg(agg, AVG)
    print_agg(agg, STD)


def print_modality(ann_stat, agg):
    print("### Modality")
    values = [["Name", "TP", "FP", "FN", "Precision", "Recall"]]
    all_true = 0
    for mod, mod_stat in ann_stat[MOD].items():
        if mod == CNT_RULE or mod == CNT_ALL:
            continue
        prec = mod_stat[TP] / (mod_stat[TP] + mod_stat[FP])
        rec = mod_stat[TP] / (mod_stat[TP] + mod_stat[FN])
        all_true += mod_stat[TP]
        values.append([mod, mod_stat[TP], mod_stat[FP], mod_stat[FN], prec, rec])
        if mod not in agg[MOD]:
            agg[MOD][mod] = {
                PREC: [],
                REC: [],
            }
        agg[MOD][mod][PREC].append(prec)
        agg[MOD][mod][REC].append(rec)
    correct_all = values[1][1] + values[2][1] + values[3][1] + values[4][1]
    correct_all_ratio = correct_all / ann_stat[MOD][CNT_ALL]
    correct_rules = values[1][1] + values[2][1] + values[3][1]
    correct_rules_ratio = correct_rules / ann_stat[MOD][CNT_RULE]
    print(f"Correct / All: {correct_all} / {ann_stat[MOD][CNT_ALL]} = {correct_all_ratio:.3f}")
    print()
    print(
        f"Correct rules / All rules: {correct_rules} / {ann_stat[MOD][CNT_RULE]} = {correct_rules_ratio:.3f}"
    )
    agg[MOD][CORR_ALL_RATIO].append(correct_all_ratio)
    agg[MOD][CORR_RULE_RATIO].append(correct_rules_ratio)
    print()
    print(make_markdown_table(values))


def print_agg(agg, name):
    if name == AVG:
        print("## Average")
    elif name == STD:
        print("## STD")

    print("### Modality")
    agg_corr_all = 0
    agg_corr_rule = 0
    if name == AVG:
        agg_corr_all = st.mean(agg[MOD][CORR_ALL_RATIO])
        agg_corr_rule = st.mean(agg[MOD][CORR_RULE_RATIO])
    elif name == STD:
        agg_corr_all = st.stdev(agg[MOD][CORR_ALL_RATIO])
        agg_corr_rule = st.stdev(agg[MOD][CORR_RULE_RATIO])
    print(f"Correct / All: {agg_corr_all:.3f}")
    print()
    print(f"Correct rules / All rules: {agg_corr_rule:.3f}")
    values = [["Name", "Precision", "Recall"]]
    for mod, mod_stat in agg[MOD].items():
        if mod == CORR_ALL_RATIO or mod == CORR_RULE_RATIO:
            continue
        agg_prec = 0
        agg_rec = 0
        if name == AVG:
            agg_prec = st.mean(mod_stat[PREC])
            agg_rec = st.mean(mod_stat[REC])
        elif name == STD:
            agg_prec = st.stdev(mod_stat[PREC])
            agg_rec = st.stdev(mod_stat[REC])
        values.append([mod, agg_prec, agg_rec])
    print()
    print(make_markdown_table(values))


def get_args():
    parser = argparse.ArgumentParser(description="")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    annotator_stat()
