import argparse
from brise_plandok.constants import ANNOTATOR_NAME_INDEX
import json
import logging
import os
import pandas
from collections import Counter, defaultdict

import numpy as np
import openpyxl
from sklearn.metrics import cohen_kappa_score

from tuw_nlp.common.eval import print_cat_stats
from tuw_nlp.common.vocabulary import Vocabulary

IGNORE_EMPTY = True

REPLACEMENT_PAIRS = {('BBDachneigungMax', 'DachneigungMax')}

ATTR_IGNORE = {
    "AusnahmePruefungErforderlich",
    "WeitereBestimmungPruefungErforderlich",
    "ZuVorherigemSatzGehoerig",
    "Segmentierungsfehler",
    "NoAttribute",
    "N/A",
    "StrittigeBedeutung"
}

IAA_COLUMNS = ["Freq", "Attr",
               "Avg K (gold)", "Ks (gold)", "Avg K (inter)", "Ks (inter)", "counts by sen"]


def all_equal(iterator):
    # https://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)


def preprocess_attr(attr):
    for a, b in REPLACEMENT_PAIRS:
        if attr == a:
            return b
    return attr


def xlsx_to_data(fn):
    xlsx = openpyxl.load_workbook(fn)
    sheet = xlsx.active
    return [[cell.value for cell in row] for row in sheet.rows]


def eval_against_gold(data, attr_vocab, annotator_vocab):
    if "gold" not in annotator_vocab.word_to_id:
        logging.info(
            "No gold data is provided - skipping evaluation against gold")
        return
    gold_ann = annotator_vocab.get_id('gold')
    print('gold ann id:', gold_ann)
    attr_stats = defaultdict(
        lambda: {
            ann: Counter() for ann in annotator_vocab.id_to_word
            if ann != gold_ann})

    for i, (sen_id, sen) in enumerate(data.items()):
        # 1. True positives and false negatives
        for attr in sen['annot'][gold_ann]:
            for ann in annotator_vocab.id_to_word:
                if ann == gold_ann:
                    continue
                if attr in sen['annot'][ann]:
                    attr_stats[attr][ann]['TP'] += 1
                else:
                    attr_stats[attr][ann]['FN'] += 1

        # 2. False positives
        for ann in annotator_vocab.id_to_word:
            if ann == gold_ann:
                continue
            if ann not in sen['annot']:
                raise ValueError(f'no annotation from {ann} on {sen_id}')
            for attr in sen['annot'][ann]:
                if attr not in sen['annot'][gold_ann]:
                    attr_stats[attr][ann]['FP'] += 1

    attr_stats[attr_vocab.get_id('total', allow_new=True)] = {
        ann: {
            figure: sum(attr_stats[attr][ann][figure] for attr in attr_stats)
            for figure in ('TP', 'FN', 'FP')}
        for ann in annotator_vocab.id_to_word if ann != gold_ann}

    attr_stats = sorted(
        attr_stats.items(),
        key=lambda st: sum(sum(a_s.values()) for a_s in st[1].values()),
        reverse=True)

    for attr, stats in attr_stats[:10]:
        named_stats = {
            annotator_vocab.get_word(ann): st for ann, st in stats.items()}

        real_annot = {
            ann: st for ann, st in named_stats.items()
            if not ann.startswith('min')}

        vote_annot = {
            ann: st for ann, st in named_stats.items()
            if ann.startswith('min')}

        print('===============')
        print(attr_vocab.get_word(attr))
        print('===============')
        print_cat_stats(real_annot)
        print_cat_stats(vote_annot)


def add_votes(data, attr_vocab, annotator_vocab):
    """add new annotators representing the adjudication strategies of choosing
    attributes that are chosen by at least 1, 2, 3 annotators"""
    real_annotators = list(annotator_vocab.id_to_word.keys())
    vote_anns = {
        n: annotator_vocab.get_id(f'min{n}', allow_new=True)
        for n in (1, 2, 3)}

    for i, (sen_id, sen) in enumerate(data.items()):
        attr_counter = Counter()
        for ann in real_annotators:
            if annotator_vocab.get_word(ann) == 'gold':
                continue
            for attr in sen['annot'][ann]:
                attr_counter[attr] += 1

        vote_sets = {n: set() for n in vote_anns}
        for attr, count in attr_counter.items():
            for n in vote_sets:
                if count >= n:
                    vote_sets[n].add(attr)

        for n, attrs in vote_sets.items():
            sen['annot'][vote_anns[n]] = sorted(attrs)

    return data


