ATTRIBUTE_NORM_MAP = {
    "Verkehrsflaeche_ID": "VerkehrsflaecheID", 
    "VorkehrungBepflanzungOeffentlicheVerkehrsflaeche": "VorkehrungBepflanzung",
    "AnBaulinie": "AnFluchtlinie",
    "AnStrassenfluchtlinie": "AnFluchtlinie",
    "Bauklasse_ID": "Bauklasse",
    "HochhausUnzulaessigGemaessBB": "HochhausZulaessigGemaessBB",
    "StruktureinheitBebaubar": "Struktureinheit",
}

GOLD_PREFIX = "GOLD"
GOLD_COLOR = "FFD700"

ANNOTATOR_NAME_INDEX = -3

class JsonFields:
    ATTRIBUTES = "attributes"
    GENERATED_ATTRIBUTES = "gen_attributes"
    GOLD_EXISTS = "gold_exists"
    GOLD_ATTRIBUTES = "gold_attributes"
    
