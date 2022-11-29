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


def predict_modality(doc):
    for sen in doc[DocumentFields.SENS].values():
        attrs = sen[SenFields.GOLD_ATTRIBUTES] or sen[SenFields.PREDICTED_ATTRIBUTES]
        if not attrs:
            sen["predicted_modality"] = None
        elif attrs.keys() & PER_ATTRS:
            sen["predicted_modality"] = "permission"
        elif attrs.keys() & FOR_ATTRS:
            sen["predicted_modality"] = "prohibition"
        else:
            sen["predicted_modality"] = "obligation"

    return doc


def main():
    for line in sys.stdin:
        doc = json.loads(line)
        predict_modality(doc)
        sys.stdout.write(json.dumps(doc) + "\n")


if __name__ == "__main__":
    main()
