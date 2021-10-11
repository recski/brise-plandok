import argparse
import json
import sys

from brise_plandok.constants import SenFields

class ValueEvaluator:

    def __init__(self, args):
        self.attributes = args.attributes
        self.tp = 0
        self.fp = 0
        self.fn = 0
        self.tp_list = []
        self.fp_list = []
        self.fn_list = []
        self.print_tp = args.true_positive
        self.print_fp = args.false_positive
        self.print_fn = args.false_negative

    def evaluate(self, doc):
        for sen in doc:
            for attribute in self.attributes:
                self._eval_for_attr(sen, attribute)
        self._calc_sore()

    def _eval_for_attr(self, sen, attribute):
        for value in sen[SenFields.GEN_VALUES][attribute]:
            if value in sen[SenFields.GOLD_VALUES][attribute]:
                self.tp += 1
                self.tp_list.append((sen[SenFields.ID], sen[SenFields.TEXT], sen[SenFields.GOLD_VALUES][attribute], value))
            else:
                self.fp += 1
                self.fp_list.append((sen[SenFields.ID], sen[SenFields.TEXT], sen[SenFields.GOLD_VALUES][attribute], value))
        for value in sen[SenFields.GOLD_VALUES][attribute]:
            if value not in sen[SenFields.GEN_VALUES][attribute]:
                self.fn += 1
                self.fn_list.append((sen[SenFields.ID], sen[SenFields.TEXT], sen[SenFields.GOLD_VALUES][attribute], value))


    def _calc_sore(self):
        precision = self.tp / (self.tp + self.fp)
        recall = self.tp / (self.tp + self.fn)
        print(f"precision: {precision}\trecall: {recall}")
        print(f"number of TP: {len(self.tp_list)}")
        print(f"number of FP: {len(self.fp_list)}")
        print(f"number of FN: {len(self.fn_list)}\n")
        self._print_tp()
        self._print_fp()
        self._print_fn()

    def _print_tp(self):
        if self.print_tp:
            for item in self.tp_list:
                print(f"{item}\n")

    def _print_fp(self):
        if self.print_fp:
            for item in self.fp_list:
                print(f"{item}\n")

    def _print_fn(self):
        if self.print_fn:
            for item in self.fn_list:
                print(f"{item}\n")

def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-a", "--attributes", nargs="+", default=None)
    parser.add_argument("-tp", "--true-positive", action="store_true", default=False)
    parser.add_argument("-fp", "--false-positive", action="store_true", default=False)
    parser.add_argument("-fn", "--false-negative", action="store_true", default=False)
    return parser.parse_args()

def main():
    args = get_args()
    value_extractor = ValueEvaluator(args)
    for line in sys.stdin:
        doc = json.loads(line)
        value_extractor.evaluate(doc)


if __name__ == "__main__":
    main()