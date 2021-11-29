NUMBER_WITH_METER = r"((\+|-)?\d\d*( ?, ?\d\d*)? ?m)"
PERCENT = r"(\d+ ?(%|v. ?H.))"
AREA_SIZE = r"((\d\d*.\d*) ?(m ?(²|2)|v. ?H.?|%))"

SPACE_OR_BRACKET = r"[\s\(\)]"

DACH =r"(dach|dächer)"

STRASSE = r" (((?!Verkehrsfläche)[A-ZÖ]\w+[- ]?)+(( S|-S|s)traße|( G|-G|g)asse|( P|-P|p)latz|( Z|-Z|z)eile|( G|-G|g)ürtel))"

ALL = r".*"

TRUE = "True"
FALSE = "False"

GROUP = "group"
VALUE = "value"
TYPE = "type"