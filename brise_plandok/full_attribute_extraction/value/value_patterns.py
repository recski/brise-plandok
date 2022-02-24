from brise_plandok.constants import AttributesNames
from brise_plandok.full_attribute_extraction.constants import NUMBER_WITH_METER, GROUP, ALL, VALUE, TRUE, \
    NUMBER_WITH_PERCENT, GAERTNERISH_GESTALTEN, DACH, NUMBER_WITH_DEGREE, NUMBER_WITH_SQUARE_METER, FALSE, \
    STRASSE, NUMBER_WITH_CUBIC_METER, NUMBER
from brise_plandok.full_attribute_extraction.value.widmung_patterns import WIDMUNG

VALUE_PATTERNS = {

    AttributesNames.AbschlussDachMaxBezugGebaeude: {
        r"(nicht höher als|nicht mehr als|höchstens|maximal|bis zu) " + NUMBER_WITH_METER + r" über": {
            GROUP: 2,
        },
    },

    AttributesNames.AnFluchtlinie: {
        ALL: {
            VALUE: TRUE,
        },
    },

    AttributesNames.AnlageZumEinstellenVorhanden: {
        ALL: {
            VALUE: TRUE,
        },
    },

    AttributesNames.AnOeffentlichenVerkehrsflaechen: {
        ALL: {
            VALUE: TRUE,
        },
    },

    AttributesNames.AnordnungGaertnerischeAusgestaltung: {
        ALL: {
            VALUE: TRUE,
        },
    },

    AttributesNames.AnordnungGaertnerischeAusgestaltungProzentual: {
        NUMBER_WITH_PERCENT: {
            GROUP: 1,
        },
    },

    AttributesNames.AnteilBaumbepflanzung: {
        NUMBER_WITH_PERCENT: {
            GROUP: 1,
        },
    },

    AttributesNames.AnteilDachbegruenung: {
        NUMBER_WITH_PERCENT: {
            GROUP: 1,
        },
    },

    AttributesNames.AnzahlGebaeudeMax: {
        r"[Pp]ro Bauplatz( darf)?( nur)? (ein)( Nebengebäude)": {
            GROUP: 3,
        },
    },

    AttributesNames.ArkadeHoehe: {
        r"(H|h)öhe von( mindestens)? " + NUMBER_WITH_METER: {
            GROUP: 3,
        },
    },

    AttributesNames.AufbautenZulaessig: {
        r"nicht zulässig": {
            VALUE: FALSE,
        },
        r"((?!nicht).)* zulässig": {
            VALUE: TRUE,
        },
    },

    AttributesNames.AusnahmeVonWohnungenUnzulaessig: {
        r"mit Ausnahme( der| von)? (.*) untersagt": {
            GROUP: 2,
        },
    },

    AttributesNames.AusnahmeGaertnerischAuszugestaltende: {
        r"mit Ausnahme( der| von| für)? ([^:]*),? " + GAERTNERISH_GESTALTEN: {
            GROUP: 2,
        },
        r"mit Ausnahme( der| von)? (.*), wird bestimmt*": {
            GROUP: 2,
        },
        r"soweit sie nicht (für|als) (.*) benötigt werden, .*gärtnerisch": {
            GROUP: 2,
        },
        r"soweit nicht (.*) erforderlich ist, " + GAERTNERISH_GESTALTEN: {
            GROUP: 1,
        },
        r"soweit sie nicht für (.*) benötigt werden": {
            GROUP: 1,
        },
        r"sofern nicht eine Befestigung für die Nutzung als (.*) erforderlich ist, " + GAERTNERISH_GESTALTEN: {
            GROUP: 1,
        },
        r"nicht von (.*) in Anspruch genommenen Bereiche,? sind " + GAERTNERISH_GESTALTEN: {
            GROUP: 1,
        },
        r"(A|a)usgenommen davon sind (.*).": {
            GROUP: 2,
        },
        r"(Sport- und Spielplätzen)": {
            GROUP: 1,
        },
    },

    AttributesNames.Bauklasse: {
        r" (I|II|III|IV|V|VI)[ ,]": {
            GROUP: 1,
        },
    },

    AttributesNames.BauweiseID: {
        r"(geschlossen|offen|gekuppelt|gruppenbauweise)": {
            GROUP: 1,
        },
    },

    AttributesNames.BebauteFlaecheMax: {
        NUMBER_WITH_SQUARE_METER: {
            GROUP: 1,
        },
    },

    AttributesNames.BebauteFlaecheMaxNebengebaeude: {
        NUMBER_WITH_SQUARE_METER: {
            GROUP: 1,
        },
    },

    AttributesNames.BebauteFlaecheMaxProzentual: {
        NUMBER_WITH_PERCENT: {
            GROUP: 1,
        },
    },

    AttributesNames.BebauteFlaecheMin: {
        NUMBER_WITH_SQUARE_METER: {
            GROUP: 1,
        },
    },

    AttributesNames.BegruenungDach: {
        ALL: {
            VALUE: TRUE,
        },
    },

    AttributesNames.Dachart: {
        r"(Flach)" + DACH: {
            VALUE: "Flachdach",
        },
        r"(Pult)" + DACH: {
            VALUE: "Pultdach",
        },
        r"(Glas)" + DACH: {
            VALUE: "Glasdach",
        },
        r"(Flug)" + DACH: {
            VALUE: "Flugdach",
        },
        r"(Vor)" + DACH: {
            VALUE: "Vordach",
        },
        r"(begehbar)": {
            GROUP: 1,
        },
    },

    AttributesNames.DachneigungMax: {
        r"((bis zu|mit) einer (Dach)?[Nn]eigung von|maximal|bis|bis zu) " + NUMBER_WITH_DEGREE: {
            GROUP: 4
        },
        r"zwischen " + NUMBER + r" und " + NUMBER_WITH_DEGREE: {
            GROUP: 6
        },
        r"Dachneigung( darf)? " + NUMBER_WITH_DEGREE + r" nicht überschreiten": {
            GROUP: 2
        },
        r"(fünf Grad)": {
            GROUP: 1
        },
        r"Dachneigung mindestens " + NUMBER_WITH_DEGREE + r" und höchstens " + NUMBER_WITH_DEGREE + r" zu betragen": {
            GROUP: 6
        },
        r"[Nn]eigung von höchstens " + NUMBER_WITH_DEGREE: {
            GROUP: 6
        },
    },

    AttributesNames.DachneigungMin: {
        r"von einer Dachneigung von mindestens " + NUMBER_WITH_DEGREE: {
            GROUP: 1
        },
        r"zwischen " + NUMBER + r" und " + NUMBER_WITH_DEGREE: {
            GROUP: 1
        },
        r"Dachneigung darf " + NUMBER_WITH_DEGREE + r" nicht unterschreiten": {
            GROUP: 1
        },
        r"Dachneigung mindestens " + NUMBER_WITH_DEGREE + r" und höchstens " + NUMBER_WITH_DEGREE + r" zu betragen": {
            GROUP: 1
        },
    },

    AttributesNames.DachflaecheMin: {
        NUMBER_WITH_SQUARE_METER: {
            GROUP: 1
        },
    },

    AttributesNames.DurchfahrtBreite: {
        r"(B|b)reite von( mindestens)? " + NUMBER_WITH_METER: {
            GROUP: 3
        },
        r" " + NUMBER_WITH_METER + r" (B|b)reite": {
            GROUP: 1
        },
        r"hat " + NUMBER_WITH_METER + r" zu betragen": {
            GROUP: 1
        },
        r"(im Plan dargestellten Breite)": {
            GROUP: 1
        },
    },

    AttributesNames.DurchfahrtHoehe: {
        r"(H|h)öhe von( mindestens)? " + NUMBER_WITH_METER: {
            GROUP: 3
        },
        r" " + NUMBER_WITH_METER + r" (H|h)[öo]he": {
            GROUP: 1
        },
    },

    AttributesNames.DurchgangBreite: {
        r"[Bb]reite von( mindestens)? (von )?" + NUMBER_WITH_METER: {
            GROUP: 3
        },
        r" " + NUMBER_WITH_METER + r" [Bb]reite": {
            GROUP: 1
        },
        r"hat " + NUMBER_WITH_METER + r" zu betragen": {
            GROUP: 1
        },
        r"(im Plan dargestellten Breite)": {
            GROUP: 1
        },
        r"mit einer lichten Breite und einer lichten Höhe von je mindestens " + NUMBER_WITH_METER: {
            GROUP: 1
        },
    },

    AttributesNames.DurchgangHoehe: {
        r"(H|h)öhe von(( je)? mindestens)? " + NUMBER_WITH_METER: {
            GROUP: 4,
        },
        NUMBER_WITH_METER + r"( lichter)? [Hh][oö]he": {
            GROUP: 1,
        },
        r"einer (lichten )?Höhe von (mindestens )?" + NUMBER_WITH_METER: {
            GROUP: 3,
        },
        r"mit einer lichten Breite und einer lichten Höhe von je mindestens " + NUMBER_WITH_METER: {
            GROUP: 1
        },
    },

    AttributesNames.EinfriedungAusgestaltung: {
        r"((ab einer Höhe von " + NUMBER_WITH_METER + r" )?(den freien Durchblick|die freie Durchsicht) nicht hindern)": {
            GROUP: 1,
        },
        r"(transparent|vollflächig|fassadenmäßig)": {
            GROUP: 1,
        },
    },

    AttributesNames.EinfriedungHoeheGesamt: {
        r"dürfen " + NUMBER_WITH_METER + r"( Höhe)? nicht überragen": {
            GROUP: 1,
        },
        r"(bis zu einer Höhe von|höchstens) " + NUMBER_WITH_METER: {
            GROUP: 2,
        },
        r"maximal(en Höhe von)? " + NUMBER_WITH_METER: {
            GROUP: 2,
        },
        r"Höhe von (bis zu )?" + NUMBER_WITH_METER: {
            GROUP: 1,
        },
        r"darf nicht höher als " + NUMBER_WITH_METER + r" über Wiener Null liegen": {
            GROUP: 1,
        },
        NUMBER_WITH_METER + r"( nicht)? überragen": {
            GROUP: 1,
        },
    },

    AttributesNames.EinfriedungLage: {
        r"((an|zu) (den )?(seitlichen und hinteren )?(zu Verkehrsflächen gewandten )?(Grund|Bauplatz)(stück)?grenzen)": {
            GROUP: 1,
        },
        r"(gegen die öffentlichen Verkehrsflächen)": {
            GROUP: 1,
        },
    },

    AttributesNames.EinfriedungZulaessig: {
        r"(die Errichtung .* Einfriedungen zulässig|ist zulässig)": {
            VALUE: TRUE,
        },
        r"(nicht zulässig|untersagt)": {
            VALUE: FALSE,
        },
    },

    AttributesNames.EinleitungNiederschlagswaesser: {
        r"Einleitung von Niederschlagswässern in den Kanal ist (.*), zulässig.": {
            GROUP: 1,
        },
        r"(im Neubaufall .* nicht überschreiten)": {
            GROUP: 1,
        },
        r"(in den Kanal).* nicht zulässig": {
            GROUP: 1,
        },
    },

    AttributesNames.ErrichtungGebaeude: {
        r"((darf|dürfen) unmittelbar bebaut werden|sind unmittelbar bebaubar|Errichtung ((?!nicht).)* zulässig)": {
            VALUE: TRUE,
        },
        r"sind Gebäude und bauliche Anlagen ((?!nicht).)* zulässig": {
            VALUE: TRUE,
        },
        r"(Errichtung .* (untersagt|unzulässig)|keine .* errichtet werden)": {
            VALUE: FALSE,
        },
        r"nicht zulässig": {
            VALUE: FALSE,
        },
    },

    AttributesNames.FBOKMinimumWohnungen: {
        r"Fußboden.* mindestens " + NUMBER_WITH_METER: {
            GROUP: 1,
        },
    },

    AttributesNames.GebaeudeBautyp: {
        r"(Hauptgebäude)": {
            GROUP: 1,
        },
        r"(Nebengebäude)": {
            GROUP: 1,
        },
        r"(Glashaus|Glashäuser)": {
            GROUP: 1,
        },
        r"(Kleingartenhäuser)": {
            GROUP: 1,
        },
        r"(Kleingartenwohnhäuser)": {
            GROUP: 1,
        },
    },

    AttributesNames.GebaeudeHoeheArt: {
        r"(tatsächlich(en)? errichtet)": {
            GROUP: 1,
        },
        r"(tatsächlich(en)? erreichte)": {
            GROUP: 1,
        },
        r"((tatsächlich )?ausgeführt)": {
            GROUP: 1,
        },
        r"(festgesetzt)": {
            GROUP: 1,
        },
        r"(zulässig)": {
            GROUP: 1,
        },
    },

    AttributesNames.GebaeudeHoeheMax: {
        r"(Gebäudehöhe|Höhe) (wird mit|von maximal|von|von bis zu|darf|beträgt|darf nicht mehr als|darf höchstens) " + NUMBER_WITH_METER: {
            GROUP: 3,
        },
        NUMBER_WITH_METER + r" über Wr. Null": {
            GROUP: 1,
        },
    },

    AttributesNames.GehsteigbreiteMin: {
        r"Gehsteige? mit mindestens " + NUMBER_WITH_METER: {
            GROUP: 1,
        },
        r"Gehsteige? mit (jeweils|einer Breite von|je) mindestens " + NUMBER_WITH_METER: {
            GROUP: 2,
        },
        r"mindestens " + NUMBER_WITH_METER + r" Breite als Gehsteig": {
            GROUP: 1,
        },
        r"Gehsteige mit (insgesamt )?mindestens " + NUMBER_WITH_METER + r" Breite": {
            GROUP: 2,
        },
    },

    AttributesNames.GaragengebaeudeAusfuehrung: {
        r"mit einer maximalen Gebäudehöhe von " + NUMBER_WITH_METER: {
            GROUP: 1,
        },
    },

    AttributesNames.GesamtePlangebiet: {
        ALL: {
            VALUE: TRUE,
        },
    },

    AttributesNames.HoehenlageGrundflaeche: {
        r"Höhenlage von (" + NUMBER_WITH_METER + r" über Wr. Null) herzustellen": {
            GROUP: 1,
        },
        r"Höhenlage mit " + NUMBER_WITH_METER: {
            GROUP: 1,
        },
    },

    AttributesNames.InSchutzzone: {
        ALL: {
            VALUE: TRUE,
        },
    },

    AttributesNames.Kleinhaeuser: {
        ALL: {
            VALUE: TRUE,
        },
    },

    AttributesNames.MaxAnzahlGeschosseOberirdisch: {
        r"mit höchstens (zwei|drei|vier|fünf) Hauptgeschossen zulässig": {
            GROUP: 1,
        },
    },

    AttributesNames.MindestraumhoeheEG: {
        r"Mindestraumhöhe im Erdgeschoß hat " + NUMBER_WITH_METER: {
            GROUP: 1,
        },
        r"[Hh]öhe im Erdgeschoß hat mindestens" + NUMBER_WITH_METER: {
            GROUP: 1,
        },
    },

    AttributesNames.OeffentlicheVerkehrsflaecheBreiteMin: {
        r"(von (mehr als |über )?|ab )" + NUMBER_WITH_METER + r"( (und|oder) mehr)?": {
            GROUP: 3,
        },
    },

    AttributesNames.Planzeichen: {
        r"(BB(S| ?\d?\d?))": {
            GROUP: 1,
        },
        r" ([A-Z](-[A-Z])+),? ": {
            GROUP: 1,
        },
        r" ([A-Z][A-Z] und [A-Z][A-Z]) ": {
            GROUP: 1,
        },
        r" ([a-z](-[a-z])+),? ": {
            GROUP: 1,
        },
        r"\s((Ak )?(öD[gf]))\s": {
            GROUP: 1,
        },
        r"\s(Ak)\s": {
            GROUP: 1,
        },
        r"\s(D[fg])\s": {
            GROUP: 1,
        },
        r"(Punkten?|Buchstaben?) ([a-zA-Z] und [a-zA-Z])": {
            GROUP: 2,
        },
    },

    AttributesNames.StellplatzImNiveauZulaessig: {
        ALL: {
            VALUE: TRUE,
        },
    },

    AttributesNames.StellplatzregulativUmfangMaximumRelativ: {
        r"(insgesamt|höchstens|insgesamt höchstens) " + NUMBER_WITH_PERCENT: {
            GROUP: 2,
        },
        r"maximale Stellplatzzahl mit " + NUMBER_WITH_PERCENT: {
            GROUP: 1,
        },
    },

    AttributesNames.StellplatzregulativUmfangMinimumRelativ: {
        r"Stellplatzverpflichtung .*" + NUMBER_WITH_PERCENT: {
            GROUP: 1,
        },
        r"mit " + NUMBER_WITH_PERCENT + " und die maximale": {
            GROUP: 1,
        },
    },

    AttributesNames.Stockwerk: {
        r"((Erd|Dach|Haupt)(geschoss|geschoß))": {
            GROUP: 1,
        },
    },

    AttributesNames.StrassenbreiteMax: {
        r"Straßen(breiten?|querschnitte)?( bis| von)? unter " + NUMBER_WITH_METER: {
            GROUP: 3,
        },
        r"Straßen mit weniger als " + NUMBER_WITH_METER: {
            GROUP: 1,
        },
        r"Straßen(breiten?|querschnitte)? bis (zu |zu einer Breite von )?" + NUMBER_WITH_METER + r"( Breite)?": {
            GROUP: 3,
        },
    },

    AttributesNames.StrassenbreiteMin: {
        r"[Ss]traßen(breiten?|querschnitte)? (ab|von mehr als|von über|über|mit mehr als) " + NUMBER_WITH_METER: {
            GROUP: 3,
        },
        r"Straßen mit einer Breite von " + NUMBER_WITH_METER + r" oder mehr": {
            GROUP: 1,
        },
    },

    AttributesNames.StrassenbreiteVonBis: {
        r"Straßenbreite (von " + NUMBER_WITH_METER + r" bis (unter )?" + NUMBER_WITH_METER + r")": {
            GROUP: 1,
        },
    },

    AttributesNames.Struktureinheit: {
        ALL: {
            VALUE: TRUE,
        },
    },

    AttributesNames.TechnischeAufbautenHoeheMax: {
        r"bis zu einer Gesamthöhe von " + NUMBER_WITH_METER: {
            GROUP: 1,
        },
    },

    AttributesNames.UnterbrechungGeschlosseneBauweise: {
        ALL: {
            VALUE: TRUE,
        },
    },

    AttributesNames.UnterirdischeBaulichkeiten: {
        ALL: {
            VALUE: TRUE,
        },
    },

    AttributesNames.VerbotBueroGeschaeftsgebaeude: {
        ALL: {
            VALUE: TRUE,
        },
    },

    AttributesNames.VerbotFensterZuOeffentlichenVerkehrsflaechen: {
        ALL: {
            VALUE: TRUE,
        },
    },

    AttributesNames.VerbotStaffelung: {
        ALL: {
            VALUE: TRUE,
        },
    },

    AttributesNames.VerbotWohnung: {
        ALL: {
            VALUE: TRUE,
        },
    },

    AttributesNames.VerkehrsflaecheID: {
        r"(" + STRASSE + r"( und " + STRASSE + r")?)": {
            GROUP: 1,
        },
    },

    AttributesNames.VolumenUndUmbaubarerRaum: {
        NUMBER_WITH_PERCENT: {
            GROUP: 1,
        },
        NUMBER_WITH_CUBIC_METER: {
            GROUP: 1,
        },
    },

    AttributesNames.VorbautenVerbot: {
        r" Errichtung von (((?!Baulinien).)*) (an den Baulinien|untersagt|nicht zulässig)": {
            GROUP: 1,
        },
        r" dürfen keine (.*) vorragen": {
            GROUP: 1,
        },
    },

    AttributesNames.VonBebauungFreizuhalten: {
        r"ist (von.* Bebauung) freizuhalten": {
            GROUP: 1,
        },
        r"((ober|unter)irdische(n|r)? (Bauten?|Bebauung|Bauwerk(en)?))": {
            GROUP: 1,
        },
        r"((ober- und unterirdischen|oberund unterirdischen|oberirdische[rn]|unterirdische[rn]|oberirdischen und unterirdischen) (Gebäude|Baulichkeit|Bauten?))": {
            GROUP: 1,
        },
        r"(keine Bauwerke)": {
            GROUP: 1,
        },
    },

    AttributesNames.VorkehrungBepflanzung: {
        r"(((Erhaltung|Pflanzung|(für )?das Pflanzen|Herstellung|Erreichung) .*) (zu ermöglichen|ermöglicht|zu treffen|vorhanden bleiben|möglich|geschaffen werden können|zu sichern))": {
            GROUP: 2,
        },
        r"(der Bestand der Baumreihen sicher zu stellen)": {
            GROUP: 1,
        },
        r"(Aufbringung eines Erdkörpers mit der Mächtigkeit von " + NUMBER_WITH_METER + r")": {
            GROUP: 1,
        },
    },

    AttributesNames.VorstehendeBauelementeAusladungMax: {
        r"Ausladung von (höchstens )?" + NUMBER_WITH_METER: {
            GROUP: 2,
        },
        r"höchstens " + NUMBER_WITH_METER + r" (zulässig|über die Baulinien? (vor)?ragen|und|,)": {
            GROUP: 1,
        },
    },

    AttributesNames.WidmungInMehrerenEbenen: WIDMUNG,

    AttributesNames.WidmungUndZweckbestimmung: WIDMUNG,

}
