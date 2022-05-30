from brise_plandok.constants import AttributesNames


class PSETJson:
    SECTION_ID = "section_id"
    SECTION_TEXT = "section_text"
    GOLD_ATTRIBUTES = "gold_attributes"
    PRED_ATTRIBUTES = "predicted_attributes"
    GOLD_PSETS = "gold_psets"
    PRED_PSETS = "predicted_psets"
    PROPERTIES = "properties"
    PROPERTY_NAME = "name"
    PROPERTY_VALUE = "value"
    PROPERTY_TYPE = "datatype"
    REQUIRED = "required"
    OPTIONAL = "optional"


class PSETNames:
    Bebauungfreizuhalten = "WIenBV_TBBebauungfreizuhalten"
    Dachneigung = "WienBV_TBDachneigung"
    Dachbegruenung = "WienBV_TBDachbegruenung"
    VerbotWohnung = "WienBV_TBVerbotWohnung"
    Stellplaetze = "WienBV_TBStellplaetze"
    Gebaeudehoehe = "WienBV_TBGebaeudehoehe"
    Dachabschluss = "WienBV_TBDachabschluss"
    Vorbauten = "WienBV_TBVorbauten"
    VorbautenAusladung = "WienBV_TBVorbautenAusladung"
    VerbotFenster = "WIenBV_TBVerbotFenster"


class IFCType:
    TEXT = "Text"
    BOOL = "Wahrheitswert"
    PERCENT = "positive Zahl [%]"
    LENGTH = "positive Zahl [m]"
    SQUARE = "positive Zahl [m2]"
    DEGREE = "positive Zahl (Gradzahl)"


