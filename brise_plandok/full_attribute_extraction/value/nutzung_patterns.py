from brise_plandok.full_attribute_extraction.constants import GROUP

NUTZUNG = {
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
    r"((Bauten und baulichen )?(Anlagen für die )?in freier Natur (der )?Erholung suchenden? Bevölkerung( dienendes Bauwerk)?)": {
        GROUP: 1,
    },
    r"(Bauwerke für die Erholung suchende Bevölkerung)": {
        GROUP: 1,
    },
    r"(landwirtschaftliche[sn] Nutz(bauwerk|bauten?))": {
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

    # Not included in the list from WP4
    r"(Sporthalle)": {
        GROUP: 1,
    },
    r"(Radverkehrsanlage)": {
        GROUP: 1,
    },
    r"(Bildungszwecke?)": {
        GROUP: 1,
    },
    r"(Gemeinschaftsfläche?)": {
        GROUP: 1,
    },
    r"(Sport- und (Spielzwecke|Spiel(platz)?fläche))": {
        GROUP: 1,
    },
    r"(medizinische Zwecke)": {
        GROUP: 1,
    },
    r"(Bildung.*[Zz]wecke)": {
        GROUP: 1,
    },
    r"(Lagerzwecke)": {
        GROUP: 1,
    },
    r"(Wohnzwecke)": {
        GROUP: 1,
    },
    r"(Radfahranlage)": {
        GROUP: 1,
    },
    r"(Kinderbetreuungseinrichtung)": {
        GROUP: 1,
    },
    r"Zwecke (der )?(öffentlichen Verwaltung|sozialer Einrichtungen)": {
        GROUP: 2,
    },
    r"(Wasserbehälter)": {
        GROUP: 1,
    },
    r"(Erschließungszwecken)": {
        GROUP: 1,
    },
    r"(Sozial- oder Betreuungseinrichtung)": {
        GROUP: 1,
    },
    r"(Bildungs- und Betreuungseinrichtung für Kinder)": {
        GROUP: 1,
    },
    r"(Pflege- und Betreuungseinrichtungen sowie soziale Zwecke)": {
        GROUP: 1,
    },
    r"(religiösen, kulturellen oder sozialen Zwecken)": {
        GROUP: 1,
    },
    r"(land- und forstwirtschaftlichen Zwecken)": {
        GROUP: 1,
    },

    # Konstruktionen
    r"Schaffung von (.* dienen)": {
        GROUP: 1,
    },
}
