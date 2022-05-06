import json
import os

import pandas as pd

from brise_plandok.full_attribute_extraction.attribute.potato.constants import (
    GOLD,
    SEGMENTATION_ERROR,
    GOLD_ATTRIBUTES,
    ANNOTATED_ATTRIBUTES,
    DO_NOT_ANNOTATE,
)


def load_data_to_df(dir_path, only_gold):
    data = []
    for filename in os.listdir(dir_path):
        with open(os.path.join(dir_path, filename), "rt") as f:
            doc = json.load(f)
            if only_gold and not doc[GOLD]:
                continue
            append_doc_to_data(data, doc)
    df = pd.DataFrame.from_dict(data)
    return df


def append_doc_to_data(data, doc, labels_present=True):
    for sen in doc["sens"].values():
        if sen[SEGMENTATION_ERROR]:
            continue
        labels = None
        if labels_present:
            if doc[GOLD]:
                labels = _get_attributes(sen[GOLD_ATTRIBUTES].keys())
            else:
                labels = _get_attributes(sen[ANNOTATED_ATTRIBUTES].keys())
        data.append(
            {
                "sen_id": sen["id"],
                "text": sen["text"],
                "labels": labels,
            }
        )


def _get_attributes(keys):
    return list(set([key for key in keys if key != DO_NOT_ANNOTATE]))
