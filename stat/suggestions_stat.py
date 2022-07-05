import argparse
import os

from brise_plandok.constants import DocumentFields, SenFields, AttributesNames
from brise_plandok.utils import load_json

DATASET_FOLDERS = ["data/train", "data/valid", "data/test"]
FIRST_STAGE_IDS = "stat/first_stage_gold_ids.txt"


def print_suggestions_stat(only_rules, original_attributes, first_stage, combined):
    all_sentences = 0
    all_gold_attributes = 0
    all_suggested_attributes = 0
    sentences_with_suggestions = 0
    correct_suggestions = 0

    first_stage_gold_ids = None
    if first_stage or combined:
        with open(FIRST_STAGE_IDS) as f:
            first_stage_gold_ids = f.read().splitlines()

    for folder in DATASET_FOLDERS:
        for filename in os.listdir(folder):
            fn = os.path.join(folder, filename)
            if first_stage:
                if not filename.split(".")[0] in first_stage_gold_ids:
                    continue
            doc = load_json(fn)
            for sen in doc[DocumentFields.SENS].values():
                if not only_rules or (
                    SenFields.GOLD_MODALITY in sen and sen[SenFields.GOLD_MODALITY] is not None
                ):
                    gen_attributes_field = get_gen_attr_field(
                        first_stage, combined, doc[DocumentFields.ID], first_stage_gold_ids
                    )
                    all_sentences += 1
                    all_gold_attributes += len(sen[SenFields.GOLD_ATTRIBUTES])
                    all_suggested_attributes += len(sen[gen_attributes_field])
                    suggested_attrs = sen[gen_attributes_field].keys()
                    if len(suggested_attrs) != 0:
                        sentences_with_suggestions += 1
                        gold_attrs = sen[SenFields.GOLD_ATTRIBUTES].keys()
                        if original_attributes:
                            gold_attrs = convert_back_post_processed(gold_attrs)
                        correct_suggestions += len(gold_attrs & suggested_attrs)
    print_stat(
        all_gold_attributes,
        all_sentences,
        all_suggested_attributes,
        correct_suggestions,
        sentences_with_suggestions,
    )


def get_gen_attr_field(first_stage, combined, doc_id, first_stage_gold_ids):
    if first_stage or (combined and doc_id in first_stage_gold_ids):
        gen_attributes_field = SenFields.GEN_ATTRIBUTES_ON_ANNOTATION
    else:
        gen_attributes_field = SenFields.GEN_ATTRIBUTES_ON_FULL_ANNOTATION
    return gen_attributes_field


def print_stat(
    all_gold_attributes,
    all_sentences,
    all_suggested_attributes,
    correct_suggestions,
    sentences_with_suggestions,
):
    print(f"Number of all sentences: {all_sentences}")
    print(f"Number of sentences with suggestions: {sentences_with_suggestions}")
    print(
        f"Ratio of sentences with suggestions: {(sentences_with_suggestions / all_sentences) * 100:.2f}%"
    )
    print()
    print(f"Number of all gold attributes: {all_gold_attributes}")
    print(f"Number of correct suggestions: {correct_suggestions}")
    print(
        f"Ratio of correctly suggested gold attributes: {(correct_suggestions / all_gold_attributes) * 100:.2f}%"
    )
    print()
    print(f"Number of all suggested attributes: {all_suggested_attributes}")
    print(f"Number of wrong suggestions: {all_suggested_attributes - correct_suggestions}")
    print(
        f"Ratio of wrong suggestions: {((all_suggested_attributes - correct_suggestions) / all_suggested_attributes) * 100:.2f}%"
    )


def convert_back_post_processed(gold_attrs):
    if AttributesNames.Widmung in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.Widmung}) | {"WidmungUndZweckbestimmung"}
    if AttributesNames.Nutzungsart in gold_attrs:
        gold_attrs = (gold_attrs - {AttributesNames.Nutzungsart}) | {"WidmungUndZweckbestimmung"}
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


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-r", "--only-rules", action="store_true")
    parser.add_argument("-o", "--original-attributes", action="store_true")
    parser.add_argument("-f", "--first-stage", action="store_true")
    parser.add_argument("-c", "--combined", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    print_suggestions_stat(
        args.only_rules, args.original_attributes, args.first_stage, args.combined
    )
