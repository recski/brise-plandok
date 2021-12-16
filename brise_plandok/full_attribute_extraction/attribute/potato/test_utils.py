import unittest

import numpy as np

from brise_plandok.full_attribute_extraction.attribute.potato.constants import TOP_15_ANNOTATED, NOT
from brise_plandok.full_attribute_extraction.attribute.potato.utils import load_data_to_df, filter_labels, \
    get_label_vocab

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
