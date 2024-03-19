# Annotator agreement - Types
This statistics is calculated without the sentences with a segmentation error.  
Only sentences containing a rule (a.k.a. gold_modality != None) are taken into account.  
We use Cohen's kappa for calculating the inter-annotator agreement: [cohen_kappa_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html).  
Frequencies of attributes are calculated as the number of sentences where the attribute appears as either gold or annotated either in the first or in the second phase.  
For complexity reasons, agreement is only calculated for cases, where the attribute occurs in gold exactly once, and where both annotators gave at least one annotation for the attribute. In case an annotator labeled the attribute within the same sentence multiple times, the most beneficial type annotation is taken into account, i.e. if the annotator labeled both gold and non-gold types, we regard the gold one.
## Without kappa correction

|  Attr | Freq | Macro | Weighted | ('01', '02') | ('01', '03') | ('01', '04') | ('01', '05') | ('01', '06') | ('02', '03') | ('02', '04') | ('02', '05') | ('02', '06') | ('03', '04') | ('03', '05') | ('03', '06') | ('04', '05') | ('04', '06') | ('05', '06') |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| Number of sentences  | - | - | - | 91 | 30 | 60 | 115 | 118 | 101 | 96 | 23 | 73 | 114 | 38 | 91 | 161 | 29 | 100 | 
| Planzeichen | 1987 | 0.500 | 0.500 | 1.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | nan | 
| Number of sentences  | - | - | - | 20 | 9 | 9 | 22 | 19 | 31 | 33 | 2 | 22 | 25 | 8 | 22 | 45 | 1 | 19 | 
| WidmungUndZweckbestimmung | 1161 | 0.405 | 0.488 | 0.778 | 0.000 | 0.000 | 0.908 | 0.573 | 0.594 | 0.750 | 0.000 | 0.290 | 0.238 | 0.304 | 0.308 | 0.411 | nan | 0.520 | 
| Number of sentences  | - | - | - | 36 | 8 | 11 | 19 | 23 | 14 | 18 | 9 | 10 | 28 | 8 | 23 | 40 | 7 | 26 | 
| Flaechen | 791 | 0.378 | 0.315 | 0.933 | 1.000 | 0.000 | 0.642 | 0.465 | 0.576 | 0.000 | 0.727 | nan | 0.000 | 0.600 | 0.000 | -0.026 | nan | 0.000 | 
| Number of sentences  | - | - | - | 19 | 1 | 6 | 9 | 8 | 11 | 20 | 4 | 8 | 11 | 5 | 14 | 15 | 6 | 13 | 
| VerkehrsflaecheID | 457 | 0.235 | 0.203 | nan | 0.000 | nan | -0.059 | nan | nan | nan | nan | nan | 0.000 | nan | nan | nan | 1.000 | nan | 
| Number of sentences  | - | - | - | 31 | 6 | 16 | 20 | 18 | 25 | 20 | 12 | 12 | 25 | 8 | 22 | 20 | 5 | 20 | 
| AnFluchtlinie | 393 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 36 | 6 | 10 | 19 | 31 | 21 | 18 | 9 | 9 | 25 | 10 | 24 | 26 | 5 | 21 | 
| AnordnungGaertnerischeAusgestaltung | 356 | 0.882 | 0.870 | 0.943 | 1.000 | 1.000 | 0.678 | 0.775 | 1.000 | 1.000 | 0.769 | 0.625 | 0.828 | 1.000 | 0.913 | 0.693 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 17 | 5 | 9 | 8 | 14 | 11 | 21 | 2 | 19 | 10 | 3 | 30 | 23 | 2 | 33 | 
| GebaeudeHoeheMax | 333 | 0.618 | 0.625 | 1.000 | nan | nan | nan | 0.759 | 0.621 | 0.644 | nan | 0.486 | 0.737 | 0.000 | 0.444 | 0.198 | 1.000 | 0.904 | 
| Number of sentences  | - | - | - | 22 | 4 | 5 | 21 | 21 | 17 | 18 | 3 | 12 | 27 | 2 | 16 | 24 | 8 | 16 | 
| Dachart | 303 | 0.848 | 0.834 | 0.889 | 1.000 | 0.583 | 0.889 | 0.901 | 0.655 | 0.870 | nan | 1.000 | 0.822 | 1.000 | 0.733 | 0.798 | 1.000 | 0.733 | 
| Number of sentences  | - | - | - | 2 | 1 | 4 | 3 | 0 | 6 | 2 | 0 | 1 | 12 | 1 | 3 | 0 | 0 | 10 | 
| WidmungInMehrerenEbenen | 294 | 0.000 | 0.000 | nan | nan | 0.000 | 0.000 | nan | nan | nan | nan | nan | 0.000 | nan | nan | nan | nan | 0.000 | 
| Number of sentences  | - | - | - | 21 | 5 | 3 | 23 | 21 | 19 | 14 | 6 | 13 | 16 | 12 | 27 | 30 | 4 | 18 | 
| GebaeudeHoeheArt | 290 | 0.103 | 0.070 | 0.000 | -0.250 | nan | 0.000 | nan | 0.000 | 0.000 | nan | 0.000 | 0.600 | 1.000 | 0.000 | -0.216 | nan | 0.000 | 
| Number of sentences  | - | - | - | 32 | 4 | 6 | 26 | 23 | 22 | 16 | 6 | 11 | 18 | 13 | 22 | 27 | 5 | 14 | 
| VorkehrungBepflanzung | 282 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | 
| Number of sentences  | - | - | - | 9 | 1 | 10 | 8 | 15 | 13 | 15 | 0 | 5 | 13 | 4 | 9 | 5 | 0 | 16 | 
| ErrichtungGebaeude | 271 | 0.000 | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 17 | 1 | 4 | 10 | 12 | 11 | 12 | 3 | 4 | 13 | 1 | 8 | 15 | 4 | 8 | 
| PlangebietAllgemein | 269 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 10 | 4 | 7 | 11 | 8 | 12 | 11 | 3 | 7 | 9 | 4 | 12 | 9 | 5 | 17 | 
| VonBebauungFreizuhalten | 255 | 0.000 | 0.000 | nan | nan | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | 
| Number of sentences  | - | - | - | 26 | 5 | 8 | 21 | 25 | 12 | 13 | 7 | 17 | 20 | 8 | 18 | 18 | 4 | 15 | 
| BegruenungDach | 247 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 17 | 4 | 3 | 22 | 16 | 20 | 14 | 6 | 9 | 18 | 12 | 26 | 27 | 4 | 18 | 
| AbschlussDachMaxBezugGebaeude | 235 | -0.023 | -0.029 | nan | 0.000 | nan | nan | nan | nan | -0.077 | nan | 0.000 | 0.000 | nan | nan | -0.038 | nan | nan | 
| Number of sentences  | - | - | - | 15 | 4 | 6 | 13 | 11 | 16 | 10 | 3 | 5 | 14 | 6 | 14 | 18 | 1 | 10 | 
| GehsteigbreiteMin | 213 | -0.077 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | -0.077 | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 11 | 3 | 4 | 16 | 16 | 15 | 11 | 6 | 7 | 18 | 6 | 20 | 19 | 1 | 16 | 
| StrassenbreiteMin | 207 | -0.080 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | -0.080 | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 21 | 4 | 3 | 12 | 18 | 14 | 14 | 6 | 4 | 20 | 7 | 15 | 11 | 3 | 10 | 
| GebaeudeBautyp | 207 | 0.346 | 0.425 | 0.588 | 0.500 | 0.400 | 0.625 | 1.000 | 0.432 | 0.255 | 0.000 | -0.500 | 0.178 | 0.588 | 0.186 | 0.389 | 0.000 | 0.545 | 
| Number of sentences  | - | - | - | 16 | 2 | 4 | 13 | 18 | 11 | 4 | 4 | 11 | 12 | 5 | 7 | 17 | 2 | 15 | 
| AufbautenZulaessig | 176 | 0.000 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | 0.000 | nan | nan | nan | nan | 0.000 | 
| Number of sentences  | - | - | - | 13 | 5 | 4 | 14 | 11 | 12 | 13 | 4 | 7 | 23 | 6 | 12 | 14 | 3 | 9 | 
| UnterbrechungGeschlosseneBauweise | 158 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 12 | 4 | 6 | 10 | 11 | 8 | 9 | 2 | 4 | 18 | 5 | 12 | 15 | 4 | 8 | 
| DachneigungMax | 146 | 0.802 | 0.811 | 0.143 | 1.000 | 0.571 | 1.000 | 0.744 | 1.000 | 1.000 | nan | 0.000 | 0.769 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 7 | 1 | 3 | 1 | 5 | 8 | 2 | 0 | 1 | 6 | 0 | 3 | 6 | 1 | 2 | 
| AnOeffentlichenVerkehrsflaechen | 143 | 0.000 | 0.000 | nan | nan | 0.000 | nan | 0.000 | nan | 0.000 | nan | nan | nan | nan | nan | 0.000 | nan | nan | 
| Number of sentences  | - | - | - | 3 | 1 | 1 | 1 | 2 | 12 | 6 | 0 | 3 | 14 | 0 | 0 | 0 | 0 | 1 | 
| BauweiseID | 123 | 0.333 | 0.419 | 1.000 | nan | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | nan | 1.000 | 0.000 | nan | nan | nan | nan | 0.000 | 
| Number of sentences  | - | - | - | 6 | 2 | 1 | 10 | 4 | 16 | 5 | 0 | 8 | 6 | 0 | 2 | 3 | 0 | 7 | 
| Bauklasse | 118 | 0.482 | 0.614 | 1.000 | 1.000 | 0.000 | 0.194 | 0.000 | 0.875 | 0.000 | nan | 1.000 | 1.000 | nan | 0.000 | 0.000 | nan | 0.720 | 
| Number of sentences  | - | - | - | 11 | 2 | 3 | 9 | 12 | 10 | 8 | 3 | 3 | 7 | 3 | 6 | 8 | 1 | 5 | 
| EinfriedungAusgestaltung | 117 | 0.000 | 0.000 | nan | nan | nan | nan | 0.000 | nan | 0.000 | nan | nan | nan | nan | 0.000 | nan | 0.000 | nan | 
| Number of sentences  | - | - | - | 6 | 0 | 3 | 10 | 11 | 17 | 6 | 2 | 5 | 10 | 4 | 12 | 6 | 2 | 9 | 
| DurchgangBreite | 113 | 0.000 | 0.000 | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | 0.000 | nan | nan | nan | nan | 0.000 | 
| Number of sentences  | - | - | - | 2 | 1 | 0 | 0 | 0 | 3 | 1 | 2 | 5 | 1 | 0 | 3 | 2 | 3 | 9 | 
| AusnahmeGaertnerischAuszugestaltende | 110 | 0.007 | -0.008 | 0.000 | nan | nan | nan | nan | 0.400 | 0.000 | nan | nan | 0.000 | nan | 0.000 | 0.000 | -0.286 | -0.059 | 
| Number of sentences  | - | - | - | 8 | 1 | 3 | 9 | 12 | 8 | 3 | 5 | 4 | 13 | 3 | 10 | 8 | 1 | 5 | 
| StrassenbreiteMax | 105 | 0.000 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | 0.000 | nan | nan | 
| Number of sentences  | - | - | - | 6 | 0 | 1 | 10 | 6 | 12 | 3 | 2 | 2 | 8 | 5 | 6 | 6 | 2 | 9 | 
| DurchgangHoehe | 105 | 0.000 | 0.000 | nan | nan | nan | nan | nan | 0.000 | nan | nan | nan | nan | 0.000 | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 12 | 1 | 1 | 9 | 7 | 8 | 5 | 1 | 1 | 7 | 1 | 6 | 2 | 1 | 2 | 
| UnterirdischeBaulichkeiten | 99 | 0.209 | 0.340 | 1.000 | nan | 0.000 | 0.000 | 0.000 | 0.758 | 0.000 | nan | nan | 0.000 | nan | 0.333 | 0.000 | nan | 0.000 | 
| Number of sentences  | - | - | - | 6 | 0 | 1 | 1 | 4 | 4 | 6 | 0 | 5 | 0 | 1 | 8 | 0 | 0 | 4 | 
| Struktureinheit | 97 | 0.261 | 0.312 | 0.714 | nan | 0.000 | nan | nan | 0.600 | 0.571 | nan | 0.000 | nan | 0.000 | 0.000 | nan | nan | 0.200 | 
| Number of sentences  | - | - | - | 7 | 1 | 9 | 2 | 5 | 4 | 12 | 0 | 2 | 8 | 14 | 6 | 3 | 0 | 13 | 
| VolumenUndUmbaubarerRaum | 94 | 0.000 | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 5 | 2 | 2 | 5 | 2 | 4 | 5 | 2 | 2 | 6 | 1 | 1 | 4 | 1 | 1 | 
| EinfriedungHoeheGesamt | 90 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 9 | 2 | 1 | 2 | 4 | 5 | 8 | 1 | 4 | 6 | 4 | 4 | 2 | 2 | 2 | 
| Stockwerk | 85 | 0.074 | 0.140 | 0.609 | nan | 0.000 | nan | 0.000 | nan | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 | 0.000 | nan | 0.000 | 
| Number of sentences  | - | - | - | 7 | 0 | 1 | 4 | 7 | 5 | 3 | 3 | 3 | 7 | 3 | 6 | 5 | 1 | 6 | 
| DachflaecheMin | 84 | -0.059 | -0.078 | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | -0.235 | nan | nan | 0.000 | nan | 0.000 | 
| Number of sentences  | - | - | - | 9 | 0 | 0 | 6 | 7 | 8 | 4 | 1 | 0 | 4 | 0 | 2 | 6 | 2 | 1 | 
| EinfriedungLage | 77 | 0.000 | 0.000 | nan | nan | nan | 0.000 | 0.000 | nan | 0.000 | nan | nan | nan | nan | nan | 0.000 | 0.000 | nan | 
| Number of sentences  | - | - | - | 9 | 1 | 1 | 0 | 4 | 5 | 4 | 0 | 0 | 2 | 0 | 2 | 1 | 0 | 2 | 
| AnlageZumEinstellenVorhanden | 77 | 0.000 | 0.000 | nan | nan | nan | nan | 0.000 | 0.000 | 0.000 | nan | nan | 0.000 | nan | nan | 0.000 | nan | 0.000 | 
| Number of sentences  | - | - | - | 2 | 0 | 1 | 1 | 4 | 1 | 2 | 0 | 2 | 1 | 0 | 0 | 1 | 1 | 1 | 
| VorstehendeBauelementeAusladungMax | 69 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 8 | 1 | 1 | 2 | 7 | 4 | 6 | 3 | 5 | 8 | 3 | 4 | 6 | 2 | 4 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen | 68 | 0.000 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | 0.000 | nan | nan | 0.000 | 
| Number of sentences  | - | - | - | 1 | 0 | 2 | 3 | 4 | 1 | 3 | 1 | 1 | 2 | 2 | 6 | 3 | 2 | 4 | 
| EinfriedungZulaessig | 66 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 4 | 1 | 1 | 3 | 4 | 2 | 3 | 1 | 3 | 4 | 1 | 4 | 9 | 3 | 9 | 
| VerbotWohnung | 61 | 0.000 | nan | nan | nan | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 1 | 1 | 2 | 8 | 3 | 3 | 2 | 3 | 7 | 1 | 4 | 2 | 1 | 2 | 
| StrassenbreiteVonBis | 59 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | 
| Number of sentences  | - | - | - | 5 | 3 | 0 | 6 | 4 | 2 | 5 | 0 | 0 | 2 | 1 | 3 | 3 | 1 | 3 | 
| AnordnungGaertnerischeAusgestaltungProzentual | 55 | 0.000 | 0.000 | nan | 0.000 | nan | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | 
| Number of sentences  | - | - | - | 4 | 1 | 4 | 3 | 2 | 4 | 0 | 2 | 1 | 8 | 1 | 2 | 5 | 0 | 2 | 
| OeffentlicheVerkehrsflaecheBreiteMin | 54 | 0.357 | 0.440 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.714 | nan | nan | 0.000 | nan | nan | 
| Number of sentences  | - | - | - | 5 | 1 | 0 | 3 | 4 | 6 | 3 | 3 | 2 | 4 | 2 | 3 | 3 | 1 | 3 | 
| VorbautenVerbot | 48 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 
| HoehenlageGrundflaeche | 47 | 0.000 | nan | nan | nan | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 2 | 0 | 1 | 2 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 
| VorbautenBeschraenkung | 41 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 1 | 3 | 2 | 3 | 1 | 1 | 3 | 0 | 0 | 8 | 4 | 6 | 
| AnteilDachbegruenung | 41 | 0.000 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | 0.000 | nan | nan | 0.000 | 0.000 | nan | 
| Number of sentences  | - | - | - | 1 | 2 | 3 | 2 | 2 | 3 | 4 | 1 | 0 | 2 | 2 | 2 | 4 | 1 | 4 | 
| EinleitungNiederschlagswaesser | 39 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 
| AbschlussDachMaxBezugGelaende | 37 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 4 | 1 | 2 | 1 | 3 | 4 | 1 | 3 | 1 | 3 | 2 | 1 | 5 | 0 | 0 | 
| VerbotStaffelung | 34 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 3 | 6 | 4 | 0 | 1 | 0 | 2 | 2 | 0 | 2 | 1 | 3 | 
| ArkadeHoehe | 32 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 3 | 1 | 0 | 2 | 1 | 1 | 3 | 0 | 0 | 1 | 1 | 0 | 5 | 1 | 1 | 
| StellplatzImNiveauZulaessig | 31 | 0.545 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.545 | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 5 | 0 | 3 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 7 | 
| MaxAnzahlGeschosseOberirdisch | 27 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 3 | 
| GebaeudeHoeheMin | 27 | 0.400 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.400 | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 
| GaragengebaeudeAusfuehrung | 26 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben | 26 | 0.000 | 0.000 | 0.000 | nan | nan | nan | nan | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 3 | 1 | 1 | 0 | 
| StellplatzregulativUmfangMaximumRelativ | 25 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 2 | 4 | 0 | 1 | 
| Massengliederung | 24 | 0.000 | 0.000 | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | 0.000 | nan | 0.000 | nan | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 
| StellplatzregulativUmfangMaximumAbsolut | 23 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 8 | 0 | 1 | 
| StellplatzMax | 23 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 
| OberflaecheBestimmungP | 23 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 2 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 1 | 1 | 0 | 0 | 
| InSchutzzone | 22 | 0.000 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | 0.000 | nan | nan | 
| Number of sentences  | - | - | - | 4 | 0 | 0 | 2 | 1 | 2 | 1 | 1 | 0 | 3 | 0 | 0 | 1 | 1 | 1 | 
| AnzahlGebaeudeMax | 21 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 1 | 2 | 1 | 1 | 1 | 0 | 1 | 8 | 0 | 1 | 2 | 0 | 0 | 
| FBOKMinimumWohnungen | 20 | 0.000 | 0.000 | nan | nan | 0.000 | nan | nan | nan | nan | nan | 0.000 | 0.000 | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 2 | 0 | 
| TechnischeAufbautenHoeheMax | 18 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 2 | 1 | 1 | 2 | 0 | 0 | 0 | 1 | 1 | 4 | 0 | 0 | 1 | 
| StellplatzregulativUmfangMinimumRelativ | 18 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 
| GebaeudeEinschraenkungP | 17 | 0.000 | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 0 | 4 | 0 | 2 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 
| DurchfahrtHoehe | 17 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 2 | 1 | 0 | 0 | 2 | 1 | 0 | 0 | 2 | 0 | 2 | 2 | 0 | 0 | 
| DachneigungMin | 17 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 1 | 3 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 2 | 0 | 0 | 
| Kleinhaeuser | 16 | 0.000 | 0.000 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | 0.000 | nan | 0.000 | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 1 | 1 | 0 | 3 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 1 | 
| BauklasseVIHoeheMax | 16 | 0.000 | 0.000 | nan | nan | 0.000 | 0.000 | nan | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 2 | 2 | 0 | 2 | 0 | 0 | 1 | 1 | 0 | 2 | 0 | 0 | 
| MaxAnzahlDachgeschosse | 14 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 1 | 
| BauklasseVIHoeheMin | 14 | 0.000 | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| StellplatzverpflichtungArt | 12 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 3 | 0 | 1 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 
| VerbotBueroGeschaeftsgebaeude | 11 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau | 11 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 
| AusnahmeVonWohnungenUnzulaessig | 10 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 1 | 0 | 
| DurchfahrtBreite | 9 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 
| Geschaeftsstrassen | 8 | 1.000 | nan | nan | nan | nan | nan | nan | 1.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| VerbotUnterirdischeBauwerkeUeberBaufluchtlinie | 7 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 
| MindestraumhoeheEG | 7 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 
| HochhausZulaessigGemaessBB | 7 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| StellplatzregulativVorhanden | 6 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 
| MaxAnzahlGeschosseOberirdischOhneDachgeschoss | 6 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| VerbotAufenthaltsraum | 4 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| EinfriedungHoeheSockel | 4 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 
| Einbautrasse | 4 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| GelaendeneigungMin | 3 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 
| AnteilBaumbepflanzung | 3 | 0.000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| ZulaessigeGeschossanzahlEinkaufszentrum | 2 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| VerbotStellplaetzeUndParkgebaeude | 2 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| ArkadeLaenge | 2 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| MaxHoeheWohngebaeude | 1 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| LaubengangHoehe | 1 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 