class PSETAttributes:
    Planzeichen = {
        PSETJson.PROPERTY_NAME: AttributesNames.Planzeichen,
        PSETJson.PROPERTY_TYPE: IFCType.TEXT,
    }
    Widmung = {
        PSETJson.PROPERTY_NAME: AttributesNames.Widmung,
        PSETJson.PROPERTY_TYPE: IFCType.TEXT,
    }
    Nutzungsart = {
        PSETJson.PROPERTY_NAME: AttributesNames.Nutzungsart,
        PSETJson.PROPERTY_TYPE: IFCType.TEXT,
    }
    BBAllgemein = {
        PSETJson.PROPERTY_NAME: AttributesNames.BBAllgemein,
        PSETJson.PROPERTY_TYPE: IFCType.TEXT,
    }
    AnFluchtlinie = {
        PSETJson.PROPERTY_NAME: AttributesNames.AnFluchtlinie,
        PSETJson.PROPERTY_TYPE: IFCType.BOOL,
    }
    Dachart = {
        PSETJson.PROPERTY_NAME: AttributesNames.Dachart,
        PSETJson.PROPERTY_TYPE: IFCType.TEXT,
    }
    GebaeudeHoeheArt = {
        PSETJson.PROPERTY_NAME: AttributesNames.GebaeudeHoeheArt,
        PSETJson.PROPERTY_TYPE: IFCType.TEXT,
    }
    DachneigungMax = {
        PSETJson.PROPERTY_NAME: AttributesNames.DachneigungMax,
        PSETJson.PROPERTY_TYPE: IFCType.DEGREE,
    }
    Bauklasse = {
        PSETJson.PROPERTY_NAME: AttributesNames.Bauklasse,
        PSETJson.PROPERTY_TYPE: IFCType.TEXT,
    }
    InSchutzzone = {
        PSETJson.PROPERTY_NAME: AttributesNames.InSchutzzone,
        PSETJson.PROPERTY_TYPE: IFCType.BOOL,
    }
    DachneigungMin = {
        PSETJson.PROPERTY_NAME: AttributesNames.DachneigungMin,
        PSETJson.PROPERTY_TYPE: IFCType.DEGREE,
    }
    BegruenungDach = {
        PSETJson.PROPERTY_NAME: AttributesNames.BegruenungDach,
        PSETJson.PROPERTY_TYPE: IFCType.BOOL,
    }
    GebaeudeHoeheMaxAbsolut = {
        PSETJson.PROPERTY_NAME: AttributesNames.GebaeudeHoeheMaxAbsolut,
        PSETJson.PROPERTY_TYPE: IFCType.LENGTH,
    }
    GebaeudeHoeheMaxWN = {
        PSETJson.PROPERTY_NAME: AttributesNames.GebaeudeHoeheMaxWN,
        PSETJson.PROPERTY_TYPE: IFCType.LENGTH,
    }
    GebaeudeBautyp = {
        PSETJson.PROPERTY_NAME: AttributesNames.GebaeudeBautyp,
        PSETJson.PROPERTY_TYPE: IFCType.TEXT,
    }
    DachflaecheMin = {
        PSETJson.PROPERTY_NAME: AttributesNames.DachflaecheMin,
        PSETJson.PROPERTY_TYPE: IFCType.SQUARE,
    }
    AnteilDachbegruenung = {
        PSETJson.PROPERTY_NAME: AttributesNames.AnteilDachbegruenung,
        PSETJson.PROPERTY_TYPE: IFCType.PERCENT,
    }
    GesamtePlangebiet = {
        PSETJson.PROPERTY_NAME: AttributesNames.GesamtePlangebiet,
        PSETJson.PROPERTY_TYPE: IFCType.BOOL,
    }
    VerbotWohnung = {
        PSETJson.PROPERTY_NAME: AttributesNames.VerbotWohnung,
        PSETJson.PROPERTY_TYPE: IFCType.BOOL,
    }
    Stockwerk = {
        PSETJson.PROPERTY_NAME: AttributesNames.Stockwerk,
        PSETJson.PROPERTY_TYPE: IFCType.TEXT,
    }
    StellplatzregulativUmfangMaximumRelativ = {
        PSETJson.PROPERTY_NAME: AttributesNames.StellplatzregulativUmfangMaximumRelativ,
        PSETJson.PROPERTY_TYPE: IFCType.PERCENT,
    }
    StellplatzregulativUmfangMinimumRelativ = {
        PSETJson.PROPERTY_NAME: AttributesNames.StellplatzregulativUmfangMinimumRelativ,
        PSETJson.PROPERTY_TYPE: IFCType.PERCENT,
    }
    BebauteFlaecheMin = {
        PSETJson.PROPERTY_NAME: AttributesNames.BebauteFlaecheMin,
        PSETJson.PROPERTY_TYPE: IFCType.SQUARE,
    }
    BebauteFlaecheMax = {
        PSETJson.PROPERTY_NAME: AttributesNames.BebauteFlaecheMax,
        PSETJson.PROPERTY_TYPE: IFCType.SQUARE,
    }
    BebauteFlaecheMaxProzentual = {
        PSETJson.PROPERTY_NAME: AttributesNames.BebauteFlaecheMaxProzentual,
        PSETJson.PROPERTY_TYPE: IFCType.PERCENT,
    }
    BebauteFlaecheMaxNebengebaeude = {
        PSETJson.PROPERTY_NAME: AttributesNames.BebauteFlaecheMaxNebengebaeude,
        PSETJson.PROPERTY_TYPE: IFCType.SQUARE,
    }
    VerkehrsflaecheID = {
        PSETJson.PROPERTY_NAME: AttributesNames.VerkehrsflaecheID,
        PSETJson.PROPERTY_TYPE: IFCType.TEXT,
    }
    VorbautenVerbot = {
        PSETJson.PROPERTY_NAME: AttributesNames.VorbautenVerbot,
        PSETJson.PROPERTY_TYPE: IFCType.TEXT,
    }
    AnOeffentlichenVerkehrsflaechen = {
        PSETJson.PROPERTY_NAME: AttributesNames.AnOeffentlichenVerkehrsflaechen,
        PSETJson.PROPERTY_TYPE: IFCType.BOOL,
    }
    VerbotFensterZuOeffentlichenVerkehrsflaechen = {
        PSETJson.PROPERTY_NAME: AttributesNames.VerbotFensterZuOeffentlichenVerkehrsflaechen,
        PSETJson.PROPERTY_TYPE: IFCType.BOOL,
    }
    AbschlussDachMaxBezugGebaeude = {
        PSETJson.PROPERTY_NAME: AttributesNames.AbschlussDachMaxBezugGebaeude,
        PSETJson.PROPERTY_TYPE: IFCType.LENGTH,
    }
    VorstehendeBauelementeAusladungMax = {
        PSETJson.PROPERTY_NAME: AttributesNames.VorstehendeBauelementeAusladungMax,
        PSETJson.PROPERTY_TYPE: IFCType.LENGTH,
    }
    VonBebauungFreizuhalten = {
        PSETJson.PROPERTY_NAME: AttributesNames.VonBebauungFreizuhalten,
        PSETJson.PROPERTY_TYPE: IFCType.TEXT,
    }


