import argparse
import os.path
import re

import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from tuw_nlp.text.pipeline import CachedStanzaPipeline, CustomStanzaPipeline

from brise_plandok.baselines.constants import ALL_LABELS_SORTED
from brise_plandok.constants import TRAIN, DATA_FOLDER
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


def featurize(sub_dir):
    data_df = create_input(os.path.join(DATA_FOLDER, sub_dir))
    features_df = get_bow_features(data_df)
    labels_df = binarize_labels(data_df)
    data_df.to_csv(os.path.join(os.path.dirname(__file__), "input", f"{sub_dir}_data.csv"))
    features_df.to_csv(os.path.join(os.path.dirname(__file__), "input", f"{sub_dir}_features.csv"))
    labels_df.to_csv(os.path.join(os.path.dirname(__file__), "input", f"{sub_dir}_labels.csv"))


def binarize_labels(data_df):
    mlb = MultiLabelBinarizer(classes=ALL_LABELS_SORTED)
    labels = pd.DataFrame(mlb.fit_transform(data_df.Labels), columns=mlb.classes_)
    return data_df[["ID", "Labels"]].join(labels)


def get_bow_features(data_df):
    de_stopwords = set(stopwords.words("german"))
    nlp_pipeline = CustomStanzaPipeline(processors="tokenize,mwt,lemma", lang="de")
    with CachedStanzaPipeline(nlp_pipeline, "cache/preproc.json") as nlp:
        vectorizer = CountVectorizer(
            max_features=3000,
            tokenizer=LemmaTokenizer(nlp),
            stop_words=de_stopwords,
            max_df=0.8,
            min_df=0.001,
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
    featurize(TRAIN)
