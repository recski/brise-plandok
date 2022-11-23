import json
import logging
from copy import deepcopy

from stanza.models.common.doc import Document
from tuw_nlp.grammar.ud_fl import UD_FL
from tuw_nlp.graph.utils import graph_to_isi, read_alto_output

from brise_plandok.asail.attr_tree import AttrTree
from brise_plandok.asail.extractor import Extractor
from brise_plandok.asail.fl_attr import FL_Attr
from brise_plandok.asail.regex_decompounder import regex_decompounder

BOOLEANS = {
    "AnFluchtlinie",
    "BegruenungDach",
    "ErrichtungGebaeude",
    "Kleinhaeuser",
    "TechnischeAufbautenZulaessig",
    "UnterbrechungGeschlosseneBauweise",
    "UnzulaessigkeitUnterirdischeBauwerke",
    "VerbotStaffelung",
    "technischeUndBelichtungsAufbautenZulaessig",
    "EinfriedungZulaessig",
    "FlaecheBebaubar",
    "FlaecheBebaut",
    "UnterirdischeBaulichkeiten",
    "HochhausUnzulaessigGemaessBB",
    "HochhausZulaessigGemaessBB",
    "AnBaulinie",
    "AnOeffentlichenVerkehrsflaechen",
    "InSchutzzone",
    "PlangebietAllgemein",
    "StruktureinheitBebaubar",
    "AusnahmePruefungErforderlich",
    "nA",
    "StrittigeBedeutung",
    "WeitereBestimmungPruefungErforderlich",
    "ZuVorherigemSatzGehoerig",
    "UnzulaessigBueroGeschaeftsgebaeude",
    "VerbotAufenthaltsraum",
    "VerbotWohnung",
    "AnlageZumEinstellenVorhanden",
    "StellplatzImNiveauZulaessig",
    "StellplatzregulativVorhanden",
    "AnordnungGaertnerischeAusgestaltung",
    "AusnahmeGaertnerischAuszugestaltende",
    "BegruenungFront",
    "Einbautrasse",
    "Massengliederung",
    "UnzulaessigFensterZuOeffentlichenVerkehrsflaechen",
    "VonBebauungFreizuhalten",
    "VonBebauungFreizuhaltenAusnahme",
    "VorkehrungBepflanzung",
    "BegruenungDach",
    "EinfriedungAusgestaltung",
    "EinfriedungLage",
    "BestimmungenFuerHochhausUndGrossbauvorhaben",
    "EinkaufszentrumZweck",
    "Geschaeftsstrassen",
    "GrossbauvorhabenZweck",
    "VerkehrsflaecheID",
    "AusnahmeVonWohnungenUnzulaessig",
    "WidmungErsteEbeneBezugObjekt",
    "WidmungZweiteEbeneBezugObjekt",
    "WidmungDritteEbeneBezugObjekt",
    "ZweckbestimmungWidmungskategorie",
    "GaragengebaeudeAusfuehrung",
    "GebaeudeEinschraenkungP",
    "GebaeudeVerbotP",
    "OberflaecheBestimmungP",
    "StellplatzverpflichtungArt",
    "VorbautenBeschraenkung",
    "VorbautenVerbot",
}

CONDITIONS = {"PlanzeichenBBID", "WidmungID", "GebaeudeBautyp"}

NONQ_VALS = {"v_Esp"}

PREFIX_QS = {"BB"}

INHERITED = {"WidmungID", "PlanzeichenBBID"}


def construct_value(raw_val, vals_to_quants):
    val = raw_val.replace("v_", "").rstrip("_").replace("COMMA", ",")
    if raw_val not in vals_to_quants:
        return val
    quant = vals_to_quants[raw_val]
    if quant in PREFIX_QS:
        return quant + val
    return val + quant


