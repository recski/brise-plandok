import argparse
import os
from collections import Counter

import numpy
from sklearn.metrics import cohen_kappa_score

from brise_plandok.constants import (
    DocumentFields,
    SenFields,
    FullAnnotatedAttributeFields,
    AttributeFields,
    AnnotatedAttributeFields,
    EMPTY,
)
from brise_plandok.stat.constants import (
    DATASET_FOLDERS,
)
from brise_plandok.stat.utils import (
    make_markdown_table,
    make_markdown_table_latex_agr,
    get_ann_pair,
    collect_all_attributes,
    fill_up_kappa_stat,
    append_header_for_attr_wise_kappa,
    convert_back_post_processed,
    add_overall_rows,
)
from brise_plandok.utils import load_json


def calculate_attr_kappa(latex=False):
    kappa_stat = {}
    attr_stat = Counter()
    annotator_pairs = set()

    attr_stat, annotator_pairs, _ = collect_all_attributes(attr_stat, annotator_pairs, set())
    fill_up_kappa_stat(kappa_stat, attr_stat, annotator_pairs)

    for folder in DATASET_FOLDERS:
        for filename in os.listdir(folder):
            fn = os.path.join(folder, filename)
            doc = load_json(fn)
            ann_pair = get_ann_pair(doc)
            for sen in doc[DocumentFields.SENS].values():
                if (
                    not sen[SenFields.SEGMENTATION_ERROR]
                    and sen[SenFields.GOLD_MODALITY] is not None
                ):
                    add_kappa_stat(
                        ann_pair,
                        kappa_stat,
                        sen,
                    )
    print_stat(kappa_stat, annotator_pairs, attr_stat, latex=latex)


def add_kappa_stat(ann_pair, kappa_stat, sen):
    for attr_name, attr in sen[SenFields.GOLD_ATTRIBUTES].items():
        if len(attr) != 1:
            continue
        ann_types = {
            ann_pair[0]: EMPTY,
            ann_pair[1]: EMPTY,
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
            if ann_types[ann_pair[0]] != EMPTY and ann_types[ann_pair[1]] != EMPTY:
                kappa_stat[gold_attr][ann_pair][ann_pair[0]].append(ann_types[ann_pair[0]])
                kappa_stat[gold_attr][ann_pair][ann_pair[1]].append(ann_types[ann_pair[1]])


def print_stat(kappa_stat, annotator_pairs, attr_stat, latex=False):
    print("# Annotator agreement - Types")
    print(
        "This statistics is calculated without the sentences with a segmentation error.  \n"
        "Only sentences containing a rule (a.k.a. gold_modality != None) are taken into account.  \n"
        "We use Cohen's kappa for calculating the inter-annotator agreement: "
        "[cohen_kappa_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html)."
        "  \n"
        "Frequencies of attributes are calculated as the number of sentences where the attribute appears as either "
        "gold or annotated either in the first or in the second phase.  \n"
        "For complexity reasons, agreement is only calculated for cases, where the attribute occurs in gold exactly "
        "once, and where both annotators gave at least one annotation for the attribute. "
        "In case an annotator labeled the attribute within the same sentence multiple times, "
        "the most beneficial type annotation is taken into account, i.e. if the annotator labeled both gold and "
        "non-gold types, we regard the gold one."
    )
    print("## Without kappa correction")
    calculate_table(annotator_pairs, kappa_stat, attr_stat, latex=latex)
    print("## With kappa correction")
    print(
        "[cohen_kappa_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html) "
        "results in `nan` if both vectors are uniform and the same."
    )
    print(
        "In the table below, we substituted these `nan` values by the value of complete agreement (1.0)."
    )
    calculate_table(
        annotator_pairs, kappa_stat, attr_stat, correct_uniform_agreement=True, latex=latex
    )


def calculate_table(
    annotator_pairs, kappa_stat, attr_stat, correct_uniform_agreement=False, latex=False
):
    values = []
    macro_freqs = []
    weighted_freqs = []
    macro_avgs = []
    weighted_avgs = []
    append_header_for_attr_wise_kappa(annotator_pairs, values)
    for attr, stat in kappa_stat.items():
        num_sens_row = ["Number of sentences ", "-", "-", "-"]
        kappa_row = [attr, attr_stat[attr], "-", "-"]
        macro_freqs.append(attr_stat[attr])
        weighted_freqs.append(attr_stat[attr])
        non_nan_kappas = []
        non_nan_weights = []
        for ann_pair, labels in stat.items():
            ann_1_labels = labels[ann_pair[0]]
            ann_2_labels = labels[ann_pair[1]]
            assert len(ann_1_labels) == len(ann_2_labels)
            num_sens_row.append(len(ann_1_labels))
            if correct_uniform_agreement:
                if ann_1_labels == ann_2_labels:
                    kappa = 1.0
                else:
                    kappa = cohen_kappa_score(ann_1_labels, ann_2_labels)
            else:
                kappa = cohen_kappa_score(ann_1_labels, ann_2_labels)
            if not numpy.isnan(kappa):
                non_nan_kappas.append(kappa)
                non_nan_weights.append(len(ann_1_labels))
            kappa_row.append(kappa)
        if len(non_nan_kappas) > 0:
            kappa_row[2] = numpy.average(non_nan_kappas)
            macro_avgs.append(kappa_row[2])
        else:
            kappa_row[2] = numpy.nan
        if len(non_nan_kappas) > 1 and sum(non_nan_weights) > 0.0:
            kappa_row[3] = numpy.average(non_nan_kappas, weights=non_nan_weights)
            weighted_avgs.append(kappa_row[3])
        else:
            kappa_row[3] = numpy.nan
            weighted_freqs.pop()
        values.append(num_sens_row)
        values.append(kappa_row)
    final_values = add_overall_rows(
        annotator_pairs,
        correct_uniform_agreement,
        macro_freqs,
        weighted_freqs,
        macro_avgs,
        values,
        weighted_avgs,
    )
    print(make_markdown_table(final_values))
    if latex:
        print(make_markdown_table_latex_agr(final_values))
    else:
        print(make_markdown_table(final_values))


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-l", "--latex", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    numpy.seterr(divide="ignore", invalid="ignore")
    calculate_attr_kappa(latex=args.latex)
