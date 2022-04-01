from brise_plandok.full_attribute_extraction.constants import GROUP, SPACE_BRACKET_SLASH_DASH, SPACE_OR_BRACKET_OR_COMMA

BB_ALLGEMEIN = {
    r"(Einkaufszentr(en|um))": {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(Ekz|EKZ)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    r"(Grundflächen für öffentliche Zwecke)": {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(ÖZ)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(StrG( \d)?)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(StrE( ?\d)?)" + SPACE_OR_BRACKET_OR_COMMA: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(P)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
}
