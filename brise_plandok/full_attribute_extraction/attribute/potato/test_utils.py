import unittest

import numpy as np

from brise_plandok.full_attribute_extraction.attribute.potato.constants import TOP_15_ANNOTATED, NOT
from brise_plandok.full_attribute_extraction.attribute.potato.utils import load_data_to_df, filter_labels, \
    get_label_vocab, gen_all_attributes_names, get_all_manual_features

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
        filter_labels(df, TOP_15_ANNOTATED, NOT)
        unique_labels = len(df["labels"].explode().unique())
        self.assertEqual(unique_labels, 16)

    def test_get_label_vocab(self):
        label_vocab = get_label_vocab(TOP_15_ANNOTATED)
        self.assertSetEqual(set(label_vocab.keys()), set(TOP_15_ANNOTATED))

    def test_get_all_attributes_names(self):
        attribute_names = [attr for attr in gen_all_attributes_names()]
        self.assertLess(len(attribute_names), 100)

    def test_get_all_manual_features(self):
        all_features = get_all_manual_features()
        attribute_names = [attr for attr in gen_all_attributes_names()]
        attribute_names_from_features = [feat[-1] for feat in all_features]
        self.assertLessEqual(len(set(attribute_names_from_features)), len(set(attribute_names)))
