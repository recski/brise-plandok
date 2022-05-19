from brise_plandok.constants import AttributeTypes, AttributesNames
from brise_plandok.full_attribute_extraction.attribute.utils.constants import ALL, TYPE, NUMBER_WITH_METER, \
    SPACE_BRACKET_SLASH_DASH
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

    AttributesNames.AnlageZumEinstellenVorhanden: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.AnOeffentlichenVerkehrsflaechen: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.AnordnungGaertnerischeAusgestaltung: {
        r"gärtnerische Ausgestaltung": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"gärtnerisch auszugestaltend": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"sind gärtnerisch zu gestalten": {
            TYPE: AttributeTypes.CONTENT,
        },
        r"gärtnerisch auszugestalten[., ]": {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.AnordnungGaertnerischeAusgestaltungProzentual: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.AnteilDachbegruenung: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.AnzahlGebaeudeMax: {
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

    AttributesNames.BebauteFlaecheMax: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.BebauteFlaecheMaxNebengebaeude: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.BebauteFlaecheMaxProzentual: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.BebauteFlaecheMin: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
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
        r"als( begrünte)? .*(dach|dächer)": {
            TYPE: AttributeTypes.CONTENT,
        },
        r"mit .*(dach|dächern) ausz*": {
            TYPE: AttributeTypes.CONTENT,
        },
        r"(dach|dächern) zulässig": {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.DachflaecheMin: {
        ALL: {
            TYPE: AttributeTypes.CONDITION
        }
    },

    AttributesNames.DachneigungMax: {
        r"bis zu einer (Dachn|N)eigung von": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"mit einer (Dachn|N)eigung bis": {
            TYPE: AttributeTypes.CONDITION,
        },
        ALL: {
            TYPE: AttributeTypes.CONTENT
        }
    },

    AttributesNames.DachneigungMin: {
        ALL: {
            TYPE: AttributeTypes.CONTENT
        }
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

    AttributesNames.EinfriedungLage: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },


    AttributesNames.EinfriedungZulaessig: {
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

    AttributesNames.FBOKMinimumWohnungen: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.GebaeudeBautyp: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.GebaeudeHoeheMaxAbsolut: {
        r" (mit|bis zu) einer Gebäudehöhe von( bis zu)? " + NUMBER_WITH_METER: {
            TYPE: AttributeTypes.CONDITION,
        },
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.GebaeudeHoeheMaxWN: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.GebaeudeHoeheMin: {
        ALL: {
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

    AttributesNames.GesamtePlangebiet: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.InSchutzzone: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.Kleinhaeuser: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.MaxAnzahlGeschosseOberirdisch: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.OeffentlicheVerkehrsflaecheBreiteMin: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.Planzeichen: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.StellplatzImNiveauZulaessig: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.StellplatzregulativUmfangMaximumAbsolut: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.StellplatzregulativUmfangMaximumRelativ: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.StellplatzregulativUmfangMinimumRelativ: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.Stockwerk: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.StrassenbreiteMax: {
        ALL: {
            TYPE: AttributeTypes.CONDITION,
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

    AttributesNames.Struktureinheit: {
        r"als Strukturgebiet festgelegt": {
            TYPE: AttributeTypes.CONTENT,
        },
        r"bilden in ihrer Gesamtheit eine Struktur": {
            TYPE: AttributeTypes.CONTENT,
        },
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

    AttributesNames.VerbotBueroGeschaeftsgebaeude: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.VerbotFensterZuOeffentlichenVerkehrsflaechen: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.VerbotStaffelung: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
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

    AttributesNames.VolumenUndUmbaubarerRaum: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.VonBebauungFreizuhalten: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.VorbautenBeschraenkung: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.VorbautenVerbot: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.VorkehrungBepflanzung: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.VorstehendeBauelementeAusladungMax: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.WidmungInMehrerenEbenen: {
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

    AttributesNames.Widmung: {
        SPACE_BRACKET_SLASH_DASH + r"„?([GLWE])“?" + SPACE_BRACKET_SLASH_DASH: {
            TYPE: AttributeTypes.CONDITION,
        },
        r"(GB|GV|Spk|Esp|Eklw?|Epk|SwwL?|SO)": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"mit Ausnahme der Gartensiedlungsgebiete": {
            TYPE: AttributeTypes.CONDITION_EXCEPTION,
        },
        r"wird als .* (gewidmete|ausgewiesen)": {
            TYPE: AttributeTypes.CONTENT,
        },
        r"(als|mit) .* (gewidmete|ausgewiesen)": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"als .* bezeichnete": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"Innerhalb der (als|in|im)": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"(der Widmung|dem) (.*) zugeordnet": {
            TYPE: AttributeTypes.CONTENT,
        },
        r"[iI]m „?(\w+land|[Gg]emischte[sn] Baugebiet|Geschäftsviertel|\w+gebiet)": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"als .* festgesetzt": {
            TYPE: AttributeTypes.CONTENT,
        },
        r"[Ff]ür (das )?(Bauland|Gemischt)": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"mit der Festsetzung (Bauland|Geschäftsviertel|Wohn)": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"mit der Widmung": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"[Ii]n der Wohnzone": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"Grundflächen des Wohngebietes": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"bezeichneten Flächen des (Gemischten Baugebietes|Wohngebietes)": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"mit Grünland": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"im Bauland": {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.BBAllgemein: {
        r"Einkaufszentrum ausgewiesen": {
            TYPE: AttributeTypes.CONTENT,
        },
        ALL: {
            TYPE: AttributeTypes.CONDITION,
        },
    },

    AttributesNames.Nutzungsart: {
        r"soweit nicht eine Befestigung für die Nutzung": {
            TYPE: AttributeTypes.CONDITION_EXCEPTION,
        },
        r"Sondergebiet/": {
            TYPE: AttributeTypes.CONDITION,
        },
        r"i[nm] Zusammenhang mit [\w\s,]+[Zz]weck": {
            TYPE: AttributeTypes.CONDITION,
        },
        ALL: {
            TYPE: AttributeTypes.CONTENT,
        },
    },

}
