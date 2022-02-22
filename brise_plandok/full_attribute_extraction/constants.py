NUMBER = r"((\+|-)?\d\d*( ?[,\.] ?\d\d*)?)"
PERCENT = r"(%|v. ?H.)"

NUMBER_WITH_METER = r"(" + NUMBER + r" ?m)"
NUMBER_WITH_PERCENT = r"(" + NUMBER + r" ?" + PERCENT + r")"
NUMBER_WITH_SQUARE_METER = r"(" + NUMBER + r" ?(m ?[²2]))"
NUMBER_WITH_CUBIC_METER = r"(" + NUMBER + r" ?(m ?[³3]))"
NUMBER_WITH_DEGREE = r"(" + NUMBER + r" ?(°|Grad))"

FLAECHEN_NUMBER = r"(" + NUMBER_WITH_PERCENT + r"|" + NUMBER_WITH_SQUARE_METER + r")"

SPACE_OR_BRACKET = r"[\s\(\)]"

DACH = r"(dach|dächer)"
STRASSE = r"(((?!Verkehrsfläche)[A-ZÖ]\w+[- ]?)+(( S|-S|s)traße|( G|-G|g)asse|( P|-P|p)latz|( Z|-Z|z)eile|( G|-G|g)ürtel|( W|-W|w)eg|( A|a)llee))"
GAERTNERISH_GESTALTEN = (
    r"(gärtnerisch (auszugestalten|zu gestalten)|die gärtnerische Ausgestaltung vorgeschrieben)"
)

ALL = r".*"

TRUE = "True"
FALSE = "False"

GROUP = "group"
VALUE = "value"
TYPE = "type"