class RuleExtractor(Extractor):
    def __init__(self, *args, **kwargs):
        super(RuleExtractor, self).__init__(*args, **kwargs)
        self.ud_fl = UD_FL(cache_dir=self.cache_dir)
        self.fl_attr = FL_Attr(cache_dir=self.cache_dir)

    def get_fl(self, sen):
        fl = self.ud_fl.parse(sen, "ud", "fl", "amr-sgraph-src")
        return fl

    def _get_attr_sen(self, sen, fl, new_words):
        vocabulary = set(w.lemma for w in sen.words).union(new_words)
        attr_tree = self.fl_attr.parse(fl, "fl", "attr", "alg", vocabulary=vocabulary)
        return attr_tree

    def get_attr_sen(self, sen):
        fl = self.get_fl(sen)
        fl, new_words = self.postprocess_fl(fl)
        return self._get_attr_sen(sen, fl, new_words)

    def postprocess_fl(self, fl):
        graph, root = read_alto_output(fl)
        i = 0
        unchanged = True
        new_words = set()
        new_graph = deepcopy(graph)
        for node in graph:
            lemma, id_and_src = node.split("_")
            for new_lemma in regex_decompounder(lemma):
                new_words.add(new_lemma)
                new_id = 900 + i
                i += 1
                new_node = f"{new_lemma}_{new_id}"
                new_graph.add_edge(node, new_node, color=0)
                unchanged = False

        if unchanged:
            return fl, new_words

        logging.debug("new words:", new_words)
        new_fl = graph_to_isi(new_graph, ud=False, algebra="graph", root_id=root, preprocess=True)

        return new_fl, new_words

    def attrs_to_rules(self, attr_tree_string, to_inherit=None):
        if attr_tree_string is None:
            logging.debug("FL_Attr returned None")
            return []
        attr_tree = AttrTree.from_string(attr_tree_string)
        attr_tree.count_attr_dists()
        logging.debug(json.dumps(attr_tree.d, indent=2))
        attrs = list(attr_tree.d["self"].keys())
        rule = {
            "modality": "prohibition" if "FOR" in attrs else "obligation",
            # 'modality': 'prohibition' if 'FOR' in attrs else (
            #     'permission' if 'PER' in attrs else 'obligation'),
            "attributes": [],
        }

        names, values, quants, modalities = [], [], [], []
        for attr in attrs:
            if attr.startswith("v_"):
                values.append(attr)
            elif attr.startswith("q_"):
                quants.append(attr)
            elif len(attr) >= 3 and attr[:3] in ("PER", "OBL", "FOR", "EXC"):
                modalities.append(attr)
            else:
                names.append(attr)

        vals_to_quants = {}
        logging.debug(f"names: {names}, values: {values}, quants: {quants}" f"mods: {modalities}")
        values_remaining = [v for v in values if v not in NONQ_VALS]
        for q in quants:
            logging.debug(f"matching q: {q}")
            if not values_remaining:
                logging.debug("nothing left :(")
                continue
            val = min(values_remaining, key=lambda v: attr_tree.d[q][v])
            logging.debug(f"best v: {val}")
            vals_to_quants[val] = q.replace("q_", "").rstrip("_")
            values_remaining.remove(val)

        names_to_types = {}

        names_remaining = [n for n in names if n not in CONDITIONS]
        for mod in modalities:
            if mod.startswith("OBL") or mod.startswith("EXC") or mod.startswith("FOR"):  # noqa
                logging.debug(f"matching mod: {mod}")
                if not names_remaining:
                    logging.debug("nothing left :(")
                    continue
                name = min(names_remaining, key=lambda n: attr_tree.d[mod][n])
                if mod.startswith("OBL") or mod.startswith("FOR"):
                    names_to_types[name] = "content"
                else:
                    names_to_types[name] = "conditionException"
                logging.debug(f"best n: {name}")
                names_remaining.remove(name)

        names_to_vals = {}
        names_to_match = []
        for name in names:
            if name not in names_to_types:
                names_to_types[name] = "condition"
            if name in BOOLEANS:
                names_to_vals[name] = None
            else:
                names_to_match.append(name)

        values_remaining = [v for v in values]
        while len(values_remaining) > 0 and len(names_to_match) > 0:
            logging.debug("names and values to match:", names_to_match, values_remaining)
            all_pairs = [(n, v) for n in names_to_match for v in values_remaining]
            best_pair = min(all_pairs, key=lambda p: attr_tree.d[p[0]][p[1]])
            logging.debug("best pair:", best_pair)
            name, value = best_pair
            names_to_vals[name] = construct_value(value, vals_to_quants)
            values_remaining.remove(value)
            names_to_match.remove(name)

        for name in names:
            if name in ("OBL", "PER", "FOR"):
                continue
            rule["attributes"].append(
                {
                    "name": name.rstrip("_"),
                    "value": names_to_vals.get(name),
                    "type": names_to_types.get(name),
                }
            )

        if to_inherit:
            for name, attr in to_inherit.items():
                rule["attributes"].append(attr)

        return [rule]

    def get_rules_from_sen(self, sen, to_inherit=None):
        attr_tree = self.get_attr_sen(sen)
        return self.attrs_to_rules(attr_tree, to_inherit=to_inherit)

    def get_rules_from_parsed_section(self, sens):
        rules_by_sen = {}
        to_inherit = {}
        for sen in sens:
            parsed_sen = Document([sen["tokens"]]).sentences[0]
            rules = self.get_rules_from_sen(parsed_sen, to_inherit)
            to_inherit.update(
                {
                    attr["name"]: attr
                    for rule in rules
                    for attr in rule["attributes"]
                    if attr["name"] in INHERITED
                }
            )
            rules_by_sen[sen["sen_id"]] = rules
        return rules_by_sen

    def run_on_parsed_sections(self, sections):
        results = {}
        for section in sections:

            rules_by_sen = self.get_rules_from_parsed_section(section["sens"])

            for sen in section["sens"]:
                sen_id = sen["sen_id"]
                gen_rules = rules_by_sen[sen_id]
                if not gen_rules:
                    logging.debug(f"no rules returned for sen {sen_id}, skipping")
                    continue

                gen_mods = set(rule["modality"] for rule in gen_rules)
                assert len(gen_mods) == 1
                gen_mod = gen_mods.pop()

                results[sen_id] = {
                    "sen_id": sen_id,
                    "gen_mod": gen_mod,
                    "gen_attributes": [
                        {
                            "name": attr["name"],
                            "type": attr["type"],
                            "value": attr["value"],
                        }
                        for rule in gen_rules
                        for attr in rule["attributes"]
                    ],
                }

        return results
