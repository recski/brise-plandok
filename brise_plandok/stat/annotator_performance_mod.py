import argparse
import os
import statistics as st
from collections import Counter

from brise_plandok.constants import (
    DocumentFields,
    SenFields,
    FullAnnotatedAttributeFields,
    AnnotatedAttributeFields,
    EMPTY,
)
from brise_plandok.stat.constants import (
    DATASET_FOLDERS,
    ALL,
    RULES,
    FREQ,
    FREQ_CORR,
    TP,
    FN,
    FP,
    CORRECT_RATIO,
    AVG,
    STD,
    PREC,
    REC,
)
from brise_plandok.stat.utils import make_markdown_table
from brise_plandok.utils import load_json


def annotator_stat():
    ann_map = {}
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
    ann_map = sort_map(ann_map)
    print_stat(ann_map)


def sort_map(ann_map):
    ann_map = {k: v for k, v in sorted(ann_map.items(), key=lambda item: item[0])}
    for ann, stat in ann_map.items():
        stat[ALL] = {
            k: v for k, v in sorted(stat[ALL].items(), key=lambda item: item[0], reverse=True)
        }
        stat[RULES] = {
            k: v for k, v in sorted(stat[RULES].items(), key=lambda item: item[0], reverse=True)
        }
    return ann_map


def add_ann_to_map_if_not_present(ann_map, doc):
    assert len(doc[DocumentFields.FULL_ANNOTATORS]) == 2
    for ann in doc[DocumentFields.FULL_ANNOTATORS]:
        if ann not in ann_map:
            ann_map[ann] = {
                ALL: {
                    FREQ: 0,
                    FREQ_CORR: 0,
                },
                RULES: {
                    FREQ: 0,
                    FREQ_CORR: 0,
                },
            }


def add_modality_stat(ann_1, ann_2, ann_map, sen):
    ann_map[ann_1][ALL][FREQ] += 1
    ann_map[ann_2][ALL][FREQ] += 1
    ann_modalities = {
        ann_1: EMPTY,
        ann_2: EMPTY,
    }
    gold_mod = sen[SenFields.GOLD_MODALITY]
    if gold_mod is None:
        gold_mod = EMPTY
    else:
        ann_map[ann_1][RULES][FREQ] += 1
        ann_map[ann_2][RULES][FREQ] += 1
    if FullAnnotatedAttributeFields.MODALITY in sen[SenFields.FULL_ANNOTATED_ATTRIBUTES]:
        for mod, annotators in sen[SenFields.FULL_ANNOTATED_ATTRIBUTES][
            FullAnnotatedAttributeFields.MODALITY
        ].items():
            for ann in annotators[AnnotatedAttributeFields.ANNOTATORS]:
                assert ann_modalities[ann] == EMPTY
                ann_modalities[ann] = mod
    for ann, mod in ann_modalities.items():
        assert mod is not None
        mod_stat_all = ann_map[ann][ALL]
        mod_stat_rules = ann_map[ann][RULES]
        if gold_mod != EMPTY:
            add_mod_stat_for_rule_sens(gold_mod, mod, mod_stat_rules)
        add_mod_stat_for_all_sens(gold_mod, mod, mod_stat_all)


def add_mod_stat_for_rule_sens(gold_mod, mod, mod_stat_rules):
    if gold_mod not in mod_stat_rules:
        mod_stat_rules[gold_mod] = Counter()
    if mod != EMPTY and mod not in mod_stat_rules:
        mod_stat_rules[mod] = Counter()
    if gold_mod == mod:
        mod_stat_rules[gold_mod][TP] += 1
        mod_stat_rules[FREQ_CORR] += 1
    else:
        mod_stat_rules[gold_mod][FN] += 1
        if mod != EMPTY:
            mod_stat_rules[mod][FP] += 1


def add_mod_stat_for_all_sens(gold_mod, mod, mod_stat_all):
    if gold_mod not in mod_stat_all:
        mod_stat_all[gold_mod] = Counter()
    if mod not in mod_stat_all:
        mod_stat_all[mod] = Counter()
    if gold_mod == mod:
        mod_stat_all[gold_mod][TP] += 1
        mod_stat_all[FREQ_CORR] += 1
    else:
        mod_stat_all[gold_mod][FN] += 1
        mod_stat_all[mod][FP] += 1


def print_stat(ann_map):
    print("# Annotator performance - Modality")
    print("This statistics is calculated without the sentences with a segmentation error.")
    agg = {
        ALL: {
            CORRECT_RATIO: [],
        },
        RULES: {
            CORRECT_RATIO: [],
        },
    }
    for ann, ann_stat in ann_map.items():
        print(f"## Annotator {ann}")
        print_modality(ann_stat, agg)
    print_agg(agg, AVG)
    print_agg(agg, STD)


def print_modality(ann_stat, agg):
    for stat_type, ann_stat_mod in ann_stat.items():
        values = [["Name", TP, FP, FN, PREC, REC]]
        agg_for_stat_type = agg[stat_type]
        print(f"### {stat_type}")
        for mod, mod_stat in ann_stat_mod.items():
            if mod == FREQ or mod == FREQ_CORR:
                continue
            prec = mod_stat[TP] / (mod_stat[TP] + mod_stat[FP])
            rec = mod_stat[TP] / (mod_stat[TP] + mod_stat[FN])
            values.append([mod, mod_stat[TP], mod_stat[FP], mod_stat[FN], prec, rec])
            if mod not in agg_for_stat_type:
                agg_for_stat_type[mod] = {
                    PREC: [],
                    REC: [],
                }
            agg_for_stat_type[mod][PREC].append(prec)
            agg_for_stat_type[mod][REC].append(rec)
        correct_ratio = ann_stat_mod[FREQ_CORR] / ann_stat_mod[FREQ]
        print(
            f"Correct / All: {ann_stat_mod[FREQ_CORR]} / {ann_stat_mod[FREQ]} = {correct_ratio:.3f}"
        )
        agg_for_stat_type[CORRECT_RATIO].append(correct_ratio)
        print(make_markdown_table(values))


def print_agg(agg, name):
    if name == AVG:
        print("## Average")
    elif name == STD:
        print("## STD")
    for stat_type, agg_stat in agg.items():
        print(f"### {stat_type}")
        agg_corr_ratio = 0
        if name == AVG:
            agg_corr_ratio = st.mean(agg_stat[CORRECT_RATIO])
        elif name == STD:
            agg_corr_ratio = st.stdev(agg_stat[CORRECT_RATIO])
        print(f"Correct / All: {agg_corr_ratio:.3f}")
        values = [["Name", PREC, REC]]
        for mod, mod_stat in agg_stat.items():
            if mod == CORRECT_RATIO:
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
        print(make_markdown_table(values))


def get_args():
    parser = argparse.ArgumentParser(description="")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    annotator_stat()
