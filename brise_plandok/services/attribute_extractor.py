import argparse
import json
import sys
import traceback

import graphviz
from brise_plandok.convert import Converter
from brise_plandok.extractor import get_extractor
from brise_plandok.rule_extractor import RuleExtractor
from flask import Flask, request
from tuw_nlp.text.pipeline import CachedStanzaPipeline, CustomStanzaPipeline

HOST = "localhost"
PORT = 5005
app = Flask(__name__)

# nlp_pipeline = CustomStanzaPipeline(
#         processors='tokenize,mwt,pos,lemma,depparse')
# extractor = RuleExtractor(nlp_pipeline, cache_dir="cache")

INHERITED = {"WidmungID", "PlanzeichenBBID"}


def convert_json_to_html(rules):
    def handle_list(v):
        t = "<ul>"
        for i in v:
            if isinstance(i, dict):
                t += f'<li><b>Name:</b> {i["name"]}, <b>Value:</b> {i["value"]}, <b>Type:</b> {i["type"]}</li>'
            else:
                t += f"<li>{i}</li>"
        t += "</ul>"

        return t

    def dict_to_html_ul(dd, level=0):
        """
        Convert dict to html using ul/li tags
        """
        text = "<ul>"
        for k, v in dd.items():
            text += "<li><b>%s</b>: %s</li>" % (
                k,
                dict_to_html_ul(v, level + 1)
                if isinstance(v, dict)
                else (handle_list(v) if isinstance(v, list) else v),
            )
        text += "</ul>"
        return text

    return dict_to_html_ul(rules)


# echo '0 Die Gebäudehöhe darf 6,5 m nicht überschreiten.' | python brise_plandok/get_attributes.py
def visualize(parsed):
    dot = graphviz.Digraph()
    dot.node("0", "ROOT", shape="box")
    for sentence in parsed.sentences:
        for token in sentence.tokens:
            for word in token.words:
                dot.node(str(word.id), word.text)
                dot.edge(str(word.head), str(word.id), label=word.deprel)
    return dot


@app.route("/extract", methods=["POST"])
def extract():
    ret_value = {
        "result": {
            "errors": None,
            "rules": [],
            "prover_form": [],
            "logical_form": [],
            "graph": [],
            "ud": None,
        }
    }
    data = request.get_json()

    if len(data) == 0 or not data["text"]:
        print("No input text found")
        ret_value["result"]["errors"] = "No input text found"
        sys.stdout.flush()
        return json.dumps(ret_value)

    print("Text to process: {0}".format(data))

    try:
        text = data["text"]
        args = argparse.Namespace(cache_dir="cache", rule_ext=True)
        with get_extractor(args) as extractor:
            doc = extractor.parse(text)
            ret_value["result"]["ud"] = visualize(doc).source
            to_inherit = {}
            for sen in doc.sentences:
                fl = extractor.get_fl(sen)
                fl, new_words = extractor.postprocess_fl(fl)
                ret_value["result"]["graph"].append(fl)
                vocabulary = set(w.lemma for w in sen.words).union(new_words)
                attr_tree = extractor.fl_attr.parse(fl, "fl", "attr", "alg", vocabulary=vocabulary)

                rules = extractor.attrs_to_rules(attr_tree, to_inherit)
                to_inherit.update(
                    {
                        attr["name"]: attr
                        for rule in rules
                        for attr in rule["attributes"]
                        if attr["name"] in INHERITED
                    }
                )

                for rule in rules:
                    logical_form, prover_form = Converter.convert_to_logical_form(rule)
                    ret_value["result"]["logical_form"].append(logical_form)
                    ret_value["result"]["prover_form"].append(prover_form)

                ret_value["result"]["rules"].append(convert_json_to_html(rules[0]))

    except Exception as e:
        traceback.print_exc()
        ret_value["result"]["errors"] = str(e)

    print("Returning: {0}".format(ret_value))
    sys.stdout.flush()
    return json.dumps(ret_value)


if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
