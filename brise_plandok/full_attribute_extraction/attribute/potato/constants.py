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
