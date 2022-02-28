from brise_plandok.constants import AttributesNames


class PSETJson:
    SECTION_ID = "section_id"
    SECTION_TEXT = "section_text"
    GOLD_ATTRIBUTES = "gold_attributes"
    PRED_ATTRIBUTES = "predicted_attributes"
    GOLD_PSETS = "gold_psets"
    PRED_PSETS = "predicted_psets"
    PROPERTIES = "properties"
    PROPERTY_NAME = "property_name"
    PROPERTY_VALUE = "property_value"


class PSETNames:
    Dachneigung = "WienBV_TBDachneigung"
    Dachbegruenung = "WienBV_TBDachbegruenung"
    VerbotWohnung = "WienBV_TBVerbotWohnung"
    Stellplaetze = "WienBV_TBStellplaetze"
    Gebaeudehoehe = "WienBV_TBGebaeudehoehe"
    Dachabschluss = "WienBV_TBDachabschluss"
    Vorbauten = "WienBV_TBVorbauten"
    VerbotFenster = "WIenBV_TBVerbotFenster"


PSETS = {
    PSETNames.Dachneigung: [
        AttributesNames.Planzeichen,
        AttributesNames.WidmungUndZweckbestimmung,
        AttributesNames.AnFluchtlinie,
        AttributesNames.Dachart,
        AttributesNames.GebaeudeHoeheArt,
        AttributesNames.DachneigungMax,
        AttributesNames.Bauklasse,
        AttributesNames.InSchutzzone,
        AttributesNames.DachneigungMin,
    ],
    PSETNames.Dachbegruenung: [
        AttributesNames.Planzeichen,
        AttributesNames.WidmungUndZweckbestimmung,
        AttributesNames.Dachart,
        AttributesNames.BegruenungDach,
        AttributesNames.GebaeudeHoeheMax,
        AttributesNames.GebaeudeBautyp,
        AttributesNames.GebaeudeHoeheArt,
        AttributesNames.DachneigungMax,
        AttributesNames.DachflaecheMin,
        AttributesNames.Bauklasse,
        AttributesNames.AnteilDachbegruenung,
    ],
    PSETNames.VerbotWohnung: [
        AttributesNames.Planzeichen,
        AttributesNames.WidmungUndZweckbestimmung,
        AttributesNames.GesamtePlangebiet,
        AttributesNames.VerbotWohnung,
        AttributesNames.Stockwerk,
    ],
    PSETNames.Stellplaetze: [
        AttributesNames.Planzeichen,
        AttributesNames.WidmungUndZweckbestimmung,
        AttributesNames.StellplatzregulativUmfangMaximumRelativ,
        AttributesNames.StellplatzregulativUmfangMinimumRelativ,
    ],
    PSETNames.Gebaeudehoehe: [
        AttributesNames.Planzeichen,
        AttributesNames.BebauteFlaecheMin,
        AttributesNames.BebauteFlaecheMax,
        AttributesNames.BebauteFlaecheMaxProzentual,
        AttributesNames.BebauteFlaecheMaxNebengebaeude,
        AttributesNames.WidmungUndZweckbestimmung,
        AttributesNames.GesamtePlangebiet,
        AttributesNames.GebaeudeHoeheMax,
        AttributesNames.Bauklasse,
    ],
    PSETNames.Dachabschluss: [
        AttributesNames.Planzeichen,
        AttributesNames.BebauteFlaecheMin,
        AttributesNames.BebauteFlaecheMax,
        AttributesNames.BebauteFlaecheMaxProzentual,
        AttributesNames.BebauteFlaecheMaxNebengebaeude,
        AttributesNames.WidmungUndZweckbestimmung,
        AttributesNames.AnFluchtlinie,
        AttributesNames.VerkehrsflaecheID,
        AttributesNames.GesamtePlangebiet,
        AttributesNames.VorbautenVerbot,
        AttributesNames.AnOeffentlichenVerkehrsflaechen,
    ],
    PSETNames.VerbotFenster: [
        AttributesNames.Planzeichen,
        AttributesNames.AnFluchtlinie,
        AttributesNames.VerkehrsflaecheID,
        AttributesNames.VerbotFensterZuOeffentlichenVerkehrsflaechen,
        AttributesNames.Stockwerk,
    ],
}
