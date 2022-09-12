import datetime
import json
import os
import random
import re

import networkx as nx
import penman as pn
import requests
import streamlit as st
import streamlit.components.v1 as components

# SessionState module from https://gist.github.com/tvst/036da038ab3e999a64497f42de966a92
import SessionState

HOST = "http://localhost"
PORT = 5005

assumptions_set = SessionState.get(assumptions=[])


def to_dot(graph, marked_nodes=set()):
    lines = ["digraph finite_state_machine {", "\tdpi=70;"]
    # lines.append('\tordering=out;')
    # sorting everything to make the process deterministic
    node_lines = []
    for node, n_data in graph.nodes(data=True):
        d_node = d_clean(node)
        printname = d_clean("_".join(d_node.split("_")[:-1]))
        if "expanded" in n_data and n_data["expanded"] and printname in marked_nodes:
            node_line = '\t{0} [shape = circle, label = "{1}", \
                    style=filled, fillcolor=purple];'.format(
                d_node, printname
            ).replace(
                "-", "_"
            )
        elif "expanded" in n_data and n_data["expanded"]:
            node_line = '\t{0} [shape = circle, label = "{1}", \
                    style="filled"];'.format(
                d_node, printname
            ).replace(
                "-", "_"
            )
        elif "fourlang" in n_data and n_data["fourlang"]:
            node_line = '\t{0} [shape = circle, label = "{1}", \
                    style="filled", fillcolor=red];'.format(
                d_node, printname
            ).replace(
                "-", "_"
            )
        elif "substituted" in n_data and n_data["substituted"]:
            node_line = '\t{0} [shape = circle, label = "{1}", \
                    style="filled"];'.format(
                d_node, printname
            ).replace(
                "-", "_"
            )
        elif printname in marked_nodes:
            node_line = (
                '\t{0} [shape = circle, label = "{1}", style=filled, fillcolor=lightblue];'.format(
                    d_node, printname
                ).replace("-", "_")
            )
        else:
            node_line = '\t{0} [shape = circle, label = "{1}"];'.format(d_node, printname).replace(
                "-", "_"
            )
        node_lines.append(node_line)
    lines += sorted(node_lines)

    edge_lines = []
    for u, v, edata in graph.edges(data=True):
        if "color" in edata:
            d_node1 = d_clean(u)
            d_node2 = d_clean(v)
            edge_lines.append(
                '\t{0} -> {1} [ label = "{2}" ];'.format(
                    d_clean(d_node1), d_clean(d_node2), edata["color"]
                )
            )

    lines += sorted(edge_lines)
    lines.append("}")
    return "\n".join(lines)


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def gen_tmp_path():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    rand_id = random.randrange(100000, 999999)
    path = os.path.join("tmp", f"{timestamp}_{rand_id}")
    ensure_dir(path)
    return path


def prove_logic(deontic, to_prove, output_format):
    host = f"{HOST}:5007"
    data_json = json.dumps({"deontic": deontic, "prove": to_prove, "format": output_format})
    headers = {
        "Content-type": "application/json",
    }
    r = requests.post(host + "/prove", data=data_json, headers=headers)
    result = r.json()["result"]

    return result


def extract(text):
    host = f"{HOST}:{PORT}"
    data_json = json.dumps({"text": text})
    headers = {
        "Content-type": "application/json",
    }
    r = requests.post(host + "/extract", data=data_json, headers=headers)
    result = r.json()["result"]

    return result


def read_alto_output(raw_dl):
    id_to_word = {}

    g = pn.decode(raw_dl)

    G = nx.MultiDiGraph()
    root = None

    for i, trip in enumerate(g.triples):
        if i == 0:
            ind = trip[0].split("_")[1]
            root = f"{trip[2]}_{ind}"
        if trip[1] == ":instance":
            id_to_word[trip[0]] = trip[2]

    for trip in g.triples:
        if trip[1] != ":instance":
            node1_unique = trip[0].split("_")[1]
            node2_unique = trip[2].split("_")[1]
            dep1 = f"{id_to_word[trip[0]]}_{node1_unique}"
            dep2 = f"{id_to_word[trip[2]]}_{node2_unique}"
            edge = trip[1].split(":")[1]
            G.add_edge(dep1, dep2, color=int(edge))

    if len(G.nodes()) == 0:
        G.add_node(root)

    return G, root


