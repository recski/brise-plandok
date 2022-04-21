import logging
from copy import deepcopy

from stanza.models.common.doc import Document
from tuw_nlp.grammar.ud_fl import UD_FL
from tuw_nlp.graph.utils import pn_to_graph, GraphMatcher

from brise_plandok.annotation.attributes import ATTR_TO_CAT
from brise_plandok.constants import SenFields
from brise_plandok.extractor import Extractor
from brise_plandok.regex_decompounder import regex_decompounder

PATTERNS_BY_ATTR = {
    "AbschlussDachMaxBezugGebaeude": {
        "(u_0 / liegen :0 (u_1 / hoch :0 (u_2 / NEG)) :1 (u_3 / Punkt :0 (u_4 / Dach)))",  # noqa
        "(u_0 / Punkt :0 (u_1 / Dach) :0 (u_2 / hoch))",
    },
    "AnFluchtlinie": {
        "(u_0 / entlang  :2 (u_1 / Fluchtlinie))",
        "(u_0 / an  :2 (u_1 / Fluchtlinie))",
        "(u_0 / entlang  :2 (u_1 / Baulinie))",
        "(u_0 / an  :2 (u_1 / Baulinie))",
    },
    "AnordnungGaertnerischeAusgestaltung": {"(u_0 / gaertnerisch)"},
    "AufbautenZulaessig": {"(u_0 / Belichtung)"},
    "BegruenungDach": {"(u_0 / begruenen)", "(u_0 / begruent)"},
    "Dachart": {
        "(u_0 / Flachdaecher)",
    },
    "DachflaecheMin": {"(u_0 / ab :2 (u_1 / Groesse) :1 (u_2 / ausbilden :2 (u_3 / Dach)))"},
    "DachneigungMax": {"(u_0 / Dachneigung :0 (u_1 / bis))"},
    "Flaechen": {
        "(u_0 / Bauplatzflaeche)",
        "(u_0 / Brutto)",
        "(u_0 / Flaeche :0 (u_2 / bebaut))",
        "(u_0 / Flaeche :0 (u_2 / unbebaut))",
    },
    "GebaeudeBautyp": {"(u_0 / Nebengebaeude)"},
    "GebaeudeHoeheArt": {"(u_0 / tatsaechlich)"},
    "GebaeudeHoeheMax": {
        "(u_0 / Gebaeudehoehe :0 (u_1 / maximal))",
        "(u_0 / ueberschreiten :1 (u_1 / Gebaeudehoehe))",
        "(u_0 / bis :2 (u_1 / Gebaeudehoehe))",
    },
    "GehsteigbreiteMin": {
        "(u_0 / Gehsteige :0 (u_1 / Breite))",
        "(u_0 / mit :2 (u_1 / Breite) :1 (u_2 / herstellen :2 (u_3 / Gehsteige)))",  # noqa
    },
    "Planzeichen": {
        "(u_0 / BB)",
        "(u_0 / Esp)",
        "(u_0 / öDg)",
        "(u_0 / öDf)",
    },
    "Stockwerk": {
        "(u_0 / Erdgeschoss)",
    },
    "StrassenbreiteMin": {
        "(u_0 / Strassenbreite)",
        "(u_0 / Strassenbreite :0 (u_1 :0 (u_2 / ab)))",
    },
    "UnterbrechungGeschlosseneBauweise": {
        "(u_0 / Unterbrechung)",
    },
    "VerkehrsflaecheID": {
        "(u_0 / Strasse)",
        "(u_0 / Xstrasse)",
        "(u_0 / Gasse)",
        "(u_0 / Xgasse)",
    },
    "VorkehrungBepflanzung": {"(u_0 / Pflanze)", "(u_0 / Pflanzung)"},
    "WidmungInMehrerenEbenen": {"(u_0 / darueber)"},
    "WidmungUndZweckbestimmung": {
        "(u_0 / Zweck)",
        "(u_0 / Nutzung)",
        "(u_0 / Zusammenhang)",
        "(u_0 / Esp)",
    },
}


def get_patterns():
    all_patterns = []
    for attr, patterns in PATTERNS_BY_ATTR.items():
        if attr not in ATTR_TO_CAT:
            logging.warning(f"Attribute not in the list (might be deprecated): {attr}")
        for patt in patterns:
            all_patterns.append((patt, attr))
    return all_patterns


class AttributeExtractor(Extractor):
    def __init__(self, *args, **kwargs):
        super(AttributeExtractor, self).__init__(*args, **kwargs)

        # initialize IRTG-based UD-FL conversion
        self.ud_fl = UD_FL(cache_dir=self.cache_dir)

        # networkx-based graph matching for attribute extraction
        patterns = get_patterns()
        self.fl_attr = GraphMatcher(patterns)

    def get_fl(self, sen):
        fl = self.ud_fl.parse(sen, "ud", "fl", "amr-sgraph-src")
        return fl

    def get_attr_from_graph(self, graph):
        attrs = []
        # run the attribute matcher and return the extracted attributes
        for attr in self.fl_attr.match(graph):
            attrs.append({"name": attr, "value": None, "type": None})
        return attrs

    def get_attr_sen(self, sen):
        # run the ud-fl conversion with IRTGs
        fl = self.get_fl(sen)
        logging.debug(f"FL: {fl}")
        graph, _ = self.postprocess_fl(fl)
        return self.get_attr_from_graph(graph)

    def postprocess_fl(self, fl):
        graph, root = pn_to_graph(fl)
        i = 0
        new_graph = deepcopy(graph)
        for node in graph:
            lemma = graph.nodes[node]["name"]
            for new_lemma in regex_decompounder(lemma):
                new_node = 900 + i
                i += 1
                new_graph.add_node(new_node, name=new_lemma)
                new_graph.add_edge(node, new_node, color=0)

        return new_graph, root

    def run_on_parsed_sections(self, sections):
        """First running the UD-FL conversion, then running the attribute matcher IRTG

        Args:
            sections (json): the json object without the attributes

        Returns:
            json: returns the filled attributes added to the json object
        """
        results = {}
        for section in sections:
            for sen in section["sens"]:
                if SenFields.ID in sen:
                    sen_id = sen[SenFields.ID]
                else:
                    sen_id = sen["sen_id"]
                parsed_sen = Document([sen["tokens"]]).sentences[0]
                logging.debug(f"processing sen {sen_id}")
                attrs = self.get_attr_sen(parsed_sen)
                results[sen_id] = {
                    "sen_id": sen_id,
                    "gen_mod": None,
                    "gen_attributes": attrs,
                }

        return results