## With kappa correction
[cohen_kappa_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html) results in `nan` if both vectors are uniform and the same.
In the table below, we substituted these `nan` values by the value of complete agreement (1.0).

|  Attr | Freq | Macro | Weighted | ('01', '02') | ('01', '03') | ('01', '04') | ('01', '05') | ('01', '06') | ('02', '03') | ('02', '04') | ('02', '05') | ('02', '06') | ('03', '04') | ('03', '05') | ('03', '06') | ('04', '05') | ('04', '06') | ('05', '06') |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| Overall | - | 0.868 | 0.769 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | 
| Overall weighted | - | 0.770 | 0.727 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | 
| Number of sentences  | - | - | - | 91 | 30 | 60 | 115 | 118 | 101 | 96 | 23 | 73 | 114 | 38 | 91 | 161 | 29 | 100 | 
| Planzeichen | 1987 | 0.933 | 0.927 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 20 | 9 | 9 | 22 | 19 | 31 | 33 | 2 | 22 | 25 | 8 | 22 | 45 | 1 | 19 | 
| WidmungUndZweckbestimmung | 1161 | 0.445 | 0.490 | 0.778 | 0.000 | 0.000 | 0.908 | 0.573 | 0.594 | 0.750 | 0.000 | 0.290 | 0.238 | 0.304 | 0.308 | 0.411 | 1.000 | 0.520 | 
| Number of sentences  | - | - | - | 36 | 8 | 11 | 19 | 23 | 14 | 18 | 9 | 10 | 28 | 8 | 23 | 40 | 7 | 26 | 
| Flaechen | 791 | 0.461 | 0.357 | 0.933 | 1.000 | 0.000 | 0.642 | 0.465 | 0.576 | 0.000 | 0.727 | 1.000 | 0.000 | 0.600 | 0.000 | -0.026 | 1.000 | 0.000 | 
| Number of sentences  | - | - | - | 19 | 1 | 6 | 9 | 8 | 11 | 20 | 4 | 8 | 11 | 5 | 14 | 15 | 6 | 13 | 
| VerkehrsflaecheID | 457 | 0.796 | 0.856 | 1.000 | 0.000 | 1.000 | -0.059 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 31 | 6 | 16 | 20 | 18 | 25 | 20 | 12 | 12 | 25 | 8 | 22 | 20 | 5 | 20 | 
| AnFluchtlinie | 393 | 0.933 | 0.904 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 36 | 6 | 10 | 19 | 31 | 21 | 18 | 9 | 9 | 25 | 10 | 24 | 26 | 5 | 21 | 
| AnordnungGaertnerischeAusgestaltung | 356 | 0.882 | 0.870 | 0.943 | 1.000 | 1.000 | 0.678 | 0.775 | 1.000 | 1.000 | 0.769 | 0.625 | 0.828 | 1.000 | 0.913 | 0.693 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 17 | 5 | 9 | 8 | 14 | 11 | 21 | 2 | 19 | 10 | 3 | 30 | 23 | 2 | 33 | 
| GebaeudeHoeheMax | 333 | 0.720 | 0.668 | 1.000 | 1.000 | 1.000 | 1.000 | 0.759 | 0.621 | 0.644 | 1.000 | 0.486 | 0.737 | 0.000 | 0.444 | 0.198 | 1.000 | 0.904 | 
| Number of sentences  | - | - | - | 22 | 4 | 5 | 21 | 21 | 17 | 18 | 3 | 12 | 27 | 2 | 16 | 24 | 8 | 16 | 
| Dachart | 303 | 0.858 | 0.837 | 0.889 | 1.000 | 0.583 | 0.889 | 0.901 | 0.655 | 0.870 | 1.000 | 1.000 | 0.822 | 1.000 | 0.733 | 0.798 | 1.000 | 0.733 | 
| Number of sentences  | - | - | - | 2 | 1 | 4 | 3 | 0 | 6 | 2 | 0 | 1 | 12 | 1 | 3 | 0 | 0 | 10 | 
| WidmungInMehrerenEbenen | 294 | 0.733 | 0.356 | 1.000 | 1.000 | 0.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 
| Number of sentences  | - | - | - | 21 | 5 | 3 | 23 | 21 | 19 | 14 | 6 | 13 | 16 | 12 | 27 | 30 | 4 | 18 | 
| GebaeudeHoeheArt | 290 | 0.342 | 0.206 | 0.000 | -0.250 | 1.000 | 0.000 | 1.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.600 | 1.000 | 0.000 | -0.216 | 1.000 | 0.000 | 
| Number of sentences  | - | - | - | 32 | 4 | 6 | 26 | 23 | 22 | 16 | 6 | 11 | 18 | 13 | 22 | 27 | 5 | 14 | 
| VorkehrungBepflanzung | 282 | 0.933 | 0.890 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 9 | 1 | 10 | 8 | 15 | 13 | 15 | 0 | 5 | 13 | 4 | 9 | 5 | 0 | 16 | 
| ErrichtungGebaeude | 271 | 0.933 | 0.878 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 17 | 1 | 4 | 10 | 12 | 11 | 12 | 3 | 4 | 13 | 1 | 8 | 15 | 4 | 8 | 
| PlangebietAllgemein | 269 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 10 | 4 | 7 | 11 | 8 | 12 | 11 | 3 | 7 | 9 | 4 | 12 | 9 | 5 | 17 | 
| VonBebauungFreizuhalten | 255 | 0.867 | 0.814 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 
| Number of sentences  | - | - | - | 26 | 5 | 8 | 21 | 25 | 12 | 13 | 7 | 17 | 20 | 8 | 18 | 18 | 4 | 15 | 
| BegruenungDach | 247 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 17 | 4 | 3 | 22 | 16 | 20 | 14 | 6 | 9 | 18 | 12 | 26 | 27 | 4 | 18 | 
| AbschlussDachMaxBezugGebaeude | 235 | 0.659 | 0.657 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | -0.077 | 1.000 | 0.000 | 0.000 | 1.000 | 1.000 | -0.038 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 15 | 4 | 6 | 13 | 11 | 16 | 10 | 3 | 5 | 14 | 6 | 14 | 18 | 1 | 10 | 
| GehsteigbreiteMin | 213 | 0.928 | 0.897 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | -0.077 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 11 | 3 | 4 | 16 | 16 | 15 | 11 | 6 | 7 | 18 | 6 | 20 | 19 | 1 | 16 | 
| StrassenbreiteMin | 207 | 0.928 | 0.885 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | -0.080 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 21 | 4 | 3 | 12 | 18 | 14 | 14 | 6 | 4 | 20 | 7 | 15 | 11 | 3 | 10 | 
| GebaeudeBautyp | 207 | 0.346 | 0.425 | 0.588 | 0.500 | 0.400 | 0.625 | 1.000 | 0.432 | 0.255 | 0.000 | -0.500 | 0.178 | 0.588 | 0.186 | 0.389 | 0.000 | 0.545 | 
| Number of sentences  | - | - | - | 16 | 2 | 4 | 13 | 18 | 11 | 4 | 4 | 11 | 12 | 5 | 7 | 17 | 2 | 15 | 
| AufbautenZulaessig | 176 | 0.800 | 0.730 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 
| Number of sentences  | - | - | - | 13 | 5 | 4 | 14 | 11 | 12 | 13 | 4 | 7 | 23 | 6 | 12 | 14 | 3 | 9 | 
| UnterbrechungGeschlosseneBauweise | 158 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 12 | 4 | 6 | 10 | 11 | 8 | 9 | 2 | 4 | 18 | 5 | 12 | 15 | 4 | 8 | 
| DachneigungMax | 146 | 0.815 | 0.814 | 0.143 | 1.000 | 0.571 | 1.000 | 0.744 | 1.000 | 1.000 | 1.000 | 0.000 | 0.769 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 7 | 1 | 3 | 1 | 5 | 8 | 2 | 0 | 1 | 6 | 0 | 3 | 6 | 1 | 2 | 
| AnOeffentlichenVerkehrsflaechen | 143 | 0.733 | 0.652 | 1.000 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 3 | 1 | 1 | 1 | 2 | 12 | 6 | 0 | 3 | 14 | 0 | 0 | 0 | 0 | 1 | 
| BauweiseID | 123 | 0.600 | 0.432 | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 
| Number of sentences  | - | - | - | 6 | 2 | 1 | 10 | 4 | 16 | 5 | 0 | 8 | 6 | 0 | 2 | 3 | 0 | 7 | 
| Bauklasse | 118 | 0.586 | 0.614 | 1.000 | 1.000 | 0.000 | 0.194 | 0.000 | 0.875 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | 1.000 | 0.720 | 
| Number of sentences  | - | - | - | 11 | 2 | 3 | 9 | 12 | 10 | 8 | 3 | 3 | 7 | 3 | 6 | 8 | 1 | 5 | 
| EinfriedungAusgestaltung | 117 | 0.733 | 0.703 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 
| Number of sentences  | - | - | - | 6 | 0 | 3 | 10 | 11 | 17 | 6 | 2 | 5 | 10 | 4 | 12 | 6 | 2 | 9 | 
| DurchgangBreite | 113 | 0.800 | 0.757 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 
| Number of sentences  | - | - | - | 2 | 1 | 0 | 0 | 0 | 3 | 1 | 2 | 5 | 1 | 0 | 3 | 2 | 3 | 9 | 
| AusnahmeGaertnerischAuszugestaltende | 110 | 0.470 | 0.244 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.400 | 0.000 | 1.000 | 1.000 | 0.000 | 1.000 | 0.000 | 0.000 | -0.286 | -0.059 | 
| Number of sentences  | - | - | - | 8 | 1 | 3 | 9 | 12 | 8 | 3 | 5 | 4 | 13 | 3 | 10 | 8 | 1 | 5 | 
| StrassenbreiteMax | 105 | 0.867 | 0.774 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 6 | 0 | 1 | 10 | 6 | 12 | 3 | 2 | 2 | 8 | 5 | 6 | 6 | 2 | 9 | 
| DurchgangHoehe | 105 | 0.867 | 0.782 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 12 | 1 | 1 | 9 | 7 | 8 | 5 | 1 | 1 | 7 | 1 | 6 | 2 | 1 | 2 | 
| UnterirdischeBaulichkeiten | 99 | 0.473 | 0.392 | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.758 | 0.000 | 1.000 | 1.000 | 0.000 | 1.000 | 0.333 | 0.000 | 1.000 | 0.000 | 
| Number of sentences  | - | - | - | 6 | 0 | 1 | 1 | 4 | 4 | 6 | 0 | 5 | 0 | 1 | 8 | 0 | 0 | 4 | 
| Struktureinheit | 97 | 0.606 | 0.398 | 0.714 | 1.000 | 0.000 | 1.000 | 1.000 | 0.600 | 0.571 | 1.000 | 0.000 | 1.000 | 0.000 | 0.000 | 1.000 | 1.000 | 0.200 | 
| Number of sentences  | - | - | - | 7 | 1 | 9 | 2 | 5 | 4 | 12 | 0 | 2 | 8 | 14 | 6 | 3 | 0 | 13 | 
| VolumenUndUmbaubarerRaum | 94 | 0.933 | 0.860 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 5 | 2 | 2 | 5 | 2 | 4 | 5 | 2 | 2 | 6 | 1 | 1 | 4 | 1 | 1 | 
| EinfriedungHoeheGesamt | 90 | 0.933 | 0.953 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 9 | 2 | 1 | 2 | 4 | 5 | 8 | 1 | 4 | 6 | 4 | 4 | 2 | 2 | 2 | 
| Stockwerk | 85 | 0.321 | 0.309 | 0.609 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 | 0.000 | 1.000 | 0.000 | 
| Number of sentences  | - | - | - | 7 | 0 | 1 | 4 | 7 | 5 | 3 | 3 | 3 | 7 | 3 | 6 | 5 | 1 | 6 | 
| DachflaecheMin | 84 | 0.718 | 0.629 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | -0.235 | 1.000 | 1.000 | 0.000 | 1.000 | 0.000 | 
| Number of sentences  | - | - | - | 9 | 0 | 0 | 6 | 7 | 8 | 4 | 1 | 0 | 4 | 0 | 2 | 6 | 2 | 1 | 
| EinfriedungLage | 77 | 0.667 | 0.500 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | 1.000 | 
| Number of sentences  | - | - | - | 9 | 1 | 1 | 0 | 4 | 5 | 4 | 0 | 0 | 2 | 0 | 2 | 1 | 0 | 2 | 
| AnlageZumEinstellenVorhanden | 77 | 0.600 | 0.419 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | 0.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.000 | 1.000 | 0.000 | 
| Number of sentences  | - | - | - | 2 | 0 | 1 | 1 | 4 | 1 | 2 | 0 | 2 | 1 | 0 | 0 | 1 | 1 | 1 | 
| VorstehendeBauelementeAusladungMax | 69 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 8 | 1 | 1 | 2 | 7 | 4 | 6 | 3 | 5 | 8 | 3 | 4 | 6 | 2 | 4 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen | 68 | 0.800 | 0.750 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.000 | 
| Number of sentences  | - | - | - | 1 | 0 | 2 | 3 | 4 | 1 | 3 | 1 | 1 | 2 | 2 | 6 | 3 | 2 | 4 | 
| EinfriedungZulaessig | 66 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 4 | 1 | 1 | 3 | 4 | 2 | 3 | 1 | 3 | 4 | 1 | 4 | 9 | 3 | 9 | 
| VerbotWohnung | 61 | 0.933 | 0.981 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 1 | 1 | 2 | 8 | 3 | 3 | 2 | 3 | 7 | 1 | 4 | 2 | 1 | 2 | 
| StrassenbreiteVonBis | 59 | 0.933 | 0.950 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 
| Number of sentences  | - | - | - | 5 | 3 | 0 | 6 | 4 | 2 | 5 | 0 | 0 | 2 | 1 | 3 | 3 | 1 | 3 | 
| AnordnungGaertnerischeAusgestaltungProzentual | 55 | 0.800 | 0.737 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 
| Number of sentences  | - | - | - | 4 | 1 | 4 | 3 | 2 | 4 | 0 | 2 | 1 | 8 | 1 | 2 | 5 | 0 | 2 | 
| OeffentlicheVerkehrsflaecheBreiteMin | 54 | 0.914 | 0.813 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.714 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 5 | 1 | 0 | 3 | 4 | 6 | 3 | 3 | 2 | 4 | 2 | 3 | 3 | 1 | 3 | 
| VorbautenVerbot | 48 | 0.933 | 0.907 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 
| HoehenlageGrundflaeche | 47 | 0.933 | 0.800 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 2 | 0 | 1 | 2 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 
| VorbautenBeschraenkung | 41 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 1 | 3 | 2 | 3 | 1 | 1 | 3 | 0 | 0 | 8 | 4 | 6 | 
| AnteilDachbegruenung | 41 | 0.733 | 0.529 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | 1.000 | 1.000 | 0.000 | 0.000 | 1.000 | 
| Number of sentences  | - | - | - | 1 | 2 | 3 | 2 | 2 | 3 | 4 | 1 | 0 | 2 | 2 | 2 | 4 | 1 | 4 | 
| EinleitungNiederschlagswaesser | 39 | 0.933 | 0.970 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 
| AbschlussDachMaxBezugGelaende | 37 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 4 | 1 | 2 | 1 | 3 | 4 | 1 | 3 | 1 | 3 | 2 | 1 | 5 | 0 | 0 | 
| VerbotStaffelung | 34 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 3 | 6 | 4 | 0 | 1 | 0 | 2 | 2 | 0 | 2 | 1 | 3 | 
| ArkadeHoehe | 32 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 3 | 1 | 0 | 2 | 1 | 1 | 3 | 0 | 0 | 1 | 1 | 0 | 5 | 1 | 1 | 
| StellplatzImNiveauZulaessig | 31 | 0.970 | 0.886 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.545 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 5 | 0 | 3 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 7 | 
| MaxAnzahlGeschosseOberirdisch | 27 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 3 | 
| GebaeudeHoeheMin | 27 | 0.960 | 0.743 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.400 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 
| GaragengebaeudeAusfuehrung | 26 | 0.933 | 0.667 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben | 26 | 0.867 | 0.500 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 3 | 1 | 1 | 0 | 
| StellplatzregulativUmfangMaximumRelativ | 25 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 2 | 4 | 0 | 1 | 
| Massengliederung | 24 | 0.800 | 0.500 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 
| StellplatzregulativUmfangMaximumAbsolut | 23 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 8 | 0 | 1 | 
| StellplatzMax | 23 | 0.933 | 0.467 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 
| OberflaecheBestimmungP | 23 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 2 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 1 | 1 | 0 | 0 | 
| InSchutzzone | 22 | 0.867 | 0.700 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 4 | 0 | 0 | 2 | 1 | 2 | 1 | 1 | 0 | 3 | 0 | 0 | 1 | 1 | 1 | 
| AnzahlGebaeudeMax | 21 | 0.933 | 0.941 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 1 | 2 | 1 | 1 | 1 | 0 | 1 | 8 | 0 | 1 | 2 | 0 | 0 | 
| FBOKMinimumWohnungen | 20 | 0.800 | 0.444 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 2 | 0 | 
| TechnischeAufbautenHoeheMax | 18 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 1 | 0 | 2 | 1 | 1 | 2 | 0 | 0 | 0 | 1 | 1 | 4 | 0 | 0 | 1 | 
| StellplatzregulativUmfangMinimumRelativ | 18 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 
| GebaeudeEinschraenkungP | 17 | 0.933 | 0.667 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 0 | 4 | 0 | 2 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 
| DurchfahrtHoehe | 17 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 2 | 1 | 0 | 0 | 2 | 1 | 0 | 0 | 2 | 0 | 2 | 2 | 0 | 0 | 
| DachneigungMin | 17 | 0.933 | 0.833 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 1 | 3 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 2 | 0 | 0 | 
| Kleinhaeuser | 16 | 0.733 | 0.500 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 1 | 1 | 0 | 3 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 1 | 
| BauklasseVIHoeheMax | 16 | 0.800 | 0.643 | 1.000 | 1.000 | 0.000 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 2 | 2 | 0 | 2 | 0 | 0 | 1 | 1 | 0 | 2 | 0 | 0 | 
| MaxAnzahlDachgeschosse | 14 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 1 | 
| BauklasseVIHoeheMin | 14 | 0.933 | 0.727 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| StellplatzverpflichtungArt | 12 | 1.000 | nan | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 3 | 0 | 1 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 
| VerbotBueroGeschaeftsgebaeude | 11 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau | 11 | 1.000 | nan | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 
| AusnahmeVonWohnungenUnzulaessig | 10 | 0.933 | 0.500 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 1 | 0 | 
| DurchfahrtBreite | 9 | 0.933 | 0.833 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 
| Geschaeftsstrassen | 8 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| VerbotUnterirdischeBauwerkeUeberBaufluchtlinie | 7 | 1.000 | nan | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 
| MindestraumhoeheEG | 7 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 
| HochhausZulaessigGemaessBB | 7 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| StellplatzregulativVorhanden | 6 | 1.000 | nan | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 
| MaxAnzahlGeschosseOberirdischOhneDachgeschoss | 6 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| VerbotAufenthaltsraum | 4 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| EinfriedungHoeheSockel | 4 | 1.000 | nan | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 
| Einbautrasse | 4 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| GelaendeneigungMin | 3 | 1.000 | nan | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 
| AnteilBaumbepflanzung | 3 | 0.933 | 0.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| ZulaessigeGeschossanzahlEinkaufszentrum | 2 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| VerbotStellplaetzeUndParkgebaeude | 2 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| ArkadeLaenge | 2 | 1.000 | nan | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| MaxHoeheWohngebaeude | 1 | 1.000 | nan | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| LaubengangHoehe | 1 | 1.000 | nan | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 