def measure_agreement(data, attr_vocab, annotator_vocab):
    # attr * annotators * sens
    ratings = np.zeros(
        (len(attr_vocab), len(annotator_vocab), len(data)), dtype='int')

    attr_counts = {attr: Counter() for attr in attr_vocab.id_to_word.keys()}

    for i, (sen_id, sen) in enumerate(data.items()):
        for ann in annotator_vocab.id_to_word:
            if ann not in sen['annot']:
                raise ValueError(f'no annotation from {ann} on {sen_id}')
            for attr in sen['annot'][ann]:
                ratings[attr][ann][i] = 1

        for attr, count in sen['attr_stats'].items():
            attr_counts[attr][count] += 1

    stats = []
    for attr, attr_name in attr_vocab.id_to_word.items():
        # print("==================================")
        # print(f"{attr_name}:")
        # print("==================================")
        attr_kappas = []
        gold_kappas = []
        for ann1, ann1_name in annotator_vocab.id_to_word.items():
            for ann2, ann2_name in annotator_vocab.id_to_word.items():
                if ann1 >= ann2:
                    continue
                vec1, vec2 = ratings[attr][ann1], ratings[attr][ann2]
                if not vec1.any() and not vec2.any():
                    kappa = 1.0
                else:
                    kappa = cohen_kappa_score(vec1, vec2)

                if ann1_name == 'gold' or ann2_name == 'gold':
                    gold_kappas.append(kappa)
                else:
                    attr_kappas.append(kappa)
                # print(f"{ann1}\t{ann2}\t{kappa}")

        avg = sum(attr_kappas) / len(attr_kappas)
        avg_gold = sum(gold_kappas) / len(gold_kappas) if gold_kappas else 0
        # print(f"AVG: {avg}")
        attr_freq = ratings[attr].sum()

        attr_counts_str = " ".join(
            f"{n}:{count}"
            for n, count in sorted(attr_counts[attr].items(), reverse=True))

        stats.append((
            attr_freq, attr_name, avg_gold, gold_kappas, avg, attr_kappas,
            attr_counts_str))

    stats.sort(key=lambda s: -s[0])

    print_iaa(stats)


def print_iaa(stats):
    df = pandas.DataFrame(columns=IAA_COLUMNS)
    for attr_freq, attr_name, avg_gold, gold_kappas, avg, attr_kappas, attr_counts_str in stats:  # noqa
        gold_kappas_str = " ".join(f"{k:.2f}" for k in gold_kappas) if gold_kappas else 'N/A'  # noqa
        attr_kappas_str = " ".join(f"{k:.2f}" for k in attr_kappas)
        df = df.append(pandas.DataFrame([[attr_freq, attr_name, avg_gold, gold_kappas_str,
                       avg, attr_kappas_str, attr_counts_str]], columns=IAA_COLUMNS), ignore_index=True)
    logging.info(f"IAA:\n{df}")
    disagree = df[df["Avg K (inter)"] < 1.0].iloc[:, [0,1,4,-1]]
    _print_disagree(df, disagree)

def _print_disagree(df, disagree):
    logging.info(f"Disagree: {disagree.shape[0]}/{df.shape[0]} - {int(disagree.shape[0]/df.shape[0]*100)}%\n{disagree}")


def load_data(filenames):
    annotator_vocab = Vocabulary()
    attr_vocab = Vocabulary()
    data = {}
    for fn in filenames:
        name, filetype = os.path.basename(fn).split('.')
        try:
            doc_id, annotator, date = name.split('_')
        except ValueError:
            try:
                doc_id, annotator = name.split('_')
            except ValueError:
                annotator = os.path.normpath(fn).split(
                    os.path.sep)[ANNOTATOR_NAME_INDEX]

        annotator = annotator_vocab.get_id(annotator.lower(), allow_new=True)

        for sen in gen_sens_from_file(fn, filetype):
            if _is_header(sen):
                continue
            if sen['id'] in data:
                assert data[sen['id']]['text'] == sen['text'], f'changed text in {fn} sentence {sen["id"]}'  # noqa
            else:
                data[sen['id']] = {
                    "id": sen['id'], "text": sen['text'], 'annot': {},
                    'attr_stats': Counter()}

            assert annotator not in data[sen['id']]['annot']

            data[sen['id']]['annot'][annotator] = sorted([
                attr_vocab.get_id(preprocess_attr(attr), allow_new=True)
                for attr in set(sen['attributes'])])

            if annotator_vocab.get_word(annotator) != 'gold':
                for attr in data[sen['id']]['annot'][annotator]:
                    data[sen['id']]['attr_stats'][attr] += 1
            else:
                for attr in data[sen['id']]['annot'][annotator]:
                    if attr not in data[sen['id']]['attr_stats']:
                        data[sen['id']]['attr_stats'][attr] = 0

    return data, attr_vocab, annotator_vocab


