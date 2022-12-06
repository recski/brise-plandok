import argparse
import json
import sys

from brise_plandok.constants import DocumentFields, SenFields


PER_ATTRS = {
    "ErrichtungGebaeude",
    "UnterbrechungGeschlosseneBauweise",
    "AufbautenZulaessig",
    "MaxAnzahlGeschosseOberirdischOhneDachgeschoss",
}

FOR_ATTRS = {
    "Stockwerk",
    "VerbotFensterZuOeffentlichenVerkehrsflaechen",
    "VerbotWohnung",
    "AnOeffentlichenVerkehrsflaechen",
    "EinfriedungZulaessig",
    "VorbautenVerbot",
    "VerbotStaffelung",
    "InSchutzzone",
    "VerbotBueroGeschaeftsgebaeude",
    "AusnahmeVonWohnungenUnzulaessig",
    "HochhausZulaessigGemaessBB",
    "VerbotAufenthaltsraum",
    "VerbotStellplaetzeUndParkgebaeude",
}


def predict_modality(doc, pred_only=False):
    for sen in doc[DocumentFields.SENS].values():
        predict_modality_for_sen(sen, pred_only)


def predict_modality_for_sen(sen, pred_only):
    if pred_only:
        attrs = sen[SenFields.PREDICTED_ATTRIBUTES]
    else:
        attrs = sen[SenFields.GOLD_ATTRIBUTES] or sen[SenFields.PREDICTED_ATTRIBUTES]
    if not attrs:
        sen["predicted_modality"] = None
    elif attrs.keys() & PER_ATTRS:
        sen["predicted_modality"] = "permission"
    elif attrs.keys() & FOR_ATTRS:
        sen["predicted_modality"] = "prohibition"
    else:
        sen["predicted_modality"] = "obligation"


def get_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-p", "--pred_only", action="store_true")
    return parser.parse_args()


def main():
    args = get_args()
    for line in sys.stdin:
        doc = json.loads(line)
        predict_modality(doc, args.pred_only)
        sys.stdout.write(json.dumps(doc) + "\n")


if __name__ == "__main__":
    main()
