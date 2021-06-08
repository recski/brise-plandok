import argparse
import json
import logging
import sys
from collections import Counter, defaultdict

from brise_plandok.extractor import get_extractor

from tuw_nlp.common.eval import print_cat_stats


ATTR_IGNORE = {
    "?",
    "N/A",
    "Weitere_Bestimmung_Prüfung_erforderlich",
    'WeitereBestimmungPruefungErforderlich',
    'AusnahmePruefungErforderlich',
    "ZuVorherigemSatzGehoerig",
    "Plangebiet",
    # "PlanzeichenBBID",
    # "WidmungID",
    "obligation",
    "prohibition",
    "permission"}

ATTR_CATS = {}
# ATTR_CATS = {label: '*Flaeche*' for label in {
#    'BBBebaubareFlaecheAbgegrenzt',
#    'BBBebaubareFlaecheJeBauplatz',
#    'BBBebaubareFlaecheGesamterBauplatz',
#    'BBAusnuetzbarkeitFlaecheGrundflaechenbezugRelativ',
#    'BBAusnuetzbarkeitFlaecheGrundflaechenbezug',
#    'BBAusnuetzbarkeitFlaecheWohnnutzflaeche'}}


def preprocess_attrs(attrs):
    pp_attrs = []
    for attr in attrs:
        name = attr['name']
        if not name.startswith('"'):
            new_name = name.replace('(?)', '').strip('? ').replace('ä', 'ae')

            if attr['value']:
                attr['value'] = attr['value'].replace('ä', 'ae')
            pp_attrs.append({
                "name": new_name,
                "value": attr['value'],
                'type': attr['type']
            })

    return pp_attrs


def load_sample(stream):
    sections = []
    for line in stream:
        doc = json.loads(line)
        for section in doc['sections']:
            sections.append({"sens": []})
            for sen in section['sens']:
                if not sen['attributes']:
                    continue
                if not sen['modality']:
                    continue
                sen['attrs'] = preprocess_attrs(sen['attributes'])
                sections[-1]['sens'].append(sen)

    return sections


def get_err_ids(label, results):
    return [
        i for i, (text, attrs, preds) in enumerate(results)
        if (label in attrs) ^ (label in preds)]


def get_err_ids_cat(cat, results):
    def cats(s):
        return {ATTR_CATS.get(a, a) for a in s}

    return [
        i for i, (text, attrs, preds) in enumerate(results)
        if (cat in cats(attrs)) ^ (cat in cats(preds))]


def print_output(results, fn):
    with open(fn, 'w') as f_obj:
        for _, rec in results.items():
            json.dump(rec, f_obj)


def count_attr_stats(sample, label_cats=None, print_errs=False):
    cats = defaultdict(Counter)
    for sen_id, orig_attrs, orig_preds in sample:
        attrs = {
            label_cats.get(a, a) for a in orig_attrs if a not in ATTR_IGNORE}
        preds = {
            label_cats.get(a, a) for a in orig_preds if a not in ATTR_IGNORE}
        for attr in attrs & preds:
            cats[attr]['TP'] += 1
        for attr in attrs - preds:
            cats[attr]['FN'] += 1
            if print_errs:
                print(f"FN: {attr}: {sen_id}")
        for attr in preds - attrs:
            cats[attr]['FP'] += 1
            if print_errs:
                print(f"FP: {attr}: {sen_id}")

    cats['total'] = {
        stat: sum(s[stat] for s in cats.values())
        for stat in ('TP', 'FN', 'FP')}

    return cats


def eval_attrs(results, print_errs=False):
    print()
    print('='*10)
    print('Attribute extraction')
    print('='*10)
    attr_results = []
    for sen_id, sen in results.items():
        gold_attr_names = set(attr['name'] for attr in sen['attributes'])
        gen_attr_names = set(attr['name'] for attr in sen['gen_attributes'])
        attr_results.append(
            (sen_id, gold_attr_names, gen_attr_names))

    cats = count_attr_stats(
        attr_results, label_cats=ATTR_CATS, print_errs=print_errs)
    print_cat_stats(cats, 500)