def _is_header(sen):
    section = int(sen["id"].split("_")[-2])
    return section == 0

def remove_empty(data):
    new_data = {
        sen_id: sen_data for sen_id, sen_data in data.items()
        if any(sen_data['annot'].values())}

    logging.warning(
        'ignoring sentences with no annotation from anyone, '
        'keeping {} of {} sens'.format(len(new_data), len(data)))
    return new_data


def gen_sens_from_file(fn, extension):
    logging.warning(f'processing {fn}')
    if extension == "xlsx":
        return gen_sens_from_xlsx(fn)
    elif extension == "json":
        return gen_sens_from_json(fn)
    else:
        raise ValueError("Extension must either be 'xlsx' or 'json'")


def gen_sens_from_json(fn):
    with open(fn) as f:
        doc = json.load(f)
    for sen in doc["sens"]:
        if "gold_attributes" in sen:
            yield {
                "id": sen["id"],
                "text": sen["text"],
                "attributes": sorted([attr["name"] for attr in sen["gold_attributes"]])
            }


def gen_sens_from_xlsx(fn):
    for i, row in enumerate(xlsx_to_data(fn)):
        if i == 0:
            assert row[0] == 'Sentence_ID' or row[
                0] == 'ID', f'unexpected header in {fn}: {row}'
            continue

        if row[0] is None:
            assert i == 1
            continue

        sen_id, sen_text, rest = row[0], row[1], row[2:12]

        attributes = [
            field for j, field in enumerate(rest)
            if field and j % 2 == 1 and field not in ATTR_IGNORE]

        yield {
            "id": sen_id,
            "text": sen_text,
            "attributes": sorted(attributes)}


def print_data(data, attr_vocab, annotator_vocab, out_fn):
    cols = ["sen_id", "sen"] + list(annotator_vocab.word_to_id.keys()) + \
        ["attribute counts", "full_agreement"]
    df = pandas.DataFrame(columns=cols)
    for sen in data.values():
        sen['full_agreement'] = all_equal(sen['annot'].values())
        try: 
            df = df.append(pandas.DataFrame([
                [sen['id'], sen['text']] +
                [",".join(
                    attr_vocab.get_word(attr) for attr in attrs) if attrs else 'no_attr' 
                    for ann, attrs in sen['annot'].items()] +
                _get_attr_summary(attr_vocab, sen) +
                [sen['full_agreement']]
            ], columns=cols), ignore_index=True)
        except:
            pass
    df.to_csv(path_or_buf=out_fn, sep="\t", index=False)
    disagree = df[df["full_agreement"] == False].iloc[:, [0]]
    _print_disagree(df, disagree)


def _get_attr_summary(attr_vocab, sen):
    return [" ".join(
        "{}:{}".format(
            attr_vocab.get_word(attr), sen['attr_stats'][attr]) 
            for attr in set(a for attrs in sen['annot'].values() for a in sorted(attrs)))]


def _get_attr_by_annotator(attr_vocab, sen):
    return [",".join(
        attr_vocab.get_word(attr) for attr in attrs) if attrs else 'no_attr' 
        for ann, attrs in sen['annot'].items()]


def print_json(sen, attr_vocab):
    print(json.dumps({
        "id": sen['id'],
        "text": sen['text'],
        "annot": {
            ann: [attr_vocab.get_word(attr) for attr in attrs]
            for ann, attrs in sen['annot'].items()}}))


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-of", "--output-file", type=str)
    parser.add_argument("-a", "--annotations", nargs="+", default=None)
    parser.set_defaults(output_file='annotation_output.tsv')
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s : " +
        "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()
    filenames = args.annotations
    if len(filenames) < 2:
        logging.error(
            "At least two annotation files are required.")
        return
    out_fn = args.output_file
    data, attr_vocab, annotator_vocab = load_data(filenames)
    print_data(data, attr_vocab, annotator_vocab, out_fn)
    if IGNORE_EMPTY:
        data = remove_empty(data)

    measure_agreement(data, attr_vocab, annotator_vocab)
    data = add_votes(data, attr_vocab, annotator_vocab)
    eval_against_gold(data, attr_vocab, annotator_vocab)


if __name__ == "__main__":
    main()
