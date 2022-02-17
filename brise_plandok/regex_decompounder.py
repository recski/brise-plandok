import re

SIMPLE_PATTERNS = {
    # case sensitive on purpose :( (to avoid e.g. Strassenbreite)
    "Xstrasse": [re.compile("strasse")],
    "Xgasse": [re.compile("gasse")],
    "Xdach": [re.compile("dae?ch")],
}

GROUP_PATTERNS = {
    # quantities with units
    re.compile(r"^([1-9][0-9]*)(m[23]?)$"),
    # BB
    re.compile(r"^(BB)([1-9][0-9]*)$"),
    # /
    re.compile(r"(.*)SLASH(.*)"),
}


def regex_decompounder(word):
    lemmas = []
    for patt in GROUP_PATTERNS:
        match = patt.search(word)
        if match:
            lemmas += [s for s in match.groups() if s]
    for lemma, patterns in SIMPLE_PATTERNS.items():
        if lemma == word:
            continue
        for patt in patterns:
            if patt.search(word):
                lemmas.append(lemma)
                break

    lemmas += [slemma for lemma in lemmas for slemma in regex_decompounder(lemma)]

    return lemmas
