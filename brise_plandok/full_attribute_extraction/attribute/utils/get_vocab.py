import inspect

from brise_plandok.constants import AttributesNames
from brise_plandok.full_attribute_extraction.attribute.potato.constants import NOT


def get_vocab_for_all_attributes():
    all_attribute_names = [NOT] + [attr_name for attr_name in _gen_all_attributes_names()]
    return _get_label_vocab(all_attribute_names)


def _gen_all_attributes_names():
    for i in inspect.getmembers(AttributesNames()):
        if not i[0].startswith("_"):
            if not inspect.ismethod(i[1]):
                yield i[1]


def _get_label_vocab(labels):
    label_vocab = {}
    for i, l in enumerate(labels):
        label_vocab[l] = i
    return label_vocab
