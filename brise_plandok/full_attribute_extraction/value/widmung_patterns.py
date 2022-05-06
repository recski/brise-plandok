from brise_plandok.full_attribute_extraction.attribute.utils.constants import GROUP, SPACE_BRACKET_SLASH_DASH

WIDMUNG = {
    # Widmung
    r"(Ländliche Gebiete)": {
        GROUP: 1,
    },
    r"(Erholungsgebiet)(es)?": {
        GROUP: 1,
    },
    r"(Sport-? ?und Spielplätze)": {
        GROUP: 1,
    },
    r"(Parkanlage)": {
        GROUP: 1,
    },
    r"(Grünland)": {
        GROUP: 1,
    },
    r"(Kleingartengebiete?(  für ganzjähriges Wohnen)?)": {
        GROUP: 1,
    },
    r"(Freibäder)": {
        GROUP: 1,
    },
    r"(Grundflächen für Badehütten)": {
        GROUP: 1,
    },
    r"(Schutzgebiet)": {
        GROUP: 1,
    },
    r"(Schutzzone)": {
        GROUP: 1,
    },
    r"(Wald- und Wiesengürtel)": {
        GROUP: 1,
    },
    r"(Parkschutzgebiet)": {
        GROUP: 1,
    },
    r"(Friedhöfe)": {
        GROUP: 1,
    },
    r"(Sondernutzungsgebiete)": {
        GROUP: 1,
    },
    r"(Verkehrs(bänder|band))": {
        GROUP: 1,
    },
    r"(Wohngebiet)": {
        GROUP: 1,
    },
    r"(Industriegebiet)": {
        GROUP: 1,
    },
    r"(Geschäftsviertel)": {
        GROUP: 1,
    },
    r"(Wohnzone)": {
        GROUP: 1,
    },
    r"(Wohngebiet Teil für Geschäftsviertel)": {
        GROUP: 1,
    },
    r"(Wohngebiet - geförderter Wohnbau)": {
        GROUP: 1,
    },
    r"(Wohngebiet Teil für förderbaren Wohnbau)": {
        GROUP: 1,
    },
    r"(Gartensiedlungsgebiet)(es)?": {
        GROUP: 1,
    },
    r"(Gartensiedlungsgebiet)": {
        GROUP: 1,
    },
    r"(Gemeinschaftsanlage)": {
        GROUP: 1,
    },
    r"(Gemeinschaftseinrichtung)": {
        GROUP: 1,
    },
    r"([Gg]emischte[sn]? Baugebiet)": {
        GROUP: 1,
    },
    r"(Betriebsbaugebiet)": {
        GROUP: 1,
    },
    r"(Sondergebiet)(es)?": {
        GROUP: 1,
    },
    r"(Kläranlage)": {
        GROUP: 1,
    },
    r"(Lagerplätze und Landflächen)": {
        GROUP: 1,
    },

    # Kürzel
    SPACE_BRACKET_SLASH_DASH + r"(L)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"„?(E)“?" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(Epk)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(Ekl)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(Eklw)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(Esp)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(Ebd)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(Ebh)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(Lagerwiese)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(Sww)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(SwwL)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(Spk)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(F)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(SN)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(VB)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(W)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(WGV)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(WGF)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(WFB)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(GS)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(GSGM)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(GB(cv)?)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(GB)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(GV)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(GBGF)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(GBGV)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(GBFB)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(GBBG)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(GBF)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(BG)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(IG)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(IGBS)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(IGSI)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"„?(SO)“?" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(SOKläranlage)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(SOLL)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(SOLL/BS)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(SOSI)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"(SOMarkt)" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },
    SPACE_BRACKET_SLASH_DASH + r"„?(G)“?" + SPACE_BRACKET_SLASH_DASH: {
        GROUP: 1,
    },

    # Not included in the list from WP4
    r"(Landesverteidigung)": {
        GROUP: 1,
    },
    r"(Wohn- oder gemischtem Baugebiet)": {
        GROUP: 1,
    },

}
