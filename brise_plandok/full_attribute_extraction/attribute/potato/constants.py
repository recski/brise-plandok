from brise_plandok.constants import AttributesNames

GOLD_ATTRIBUTES = "gold_attributes"
GOLD = "full_gold"
ANNOTATED_ATTRIBUTES = "annotated_attributes"
SEGMENTATION_ERROR = "segmentation_error"

NOT = "NOT"
DO_NOT_ANNOTATE = "DON'T ANNOTATE THIS SENTENCE"

TOP_14_ANNOTATED = [
    NOT,
    AttributesNames.Planzeichen,
    AttributesNames.Widmung,
    AttributesNames.VerkehrsflaecheID,
    AttributesNames.AnFluchtlinie,
    AttributesNames.AnordnungGaertnerischeAusgestaltung,
    AttributesNames.GebaeudeHoeheMaxAbsolut,
    AttributesNames.Dachart,
    AttributesNames.GebaeudeHoeheArt,
    AttributesNames.VorkehrungBepflanzung,
    AttributesNames.WidmungInMehrerenEbenen,
    AttributesNames.BegruenungDach,
    AttributesNames.AbschlussDachMaxBezugGebaeude,
    AttributesNames.VonBebauungFreizuhalten,
    AttributesNames.GebaeudeBautyp,
]

KEPT_40_ATTRS = {
    AttributesNames.AbschlussDachMaxBezugGebaeude,
    AttributesNames.AnFluchtlinie,
    AttributesNames.AnOeffentlichenVerkehrsflaechen,
    AttributesNames.AnordnungGaertnerischeAusgestaltungProzentual,
    AttributesNames.AnordnungGaertnerischeAusgestaltung,
    AttributesNames.AnteilDachbegruenung,
    AttributesNames.AufbautenZulaessig,
    AttributesNames.AusnahmeGaertnerischAuszugestaltende,
    AttributesNames.BauweiseID,
    AttributesNames.BBAllgemein,
    AttributesNames.BebauteFlaecheMaxNebengebaeude,
    AttributesNames.BebauteFlaecheMaxProzentual,
    AttributesNames.BebauteFlaecheMax,
    AttributesNames.BebauteFlaecheMin,
    AttributesNames.BegruenungDach,
    AttributesNames.Dachart,
    AttributesNames.DachflaecheMin,
    AttributesNames.DachneigungMax,
    AttributesNames.DurchgangBreite,
    AttributesNames.DurchgangHoehe,
    AttributesNames.FBOKMinimumWohnungen,
    AttributesNames.GebaeudeBautyp,
    AttributesNames.GebaeudeHoeheArt,
    AttributesNames.GebaeudeHoeheMaxAbsolut,
    AttributesNames.GebaeudeHoeheMaxWN,
    AttributesNames.GehsteigbreiteMin,
    AttributesNames.Nutzungsart,
    AttributesNames.OeffentlicheVerkehrsflaecheBreiteMin,
    AttributesNames.Planzeichen,
    AttributesNames.StellplatzregulativUmfangMaximumRelativ,
    AttributesNames.StellplatzregulativUmfangMinimumRelativ,
    AttributesNames.Stockwerk,
    AttributesNames.UnterbrechungGeschlosseneBauweise,
    AttributesNames.VerbotFensterZuOeffentlichenVerkehrsflaechen,
    AttributesNames.VerbotWohnung,
    AttributesNames.VolumenUndUmbaubarerRaum,
    AttributesNames.VonBebauungFreizuhalten,
    AttributesNames.VorkehrungBepflanzung,
    AttributesNames.WidmungInMehrerenEbenen,
    AttributesNames.Widmung,
}
