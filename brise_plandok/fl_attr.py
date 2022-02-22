import os

from tuw_nlp.grammar.alto import get_rule_string
from tuw_nlp.grammar.irtg import IRTGGrammar
from tuw_nlp.graph.utils import preprocess_lemma, preprocess_node_alto


class FL_Attr(IRTGGrammar):
    interpretations = {
        "fl": "de.up.ling.irtg.algebra.graph.GraphAlgebra",
        "attr": "de.up.ling.irtg.algebra.TreeAlgebra",
    }

    def __init__(self, **kwargs):
        super(FL_Attr, self).__init__(**kwargs)
        self.static_grammar_fn = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "fl_to_attr.irtg"
        )
        # with open(self.static_grammar_fn) as f:
        #   self.static_grammar = (line.strip('\n') for line in f.readlines())

        self.vocabulary = ["COORD", "FOR", "NEG", "OBL", "PER"]

    def gen_grammar_header(self):
        return []

    def preprocess_input(self, input_obj, **kwargs):
        self.vocabulary += sorted(
            set(preprocess_node_alto(preprocess_lemma(word)) for word in kwargs["vocabulary"])
        )
        return input_obj

    def gen_rule_strings(self):
        with open(self.static_grammar_fn) as f:
            yield from (line.strip("\n") for line in f.readlines())
        yield from (
            get_rule_string(irtg_rule, interpretations)
            for irtg_rule, interpretations, _ in (
                self.get_terminal_rule(word) for word in self.vocabulary
            )
        )

    def postprocess_output(self, output, **kwargs):
        if output is None:
            return
        return output

    def get_terminal_rule(self, raw_word):
        word = preprocess_node_alto(preprocess_lemma(raw_word))
        return (
            f"E -> e_{word} [1]",
            {"fl": f'"(u<root> / {word})"', "attr": '""'},
            "terminal",
        )
