import argparse
import os.path
import re

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from tuw_nlp.text.pipeline import CachedStanzaPipeline, CustomStanzaPipeline

from brise_plandok.baselines.constants import ALL_LABELS_SORTED
from brise_plandok.baselines.utils import (
    get_labels_df_path,
    get_features_df_path,
    get_data_df_path,
)
from brise_plandok.constants import TRAIN, DATA_FOLDER, VALID, TEST
from brise_plandok.utils import create_input


def clean_text(text):
    new_text = re.sub(r"[^\w\s]", "", text)
    new_text = re.sub(r"[0-9]+", "", new_text)
    return new_text


class LemmaTokenizer:
    def __init__(self, nlp):
        self.nlp = nlp

    def __call__(self, text):
        return [
            word.lemma
            for sen in self.nlp(clean_text(text)).sentences
            for token in sen.tokens
            for word in token.words
        ]


def featurize(sub_dir, vocab=None):
    data_df = create_input(os.path.join(DATA_FOLDER, sub_dir))
    features_df = get_bow_features(data_df, vocab)
    labels_df = binarize_labels(data_df)
    data_df.to_csv(get_data_df_path(sub_dir), index=False)
    features_df.to_csv(get_features_df_path(sub_dir), index=False)
    labels_df.to_csv(get_labels_df_path(sub_dir), index=False)
    return features_df.columns[2:].tolist()


def binarize_labels(data_df):
    mlb = MultiLabelBinarizer(classes=list(ALL_LABELS_SORTED.keys()))
    labels = pd.DataFrame(mlb.fit_transform(data_df.Labels), columns=mlb.classes_)
    return data_df[["ID", "Labels"]].join(labels)


def get_bow_features(data_df, vocab=None):
    nlp_pipeline = CustomStanzaPipeline(processors="tokenize,mwt,lemma", lang="de")
    with CachedStanzaPipeline(nlp_pipeline, "cache/preproc.json") as nlp:
        vectorizer = CountVectorizer(
            max_features=3000,
            tokenizer=LemmaTokenizer(nlp),
            max_df=0.8,
            min_df=0.001,
            vocabulary=vocab,
            stop_words=["B", "Kalter"],  # filter nlp pipeline errors
        )
        X = vectorizer.fit_transform(data_df.Text).toarray()
        headers = vectorizer.get_feature_names_out()
        features = pd.DataFrame(X, columns=headers)
    return data_df[["ID", "Text"]].join(features)


def get_args():
    parser = argparse.ArgumentParser(description="")
    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    vocab_train = featurize(TRAIN)
    vocab_valid = featurize(VALID, vocab_train)
    vocab_test = featurize(TEST, vocab_train)
    assert vocab_train == vocab_valid and vocab_train == vocab_test
