import unittest

import numpy as np

from brise_plandok.full_attribute_extraction.attribute.potato.constants import (
    TOP_14_ANNOTATED,
    NOT,
)
from brise_plandok.full_attribute_extraction.attribute.potato.utils import (
    filter_labels,
    load_features,
)
from brise_plandok.full_attribute_extraction.attribute.utils.get_vocab import (
    _gen_all_attributes_names,
    _get_label_vocab,
)
from brise_plandok.full_attribute_extraction.attribute.utils.load_data import load_data_to_df

ONLY_GOLD = False


class TestUtils(unittest.TestCase):
    def test_load_train(self):
        df = load_data_to_df("../../../../data/train", ONLY_GOLD)
        np.testing.assert_array_equal(df.shape, np.array([8917, 3]))

        sorted_unique_labels = sorted(set(sum(df.labels.to_list(), [])))
        self.assertEqual(len(sorted_unique_labels), 94)

    def test_load_valid(self):
        df = load_data_to_df("../../../../data/valid", ONLY_GOLD)
        np.testing.assert_array_equal(df.shape, np.array([735, 3]))

        sorted_unique_labels = sorted(set(sum(df.labels.to_list(), [])))
        self.assertEqual(len(sorted_unique_labels), 65)

    def test_filter_labels(self):
        df = load_data_to_df("../../../../data/train", ONLY_GOLD)
        filter_labels(df, TOP_14_ANNOTATED, NOT)
        unique_labels = len(df["labels"].explode().unique())
        self.assertEqual(unique_labels, 16)

    def test_get_label_vocab(self):
        label_vocab = _get_label_vocab(TOP_14_ANNOTATED)
        self.assertSetEqual(set(label_vocab.keys()), set(TOP_14_ANNOTATED))

    def test_get_all_attributes_names(self):
        attribute_names = [attr for attr in _gen_all_attributes_names()]
        self.assertLess(len(attribute_names), 100)

    def test_get_all_manual_features(self):
        all_features = load_features()
        attribute_names = [attr for attr in _gen_all_attributes_names()]
        attribute_names_from_features = [feat[-1] for feat in all_features]
        self.assertLessEqual(len(set(attribute_names_from_features)), len(set(attribute_names)))