def eval_modality(results):
    print()
    print('='*10)
    print('Modality')
    print('='*10)
    stats = Counter()
    for sen_id, sen in results.items():
        stats['all'] += 1
        mod = sen['modality'][0]
        gen_mod = sen['gen_mod']
        if mod == gen_mod:
            stats['corr'] += 1
        else:
            print(f'{sen_id} incorrect modality: {gen_mod} (correct: {mod})')

    acc = stats['corr'] / stats['all']
    print(f'modality accuracy: {acc:.2%} ({stats["corr"]} of {stats["all"]})')


def eval_types_values(results):
    print()
    print('='*10)
    print('Attr. types and values')
    print('='*10)
    stats = Counter()
    fp_errs = Counter()
    fn_errs = Counter()
    for sen_id, sen in results.items():
        gold_attrs = defaultdict(lambda: defaultdict(set))
        gen_attrs = defaultdict(lambda: defaultdict(set))
        for attr in sen['attributes']:
            if attr['name'] not in ATTR_IGNORE:
                gold_attrs[attr['name']][attr['type']].add(attr['value'])

        for attr in sen['gen_attributes']:
            gen_attrs[attr['name']][attr['type']].add(attr['value'])

        all_names = set()
        for name in gen_attrs:
            all_names.add(name)
            all_types = set()
            for atype, values in gen_attrs[name].items():
                all_types.add(atype)
                stats['gen_attr'] += len(values)
                if name not in gold_attrs:
                    print(f'{sen_id} incorrect attribute: {name}')
                    stats['FP'] += len(values)
                    fp_errs['no such attr'] += len(values)
                    continue

                if atype not in gold_attrs[name]:
                    print(
                        f'{sen_id} incorrect attr type {atype} of {name}'
                        f'(correct: {gold_attrs[name]})')
                    stats['FP'] += len(values)
                    fp_errs['wrong type'] += len(values)
                    continue

                gold_vals = gold_attrs[name][atype]
                stats['TP'] += len(gold_vals & values)
                for fp in values - gold_vals:
                    fp_errs['wrong value'] += 1
                    stats['FP'] += 1
                    print(f'{sen_id} incorrect value {fp} of {name}')
                for fn in gold_vals - values:
                    stats['FN'] += 1
                    fn_errs['value'] += 1
                    print(f'{sen_id} missing value {fn} of {name}')

            for atype, gold_vals in gold_attrs[name].items():
                if atype not in all_types:
                    print(f'{sen_id} missing attr type: {atype} of {name}')
                    stats['FN'] += len(gold_vals)
                    fn_errs['type'] += len(gold_vals)

        for name in gold_attrs:
            if name not in all_names:
                print(
                    f'{sen_id} missing attribute: '
                    f'{name} ({gold_attrs[name]})')

                total = sum(
                    len(g_values) for g_values in gold_attrs[name].values())
                fn_errs['missing attr'] += total
                stats['FN'] += total

    print_cat_stats({"attrs": stats})
    print()
    print('FN errs:')
    print(fn_errs.most_common())
    print()
    print('FP errs:')
    print(fp_errs.most_common())


def eval_results(results, args):
    eval_attrs(results, print_errs=args.print_errs)
    eval_modality(results)
    eval_types_values(results)


def eval_rule_ext(args):

    extractor = get_extractor(args)

    sections = load_sample(sys.stdin)

    sections, results = extractor.run_on_sections(sections)

    if args.output_file:
        print_output(results, args.output_file)

    eval_results(results, args)


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-o", "--output-file", type=str)
    parser.add_argument(
        "-p", "--print-errs", default=False, action='store_true')
    parser.add_argument("-cd", "--cache-dir", default='cache', type=str)
    parser.add_argument("-r", "--rule-ext", default=False, action='store_true')
    return parser.parse_args()


def main():
    logging.basicConfig(
        level=logging.WARNING,
        format="%(asctime)s : " +
        "%(module)s (%(lineno)s) - %(levelname)s - %(message)s")
    args = get_args()
    eval_rule_ext(args)


if __name__ == "__main__":
    main()
