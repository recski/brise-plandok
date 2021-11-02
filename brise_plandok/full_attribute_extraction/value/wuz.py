import re

VALUES = {
    # Konstruktionen
    r".*(sind( nur der)?) ([^0-9]*) vorbehalten.*": 3,
    r".*(dem|der Widmung|der) (.*) zugeordnet.*": 2,
    r".*Nutzung (als|für) (.*) (erforderlich|zugeführt).*": 2,
    r".*für ([^0-9]*) verwendet.*": 1,
    r".*(für|als) ([^0-9]*) vor(zu)?behalten.*": 2,
    r".*als ([^0-9]*) ausgewiesen.*": 1,
    r".*als ((?!.*Esp)[^0-9]*) bezeichneten.*": 1,
    r".*als ([^0-9()]*)( \(.\))? gewidmeten.*": 1,
    r".*Errichtung( von)? ((?!gelangenden Gebäude.*)[^0-9]*) vorbehalten.*": 2,
    r".*zur Errichtung gelangenden Gebäude sind( nur der)? ([^0-9]*) vorbehalten.*": 2,
    r".*als ([^0-9]*) ÖZ festgesetzt.*": 1,
    r".*Widmung ([^0-9()]*) (\(\w\w \w\w\))? ?wird.*": 1,
    r".*Widmung ([^0-9()]*) (\(\w\w \w\w\)).*": 1,
    r".* (\w* Nutzung und Pflege).*": 1,
    r".*Zweckbestimmung „?([^„“]*)“? zuzuführen.*": 1,
    # Gesetz
    r".*(Nutzungen im Sinne des . 50 \(1\) des Wiener Garagengesetzes).*": 1,
    r".*(Nutzungen im Sinne des . 50 \(2\) des Wiener Garagengesetzes).*": 1,
    r".*(Nutzung gemäß § 6 Abs. 6 der BO für Wien).*": 1,
    # List
    r".* (Bauland) .*": 1,
    r".* (Parkschutzgebiet) .*": 1,
    r".* (Erholungsgebiet/( |-)?Sport- und Spielplätze) .*": 1,
    r".* (Bauland/Industriegebiet) .*": 1,
    r".*^(Beherbergungsstätten).*": 1,
    r".* (Wohngebiet) .*": 1,
    r".*(Wohnzone).*": 1,
    r".*(Wintergärten).*": 1,
    r".*(Einrichtungen der Haustechnik).*": 1,
    r".*(Einkaufszentrum).*": 1,
    r".*(Sporthallen).*": 1,
    r".*(Schutzzone).*": 1,
}

class WidmungUndZweckbestimmungExtractor:

    def extract(self, text):
        for regex, group in VALUES.items():
            m = re.search(regex, text)
            if m is not None:
                yield m.group(group)
