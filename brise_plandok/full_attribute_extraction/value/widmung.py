from brise_plandok.full_attribute_extraction.utils.constants import GROUP

WIDMUNG = {
    # Konstruktionen
    r"(sind( nur der)?) ([^0-9]*) vorbehalten": {
        GROUP: 3,
    },
    r"(dem|der Widmung|der) (.*) zugeordnet": {
        GROUP: 2,
    },
    r"Nutzung (als|für) (.*) (erforderlich|zugeführt)": {
        GROUP: 2,
    },
    r"für ([^0-9]*) verwendet": {
        GROUP: 1,
    },
    r"(für|als) ([^0-9]*) vor(zu)?behalten": {
        GROUP: 2,
    },
    r"als ([^0-9]*) ausgewiesen": {
        GROUP: 1,
    },
    r"als ((?!.*Esp)[^0-9]*) bezeichneten": {
        GROUP: 1,
    },
    r"als ([^0-9()]*)( \(.\))? gewidmeten": {
        GROUP: 1,
    },
    r"Errichtung( von)? ((?!gelangenden Gebäude.*)[^0-9]*) vorbehalten": {
        GROUP: 2,
    },
    r"zur Errichtung gelangenden Gebäude sind( nur der)? ([^0-9]*) vorbehalten": {
        GROUP: 2,
    },
    r"als ([^0-9]*) ÖZ festgesetzt": {
        GROUP: 1,
    },
    r"Widmung ([^0-9()]*) (\(\w\w \w\w\))? ?wird": {
        GROUP: 1,
    },
    r"Widmung ([^0-9()]*) (\(\w\w \w\w\))": {
        GROUP: 1,
    },
    r" (\w* Nutzung und Pflege)": {
        GROUP: 1,
    },
    r"Zweckbestimmung „?([^„“]*)“? zuzuführen": {
        GROUP: 1,
    },
    # Gesetz
    r"(Nutzungen im Sinne des . 50 \(1\) des Wiener Garagengesetzes)": {
        GROUP: 1,
    },
    r"(Nutzungen im Sinne des . 50 \(2\) des Wiener Garagengesetzes)": {
        GROUP: 1,
    },
    r"(Nutzung gemäß § 6 Abs. 6 der BO für Wien)": {
        GROUP: 1,
    },
    # List
    r" (Bauland) ": {
        GROUP: 1,
    },
    r" (Parkschutzgebiet) ": {
        GROUP: 1,
    },
    r" (Erholungsgebiet/( |-)?Sport- und Spielplätze) ": {
        GROUP: 1,
    },
    r" (Bauland/Industriegebiet) ": {
        GROUP: 1,
    },
    r"^(Beherbergungsstätten)": {
        GROUP: 1,
    },
    r" (Wohngebiet) ": {
        GROUP: 1,
    },
    r"(Wohnzone)": {
        GROUP: 1,
    },
    r"(Wintergärten)": {
        GROUP: 1,
    },
    r"(Einrichtungen der Haustechnik)": {
        GROUP: 1,
    },
    r"(Einkaufszentrum)": {
        GROUP: 1,
    },
    r"(Sporthallen)": {
        GROUP: 1,
    },
    r"(Schutzzone)": {
        GROUP: 1,
    },
}