def d_clean(string):
    s = string
    for c in "\\=@-,'\".!:;<>/{}[]()#^?":
        s = s.replace(c, "_")
    s = s.replace("$", "_dollars")
    s = s.replace("%", "_percent")
    s = s.replace("|", " ")
    s = s.replace("*", " ")
    if s == "#":
        s = "_number"
    keywords = ("graph", "node", "strict", "edge")
    if re.match("^[0-9]", s) or s in keywords:
        s = "X" + s
    return s


def add_to_assumptions_set(logical_form_assumption):
    # with open("assumptions_set", "r+") as f:
    #     assumptions_set = f.read().strip("\n")
    # if assumptions_set != "":
    #     assumptions_set += f", {logical_form_assumption}"
    # else:
    #     assumptions_set = logical_form_assumption

    # with open("assumptions_set", "w+") as f:
    #     f.write(assumptions_set)
    if (
        len(assumptions_set.assumptions) < 1
        or assumptions_set.assumptions[-1] != logical_form_assumption
    ):
        assumptions_set.assumptions.append(logical_form_assumption)


def main():
    st.set_page_config(layout="wide")
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {
            visibility: hidden;
            }
        footer:after {
            content:'hello';
            visibility: visible;
            display: block;
            position: relative;
            #background-color: red;
            padding: 5px;
            top: 2px;
        }
        </style>
        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    html_string = (
        "<h1 style='text-align: center; color: black;'>BRISE rule based attribute extraction</h1>"
        "<h3 style='text-align: center;'>This demo was made for our paper <b>Explainable rule extraction via semantic graphs</b> accepted at the <a href='https://sites.google.com/view/asail/asail-home'>ASAIL 2021 workshop</a> as a full paper</h3>"
        "<h3 style='text-align: center;'>Visit our <a href='https://github.com/recski/brise-plandok'>GitHub</a> page for more information and to access the code</h3><p></p>"
    )
    st.markdown(html_string, unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    col1.header("Deontic Assumptions")

    col2.header("Formula to be proved")

    sens = (
        "Für die Querschnitte der Verkehrsflächen gemäß § 5 (2) lit. c der BO für Wien wird bestimmt, dass bei einer Straßenbreite ab 10 m entlang der Fluchtlinien Gehsteige mit einer Breite von mindestens 2,0 m herzustellen sind.",
        "Flachdächer bis zu einer Dachneigung von fünf Grad sind entsprechend dem Stand der technischen Wissenschaften zu begrünen.",
        "Auf der mit BB2 bezeichneten Fläche sind die Dachflächen der Gebäude als begrünte Flachdächer auszubilden.",
        "Die Dächer dieser Nebengebäude sind ab einer Größe von 5 m2 entsprechend dem Stand der Technik als begrünte Flachdächer auszubilden, sofern es sich nicht um Glasdächer handelt.",
        "Auf der mit Esp/BB10 bezeichneten Fläche ist die Errichtung von Gebäuden mit einer maximalen Gebäudehöhe von 11,0 m zulässig. Der höchste Punkt der Dächer darf nicht höher als 3,0 m über der tatsächlich errichteten Gebäudehöhe liegen.",
        "Für die mit BB4 bezeichneten Grundflächen wird bestimmt: Die Errichtung von Gebäuden mit einer maximalen Gebäudehöhe von 8 m ist zulässig.",
        "Bei einer Straßenbreite ab 10 m sind Gehsteige mit einer Breite von mindestens 2,0 m herzustellen.",
    )

    with col1:
        option = "Enter Text Here"
        option = st.selectbox("Choose from examples to generate Assumptions", sens)

        text = st.text_area("Or input your own text for assumption", option)

        result_col1 = extract(text)

        if not result_col1["errors"]:
            save_path = gen_tmp_path()
            st.text("Extracted attributes:")
            for r in result_col1["rules"]:
                st.markdown(r, unsafe_allow_html=True)
            ud_graph_col1 = result_col1["ud"]

            fn = os.path.join(save_path, "ud_graph_assumption.dot")
            with open(fn, "w+") as f:
                f.write(ud_graph_col1)

            st.text("Logical form:")
            logical_form_assumption = ", ".join(result_col1["logical_form"])
            st.markdown(
                f'<span style="color:red"><b>{logical_form_assumption}</b></span>',
                unsafe_allow_html=True,
            )
            # st.text(f'Fourlang graph: {", ".jproverult["graph"])}')

            agree = st.button("Add assumption to the assumption set")
            if agree:
                add_to_assumptions_set(logical_form_assumption)

            if st.button("Remove the last assumption from the set"):
                assumptions_set.assumptions.pop()

            if st.button("Clear assumptions"):
                assumptions_set.assumptions.clear()

            assumptions_set_expander = st.expander("Show the assumption set:", expanded=False)

            with assumptions_set_expander:
                assumpts = ", ".join(assumptions_set.assumptions)
                st.markdown(
                    f'<span style="color:red"><b>{assumpts}</b></span>',
                    unsafe_allow_html=True,
                )

            my_expander = st.expander("Show the generated graphs:", expanded=False)

            with my_expander:
                st.graphviz_chart(ud_graph_col1, use_container_width=True)

                for i, fl in enumerate(result_col1["graph"]):
                    fourlang_graph_col1 = to_dot(read_alto_output(fl)[0])
                    fn = os.path.join(save_path, f"fourlang_graph_{i}_assumption.dot")
                    with open(fn, "w+") as f:
                        f.write(fourlang_graph_col1)
                    st.graphviz_chart(fourlang_graph_col1, use_container_width=True)

    with col2:
        sens2 = (
            "Bei einer Straßenbreite ab 12 m sind Gehsteige mit einer Breite von mindestens 1,0 m herzustellen.",
            "Bei einer Straßenbreite ab 12 m sind entlang der Fluchtlinien Gehsteige mit einer Breite von mindestens 1,0 m herzustellen.",
            "Auf der mit Esp/BB2 bezeichneten Fläche sind Flachdächer der Nebengebäude bis zu einer Dachneigung von 4 Grad zu begrünen.",
            "Auf der mit Esp/BB2 bezeichneten Fläche sind Glasdächer der Nebengebäude bis zu einer Dachneigung von fünf Grad entsprechend dem Stand der technischen Wissenschaften zu begrünen.",
            "Der höchste Punkt der Dächer auf der mit Esp/BB10 bezeichneten Fläche darf nicht genau 5,0 m über der tatsächlich errichteten Gebäudehöhe liegen. Die Errichtung von Gebäuden mit einer maximalen Gebäudehöhe von 11 m ist zulässig.",
            "Flachdächer von Nebengebäuden mit einer Dachneigung von 3 Grad sind auf der mit Esp/BB2 bezeichneten Fläche zu begrünen.",
            "Bei einer Straßenbreite bis 7 m sind Gehsteige mit einer Breite von mindestens 1,0 m herzustellen",
        )

        option = st.selectbox("Choose from examples that you want to prove", sens2)

        text = st.text_area("Or input your own text to prove", option)

        result = extract(text)

        if not result["errors"]:
            save_path = gen_tmp_path()
            st.text("Extracted attributes:")
            for r in result["rules"]:
                st.markdown(r, unsafe_allow_html=True)

            st.text("Logical form:")
            logical_form_proved = " and ".join(result["prover_form"])
            st.markdown(
                f'<span style="color:red"><b>{logical_form_proved}</b></span>',
                unsafe_allow_html=True,
            )

            output_format = st.selectbox(
                "Select the output format of the prover", ("derivation", "explanation")
            )

            if st.button("Prove"):
                prover_result = prove_logic(
                    ", ".join(assumptions_set.assumptions),
                    logical_form_proved,
                    output_format,
                )
                if not prover_result["errors"]:
                    if prover_result["output"]:
                        output = prover_result["output"]
                        if output_format == "derivation":
                            st.markdown(
                                f'<embed src="data:application/pdf;base64,{output}" width="700" height="1000" type="application/pdf">',
                                unsafe_allow_html=True,
                            )
                        else:
                            components.html(output, height=600, scrolling=True)
                    else:
                        st.text(prover_result["return_string"])
                else:
                    st.text(prover_result["errors"])
            # st.text(f'Fourlang graph: {", ".join(result["graph"])}')


if __name__ == "__main__":
    main()
