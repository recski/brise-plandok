import re

VALUES = {
    r".*der ((öffentlichen )?Verkehrsfläche( \((Fußweg|Rad- und Fußweg)\))?)(?! dem).*": 1,
    r".*(dem|der Widmung) (Verkehrsband).*": 2,
    r".*als (Verkehrsband|Verkehrsbänder).*": 1,
    r".*(dem|der Widmung) (Bauland/Wohngebiet).*": 2,
    r".*die (angrenzenden Bebauungsbestimmungen) anzuwenden.*": 1,
    r".*als (.*) festgesetzt.*": 1,
    r".*(der Errichtung von|für eine) (Anlagen? zum Einstellen von Kraftfahrzeugen) vorbehalten.*": 2,
    r".*dem ((?!Niveau.*)[^,]*) zugeordnet.*": 1,
    r".* ((Bauland/)?(g|G)emischte(n|s) Baugebiet(( ?- ?|/)Geschäftsviertel)?).*": 1,
    r".* ([^ ]*) zuzuordnen.*": 1,
    r".* dem (Grünland/Erholungsgebiet – Wasserfläche),.*": 1,
    r".*(im Plan dargestellten Widmung mit den für diese Widmung geltenden Bestimmungen).*": 1,
    r".* (Wohngebiet) .*": 1,
}

class WidmungInMehrerenEbenenExtractor:

    def extract(self, text):
        for regex, group in VALUES.items():
            m = re.search(regex, text)
            if m is not None:
                yield m.group(group)