PSETS = {
    PSETNames.Dachneigung: {
        PSETJson.REQUIRED: [
            PSETAttributes.DachneigungMax,
            PSETAttributes.DachneigungMin,
        ],
        PSETJson.OPTIONAL: [
            PSETAttributes.Planzeichen,
            PSETAttributes.Widmung,
            PSETAttributes.Nutzungsart,
            PSETAttributes.BBAllgemein,
            PSETAttributes.AnFluchtlinie,
            PSETAttributes.Dachart,
            PSETAttributes.GebaeudeHoeheArt,
            PSETAttributes.Bauklasse,
            PSETAttributes.InSchutzzone,
        ],
    },
    PSETNames.Dachbegruenung: {
        PSETJson.REQUIRED: [
            PSETAttributes.BegruenungDach,
            PSETAttributes.AnteilDachbegruenung,
        ],
        PSETJson.OPTIONAL: [
            PSETAttributes.Planzeichen,
            PSETAttributes.Widmung,
            PSETAttributes.Nutzungsart,
            PSETAttributes.BBAllgemein,
            PSETAttributes.Dachart,
            PSETAttributes.GebaeudeHoeheMaxAbsolut,
            PSETAttributes.GebaeudeHoeheMaxWN,
            PSETAttributes.GebaeudeBautyp,
            PSETAttributes.GebaeudeHoeheArt,
            PSETAttributes.DachneigungMax,
            PSETAttributes.DachflaecheMin,
            PSETAttributes.Bauklasse,
        ],
    },
    PSETNames.VerbotWohnung: {
        PSETJson.REQUIRED: [
            PSETAttributes.VerbotWohnung,
        ],
        PSETJson.OPTIONAL: [
            PSETAttributes.Planzeichen,
            PSETAttributes.Widmung,
            PSETAttributes.Nutzungsart,
            PSETAttributes.BBAllgemein,
            PSETAttributes.GesamtePlangebiet,
            PSETAttributes.Stockwerk,
        ],
    },
    PSETNames.Stellplaetze: {
        PSETJson.REQUIRED: [
            PSETAttributes.StellplatzregulativUmfangMaximumRelativ,
            PSETAttributes.StellplatzregulativUmfangMinimumRelativ,
        ],
        PSETJson.OPTIONAL: [
            PSETAttributes.Planzeichen,
            PSETAttributes.Widmung,
            PSETAttributes.Nutzungsart,
            PSETAttributes.BBAllgemein,
        ],
    },
    PSETNames.Gebaeudehoehe: {
        PSETJson.REQUIRED: [
            PSETAttributes.GebaeudeHoeheMaxAbsolut,
            PSETAttributes.GebaeudeHoeheMaxWN,
            PSETAttributes.Bauklasse,
        ],
        PSETJson.OPTIONAL: [
            PSETAttributes.Planzeichen,
            PSETAttributes.BebauteFlaecheMax,
            PSETAttributes.BebauteFlaecheMin,
            PSETAttributes.Widmung,
            PSETAttributes.Nutzungsart,
            PSETAttributes.BBAllgemein,
            PSETAttributes.GesamtePlangebiet,
        ],
    },
    PSETNames.Dachabschluss: {
        PSETJson.REQUIRED: [
            PSETAttributes.AbschlussDachMaxBezugGebaeude,
        ],
        PSETJson.OPTIONAL: [
            PSETAttributes.Planzeichen,
            PSETAttributes.BebauteFlaecheMax,
            PSETAttributes.BebauteFlaecheMin,
            PSETAttributes.Widmung,
            PSETAttributes.Nutzungsart,
            PSETAttributes.BBAllgemein,
            PSETAttributes.GesamtePlangebiet,
            PSETAttributes.GebaeudeHoeheMaxAbsolut,
            PSETAttributes.GebaeudeHoeheMaxWN,
            PSETAttributes.GebaeudeHoeheArt,
        ],
    },
    PSETNames.Vorbauten: {
        PSETJson.REQUIRED: [
            PSETAttributes.VorbautenVerbot,
        ],
        PSETJson.OPTIONAL: [
            PSETAttributes.Planzeichen,
            PSETAttributes.BebauteFlaecheMax,
            PSETAttributes.BebauteFlaecheMin,
            PSETAttributes.Widmung,
            PSETAttributes.Nutzungsart,
            PSETAttributes.BBAllgemein,
            PSETAttributes.AnFluchtlinie,
            PSETAttributes.VerkehrsflaecheID,
            PSETAttributes.GesamtePlangebiet,
            PSETAttributes.AnOeffentlichenVerkehrsflaechen,
        ],
    },
    PSETNames.VerbotFenster: {
        PSETJson.REQUIRED: [
            PSETAttributes.VerbotFensterZuOeffentlichenVerkehrsflaechen,
        ],
        PSETJson.OPTIONAL: [
            PSETAttributes.Planzeichen,
            PSETAttributes.AnFluchtlinie,
            PSETAttributes.VerkehrsflaecheID,
            PSETAttributes.Stockwerk,
        ],
    },
    PSETNames.VorbautenAusladung: {
        PSETJson.REQUIRED: [
            PSETAttributes.VorstehendeBauelementeAusladungMax,
        ],
        PSETJson.OPTIONAL: [
            PSETAttributes.Planzeichen,
            PSETAttributes.BebauteFlaecheMax,
            PSETAttributes.BebauteFlaecheMin,
            PSETAttributes.Widmung,
            PSETAttributes.Nutzungsart,
            PSETAttributes.BBAllgemein,
            PSETAttributes.AnFluchtlinie,
            PSETAttributes.VerkehrsflaecheID,
            PSETAttributes.GesamtePlangebiet,
            PSETAttributes.AnOeffentlichenVerkehrsflaechen,
        ],
    },
    PSETNames.Bebauungfreizuhalten: {
        PSETJson.REQUIRED: [
            PSETAttributes.VonBebauungFreizuhalten,
        ],
        PSETJson.OPTIONAL: [
            PSETAttributes.Planzeichen,
            PSETAttributes.Widmung,
            PSETAttributes.Nutzungsart,
            PSETAttributes.BBAllgemein,
            PSETAttributes.AnFluchtlinie,
            PSETAttributes.VerkehrsflaecheID,
            PSETAttributes.GesamtePlangebiet,
        ],
    },
}
