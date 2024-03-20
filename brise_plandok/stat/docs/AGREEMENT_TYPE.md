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
| Planzeichen | 1987 | 0.5000 | 0.5000 | 1.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | 
| Number of sentences  | - | - | - | 20 | 9 | 9 | 22 | 19 | 31 | 33 | 2 | 22 | 25 | 8 | 22 | 45 | 1 | 19 | 
| WidmungUndZweckbestimmung | 1161 | 0.4053 | 0.4877 | 0.7778 | 0.0000 | 0.0000 | 0.9076 | 0.5730 | 0.5944 | 0.7500 | 0.0000 | 0.2903 | 0.2382 | 0.3043 | 0.3077 | 0.4107 | nan | 0.5202 | 
| Number of sentences  | - | - | - | 36 | 8 | 11 | 19 | 23 | 14 | 18 | 9 | 10 | 28 | 8 | 23 | 40 | 7 | 26 | 
| Flaechen | 791 | 0.3782 | 0.3150 | 0.9328 | 1.0000 | 0.0000 | 0.6415 | 0.4651 | 0.5758 | 0.0000 | 0.7273 | nan | 0.0000 | 0.6000 | 0.0000 | -0.0256 | nan | 0.0000 | 
| Number of sentences  | - | - | - | 19 | 1 | 6 | 9 | 8 | 11 | 20 | 4 | 8 | 11 | 5 | 14 | 15 | 6 | 13 | 
| VerkehrsflaecheID | 457 | 0.2353 | 0.2026 | nan | 0.0000 | nan | -0.0588 | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | 1.0000 | nan | 
| Number of sentences  | - | - | - | 31 | 6 | 16 | 20 | 18 | 25 | 20 | 12 | 12 | 25 | 8 | 22 | 20 | 5 | 20 | 
| AnFluchtlinie | 393 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 36 | 6 | 10 | 19 | 31 | 21 | 18 | 9 | 9 | 25 | 10 | 24 | 26 | 5 | 21 | 
| AnordnungGaertnerischeAusgestaltung | 356 | 0.8816 | 0.8705 | 0.9434 | 1.0000 | 1.0000 | 0.6780 | 0.7748 | 1.0000 | 1.0000 | 0.7692 | 0.6250 | 0.8276 | 1.0000 | 0.9130 | 0.6929 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 17 | 5 | 9 | 8 | 14 | 11 | 21 | 2 | 19 | 10 | 3 | 30 | 23 | 2 | 33 | 
| GebaeudeHoeheMax | 333 | 0.6176 | 0.6246 | 1.0000 | nan | nan | nan | 0.7586 | 0.6207 | 0.6441 | nan | 0.4865 | 0.7368 | 0.0000 | 0.4444 | 0.1977 | 1.0000 | 0.9043 | 
| Number of sentences  | - | - | - | 22 | 4 | 5 | 21 | 21 | 17 | 18 | 3 | 12 | 27 | 2 | 16 | 24 | 8 | 16 | 
| Dachart | 303 | 0.8482 | 0.8342 | 0.8889 | 1.0000 | 0.5833 | 0.8889 | 0.9014 | 0.6554 | 0.8696 | nan | 1.0000 | 0.8224 | 1.0000 | 0.7333 | 0.7983 | 1.0000 | 0.7333 | 
| Number of sentences  | - | - | - | 2 | 1 | 4 | 3 | 0 | 6 | 2 | 0 | 1 | 12 | 1 | 3 | 0 | 0 | 10 | 
| WidmungInMehrerenEbenen | 294 | 0.0000 | 0.0000 | nan | nan | 0.0000 | 0.0000 | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | nan | 0.0000 | 
| Number of sentences  | - | - | - | 21 | 5 | 3 | 23 | 21 | 19 | 14 | 6 | 13 | 16 | 12 | 27 | 30 | 4 | 18 | 
| GebaeudeHoeheArt | 290 | 0.1031 | 0.0700 | 0.0000 | -0.2500 | nan | 0.0000 | nan | 0.0000 | 0.0000 | nan | 0.0000 | 0.6000 | 1.0000 | 0.0000 | -0.2162 | nan | 0.0000 | 
| Number of sentences  | - | - | - | 32 | 4 | 6 | 26 | 23 | 22 | 16 | 6 | 11 | 18 | 13 | 22 | 27 | 5 | 14 | 
| VorkehrungBepflanzung | 282 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | 
| Number of sentences  | - | - | - | 9 | 1 | 10 | 8 | 15 | 13 | 15 | 0 | 5 | 13 | 4 | 9 | 5 | 0 | 16 | 
| ErrichtungGebaeude | 271 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 17 | 1 | 4 | 10 | 12 | 11 | 12 | 3 | 4 | 13 | 1 | 8 | 15 | 4 | 8 | 
| PlangebietAllgemein | 269 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 10 | 4 | 7 | 11 | 8 | 12 | 11 | 3 | 7 | 9 | 4 | 12 | 9 | 5 | 17 | 
| VonBebauungFreizuhalten | 255 | 0.0000 | 0.0000 | nan | nan | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | 
| Number of sentences  | - | - | - | 26 | 5 | 8 | 21 | 25 | 12 | 13 | 7 | 17 | 20 | 8 | 18 | 18 | 4 | 15 | 
| BegruenungDach | 247 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 17 | 4 | 3 | 22 | 16 | 20 | 14 | 6 | 9 | 18 | 12 | 26 | 27 | 4 | 18 | 
| AbschlussDachMaxBezugGebaeude | 235 | -0.0231 | -0.0294 | nan | 0.0000 | nan | nan | nan | nan | -0.0769 | nan | 0.0000 | 0.0000 | nan | nan | -0.0385 | nan | nan | 
| Number of sentences  | - | - | - | 15 | 4 | 6 | 13 | 11 | 16 | 10 | 3 | 5 | 14 | 6 | 14 | 18 | 1 | 10 | 
| GehsteigbreiteMin | 213 | -0.0769 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | -0.0769 | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 11 | 3 | 4 | 16 | 16 | 15 | 11 | 6 | 7 | 18 | 6 | 20 | 19 | 1 | 16 | 
| StrassenbreiteMin | 207 | -0.0800 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | -0.0800 | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 21 | 4 | 3 | 12 | 18 | 14 | 14 | 6 | 4 | 20 | 7 | 15 | 11 | 3 | 10 | 
| GebaeudeBautyp | 207 | 0.3458 | 0.4252 | 0.5882 | 0.5000 | 0.4000 | 0.6250 | 1.0000 | 0.4324 | 0.2553 | 0.0000 | -0.5000 | 0.1781 | 0.5882 | 0.1860 | 0.3889 | 0.0000 | 0.5455 | 
| Number of sentences  | - | - | - | 16 | 2 | 4 | 13 | 18 | 11 | 4 | 4 | 11 | 12 | 5 | 7 | 17 | 2 | 15 | 
| AufbautenZulaessig | 176 | 0.0000 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | 0.0000 | nan | nan | nan | nan | 0.0000 | 
| Number of sentences  | - | - | - | 13 | 5 | 4 | 14 | 11 | 12 | 13 | 4 | 7 | 23 | 6 | 12 | 14 | 3 | 9 | 
| UnterbrechungGeschlosseneBauweise | 158 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 12 | 4 | 6 | 10 | 11 | 8 | 9 | 2 | 4 | 18 | 5 | 12 | 15 | 4 | 8 | 
| DachneigungMax | 146 | 0.8020 | 0.8109 | 0.1429 | 1.0000 | 0.5714 | 1.0000 | 0.7442 | 1.0000 | 1.0000 | nan | 0.0000 | 0.7692 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 7 | 1 | 3 | 1 | 5 | 8 | 2 | 0 | 1 | 6 | 0 | 3 | 6 | 1 | 2 | 
| AnOeffentlichenVerkehrsflaechen | 143 | 0.0000 | 0.0000 | nan | nan | 0.0000 | nan | 0.0000 | nan | 0.0000 | nan | nan | nan | nan | nan | 0.0000 | nan | nan | 
| Number of sentences  | - | - | - | 3 | 1 | 1 | 1 | 2 | 12 | 6 | 0 | 3 | 14 | 0 | 0 | 0 | 0 | 1 | 
| BauweiseID | 123 | 0.3333 | 0.4186 | 1.0000 | nan | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | nan | 1.0000 | 0.0000 | nan | nan | nan | nan | 0.0000 | 
| Number of sentences  | - | - | - | 6 | 2 | 1 | 10 | 4 | 16 | 5 | 0 | 8 | 6 | 0 | 2 | 3 | 0 | 7 | 
| Bauklasse | 118 | 0.4824 | 0.6139 | 1.0000 | 1.0000 | 0.0000 | 0.1935 | 0.0000 | 0.8750 | 0.0000 | nan | 1.0000 | 1.0000 | nan | 0.0000 | 0.0000 | nan | 0.7200 | 
| Number of sentences  | - | - | - | 11 | 2 | 3 | 9 | 12 | 10 | 8 | 3 | 3 | 7 | 3 | 6 | 8 | 1 | 5 | 
| EinfriedungAusgestaltung | 117 | 0.0000 | 0.0000 | nan | nan | nan | nan | 0.0000 | nan | 0.0000 | nan | nan | nan | nan | 0.0000 | nan | 0.0000 | nan | 
| Number of sentences  | - | - | - | 6 | 0 | 3 | 10 | 11 | 17 | 6 | 2 | 5 | 10 | 4 | 12 | 6 | 2 | 9 | 
| DurchgangBreite | 113 | 0.0000 | 0.0000 | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | 0.0000 | nan | nan | nan | nan | 0.0000 | 
| Number of sentences  | - | - | - | 2 | 1 | 0 | 0 | 0 | 3 | 1 | 2 | 5 | 1 | 0 | 3 | 2 | 3 | 9 | 
| AusnahmeGaertnerischAuszugestaltende | 110 | 0.0069 | -0.0078 | 0.0000 | nan | nan | nan | nan | 0.4000 | 0.0000 | nan | nan | 0.0000 | nan | 0.0000 | 0.0000 | -0.2857 | -0.0588 | 
| Number of sentences  | - | - | - | 8 | 1 | 3 | 9 | 12 | 8 | 3 | 5 | 4 | 13 | 3 | 10 | 8 | 1 | 5 | 
| StrassenbreiteMax | 105 | 0.0000 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | 0.0000 | nan | nan | 
| Number of sentences  | - | - | - | 6 | 0 | 1 | 10 | 6 | 12 | 3 | 2 | 2 | 8 | 5 | 6 | 6 | 2 | 9 | 
| DurchgangHoehe | 105 | 0.0000 | 0.0000 | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | nan | 0.0000 | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 12 | 1 | 1 | 9 | 7 | 8 | 5 | 1 | 1 | 7 | 1 | 6 | 2 | 1 | 2 | 
| UnterirdischeBaulichkeiten | 99 | 0.2091 | 0.3400 | 1.0000 | nan | 0.0000 | 0.0000 | 0.0000 | 0.7576 | 0.0000 | nan | nan | 0.0000 | nan | 0.3333 | 0.0000 | nan | 0.0000 | 
| Number of sentences  | - | - | - | 6 | 0 | 1 | 1 | 4 | 4 | 6 | 0 | 5 | 0 | 1 | 8 | 0 | 0 | 4 | 
| Struktureinheit | 97 | 0.2607 | 0.3118 | 0.7143 | nan | 0.0000 | nan | nan | 0.6000 | 0.5714 | nan | 0.0000 | nan | 0.0000 | 0.0000 | nan | nan | 0.2000 | 
| Number of sentences  | - | - | - | 7 | 1 | 9 | 2 | 5 | 4 | 12 | 0 | 2 | 8 | 14 | 6 | 3 | 0 | 13 | 
| VolumenUndUmbaubarerRaum | 94 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 5 | 2 | 2 | 5 | 2 | 4 | 5 | 2 | 2 | 6 | 1 | 1 | 4 | 1 | 1 | 
| EinfriedungHoeheGesamt | 90 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 9 | 2 | 1 | 2 | 4 | 5 | 8 | 1 | 4 | 6 | 4 | 4 | 2 | 2 | 2 | 
| Stockwerk | 85 | 0.0735 | 0.1395 | 0.6087 | nan | 0.0000 | nan | 0.0000 | nan | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.2000 | 0.0000 | 0.0000 | nan | 0.0000 | 
| Number of sentences  | - | - | - | 7 | 0 | 1 | 4 | 7 | 5 | 3 | 3 | 3 | 7 | 3 | 6 | 5 | 1 | 6 | 
| DachflaecheMin | 84 | -0.0588 | -0.0784 | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | -0.2353 | nan | nan | 0.0000 | nan | 0.0000 | 
| Number of sentences  | - | - | - | 9 | 0 | 0 | 6 | 7 | 8 | 4 | 1 | 0 | 4 | 0 | 2 | 6 | 2 | 1 | 
| EinfriedungLage | 77 | 0.0000 | 0.0000 | nan | nan | nan | 0.0000 | 0.0000 | nan | 0.0000 | nan | nan | nan | nan | nan | 0.0000 | 0.0000 | nan | 
| Number of sentences  | - | - | - | 9 | 1 | 1 | 0 | 4 | 5 | 4 | 0 | 0 | 2 | 0 | 2 | 1 | 0 | 2 | 
| AnlageZumEinstellenVorhanden | 77 | 0.0000 | 0.0000 | nan | nan | nan | nan | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0.0000 | nan | nan | 0.0000 | nan | 0.0000 | 
| Number of sentences  | - | - | - | 2 | 0 | 1 | 1 | 4 | 1 | 2 | 0 | 2 | 1 | 0 | 0 | 1 | 1 | 1 | 
| VorstehendeBauelementeAusladungMax | 69 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 8 | 1 | 1 | 2 | 7 | 4 | 6 | 3 | 5 | 8 | 3 | 4 | 6 | 2 | 4 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen | 68 | 0.0000 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | 0.0000 | nan | nan | 0.0000 | 
| Number of sentences  | - | - | - | 1 | 0 | 2 | 3 | 4 | 1 | 3 | 1 | 1 | 2 | 2 | 6 | 3 | 2 | 4 | 
| EinfriedungZulaessig | 66 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 4 | 1 | 1 | 3 | 4 | 2 | 3 | 1 | 3 | 4 | 1 | 4 | 9 | 3 | 9 | 
| VerbotWohnung | 61 | 0.0000 | nan | nan | nan | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 1 | 1 | 2 | 8 | 3 | 3 | 2 | 3 | 7 | 1 | 4 | 2 | 1 | 2 | 
| StrassenbreiteVonBis | 59 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | 
| Number of sentences  | - | - | - | 5 | 3 | 0 | 6 | 4 | 2 | 5 | 0 | 0 | 2 | 1 | 3 | 3 | 1 | 3 | 
| AnordnungGaertnerischeAusgestaltungProzentual | 55 | 0.0000 | 0.0000 | nan | 0.0000 | nan | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | 
| Number of sentences  | - | - | - | 4 | 1 | 4 | 3 | 2 | 4 | 0 | 2 | 1 | 8 | 1 | 2 | 5 | 0 | 2 | 
| OeffentlicheVerkehrsflaecheBreiteMin | 54 | 0.3571 | 0.4396 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.7143 | nan | nan | 0.0000 | nan | nan | 
| Number of sentences  | - | - | - | 5 | 1 | 0 | 3 | 4 | 6 | 3 | 3 | 2 | 4 | 2 | 3 | 3 | 1 | 3 | 
| VorbautenVerbot | 48 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 
| HoehenlageGrundflaeche | 47 | 0.0000 | nan | nan | nan | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 2 | 0 | 1 | 2 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 
| VorbautenBeschraenkung | 41 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 1 | 3 | 2 | 3 | 1 | 1 | 3 | 0 | 0 | 8 | 4 | 6 | 
| AnteilDachbegruenung | 41 | 0.0000 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | 0.0000 | nan | nan | 0.0000 | 0.0000 | nan | 
| Number of sentences  | - | - | - | 1 | 2 | 3 | 2 | 2 | 3 | 4 | 1 | 0 | 2 | 2 | 2 | 4 | 1 | 4 | 
| EinleitungNiederschlagswaesser | 39 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 
| AbschlussDachMaxBezugGelaende | 37 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 4 | 1 | 2 | 1 | 3 | 4 | 1 | 3 | 1 | 3 | 2 | 1 | 5 | 0 | 0 | 
| VerbotStaffelung | 34 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 3 | 6 | 4 | 0 | 1 | 0 | 2 | 2 | 0 | 2 | 1 | 3 | 
| ArkadeHoehe | 32 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 3 | 1 | 0 | 2 | 1 | 1 | 3 | 0 | 0 | 1 | 1 | 0 | 5 | 1 | 1 | 
| StellplatzImNiveauZulaessig | 31 | 0.5455 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.5455 | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 5 | 0 | 3 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 7 | 
| MaxAnzahlGeschosseOberirdisch | 27 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 3 | 
| GebaeudeHoeheMin | 27 | 0.4000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.4000 | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 
| GaragengebaeudeAusfuehrung | 26 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben | 26 | 0.0000 | 0.0000 | 0.0000 | nan | nan | nan | nan | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 3 | 1 | 1 | 0 | 
| StellplatzregulativUmfangMaximumRelativ | 25 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 2 | 4 | 0 | 1 | 
| Massengliederung | 24 | 0.0000 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | 0.0000 | nan | 0.0000 | nan | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 
| StellplatzregulativUmfangMaximumAbsolut | 23 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 8 | 0 | 1 | 
| StellplatzMax | 23 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 
| OberflaecheBestimmungP | 23 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 2 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 1 | 1 | 0 | 0 | 
| InSchutzzone | 22 | 0.0000 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | 0.0000 | nan | nan | 
| Number of sentences  | - | - | - | 4 | 0 | 0 | 2 | 1 | 2 | 1 | 1 | 0 | 3 | 0 | 0 | 1 | 1 | 1 | 
| AnzahlGebaeudeMax | 21 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 1 | 2 | 1 | 1 | 1 | 0 | 1 | 8 | 0 | 1 | 2 | 0 | 0 | 
| FBOKMinimumWohnungen | 20 | 0.0000 | 0.0000 | nan | nan | 0.0000 | nan | nan | nan | nan | nan | 0.0000 | 0.0000 | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 2 | 0 | 
| TechnischeAufbautenHoeheMax | 18 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 2 | 1 | 1 | 2 | 0 | 0 | 0 | 1 | 1 | 4 | 0 | 0 | 1 | 
| StellplatzregulativUmfangMinimumRelativ | 18 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 
| GebaeudeEinschraenkungP | 17 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 0 | 4 | 0 | 2 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 
| DurchfahrtHoehe | 17 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 2 | 1 | 0 | 0 | 2 | 1 | 0 | 0 | 2 | 0 | 2 | 2 | 0 | 0 | 
| DachneigungMin | 17 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 1 | 3 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 2 | 0 | 0 | 
| Kleinhaeuser | 16 | 0.0000 | 0.0000 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | 0.0000 | nan | 0.0000 | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 1 | 1 | 0 | 3 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 1 | 
| BauklasseVIHoeheMax | 16 | 0.0000 | 0.0000 | nan | nan | 0.0000 | 0.0000 | nan | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 2 | 2 | 0 | 2 | 0 | 0 | 1 | 1 | 0 | 2 | 0 | 0 | 
| MaxAnzahlDachgeschosse | 14 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 1 | 
| BauklasseVIHoeheMin | 14 | 0.0000 | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| StellplatzverpflichtungArt | 12 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 3 | 0 | 1 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 
| VerbotBueroGeschaeftsgebaeude | 11 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau | 11 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 
| AusnahmeVonWohnungenUnzulaessig | 10 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 1 | 0 | 
| DurchfahrtBreite | 9 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 
| Geschaeftsstrassen | 8 | 1.0000 | nan | nan | nan | nan | nan | nan | 1.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
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
| AnteilBaumbepflanzung | 3 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | 
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
| Overall | - | 0.8680 | 0.7686 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | 
| Overall weighted | - | 0.7703 | 0.7269 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | 
| Number of sentences  | - | - | - | 91 | 30 | 60 | 115 | 118 | 101 | 96 | 23 | 73 | 114 | 38 | 91 | 161 | 29 | 100 | 
| Planzeichen | 1987 | 0.9333 | 0.9266 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 20 | 9 | 9 | 22 | 19 | 31 | 33 | 2 | 22 | 25 | 8 | 22 | 45 | 1 | 19 | 
| WidmungUndZweckbestimmung | 1161 | 0.4449 | 0.4895 | 0.7778 | 0.0000 | 0.0000 | 0.9076 | 0.5730 | 0.5944 | 0.7500 | 0.0000 | 0.2903 | 0.2382 | 0.3043 | 0.3077 | 0.4107 | 1.0000 | 0.5202 | 
| Number of sentences  | - | - | - | 36 | 8 | 11 | 19 | 23 | 14 | 18 | 9 | 10 | 28 | 8 | 23 | 40 | 7 | 26 | 
| Flaechen | 791 | 0.4611 | 0.3566 | 0.9328 | 1.0000 | 0.0000 | 0.6415 | 0.4651 | 0.5758 | 0.0000 | 0.7273 | 1.0000 | 0.0000 | 0.6000 | 0.0000 | -0.0256 | 1.0000 | 0.0000 | 
| Number of sentences  | - | - | - | 19 | 1 | 6 | 9 | 8 | 11 | 20 | 4 | 8 | 11 | 5 | 14 | 15 | 6 | 13 | 
| VerkehrsflaecheID | 457 | 0.7961 | 0.8565 | 1.0000 | 0.0000 | 1.0000 | -0.0588 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 31 | 6 | 16 | 20 | 18 | 25 | 20 | 12 | 12 | 25 | 8 | 22 | 20 | 5 | 20 | 
| AnFluchtlinie | 393 | 0.9333 | 0.9038 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 36 | 6 | 10 | 19 | 31 | 21 | 18 | 9 | 9 | 25 | 10 | 24 | 26 | 5 | 21 | 
| AnordnungGaertnerischeAusgestaltung | 356 | 0.8816 | 0.8705 | 0.9434 | 1.0000 | 1.0000 | 0.6780 | 0.7748 | 1.0000 | 1.0000 | 0.7692 | 0.6250 | 0.8276 | 1.0000 | 0.9130 | 0.6929 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 17 | 5 | 9 | 8 | 14 | 11 | 21 | 2 | 19 | 10 | 3 | 30 | 23 | 2 | 33 | 
| GebaeudeHoeheMax | 333 | 0.7195 | 0.6682 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.7586 | 0.6207 | 0.6441 | 1.0000 | 0.4865 | 0.7368 | 0.0000 | 0.4444 | 0.1977 | 1.0000 | 0.9043 | 
| Number of sentences  | - | - | - | 22 | 4 | 5 | 21 | 21 | 17 | 18 | 3 | 12 | 27 | 2 | 16 | 24 | 8 | 16 | 
| Dachart | 303 | 0.8583 | 0.8365 | 0.8889 | 1.0000 | 0.5833 | 0.8889 | 0.9014 | 0.6554 | 0.8696 | 1.0000 | 1.0000 | 0.8224 | 1.0000 | 0.7333 | 0.7983 | 1.0000 | 0.7333 | 
| Number of sentences  | - | - | - | 2 | 1 | 4 | 3 | 0 | 6 | 2 | 0 | 1 | 12 | 1 | 3 | 0 | 0 | 10 | 
| WidmungInMehrerenEbenen | 294 | 0.7333 | 0.3556 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 
| Number of sentences  | - | - | - | 21 | 5 | 3 | 23 | 21 | 19 | 14 | 6 | 13 | 16 | 12 | 27 | 30 | 4 | 18 | 
| GebaeudeHoeheArt | 290 | 0.3423 | 0.2063 | 0.0000 | -0.2500 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.6000 | 1.0000 | 0.0000 | -0.2162 | 1.0000 | 0.0000 | 
| Number of sentences  | - | - | - | 32 | 4 | 6 | 26 | 23 | 22 | 16 | 6 | 11 | 18 | 13 | 22 | 27 | 5 | 14 | 
| VorkehrungBepflanzung | 282 | 0.9333 | 0.8898 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 9 | 1 | 10 | 8 | 15 | 13 | 15 | 0 | 5 | 13 | 4 | 9 | 5 | 0 | 16 | 
| ErrichtungGebaeude | 271 | 0.9333 | 0.8780 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 17 | 1 | 4 | 10 | 12 | 11 | 12 | 3 | 4 | 13 | 1 | 8 | 15 | 4 | 8 | 
| PlangebietAllgemein | 269 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 10 | 4 | 7 | 11 | 8 | 12 | 11 | 3 | 7 | 9 | 4 | 12 | 9 | 5 | 17 | 
| VonBebauungFreizuhalten | 255 | 0.8667 | 0.8140 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 
| Number of sentences  | - | - | - | 26 | 5 | 8 | 21 | 25 | 12 | 13 | 7 | 17 | 20 | 8 | 18 | 18 | 4 | 15 | 
| BegruenungDach | 247 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 17 | 4 | 3 | 22 | 16 | 20 | 14 | 6 | 9 | 18 | 12 | 26 | 27 | 4 | 18 | 
| AbschlussDachMaxBezugGebaeude | 235 | 0.6590 | 0.6569 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | -0.0769 | 1.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | -0.0385 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 15 | 4 | 6 | 13 | 11 | 16 | 10 | 3 | 5 | 14 | 6 | 14 | 18 | 1 | 10 | 
| GehsteigbreiteMin | 213 | 0.9282 | 0.8967 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | -0.0769 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 11 | 3 | 4 | 16 | 16 | 15 | 11 | 6 | 7 | 18 | 6 | 20 | 19 | 1 | 16 | 
| StrassenbreiteMin | 207 | 0.9280 | 0.8850 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | -0.0800 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 21 | 4 | 3 | 12 | 18 | 14 | 14 | 6 | 4 | 20 | 7 | 15 | 11 | 3 | 10 | 
| GebaeudeBautyp | 207 | 0.3458 | 0.4252 | 0.5882 | 0.5000 | 0.4000 | 0.6250 | 1.0000 | 0.4324 | 0.2553 | 0.0000 | -0.5000 | 0.1781 | 0.5882 | 0.1860 | 0.3889 | 0.0000 | 0.5455 | 
| Number of sentences  | - | - | - | 16 | 2 | 4 | 13 | 18 | 11 | 4 | 4 | 11 | 12 | 5 | 7 | 17 | 2 | 15 | 
| AufbautenZulaessig | 176 | 0.8000 | 0.7305 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 
| Number of sentences  | - | - | - | 13 | 5 | 4 | 14 | 11 | 12 | 13 | 4 | 7 | 23 | 6 | 12 | 14 | 3 | 9 | 
| UnterbrechungGeschlosseneBauweise | 158 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 12 | 4 | 6 | 10 | 11 | 8 | 9 | 2 | 4 | 18 | 5 | 12 | 15 | 4 | 8 | 
| DachneigungMax | 146 | 0.8152 | 0.8139 | 0.1429 | 1.0000 | 0.5714 | 1.0000 | 0.7442 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.7692 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 7 | 1 | 3 | 1 | 5 | 8 | 2 | 0 | 1 | 6 | 0 | 3 | 6 | 1 | 2 | 
| AnOeffentlichenVerkehrsflaechen | 143 | 0.7333 | 0.6522 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 3 | 1 | 1 | 1 | 2 | 12 | 6 | 0 | 3 | 14 | 0 | 0 | 0 | 0 | 1 | 
| BauweiseID | 123 | 0.6000 | 0.4318 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 
| Number of sentences  | - | - | - | 6 | 2 | 1 | 10 | 4 | 16 | 5 | 0 | 8 | 6 | 0 | 2 | 3 | 0 | 7 | 
| Bauklasse | 118 | 0.5859 | 0.6139 | 1.0000 | 1.0000 | 0.0000 | 0.1935 | 0.0000 | 0.8750 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 | 0.7200 | 
| Number of sentences  | - | - | - | 11 | 2 | 3 | 9 | 12 | 10 | 8 | 3 | 3 | 7 | 3 | 6 | 8 | 1 | 5 | 
| EinfriedungAusgestaltung | 117 | 0.7333 | 0.7033 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 6 | 0 | 3 | 10 | 11 | 17 | 6 | 2 | 5 | 10 | 4 | 12 | 6 | 2 | 9 | 
| DurchgangBreite | 113 | 0.8000 | 0.7573 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 
| Number of sentences  | - | - | - | 2 | 1 | 0 | 0 | 0 | 3 | 1 | 2 | 5 | 1 | 0 | 3 | 2 | 3 | 9 | 
| AusnahmeGaertnerischAuszugestaltende | 110 | 0.4704 | 0.2442 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4000 | 0.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 | -0.2857 | -0.0588 | 
| Number of sentences  | - | - | - | 8 | 1 | 3 | 9 | 12 | 8 | 3 | 5 | 4 | 13 | 3 | 10 | 8 | 1 | 5 | 
| StrassenbreiteMax | 105 | 0.8667 | 0.7742 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 6 | 0 | 1 | 10 | 6 | 12 | 3 | 2 | 2 | 8 | 5 | 6 | 6 | 2 | 9 | 
| DurchgangHoehe | 105 | 0.8667 | 0.7821 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 12 | 1 | 1 | 9 | 7 | 8 | 5 | 1 | 1 | 7 | 1 | 6 | 2 | 1 | 2 | 
| UnterirdischeBaulichkeiten | 99 | 0.4727 | 0.3916 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 0.7576 | 0.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.3333 | 0.0000 | 1.0000 | 0.0000 | 
| Number of sentences  | - | - | - | 6 | 0 | 1 | 1 | 4 | 4 | 6 | 0 | 5 | 0 | 1 | 8 | 0 | 0 | 4 | 
| Struktureinheit | 97 | 0.6057 | 0.3979 | 0.7143 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 0.6000 | 0.5714 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 0.2000 | 
| Number of sentences  | - | - | - | 7 | 1 | 9 | 2 | 5 | 4 | 12 | 0 | 2 | 8 | 14 | 6 | 3 | 0 | 13 | 
| VolumenUndUmbaubarerRaum | 94 | 0.9333 | 0.8605 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 5 | 2 | 2 | 5 | 2 | 4 | 5 | 2 | 2 | 6 | 1 | 1 | 4 | 1 | 1 | 
| EinfriedungHoeheGesamt | 90 | 0.9333 | 0.9535 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 9 | 2 | 1 | 2 | 4 | 5 | 8 | 1 | 4 | 6 | 4 | 4 | 2 | 2 | 2 | 
| Stockwerk | 85 | 0.3206 | 0.3085 | 0.6087 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.2000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 
| Number of sentences  | - | - | - | 7 | 0 | 1 | 4 | 7 | 5 | 3 | 3 | 3 | 7 | 3 | 6 | 5 | 1 | 6 | 
| DachflaecheMin | 84 | 0.7176 | 0.6287 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | -0.2353 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 
| Number of sentences  | - | - | - | 9 | 0 | 0 | 6 | 7 | 8 | 4 | 1 | 0 | 4 | 0 | 2 | 6 | 2 | 1 | 
| EinfriedungLage | 77 | 0.6667 | 0.5000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 9 | 1 | 1 | 0 | 4 | 5 | 4 | 0 | 0 | 2 | 0 | 2 | 1 | 0 | 2 | 
| AnlageZumEinstellenVorhanden | 77 | 0.6000 | 0.4194 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 
| Number of sentences  | - | - | - | 2 | 0 | 1 | 1 | 4 | 1 | 2 | 0 | 2 | 1 | 0 | 0 | 1 | 1 | 1 | 
| VorstehendeBauelementeAusladungMax | 69 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 8 | 1 | 1 | 2 | 7 | 4 | 6 | 3 | 5 | 8 | 3 | 4 | 6 | 2 | 4 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen | 68 | 0.8000 | 0.7500 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 0.0000 | 
| Number of sentences  | - | - | - | 1 | 0 | 2 | 3 | 4 | 1 | 3 | 1 | 1 | 2 | 2 | 6 | 3 | 2 | 4 | 
| EinfriedungZulaessig | 66 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 4 | 1 | 1 | 3 | 4 | 2 | 3 | 1 | 3 | 4 | 1 | 4 | 9 | 3 | 9 | 
| VerbotWohnung | 61 | 0.9333 | 0.9808 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 1 | 1 | 2 | 8 | 3 | 3 | 2 | 3 | 7 | 1 | 4 | 2 | 1 | 2 | 
| StrassenbreiteVonBis | 59 | 0.9333 | 0.9500 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 
| Number of sentences  | - | - | - | 5 | 3 | 0 | 6 | 4 | 2 | 5 | 0 | 0 | 2 | 1 | 3 | 3 | 1 | 3 | 
| AnordnungGaertnerischeAusgestaltungProzentual | 55 | 0.8000 | 0.7368 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 4 | 1 | 4 | 3 | 2 | 4 | 0 | 2 | 1 | 8 | 1 | 2 | 5 | 0 | 2 | 
| OeffentlicheVerkehrsflaecheBreiteMin | 54 | 0.9143 | 0.8132 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.7143 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 5 | 1 | 0 | 3 | 4 | 6 | 3 | 3 | 2 | 4 | 2 | 3 | 3 | 1 | 3 | 
| VorbautenVerbot | 48 | 0.9333 | 0.9070 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 
| HoehenlageGrundflaeche | 47 | 0.9333 | 0.8000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 2 | 0 | 1 | 2 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 
| VorbautenBeschraenkung | 41 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 1 | 3 | 2 | 3 | 1 | 1 | 3 | 0 | 0 | 8 | 4 | 6 | 
| AnteilDachbegruenung | 41 | 0.7333 | 0.5294 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 1 | 2 | 3 | 2 | 2 | 3 | 4 | 1 | 0 | 2 | 2 | 2 | 4 | 1 | 4 | 
| EinleitungNiederschlagswaesser | 39 | 0.9333 | 0.9697 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 
| AbschlussDachMaxBezugGelaende | 37 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 4 | 1 | 2 | 1 | 3 | 4 | 1 | 3 | 1 | 3 | 2 | 1 | 5 | 0 | 0 | 
| VerbotStaffelung | 34 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 3 | 6 | 4 | 0 | 1 | 0 | 2 | 2 | 0 | 2 | 1 | 3 | 
| ArkadeHoehe | 32 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 3 | 1 | 0 | 2 | 1 | 1 | 3 | 0 | 0 | 1 | 1 | 0 | 5 | 1 | 1 | 
| StellplatzImNiveauZulaessig | 31 | 0.9697 | 0.8864 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.5455 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 5 | 0 | 3 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 7 | 
| MaxAnzahlGeschosseOberirdisch | 27 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 3 | 
| GebaeudeHoeheMin | 27 | 0.9600 | 0.7429 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 
| GaragengebaeudeAusfuehrung | 26 | 0.9333 | 0.6667 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben | 26 | 0.8667 | 0.5000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 3 | 1 | 1 | 0 | 
| StellplatzregulativUmfangMaximumRelativ | 25 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 2 | 4 | 0 | 1 | 
| Massengliederung | 24 | 0.8000 | 0.5000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 
| StellplatzregulativUmfangMaximumAbsolut | 23 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 8 | 0 | 1 | 
| StellplatzMax | 23 | 0.9333 | 0.4667 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 
| OberflaecheBestimmungP | 23 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 2 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 1 | 1 | 0 | 0 | 
| InSchutzzone | 22 | 0.8667 | 0.7000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 4 | 0 | 0 | 2 | 1 | 2 | 1 | 1 | 0 | 3 | 0 | 0 | 1 | 1 | 1 | 
| AnzahlGebaeudeMax | 21 | 0.9333 | 0.9412 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 1 | 2 | 1 | 1 | 1 | 0 | 1 | 8 | 0 | 1 | 2 | 0 | 0 | 
| FBOKMinimumWohnungen | 20 | 0.8000 | 0.4444 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 2 | 0 | 
| TechnischeAufbautenHoeheMax | 18 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 1 | 0 | 2 | 1 | 1 | 2 | 0 | 0 | 0 | 1 | 1 | 4 | 0 | 0 | 1 | 
| StellplatzregulativUmfangMinimumRelativ | 18 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 
| GebaeudeEinschraenkungP | 17 | 0.9333 | 0.6667 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 0 | 4 | 0 | 2 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 
| DurchfahrtHoehe | 17 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 2 | 1 | 0 | 0 | 2 | 1 | 0 | 0 | 2 | 0 | 2 | 2 | 0 | 0 | 
| DachneigungMin | 17 | 0.9333 | 0.8333 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 2 | 0 | 0 | 1 | 3 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 2 | 0 | 0 | 
| Kleinhaeuser | 16 | 0.7333 | 0.5000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 1 | 1 | 0 | 3 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 1 | 
| BauklasseVIHoeheMax | 16 | 0.8000 | 0.6429 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 2 | 2 | 0 | 2 | 0 | 0 | 1 | 1 | 0 | 2 | 0 | 0 | 
| MaxAnzahlDachgeschosse | 14 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 1 | 
| BauklasseVIHoeheMin | 14 | 0.9333 | 0.7273 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| StellplatzverpflichtungArt | 12 | 1.0000 | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 3 | 0 | 1 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 
| VerbotBueroGeschaeftsgebaeude | 11 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau | 11 | 1.0000 | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 
| AusnahmeVonWohnungenUnzulaessig | 10 | 0.9333 | 0.5000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 1 | 0 | 
| DurchfahrtBreite | 9 | 0.9333 | 0.8333 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 
| Geschaeftsstrassen | 8 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| VerbotUnterirdischeBauwerkeUeberBaufluchtlinie | 7 | 1.0000 | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 
| MindestraumhoeheEG | 7 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 
| HochhausZulaessigGemaessBB | 7 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| StellplatzregulativVorhanden | 6 | 1.0000 | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 
| MaxAnzahlGeschosseOberirdischOhneDachgeschoss | 6 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| VerbotAufenthaltsraum | 4 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| EinfriedungHoeheSockel | 4 | 1.0000 | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 
| Einbautrasse | 4 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| GelaendeneigungMin | 3 | 1.0000 | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 
| AnteilBaumbepflanzung | 3 | 0.9333 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 
| Number of sentences  | - | - | - | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| ZulaessigeGeschossanzahlEinkaufszentrum | 2 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| VerbotStellplaetzeUndParkgebaeude | 2 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| ArkadeLaenge | 2 | 1.0000 | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| MaxHoeheWohngebaeude | 1 | 1.0000 | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Number of sentences  | - | - | - | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 
| LaubengangHoehe | 1 | 1.0000 | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 


