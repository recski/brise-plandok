from brise_plandok.constants import AttributesNames
from brise_plandok.full_attribute_extraction.utils.constants import ALL, AREA_SIZE, DACH, FALSE, NUMBER_WITH_METER, GROUP, PERCENT, STRASSE, TRUE, VALUE
from brise_plandok.full_attribute_extraction.value.widmung import WIDMUNG


VALUE_PATTERNS = {

    AttributesNames.AbschlussDachMaxBezugGebaeude: {
        r"(nicht höher als|nicht mehr als|höchstens|maximal) " + NUMBER_WITH_METER + r" über": {
            GROUP: 2,
        },
    },

    AttributesNames.AnFluchtlinie: {
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
        PERCENT: {
            GROUP: 1,
        },
    },

    AttributesNames.AnteilDachbegruenung: {
     PERCENT: {
            GROUP: 1,
        },
    },

    AttributesNames.AnzahlGebaeudeMax: {
     r"[Pp]ro Bauplatz( darf)?( nur)? (ein)( Nebengebäude)": {
            GROUP: 3,
        },
    },

    AttributesNames.AufbautenZulaessig: {
        ALL: {
            VALUE: TRUE,
        },
    },

    AttributesNames.AusnahmeVonWohnungenUnzulaessig: {
        r"mit Ausnahme( der| von)? (.*) untersagt": {
            GROUP: 2,
        },
    },

    AttributesNames.AusnahmeGaertnerischAuszugestaltende: {
        r"mit Ausnahme( der| von)? ([^:]*),? gärtnerisch auszugestalten": {
            GROUP: 2,
        },
        r"mit Ausnahme( der| von)? (.*), wird bestimmt*": {
            GROUP: 2,
        },
        r"soweit sie nicht (für|als) (.*) benötigt werden, .*gärtnerisch": {
            GROUP: 2,
        },
        r"soweit nicht (.*) erforderlich ist, gärtnerisch auszugestalten": {
            GROUP: 1,
        },
        r"nicht von (.*) in Anspruch genommenen Bereiche,? sind gärtnerisch auszugestalten": {
            GROUP: 1,
        },
        r"(A|a)usgenommen davon sind (.*).": {
            GROUP: 2,
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
        r"(bis zu einer Dachneigung von|maximal|bis) ((\d\d*( ?, ?\d\d*)?|.*)(°| Grad))": {
            GROUP: 2
        },
        r"zwischen ((\d\d*( ?, ?\d\d*)?|.*)(°| Grad)) und ((\d\d*( ?, ?\d\d*)?|.*)(°| Grad))": {
            GROUP: 5
        },
    },

    AttributesNames.DachflaecheMin: {
        AREA_SIZE: {
            GROUP: 1
        },
    },

    AttributesNames.DurchgangBreite: {
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

    AttributesNames.DurchgangHoehe: {
        r"(H|h)öhe von( mindestens)? (\d\d*( ?, ?\d\d*)? ?m)": {
            GROUP: 3,
        },
        r" (\d\d*( ?, ?\d\d*)? ?m)( lichter)? (H|h)öhe": {
            GROUP: 1,
        },
    },

    AttributesNames.EinfriedungAusgestaltung: {
        r"((ab einer Höhe von " + NUMBER_WITH_METER + r" )?(den freien Durchblick|die freie Durchsicht) nicht hindern)": {
            GROUP: 1,
        },
        r"(transparent)": {
            GROUP: 1,
        },
    },

    AttributesNames.EinfriedungHoeheGesamt: {
        r"dürfen " + NUMBER_WITH_METER + r" nicht überragen": {
            GROUP: 1,
        },
        r"bis zu einer Höhe von " + NUMBER_WITH_METER + r" zulässig": {
            GROUP: 1,
        },
        r"maximal " + NUMBER_WITH_METER + r" (.*)zulässig": {
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
        r"(an (den )?(seitlichen und hinteren )?(zu Verkehrsflächen gewandten )?(Grund|Bauplatz)grenzen)": {
            GROUP: 1,
        },
        r"(gegen die öffentlichen Verkehrsflächen)": {
            GROUP: 1,
        },
    },

    AttributesNames.ErrichtungGebaeude: {
        r"(darf unmittelbar bebaut werden|sind unmittelbar bebaubar|Errichtung .* zulässig)": {
            VALUE: TRUE,
        },
        r"(Errichtung .* (untersagt|unzulässig)|keine .* errichtet werden)": {
            VALUE: FALSE,
        },
    },

    AttributesNames.Flaechen: {
        # Bebaubarkeit
        r"(((b|B)ebaubare,? jedoch)? unbebaut bleibenden? (Grund|Bauland)?(F|f)lächen?)": {
            GROUP: 1,
        },
        r"((N|n)icht bebaute,? jedoch bebaubare (Grund|Bauland)flächen?)": {
            GROUP: 1,
        },
        r"((B|b)ebaubaren?,? (aber )?von Bebauung freibleibenden? (Grund|Bauland)flächen?)": {
            GROUP: 1,
        },
        r"(bebauten? Fläche)": {
            GROUP: 1,
        },
        # Maximum
        r"((in Summe|in Anspruch genommene Gesamtnutzfläche) " + AREA_SIZE + r" nicht überschreiten)": {
            GROUP: 1,
        },
        r"(höchstens " + AREA_SIZE + r")": {
            GROUP: 1,
        },
        r"(maximal(en Grundfläche von( insgesamt)?)? " + AREA_SIZE + r")": {
            GROUP: 1,
        },
        r"(bis zu einem (Flächen)?(A|a)usmaß von " + AREA_SIZE + r")": {
            GROUP: 1,
        },
        r"(die bebaute Fläche nicht mehr als " + AREA_SIZE + r")": {
            GROUP: 1,
        },
        # Minimum
        r"(f|F)lächen? (von mehr als " + AREA_SIZE + r")": {
            GROUP: 2,
        },
        r"((m|M)indestens " + AREA_SIZE + r")": {
            GROUP: 1,
        },
        r"(nicht weniger als " + AREA_SIZE + r")": {
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
        r"(tatsächlich errichtet)": {
            GROUP: 1,
        },
        r"(tatsächlich ausgeführt)": {
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
        r"(Gebäudehöhe|Höhe) \D*" + NUMBER_WITH_METER: {
            GROUP: 2,
        },
    },

    AttributesNames.GehsteigbreiteMin: {
        r"Gehsteige? mit mindestens " + NUMBER_WITH_METER: {
            GROUP: 1
        },
        r"Gehsteige? mit (jeweils|einer Breite von) mindestens " + NUMBER_WITH_METER: {
            GROUP: 2
        },
        r"mindestens " + NUMBER_WITH_METER + r" Breite als Gehsteig": {
            GROUP: 1
        },
    },

    AttributesNames.PlangebietAllgemein: {
        ALL: {
            VALUE: TRUE,
        },
    },

    AttributesNames.Planzeichen: {
        r"(BB ?\d?)": {
            GROUP: 1,
        },
        r"(A(-[A-Z])+)": {
            GROUP: 1,
        },
        r"\s((Ak )?(öD[gf]))\s": {
            GROUP: 1,
        },
    },

    AttributesNames.Stockwerk: {
        r"((Erd|Dach|Haupt)(geschoss|geschoß))": {
            GROUP: 1,
        },
    },

    AttributesNames.StrassenbreiteMax: {
        r"Straßen(breiten?)?( bis)? unter " + NUMBER_WITH_METER: {
            GROUP: 3,
        },
        r"Straßen(breiten?)? bis (zu |zu einer Breite von )?" + NUMBER_WITH_METER + r"( Breite)?": {
            GROUP: 3,
        },
    },

    AttributesNames.StrassenbreiteMin: {
        r"Straßen(breiten?)? (ab|von mehr als|von über) " + NUMBER_WITH_METER: {
            GROUP: 3,
        },
    },

    AttributesNames.StrassenbreiteVonBis: {
        r"Straßenbreite (von " + NUMBER_WITH_METER + r" bis (unter )?" + NUMBER_WITH_METER + r")": {
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

    AttributesNames.VorbautenVerbot: {
        r" Errichtung von (((?!Baulinien).)*) (an den Baulinien|untersagt|nicht zulässig)": {
            GROUP: 1,
        },
        r" dürfen keine (.*) vorragen": {
            GROUP: 1,
        },
    },

    AttributesNames.VonBebauungFreizuhalten: {
        r"(von( jeder)? Bebauung)": {
            GROUP: 1,
        },
        r"((ober|unter)irdische(n|r)? (Bauten?|Bebauung|Bauwerk(en)?))": {
            GROUP: 1,
        },
        r"((ober- und unterirdischen|oberirdischer) Gebäude)": {
            GROUP: 1,
        },
        r"(keine Bauwerke)": {
            GROUP: 1,
        },
    },

    AttributesNames.VorkehrungBepflanzung: {
        r"(((Erhaltung|Pflanzung|(für )?das Pflanzen|Herstellung) .*) (zu ermöglichen|ermöglicht|zu treffen|vorhanden bleiben|möglich|geschaffen werden können))": {
            GROUP: 2,
        },
        r"(der Bestand der Baumreihen sicher zu stellen)": {
            GROUP: 1,
        },
    },

    AttributesNames.VorstehendeBauelementeAusladungMax: {
        r"Ausladung von (höchstens )?" + NUMBER_WITH_METER: {
            GROUP: 2,
        },
        r"höchstens " + NUMBER_WITH_METER + r" (zulässig|über die Baulinie (vor)?ragen|und|,)": {
            GROUP: 1,
        },
    },

    AttributesNames.WidmungInMehrerenEbenen: WIDMUNG,

    AttributesNames.WidmungUndZweckbestimmung: WIDMUNG,

}
