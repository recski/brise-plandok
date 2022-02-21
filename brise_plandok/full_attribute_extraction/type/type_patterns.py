from brise_plandok.constants import AttributeTypes, AttributesNames
from brise_plandok.full_attribute_extraction.constants import ALL, TYPE, NUMBER_WITH_SQUARE_METER, NUMBER_WITH_METER

TYPE_PATTERNS = {

    AttributesNames.AbschlussDachMaxBezugGebaeude: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.AbschlussDachMaxBezugGelaende: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.AnFluchtlinie: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.AnOeffentlichenVerkehrsflaechen: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.AnordnungGaertnerischeAusgestaltung: {
        r"für die die gärtnerische Ausgestaltung (vorgeschrieben|angeordnet) ist": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"auf gärtnerisch auszugestaltenden (Grundf|F)lächen": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"die angrenzende gärtnerisch auszugestaltenden": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"gärtnerisch auszugestalten": {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.AnordnungGaertnerischeAusgestaltungProzentual: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.ArkadeHoehe: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.AufbautenZulaessig: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.AusnahmeGaertnerischAuszugestaltende: {
        ALL: {
            TYPE: AttributeTypes.CONDITION_EXCEPTION,
        },
    },

    AttributesNames.Bauklasse: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.BauweiseID: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.BegruenungDach: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.Dachart: {
        r"sind [^ ]*(dach|dächer)": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"(dach|dächer) dürfen": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"(dach|dächer) bis zu": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"(dach|dächer), die": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"(dach|dächer)(flächen)? sin*": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"Errichtung gelangende .*(da|dächer)": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"als( begrünte)? .*(dach|dher)": {
            TYPE: AttributeTypes.CONTENT,
        },
        r"mit .*(dach|dächern) ausz*": {
            TYPE: AttributeTypes.CONTENT,
        },
        r"(dach|dächern) zulässig": {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.DachneigungMax: {
        r"bis zu einer (Dachn|N)eigung von": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"mit einer (Dachn|N)eigung bis": {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.DurchfahrtBreite: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.DurchfahrtHoehe: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },


    AttributesNames.DurchgangBreite: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.DurchgangHoehe: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.EinleitungNiederschlagswaesser: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.ErrichtungGebaeude: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.Flaechen: {
        # Bebaubarkeit
        r"(((b|B)ebaubare,? jedoch)? unbebaut bleibenden? (Grund|Bauland)?(F|f)lächen?)": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"((N|n)icht bebaute,? jedoch bebaubare (Grund|Bauland)flächen?)": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"((B|b)ebaubaren?,? (aber )?von Bebauung freibleibenden? (Grund|Bauland)flächen?)": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"unbebauten? Fläche": {
            TYPE: AttributeTypes.CONDITION,
        },
        # Maximum
        r"((in Summe|in Anspruch genommene Gesamtnutzfläche) " + NUMBER_WITH_SQUARE_METER + r" nicht überschreiten)": {
            TYPE: AttributeTypes.CONTENT,
        },
        r"(höchstens " + NUMBER_WITH_SQUARE_METER + r")": {
            TYPE: AttributeTypes.CONTENT,
        },
        r"(maximal(en Grundfläche von( insgesamt)?)? " + NUMBER_WITH_SQUARE_METER + r")": {
            TYPE: AttributeTypes.CONTENT,
        },
        r"(bis zu einem (Flächen)?(A|a)usmaß von " + NUMBER_WITH_SQUARE_METER + r")": {
            TYPE: AttributeTypes.CONTENT,
        },
        r"(die bebaute Fläche nicht mehr als " + NUMBER_WITH_SQUARE_METER + r")": {
            TYPE: AttributeTypes.CONTENT,
        },
        # Minimum
        r"(f|F)lächen? (von mehr als " + NUMBER_WITH_SQUARE_METER + r")": {
            TYPE: AttributeTypes.CONTENT,
        },
        r"((m|M)indestens " + NUMBER_WITH_SQUARE_METER + r")": {
            TYPE: AttributeTypes.CONTENT,
        },
        r"(nicht weniger als " + NUMBER_WITH_SQUARE_METER + r")": {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.GebaeudeHoeheMax: {
        r" (mit|bis zu) einer Gebäudehöhe von( bis zu)? \d\d m": {
            TYPE: AttributeTypes.CONDITION,
        },
        NUMBER_WITH_METER + r" zulässig": {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.GebaeudeHoeheArt: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.GehsteigbreiteMin: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.Kleinhaeuser: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.OeffentlicheVerkehrsflaecheBreiteMin: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.PlangebietAllgemein: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.Planzeichen: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.StellplatzregulativUmfangMaximumAbsolut: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.StellplatzregulativUmfangMinimumRelativ: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.StrassenbreiteMin: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.StrassenbreiteVonBis: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.UnterbrechungGeschlosseneBauweise: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.UnterirdischeBaulichkeiten: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.VerbotWohnung: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.VerkehrsflaecheID: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.VonBebauungFreizuhalten: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.VorbautenVerbot: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.VerbotFensterZuOeffentlichenVerkehrsflaechen: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.VorkehrungBepflanzung: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.WidmungInMehrerenEbenen: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

}
