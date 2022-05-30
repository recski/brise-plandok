import argparse
import os

from brise_plandok.constants import DocumentFields, SenFields, AttributesNames
from brise_plandok.utils import load_json

DATASET_FOLDERS = ["data/train", "data/valid", "data/test"]


def print_suggestions_stat(only_rules, original_attributes):
    all_sentences = 0
    all_gold_attributes = 0
    all_suggested_attributes = 0
    sentences_with_suggestions = 0
    correct_suggestions = 0

    for folder in DATASET_FOLDERS:
        for filename in os.listdir(folder):
            fn = os.path.join(folder, filename)
            doc = load_json(fn)
            for sen in doc[DocumentFields.SENS].values():
                if (
                    not only_rules
                    or SenFields.GOLD_MODALITY in sen
                    and sen[SenFields.GOLD_MODALITY] is not None
                ):
                    all_sentences += 1
                    all_gold_attributes += len(sen[SenFields.GOLD_ATTRIBUTES])
                    all_suggested_attributes += len(
                        sen[SenFields.GEN_ATTRIBUTES_ON_FULL_ANNOTATION]
                    )
                    suggested_attrs = sen[SenFields.GEN_ATTRIBUTES_ON_FULL_ANNOTATION].keys()
                    if len(suggested_attrs) != 0:
                        sentences_with_suggestions += 1
                        gold_attrs = sen[SenFields.GOLD_ATTRIBUTES].keys()
                        if original_attributes:
                            if AttributesNames.Widmung in gold_attrs:
                                gold_attrs = (gold_attrs - {AttributesNames.Widmung}) | {
                                    "WidmungUndZweckbestimmung"
                                }
                            if AttributesNames.Nutzungsart in gold_attrs:
                                gold_attrs = (gold_attrs - {AttributesNames.Nutzungsart}) | {
                                    "WidmungUndZweckbestimmung"
                                }
                            if AttributesNames.BebauteFlaecheMax in gold_attrs:
                                gold_attrs = (gold_attrs - {AttributesNames.BebauteFlaecheMax}) | {
                                    "Flaechen"
                                }
                            if AttributesNames.BebauteFlaecheMin in gold_attrs:
                                gold_attrs = (gold_attrs - {AttributesNames.BebauteFlaecheMin}) | {
                                    "Flaechen"
                                }
                            if AttributesNames.BebauteFlaecheMaxProzentual in gold_attrs:
                                gold_attrs = (
                                    gold_attrs - {AttributesNames.BebauteFlaecheMaxProzentual}
                                ) | {"Flaechen"}
                            if AttributesNames.BebauteFlaecheMaxNebengebaeude in gold_attrs:
                                gold_attrs = (
                                    gold_attrs - {AttributesNames.BebauteFlaecheMaxNebengebaeude}
                                ) | {"Flaechen"}
                            if AttributesNames.GesamtePlangebiet in gold_attrs:
                                gold_attrs = (gold_attrs - {AttributesNames.GesamtePlangebiet}) | {
                                    "PlangebietAllgemein"
                                }
                            if AttributesNames.GebaeudeHoeheMaxWN in gold_attrs:
                                gold_attrs = (
                                    gold_attrs - {AttributesNames.GebaeudeHoeheMaxWN}
                                ) | {"GebaeudeHoeheMax"}
                            if AttributesNames.GebaeudeHoeheMaxAbsolut in gold_attrs:
                                gold_attrs = (
                                    gold_attrs - {AttributesNames.GebaeudeHoeheMaxAbsolut}
                                ) | {"GebaeudeHoeheMax"}
                        correct_suggestions += len(gold_attrs & suggested_attrs)
                        # print()
                        # print(gold_attrs)
                        # print(suggested_attrs)
                        # print(gold_attrs & suggested_attrs)
                        # if len(suggested_attrs - gold_attrs) != 0:
                        #     print(suggested_attrs - gold_attrs)

    print(f"Number of all sentences: {all_sentences}")
    print(f"Number of sentences with suggestions: {sentences_with_suggestions}")
    print(
        f"Ratio of sentences with suggestions: {(sentences_with_suggestions/all_sentences)*100:.2f}%"
    )
    print()
    print(f"Number of all gold attributes: {all_gold_attributes}")
    print(f"Number of correct suggestions: {correct_suggestions}")
    print(
        f"Ratio of correctly suggested gold attributes: {(correct_suggestions/all_gold_attributes)*100:.2f}%"
    )
    print()
    print(f"Number of all suggested attributes: {all_suggested_attributes}")
    print(f"Number of wrong suggestions: {all_suggested_attributes - correct_suggestions}")
    print(
        f"Ratio of wrong suggestions: {((all_suggested_attributes - correct_suggestions)/all_suggested_attributes)*100:.2f}%"
    )


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-r", "--only-rules", action="store_true")
    parser.add_argument("-o", "--original-attributes", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    print_suggestions_stat(args.only_rules, args.original_attributes)
