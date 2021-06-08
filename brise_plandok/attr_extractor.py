import logging
from copy import deepcopy

from stanza.models.common.doc import Document
from tuw_nlp.grammar.ud_fl import UD_FL
from tuw_nlp.graph.utils import pn_to_graph, GraphMatcher

from brise_plandok.extractor import Extractor
from brise_plandok.regex_decompounder import regex_decompounder


PATTERNS = [
    ("(u_0 / Zweck)", "ZweckbestimmungWidmungskategorie1"),
    ("(u_0 / Nutzung)", "ZweckbestimmungWidmungskategorie1"),
    ("(u_0 / Zusammenhang)", "ZweckbestimmungWidmungskategorie1"),
    ("(u_0 / gaertnerisch)", "AnordnungGaertnerischeAusgestaltung"),
    ("(u_0 / Strassenbreite)", "StrassenbreiteMin"),
    ("(u_0 / Strasse)", "VerkehrsflaecheID"),
    ("(u_0 / Xstrasse)", "VerkehrsflaecheID"),
    ("(u_0 / Gasse)", "VerkehrsflaecheID"),
    ("(u_0 / Xgasse)", "VerkehrsflaecheID"),
    ("(u_0 / darueber)", "WidmungErsteEbene"),
    ("(u_0 / darueber)", "WidmungZweiteEbene"),
    ("(u_0 / darueber)", "WidmungZweiteEbeneBezugObjekt"),
    ("(u_0 / Flachdaecher)", "Dachart"),
    ("(u_0 / BB)", "PlanzeichenBBID"),
    # ("(u_0 / bezeichnet)", "PlanzeichenBBID"),
    ("(u_0 / begruenen)", "BegruenungDach"),
    ("(u_0 / begruent)", "BegruenungDach"),
    ("(u_0 / Pflanze)", "VorkehrungBepflanzungOeffentlicheVerkehrsflaeche"),
    ("(u_0 / Pflanzung)", "VorkehrungBepflanzungOeffentlicheVerkehrsflaeche"),
    ("(u_0 / Belichtung)", "TechnischeUndBelichtungsAufbautenZulaessig"),
    ("(u_0 / Unterbrechung)", "UnterbrechungGeschlosseneBauweise"),
    ("(u_0 / Esp)", "WidmungID"),
    ("(u_0 / Nebengebaeude)", "GebaeudeBautyp"),
    ("(u_0 / tatsaechlich)", "GebaeudeHoeheArt"),
    ("(u_0 / Gehsteige :0 (u_1 / Breite))", "GehsteigbreiteMin"),
    ("(u_0 / Gebaeudehoehe :0 (u_1 / maximal))", "GebaeudeHoeheMax"),
    ("(u_0 / ueberschreiten :1 (u_1 / Gebaeudehoehe))", "GebaeudeHoeheMax"),
    ("(u_0 / bis :2 (u_1 / Gebaeudehoehe))", "GebaeudeHoeheMax"),
    ("(u_0 / entlang  :2 (u_1 / Fluchtlinie))", "AnFluchtlinie"),
    ("(u_0 / Dachneigung :0 (u_1 / bis))", "DachneigungMax"),
    ("(u_0 / Strassenbreite :0 (u_1 :0 (u_2 / ab)))", "StrassenbreiteMin"),
    (
        "(u_0 / mit :2 (u_1 / Breite) :1 (u_2 / herstellen :2 (u_3 / Gehsteige)))",  # noqa
        "GehsteigbreiteMin"),
    (
        "(u_0 / ab :2 (u_1 / Groesse) :1 (u_2 / ausbilden :2 (u_3 / Dach)))",
        "DachflaecheMin"),
    (
        "(u_0 / liegen :0 (u_1 / hoch :0 (u_2 / NEG)) :1 (u_3 / Punkt :0 (u_4 / Dach)))",  # noqa
        "AbschlussDachMax"),
    (
        "(u_0 / Punkt :0 (u_1 / Dach) :0 (u_2 / hoch))",  # noqa
        "AbschlussDachMax")
]


class AttributeExtractor(Extractor):
    def __init__(self, *args, **kwargs):
        super(AttributeExtractor, self).__init__(*args, **kwargs)
        self.ud_fl = UD_FL(cache_dir=self.cache_dir)
        self.fl_attr = GraphMatcher(PATTERNS)

    def get_fl(self, sen):
        fl = self.ud_fl.parse(sen, 'ud', 'fl', 'amr-sgraph-src')
        return fl

    def get_attr_from_graph(self, graph):
        attrs = []
        for attr in self.fl_attr.match(graph):
            attrs.append({"name": attr, "value": None, "type": None})
        return attrs

    def get_attr_sen(self, sen):
        fl = self.get_fl(sen)
        logging.debug(f"FL: {fl}")
        graph, _ = self.postprocess_fl(fl)
        return self.get_attr_from_graph(graph)

    def postprocess_fl(self, fl):
        graph, root = pn_to_graph(fl)
        i = 0
        new_graph = deepcopy(graph)
        for node in graph:
            lemma = graph.nodes[node]['name']
            for new_lemma in regex_decompounder(lemma):
                new_node = 900 + i
                i += 1
                new_graph.add_node(new_node, name=new_lemma)
                new_graph.add_edge(node, new_node, color=0)

        return new_graph, root

    def run_on_parsed_sections(self, sections):
        results = {}
        for section in sections:
            for sen in section['sens']:
                sen_id = sen['sen_id']
                parsed_sen = Document([sen['tokens']]).sentences[0]
                logging.debug(f'processing sen {sen_id}')
                attrs = self.get_attr_sen(parsed_sen)
                results[sen_id] = {
                    "sen_id": sen_id,
                    "gen_mod": None,
                    "gen_attributes": attrs}

        return results
