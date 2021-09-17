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
GRAY_COLOR = "DCDCDC"

ROW_HEIGHT = 75

ANNOTATOR_NAME_INDEX = -3

class DataFields:
    ID = "id"
    TEXT = "text"
    MODALITY = "modality"
    ALREADY_GOLD_ON_ANNOTATION = "already_gold_on_annotation"
    GEN_ATTRIBUTES_ON_ANNOTATION = "gen_attributes_on_annotation"
    GEN_ATTRIBUTES = "gen_attributes"
    GOLD_EXISTS = "gold_exists"
    GOLD_ATTRIBUTES = "gold_attributes"
    ANNOTATED_ATTRIBUTES = "annotated_attributes"
    ATTRIBUTES = "attributes"
    SEGMENTATION_ERROR = "segmentation_error"
    
