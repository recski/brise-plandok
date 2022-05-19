GOLD = ["7374", "7857", "7990", "8065", "8250"]
ANNOTATORS = ["01", "02", "03", "04", "05", "06"]
DOC_HEADER = [
    "order",
    "doc_id",
    "assigned",
    "nr_sens_calculated",
    "nr_sens",
    "annotator_1",
    "annotator_2",
    "assigned_2",
    "ann_1_done",
    "ann_2_done",
    "both_done",
]

CYCLE_FILE = "../input/batch_cycles.csv"
CYCLE_COL = "cycle"

ASSIGNMENT_TXT = "assignment.txt"
ASSIGNMENT_XLSX = "assignment.xlsx"
ASSIGNMENT_FILE_HEADER = ["doc_id"]
ASSIGNMENT_DF_HEADER_BASE = ["annotator", "assigned_sentences"]
ASSIGNMENT_ADDITIONAL_HEADER = ["docs_in_batch", "sentences_in_batch", "sum_sentences"]

ANNOTATOR_DOWNLOAD_FOLDER = "download"
ANNOTATOR_UPLOAD_FOLDER = "upload"

PHASE_STR = "phase"

ATTRIBUTES_TO_IGNORE = {
    "AusnahmePruefungErforderlich",
    "WeitereBestimmungPruefungErforderlich",
    "ZuVorherigemSatzGehoerig",
    "Segmentierungsfehler",
    "NoAttribute",
    "N/A",
    "StrittigeBedeutung",
}

REVIEW_DONE_FLAG = "Done"

############
# Labels review
############


class LabelReviewExcelConstants:
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


############
# Full xlsx
############


class FullAnnotationExcelConstants:
    MAIN_SHEET_NAME = "Data"
    ATTRIBUTE_NAMED_RANGE = "Attribute"
    TYPE_NAMED_RANGE = "Type"
    MODALITY_NAMED_RANGE = "Modality"

    FIRST_DATA_ROW = 2

    SEN_ID_COL = 1
    SEN_TEXT_COL = 2
    MODALITY_COL = 3

    ATTRIBUTE_OFFSET = 4
    ATTRIBUTE_STEP = 4

    CATEGORY_OFFSET = 0
    LABEL_OFFSET = 1
    VALUE_OFFSET = 2
    TYPE_OFFSET = 3

    LAST_COLUMN = "BO1"


############
# Full review
############
class FullReviewExcelConstants:
    MAIN_SHEET_NAME = "Data"
    ATTRIBUTE_NAMED_RANGE = "Attribute"
    TYPE_NAMED_RANGE = "Type"
    MODALITY_NAMED_RANGE = "Modality"
    SENTENCE_REVIEW_NAMED_RANGE = "Sentence_Review"

    ERROR_LABEL = "Error"

    FIRST_DATA_ROW = 2

    SEN_ID_COL = 1
    SEN_REVIEW_COL = 2
    SEN_TEXT_COL = 3

    MODALITY_ANN_1_COL = 4
    MODALITY_ANN_2_COL = 5
    MODALITY_ANN_REV_COL = 6

    ATTRIBUTE_OFFSET = 7
    ATTRIBUTE_STEP = 6

    CATEGORY_OFFSET = 0
    LABEL_OFFSET = 1
    VALUE_OFFSET = 2
    TYPE_ANN_1_OFFSET = 3
    TYPE_ANN_2_OFFSET = 4
    TYPE_ANN_REV_OFFSET = 5

    LAST_COLUMN = "CX1"
