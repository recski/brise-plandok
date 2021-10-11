import re

VALUES = {
    # Konstruktionen
    r".*(als|für|sind) (.*)(ausgewiesen|gewidmeten|bezeichneten|vorbehalten|verwendet|(z|Z)wecke|Nutzung).*": 2,
    r".*(der|dem) (.*) zugeordnet.*": 2,
    r".*Errichtung (von )?(.*) vorbehalten.*": 2,
    r".*Nutzung (als|für) (.*) (erforderlich|zugeführt).*": 2,
    # Gesetz
    r".*(Nutzungen im Sinne des § (.*) des Wiener Garagengesetzes).*": 1,
    # List
    r".*(Grünland).*": 1,
    r".*(Erholungsgebiet).*": 1,
    r".*(Kleingartengebiet).*": 1,
    r".*(Sport-und Spielplätze) .*": 1,
    r".*(Schutzzone).*": 1,
    r".*(Wohnzone).*": 1,
    r".*(Wohngebiet).*": 1,
    r".*(Dienstwohnung).*": 1,
    r".*(Parkanlage).*": 1,
    r".*(Parkschutzgebiet).*": 1,
    r".*(Dachterrassen).*": 1,
    r".*(Beherbergungsstätten).*": 1,
    r".*(Wintergärten).*": 1,
    r".*(Sporthallen?).*": 1,
    r".*(Einkaufszentr(um|en)).*": 1,
    r".*(Bauland).*": 1,
    r".*((Gemischtes )?Baugebiet).*": 1,
}

class WidmungUndZweckbestimmungExtractor:

    def extract(self, text):
        for regex, group in VALUES.items():
            m = re.match(regex, text)
            if m is not None:
                yield m.group(group)
