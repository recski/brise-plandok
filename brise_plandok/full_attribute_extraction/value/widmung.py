from brise_plandok.full_attribute_extraction.constants import GROUP, SPACE_OR_BRACKET

WIDMUNG = {
    # Konstruktionen
    r"(sind( nur der)?) ([^0-9]*) vorbehalten": {
        GROUP: 3,
    },
    r"(dem|der Widmung|der) ([^0-9]*) zugeordnet": {
        GROUP: 2,
    },
    r"Nutzung (als|für) (.*) (erforderlich|zugeführt)": {
        GROUP: 2,
    },
    r"für ([^0-9]*) verwendet": {
        GROUP: 1,
    },
    r"(für|als) ([^0-9]*) vor(zu)?behalten": {
        GROUP: 2,
    },
    r"als ([^0-9]*) ausgewiesen": {
        GROUP: 1,
    },
    r"als ((?!.*Esp)[^0-9]*) bezeichneten": {
        GROUP: 1,
    },
    r"als ([^0-9()]*)( \(.\))? gewidmeten": {
        GROUP: 1,
    },
    r"Errichtung( von)? ((?!gelangenden Gebäude.*)[^0-9]*) vorbehalten": {
        GROUP: 2,
    },
    r"zur Errichtung gelangenden Gebäude sind( nur der)? ([^0-9]*) vorbehalten": {
        GROUP: 2,
    },
    r"als ([^0-9]*) ÖZ festgesetzt": {
        GROUP: 1,
    },
    r"Widmung ([^0-9()]*) (\(\w\w \w\w\))? ?wird": {
        GROUP: 1,
    },
    r"Widmung ([^0-9()]*) (\(\w\w \w\w\))": {
        GROUP: 1,
    },
    r" (\w* Nutzung und Pflege)": {
        GROUP: 1,
    },
    r"Zweckbestimmung „?([^„“]*)“? zuzuführen": {
        GROUP: 1,
    },
    # Gesetz
    r"(Nutzungen im Sinne des . 50 \(1\) des Wiener Garagengesetzes)": {
        GROUP: 1,
    },
    r"(Nutzungen im Sinne des . 50 \(2\) des Wiener Garagengesetzes)": {
        GROUP: 1,
    },
    r"(Nutzung gemäß § 6 Abs. 6 der BO für Wien)": {
        GROUP: 1,
    },
    # Widmung
    r"(Ländliche Gebiete)": {
        GROUP: 1,
    },
    r"\s(Erholungsgebiet)(es)?\s": {
        GROUP: 1,
    },
    r"(Erholungsgebiet/( |-)?Sport- und Spielplätze)": {
        GROUP: 1,
    },
    r"((Grünland/)?Erholungsgebiete?/Parkanlage)": {
        GROUP: 1,
    },
    r"(Kleingartengebiete(  für ganzjähriges Wohnen)?)": {
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
    r"(Schutzzon)": {
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
    r"((Bauland/)?Wohngebiet)": {
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
    r"(Gartensiedlungsgebiet)": {
        GROUP: 1,
    },
    r"(Gartensiedlungsgebiet-Gemeinschaftsanlage)": {
        GROUP: 1,
    },
    r"((Bauland/)?Gemischtes Baugebiet) ": {
        GROUP: 1,
    },
    r"(Gemischte Baugebiet/Betriebsbaugebiet)": {
        GROUP: 1,
    },
    r"(Industriegebiet)": {
        GROUP: 1,
    },
    r"(Sondergebiet)": {
        GROUP: 1,
    },
    r"(Kläranlage)": {
        GROUP: 1,
    },
    r"(Lagerplätze und Landflächen)": {
        GROUP: 1,
    },
    # Nutzungsart
    r"(landwirtschaftliche Nutzung)": {
        GROUP: 1,
    },
    r"(forstwirtschaftliche Nutzung)": {
        GROUP: 1,
    },
    r"(berufsgärtnerische Nutzung)": {
        GROUP: 1,
    },
    r"(öffentlicher Zweck)": {
        GROUP: 1,
    },
    r"(Benützung und Erhaltung des Gebietes)": {
        GROUP: 1,
    },
    r"(Badehütte)": {
        GROUP: 1,
    },
    r"(Nutzung und Pflege notwendiges Bauwerk)": {
        GROUP: 1,
    },
    r"(in freier Natur der Erholung suchenden Bevölkerung dienendes Bauwerk)": {
        GROUP: 1,
    },
    r"(landwirtschaftliches Nutzbauwerk)": {
        GROUP: 1,
    },
    r"(Steinbruch)": {
        GROUP: 1,
    },
    r"(Schottergrube)": {
        GROUP: 1,
    },
    r"(Sandgrube)": {
        GROUP: 1,
    },
    r"(Lehmgrube)": {
        GROUP: 1,
    },
    r"(Tongrube)": {
        GROUP: 1,
    },
    r"(Andere Anlage zur Ausbeutung des Untergrundes)": {
        GROUP: 1,
    },
    r"(Bauwerk die dem Betrieb oder der Erhaltung der Bestattungsanlagen dienend)": {
        GROUP: 1,
    },
    r"(Wohngebäude)": {
        GROUP: 1,
    },
    r"(Religiöser Zweck)": {
        GROUP: 1,
    },
    r"(Kultureller Zweck)": {
        GROUP: 1,
    },
    r"(Sozialer Zweck)": {
        GROUP: 1,
    },
    r"(Öffentliche Verwaltung)": {
        GROUP: 1,
    },
    r"(Gaststätte)": {
        GROUP: 1,
    },
    r"(Beherbergungsstätte)": {
        GROUP: 1,
    },
    r"(Versammlungsstätte)": {
        GROUP: 1,
    },
    r"(Vergnügungsstätte)": {
        GROUP: 1,
    },
    r"(Bürogebäude)": {
        GROUP: 1,
    },
    r"(Geschäftsstätte)": {
        GROUP: 1,
    },
    r"(Lagerraum)": {
        GROUP: 1,
    },
    r"(Werkstätte)": {
        GROUP: 1,
    },
    r"(Pferdestallung)": {
        GROUP: 1,
    },
    r"(Büroraum)": {
        GROUP: 1,
    },
    r"(Geschäftsraum)": {
        GROUP: 1,
    },
    r"(Bauwerk mit Geschäftsräumen für Geschäfte des täglichen Bedarfs)": {
        GROUP: 1,
    },
    r"(Gemeinschaftsanlage wirtschaftlicher Zweck)": {
        GROUP: 1,
    },
    r"(Gemeinschaftsanlage sozialer Zweck)": {
        GROUP: 1,
    },
    r"(Gemeinschaftsanlage kultureller Zweck)": {
        GROUP: 1,
    },
    r"(Gemeinschaftsanlage gesundheitlicher Zweck)": {
        GROUP: 1,
    },
    r"(Gemeinschaftsanlage sportlicher Zweck)": {
        GROUP: 1,
    },
    r"(Bauwerke oder Anlagen für Betriebs- oder Geschäftszwecke)": {
        GROUP: 1,
    },
    r"(Lagerplatz)": {
        GROUP: 1,
    },
    r"(Ländefläche)": {
        GROUP: 1,
    },
    r"(Wohnungen für den Bedarf der Betriebsleitung der Betriebsaufsicht)": {
        GROUP: 1,
    },
    # BBAllgemien
    r"(Einkaufszentr(en|um))": {
        GROUP: 1,
    },
    r"(Grundflächen für öffentliche Zwecke)": {
        GROUP: 1,
    },
    r"(Strukturgebiet)": {
        GROUP: 1,
    },
    r"(Struktureinheit)": {
        GROUP: 1,
    },
    r"(Anlagen zum Einstellen von Kraftfahrzeugen)": {
        GROUP: 1,
    },
    # Kürzel
    SPACE_OR_BRACKET
    + r"(L)"
    + SPACE_OR_BRACKET: {
        GROUP: 1,
    },
    SPACE_OR_BRACKET
    + r"(E)"
    + SPACE_OR_BRACKET: {
        GROUP: 1,
    },
    r"(Epk)": {
        GROUP: 1,
    },
    r"(Ekl)": {
        GROUP: 1,
    },
    r"(Eklw)": {
        GROUP: 1,
    },
    r"(Esp)": {
        GROUP: 1,
    },
    r"(Ebd)": {
        GROUP: 1,
    },
    r"(Ebh)": {
        GROUP: 1,
    },
    r"(ELagerwiese)": {
        GROUP: 1,
    },
    r"(Sww)": {
        GROUP: 1,
    },
    r"(SwwL)": {
        GROUP: 1,
    },
    r"(Spk)": {
        GROUP: 1,
    },
    SPACE_OR_BRACKET
    + r"(F)"
    + SPACE_OR_BRACKET: {
        GROUP: 1,
    },
    r"(SN)": {
        GROUP: 1,
    },
    r"(VB)": {
        GROUP: 1,
    },
    SPACE_OR_BRACKET
    + r"(W)"
    + SPACE_OR_BRACKET: {
        GROUP: 1,
    },
    r"(WGV)": {
        GROUP: 1,
    },
    r"(WGF)": {
        GROUP: 1,
    },
    r"(WFB)": {
        GROUP: 1,
    },
    r"(GS)": {
        GROUP: 1,
    },
    r"(GSGM)": {
        GROUP: 1,
    },
    r"(GB(cv)?)": {
        GROUP: 1,
    },
    r"(GB ?GV)": {
        GROUP: 1,
    },
    r"(GBGF)": {
        GROUP: 1,
    },
    r"(GBFB)": {
        GROUP: 1,
    },
    r"(GBBG)": {
        GROUP: 1,
    },
    r"(GBF)": {
        GROUP: 1,
    },
    r"(lG)": {
        GROUP: 1,
    },
    r"(lGBS)": {
        GROUP: 1,
    },
    r"(lGSI)": {
        GROUP: 1,
    },
    r"(SO)": {
        GROUP: 1,
    },
    r"(SOKläranlage)": {
        GROUP: 1,
    },
    r"(SOLL)": {
        GROUP: 1,
    },
    r"(SOLL/BS)": {
        GROUP: 1,
    },
    r"(SOSI)": {
        GROUP: 1,
    },
    r"(SOMarkt)": {
        GROUP: 1,
    },
    SPACE_OR_BRACKET
    + r"(G)"
    + SPACE_OR_BRACKET: {
        GROUP: 1,
    },
    r"(Ekz|EKZ)": {
        GROUP: 1,
    },
    r"(ÖZ)": {
        GROUP: 1,
    },
    r"(StrG)": {
        GROUP: 1,
    },
    r"(StrE (\d)?)": {
        GROUP: 1,
    },
    SPACE_OR_BRACKET
    + r"(P)"
    + SPACE_OR_BRACKET: {
        GROUP: 1,
    },
    # Not included in the list from WP4
    r"(Winterg[aä]rten)": {
        GROUP: 1,
    },
    r"(Sporthalle)": {
        GROUP: 1,
    },
    r"(Landesverteidigung)": {
        GROUP: 1,
    },
    r"der (öffentlichen Verkehrsfläche)": {
        GROUP: 1,
    },
    r"(Gemischtes Baugebiet/Geschäftsviertel)": {
        GROUP: 1,
    },
}
