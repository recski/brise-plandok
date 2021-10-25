
ATTRIBUTES_TO_IGNORE = {
    "AusnahmePruefungErforderlich",
    "WeitereBestimmungPruefungErforderlich",
    "ZuVorherigemSatzGehoerig",
    "Segmentierungsfehler",
    "NoAttribute",
    "N/A",
    "StrittigeBedeutung",
}

class ReviewXlsxConstants:
    MAIN_SHEET_NAME = "Review"
    ATTRIBUTE_NAMED_RANGE = "Attribute"
    ATTRIBUTE_REVIEW_NAMED_RANGE = "Attribute_Review"
    SENTENCE_REVIEW_NAMED_RANGE = "Sentence_Review"

    ERROR_LABEL = "Error"

    FIRST_DATA_ROW = 2

    SEN_ID_COL = 1
    SEN_REVIEW_COL = 2
    SEN_TEXT_COL = 3

    ATTRIBUTE_OFFSET = 4
    ATTRIBUTE_STEP = 5

    CATEGORY_OFFSET = 0
    LABEL_OFFSET = 1
    COUNT_OFFSET = 2
    ANNOTATORS_OFFSET = 3
    ATTRIBUTE_REVIEW_OFFSET = 4

    ANNOTATOR_SEPARATOR = "\n"
 