# Annotator statistics - Types
This statistics is calculated without the sentences with a segmentation error.  
Post-processed attributes were converted back to their version at the time of annotation.  

For complexity reasons, agreement is only calculated for cases, where the attribute occurs in gold exactly once, and where the annotator gave at least one annotation for the attribute. In case the annotator labeled the attribute within the same sentence multiple times, the most beneficial type annotation is taken into account, i.e. if the annotator labeled both gold and non-gold types, then we regard the gold one.

## Per type summary

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| condition |  |  |  |  |  |  | 
| micro | 8272 | 6409 | 454 | 1863 | 0.934 | 0.775 | 
| content |  |  |  |  |  |  | 
| micro | 8140 | 7025 | 577 | 1115 | 0.924 | 0.863 | 
| conditionException |  |  |  |  |  |  | 
| micro | 310 | 102 | 22 | 208 | 0.823 | 0.329 | 
| contentException |  |  |  |  |  |  | 
| micro | 12 | 5 | 48 | 7 | 0.094 | 0.417 | 



## Per attribute summary

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| Planzeichen |  |  |  |  |  |  | 
| micro | 2932 | 2876 | 14 | 56 | 0.995 | 0.981 | 
| WidmungUndZweckbestimmung |  |  |  |  |  |  | 
| micro | 1520 | 457 | 155 | 1063 | 0.747 | 0.301 | 
| Flaechen |  |  |  |  |  |  | 
| micro | 570 | 522 | 42 | 48 | 0.926 | 0.916 | 
| VerkehrsflaecheID |  |  |  |  |  |  | 
| micro | 322 | 298 | 12 | 24 | 0.961 | 0.925 | 
| AnFluchtlinie |  |  |  |  |  |  | 
| micro | 548 | 521 | 2 | 27 | 0.996 | 0.951 | 
| AnordnungGaertnerischeAusgestaltung |  |  |  |  |  |  | 
| micro | 584 | 536 | 27 | 48 | 0.952 | 0.918 | 
| GebaeudeHoeheMax |  |  |  |  |  |  | 
| micro | 430 | 365 | 56 | 65 | 0.867 | 0.849 | 
| Dachart |  |  |  |  |  |  | 
| micro | 454 | 408 | 29 | 46 | 0.934 | 0.899 | 
| WidmungInMehrerenEbenen |  |  |  |  |  |  | 
| micro | 116 | 82 | 13 | 34 | 0.863 | 0.707 | 
| GebaeudeHoeheArt |  |  |  |  |  |  | 
| micro | 484 | 220 | 250 | 264 | 0.468 | 0.455 | 
| VorkehrungBepflanzung |  |  |  |  |  |  | 
| micro | 534 | 504 | 1 | 30 | 0.998 | 0.944 | 
| ErrichtungGebaeude |  |  |  |  |  |  | 
| micro | 426 | 270 | 1 | 156 | 0.996 | 0.634 | 
| PlangebietAllgemein |  |  |  |  |  |  | 
| micro | 376 | 305 | 0 | 71 | 1.000 | 0.811 | 
| VonBebauungFreizuhalten |  |  |  |  |  |  | 
| micro | 288 | 265 | 3 | 23 | 0.989 | 0.920 | 
| BegruenungDach |  |  |  |  |  |  | 
| micro | 440 | 434 | 0 | 6 | 1.000 | 0.986 | 
| AbschlussDachMaxBezugGebaeude |  |  |  |  |  |  | 
| micro | 438 | 423 | 11 | 15 | 0.975 | 0.966 | 
| GehsteigbreiteMin |  |  |  |  |  |  | 
| micro | 310 | 299 | 2 | 11 | 0.993 | 0.965 | 
| StrassenbreiteMin |  |  |  |  |  |  | 
| micro | 354 | 341 | 3 | 13 | 0.991 | 0.963 | 
| GebaeudeBautyp |  |  |  |  |  |  | 
| micro | 344 | 242 | 92 | 102 | 0.725 | 0.703 | 
| AufbautenZulaessig |  |  |  |  |  |  | 
| micro | 304 | 287 | 4 | 17 | 0.986 | 0.944 | 
| UnterbrechungGeschlosseneBauweise |  |  |  |  |  |  | 
| micro | 308 | 304 | 0 | 4 | 1.000 | 0.987 | 
| DachneigungMax |  |  |  |  |  |  | 
| micro | 264 | 240 | 18 | 24 | 0.930 | 0.909 | 
| AnOeffentlichenVerkehrsflaechen |  |  |  |  |  |  | 
| micro | 108 | 93 | 5 | 15 | 0.949 | 0.861 | 
| BauweiseID |  |  |  |  |  |  | 
| micro | 184 | 91 | 10 | 93 | 0.901 | 0.495 | 
| Bauklasse |  |  |  |  |  |  | 
| micro | 222 | 134 | 19 | 88 | 0.876 | 0.604 | 
| EinfriedungAusgestaltung |  |  |  |  |  |  | 
| micro | 230 | 158 | 29 | 72 | 0.845 | 0.687 | 
| DurchgangBreite |  |  |  |  |  |  | 
| micro | 216 | 207 | 4 | 9 | 0.981 | 0.958 | 
| AusnahmeGaertnerischAuszugestaltende |  |  |  |  |  |  | 
| micro | 204 | 72 | 33 | 132 | 0.686 | 0.353 | 
| StrassenbreiteMax |  |  |  |  |  |  | 
| micro | 196 | 186 | 5 | 10 | 0.974 | 0.949 | 
| DurchgangHoehe |  |  |  |  |  |  | 
| micro | 160 | 155 | 3 | 5 | 0.981 | 0.969 | 
| UnterirdischeBaulichkeiten |  |  |  |  |  |  | 
| micro | 170 | 89 | 44 | 81 | 0.669 | 0.524 | 
| Struktureinheit |  |  |  |  |  |  | 
| micro | 162 | 114 | 20 | 48 | 0.851 | 0.704 | 
| VolumenUndUmbaubarerRaum |  |  |  |  |  |  | 
| micro | 176 | 171 | 3 | 5 | 0.983 | 0.972 | 
| EinfriedungHoeheGesamt |  |  |  |  |  |  | 
| micro | 96 | 65 | 25 | 31 | 0.722 | 0.677 | 
| Stockwerk |  |  |  |  |  |  | 
| micro | 130 | 75 | 42 | 55 | 0.641 | 0.577 | 
| DachflaecheMin |  |  |  |  |  |  | 
| micro | 142 | 119 | 6 | 23 | 0.952 | 0.838 | 
| EinfriedungLage |  |  |  |  |  |  | 
| micro | 110 | 97 | 6 | 13 | 0.942 | 0.882 | 
| AnlageZumEinstellenVorhanden |  |  |  |  |  |  | 
| micro | 88 | 48 | 16 | 40 | 0.750 | 0.545 | 
| VorstehendeBauelementeAusladungMax |  |  |  |  |  |  | 
| micro | 36 | 35 | 0 | 1 | 1.000 | 0.972 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen |  |  |  |  |  |  | 
| micro | 132 | 124 | 4 | 8 | 0.969 | 0.939 | 
| EinfriedungZulaessig |  |  |  |  |  |  | 
| micro | 96 | 71 | 0 | 25 | 1.000 | 0.740 | 
| VerbotWohnung |  |  |  |  |  |  | 
| micro | 122 | 108 | 1 | 14 | 0.991 | 0.885 | 
| StrassenbreiteVonBis |  |  |  |  |  |  | 
| micro | 98 | 86 | 1 | 12 | 0.989 | 0.878 | 
| AnordnungGaertnerischeAusgestaltungProzentual |  |  |  |  |  |  | 
| micro | 100 | 82 | 4 | 18 | 0.953 | 0.820 | 
| OeffentlicheVerkehrsflaecheBreiteMin |  |  |  |  |  |  | 
| micro | 102 | 79 | 5 | 23 | 0.940 | 0.775 | 
| VorbautenVerbot |  |  |  |  |  |  | 
| micro | 92 | 88 | 1 | 4 | 0.989 | 0.957 | 
| HoehenlageGrundflaeche |  |  |  |  |  |  | 
| micro | 12 | 9 | 1 | 3 | 0.900 | 0.750 | 
| VorbautenBeschraenkung |  |  |  |  |  |  | 
| micro | 20 | 18 | 2 | 2 | 0.900 | 0.900 | 
| AnteilDachbegruenung |  |  |  |  |  |  | 
| micro | 70 | 64 | 5 | 6 | 0.928 | 0.914 | 
| EinleitungNiederschlagswaesser |  |  |  |  |  |  | 
| micro | 72 | 69 | 1 | 3 | 0.986 | 0.958 | 
| AbschlussDachMaxBezugGelaende |  |  |  |  |  |  | 
| micro | 28 | 8 | 0 | 20 | 1.000 | 0.286 | 
| VerbotStaffelung |  |  |  |  |  |  | 
| micro | 64 | 63 | 0 | 1 | 1.000 | 0.984 | 
| ArkadeHoehe |  |  |  |  |  |  | 
| micro | 54 | 52 | 0 | 2 | 1.000 | 0.963 | 
| StellplatzImNiveauZulaessig |  |  |  |  |  |  | 
| micro | 54 | 37 | 3 | 17 | 0.925 | 0.685 | 
| MaxAnzahlGeschosseOberirdisch |  |  |  |  |  |  | 
| micro | 38 | 30 | 8 | 8 | 0.789 | 0.789 | 
| GebaeudeHoeheMin |  |  |  |  |  |  | 
| micro | 16 | 12 | 3 | 4 | 0.800 | 0.750 | 
| GaragengebaeudeAusfuehrung |  |  |  |  |  |  | 
| micro | 18 | 8 | 4 | 10 | 0.667 | 0.444 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben |  |  |  |  |  |  | 
| micro | 14 | 10 | 2 | 4 | 0.833 | 0.714 | 
| StellplatzregulativUmfangMaximumRelativ |  |  |  |  |  |  | 
| micro | 22 | 22 | 0 | 0 | 1.000 | 1.000 | 
| Massengliederung |  |  |  |  |  |  | 
| micro | 34 | 18 | 6 | 16 | 0.750 | 0.529 | 
| StellplatzregulativUmfangMaximumAbsolut |  |  |  |  |  |  | 
| micro | 16 | 12 | 0 | 4 | 1.000 | 0.750 | 
| StellplatzMax |  |  |  |  |  |  | 
| micro | 30 | 25 | 5 | 5 | 0.833 | 0.833 | 
| OberflaecheBestimmungP |  |  |  |  |  |  | 
| micro | 22 | 13 | 0 | 9 | 1.000 | 0.591 | 
| InSchutzzone |  |  |  |  |  |  | 
| micro | 36 | 21 | 2 | 15 | 0.913 | 0.583 | 
| AnzahlGebaeudeMax |  |  |  |  |  |  | 
| micro | 38 | 35 | 1 | 3 | 0.972 | 0.921 | 
| FBOKMinimumWohnungen |  |  |  |  |  |  | 
| micro | 40 | 30 | 7 | 10 | 0.811 | 0.750 | 
| TechnischeAufbautenHoeheMax |  |  |  |  |  |  | 
| micro | 22 | 17 | 0 | 5 | 1.000 | 0.773 | 
| StellplatzregulativUmfangMinimumRelativ |  |  |  |  |  |  | 
| micro | 34 | 29 | 0 | 5 | 1.000 | 0.853 | 
| GebaeudeEinschraenkungP |  |  |  |  |  |  | 
| micro | 10 | 5 | 1 | 5 | 0.833 | 0.500 | 
| DurchfahrtHoehe |  |  |  |  |  |  | 
| micro | 22 | 22 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMin |  |  |  |  |  |  | 
| micro | 26 | 24 | 1 | 2 | 0.960 | 0.923 | 
| Kleinhaeuser |  |  |  |  |  |  | 
| micro | 26 | 9 | 15 | 17 | 0.375 | 0.346 | 
| BauklasseVIHoeheMax |  |  |  |  |  |  | 
| micro | 32 | 22 | 6 | 10 | 0.786 | 0.688 | 
| MaxAnzahlDachgeschosse |  |  |  |  |  |  | 
| micro | 22 | 21 | 0 | 1 | 1.000 | 0.955 | 
| BauklasseVIHoeheMin |  |  |  |  |  |  | 
| micro | 28 | 18 | 4 | 10 | 0.818 | 0.643 | 
| StellplatzverpflichtungArt |  |  |  |  |  |  | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotBueroGeschaeftsgebaeude |  |  |  |  |  |  | 
| micro | 20 | 19 | 0 | 1 | 1.000 | 0.950 | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau |  |  |  |  |  |  | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeVonWohnungenUnzulaessig |  |  |  |  |  |  | 
| micro | 10 | 4 | 1 | 6 | 0.800 | 0.400 | 
| DurchfahrtBreite |  |  |  |  |  |  | 
| micro | 12 | 11 | 1 | 1 | 0.917 | 0.917 | 
| Geschaeftsstrassen |  |  |  |  |  |  | 
| micro | 12 | 10 | 0 | 2 | 1.000 | 0.833 | 
| VerbotUnterirdischeBauwerkeUeberBaufluchtlinie |  |  |  |  |  |  | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MindestraumhoeheEG |  |  |  |  |  |  | 
| micro | 14 | 6 | 0 | 8 | 1.000 | 0.429 | 
| HochhausZulaessigGemaessBB |  |  |  |  |  |  | 
| micro | 8 | 7 | 0 | 1 | 1.000 | 0.875 | 
| StellplatzregulativVorhanden |  |  |  |  |  |  | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxAnzahlGeschosseOberirdischOhneDachgeschoss |  |  |  |  |  |  | 
| micro | 6 | 2 | 0 | 4 | 1.000 | 0.333 | 
| VerbotAufenthaltsraum |  |  |  |  |  |  | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungHoeheSockel |  |  |  |  |  |  | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| Einbautrasse |  |  |  |  |  |  | 
| micro | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| GelaendeneigungMin |  |  |  |  |  |  | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AnteilBaumbepflanzung |  |  |  |  |  |  | 
| micro | 2 | 1 | 1 | 1 | 0.500 | 0.500 | 
| ZulaessigeGeschossanzahlEinkaufszentrum |  |  |  |  |  |  | 
| micro | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| VerbotStellplaetzeUndParkgebaeude |  |  |  |  |  |  | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeLaenge |  |  |  |  |  |  | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxHoeheWohngebaeude |  |  |  |  |  |  | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| LaubengangHoehe |  |  |  |  |  |  | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 



## Per type details
### Annotator 01

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| condition | 1400 | 1092 | 16 | 308 | 0.986 | 0.780 | 
| content | 1325 | 1223 | 86 | 102 | 0.934 | 0.923 | 
| conditionException | 69 | 5 | 0 | 64 | 1.000 | 0.072 | 
| contentException | 1 | 0 | 3 | 1 | 0.000 | 0.000 | 
| micro | 2795 | 2320 | 105 | 475 | 0.957 | 0.830 | 
| macro |  |  |  |  | 0.730 | 0.444 | 


### Annotator 02

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| condition | 1379 | 1114 | 96 | 265 | 0.921 | 0.808 | 
| content | 1353 | 1148 | 75 | 205 | 0.939 | 0.848 | 
| conditionException | 50 | 20 | 7 | 30 | 0.741 | 0.400 | 
| contentException | 2 | 0 | 11 | 2 | 0.000 | 0.000 | 
| micro | 2784 | 2282 | 189 | 502 | 0.924 | 0.820 | 
| macro |  |  |  |  | 0.650 | 0.514 | 


### Annotator 03

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| condition | 1303 | 1068 | 111 | 235 | 0.906 | 0.820 | 
| content | 1295 | 1126 | 48 | 169 | 0.959 | 0.869 | 
| conditionException | 35 | 3 | 1 | 32 | 0.750 | 0.086 | 
| contentException | 1 | 1 | 15 | 0 | 0.062 | 1.000 | 
| micro | 2634 | 2198 | 175 | 436 | 0.926 | 0.834 | 
| macro |  |  |  |  | 0.669 | 0.694 | 


### Annotator 04

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| condition | 1459 | 1061 | 77 | 398 | 0.932 | 0.727 | 
| content | 1424 | 1155 | 173 | 269 | 0.870 | 0.811 | 
| conditionException | 48 | 4 | 0 | 44 | 1.000 | 0.083 | 
| contentException | 3 | 1 | 15 | 2 | 0.062 | 0.333 | 
| micro | 2934 | 2221 | 265 | 713 | 0.893 | 0.757 | 
| macro |  |  |  |  | 0.716 | 0.489 | 


### Annotator 05

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| condition | 1381 | 1077 | 104 | 304 | 0.912 | 0.780 | 
| content | 1414 | 1188 | 70 | 226 | 0.944 | 0.840 | 
| conditionException | 56 | 37 | 14 | 19 | 0.725 | 0.661 | 
| contentException | 4 | 2 | 4 | 2 | 0.333 | 0.500 | 
| micro | 2855 | 2304 | 192 | 551 | 0.923 | 0.807 | 
| macro |  |  |  |  | 0.729 | 0.695 | 


### Annotator 06

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| condition | 1350 | 997 | 50 | 353 | 0.952 | 0.739 | 
| content | 1329 | 1185 | 125 | 144 | 0.905 | 0.892 | 
| conditionException | 52 | 33 | 0 | 19 | 1.000 | 0.635 | 
| contentException | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2732 | 2216 | 175 | 516 | 0.927 | 0.811 | 
| macro |  |  |  |  | 0.964 | 0.816 | 



## Per attribute details
### Annotator 01

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| Planzeichen | 496 | 479 | 4 | 17 | 0.992 | 0.966 | 
| WidmungUndZweckbestimmung | 245 | 66 | 19 | 179 | 0.776 | 0.269 | 
| Flaechen | 98 | 96 | 2 | 2 | 0.980 | 0.980 | 
| VerkehrsflaecheID | 50 | 41 | 3 | 9 | 0.932 | 0.820 | 
| AnFluchtlinie | 97 | 91 | 0 | 6 | 1.000 | 0.938 | 
| AnordnungGaertnerischeAusgestaltung | 113 | 106 | 2 | 7 | 0.981 | 0.938 | 
| GebaeudeHoeheMax | 57 | 50 | 6 | 7 | 0.893 | 0.877 | 
| Dachart | 78 | 71 | 2 | 7 | 0.973 | 0.910 | 
| WidmungInMehrerenEbenen | 15 | 12 | 0 | 3 | 1.000 | 0.800 | 
| GebaeudeHoeheArt | 79 | 73 | 3 | 6 | 0.961 | 0.924 | 
| VorkehrungBepflanzung | 97 | 93 | 0 | 4 | 1.000 | 0.959 | 
| ErrichtungGebaeude | 65 | 44 | 0 | 21 | 1.000 | 0.677 | 
| PlangebietAllgemein | 67 | 54 | 0 | 13 | 1.000 | 0.806 | 
| VonBebauungFreizuhalten | 44 | 43 | 0 | 1 | 1.000 | 0.977 | 
| BegruenungDach | 85 | 85 | 0 | 0 | 1.000 | 1.000 | 
| AbschlussDachMaxBezugGebaeude | 63 | 62 | 0 | 1 | 1.000 | 0.984 | 
| GehsteigbreiteMin | 51 | 50 | 0 | 1 | 1.000 | 0.980 | 
| StrassenbreiteMin | 53 | 51 | 0 | 2 | 1.000 | 0.962 | 
| GebaeudeBautyp | 62 | 42 | 18 | 20 | 0.700 | 0.677 | 
| AufbautenZulaessig | 57 | 56 | 0 | 1 | 1.000 | 0.982 | 
| UnterbrechungGeschlosseneBauweise | 49 | 49 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMax | 44 | 40 | 4 | 4 | 0.909 | 0.909 | 
| AnOeffentlichenVerkehrsflaechen | 17 | 17 | 0 | 0 | 1.000 | 1.000 | 
| BauweiseID | 24 | 6 | 2 | 18 | 0.750 | 0.250 | 
| Bauklasse | 34 | 19 | 5 | 15 | 0.792 | 0.559 | 
| EinfriedungAusgestaltung | 43 | 33 | 5 | 10 | 0.868 | 0.767 | 
| DurchgangBreite | 32 | 32 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeGaertnerischAuszugestaltende | 45 | 0 | 3 | 45 | 0.000 | 0.000 | 
| StrassenbreiteMax | 34 | 33 | 0 | 1 | 1.000 | 0.971 | 
| DurchgangHoehe | 24 | 24 | 0 | 0 | 1.000 | 1.000 | 
| UnterirdischeBaulichkeiten | 40 | 24 | 7 | 16 | 0.774 | 0.600 | 
| Struktureinheit | 17 | 14 | 2 | 3 | 0.875 | 0.824 | 
| VolumenUndUmbaubarerRaum | 25 | 24 | 1 | 1 | 0.960 | 0.960 | 
| EinfriedungHoeheGesamt | 17 | 16 | 1 | 1 | 0.941 | 0.941 | 
| Stockwerk | 20 | 18 | 2 | 2 | 0.900 | 0.900 | 
| DachflaecheMin | 20 | 19 | 0 | 1 | 1.000 | 0.950 | 
| EinfriedungLage | 23 | 22 | 0 | 1 | 1.000 | 0.957 | 
| AnlageZumEinstellenVorhanden | 22 | 13 | 2 | 9 | 0.867 | 0.591 | 
| VorstehendeBauelementeAusladungMax | 9 | 9 | 0 | 0 | 1.000 | 1.000 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen | 19 | 19 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungZulaessig | 14 | 11 | 0 | 3 | 1.000 | 0.786 | 
| VerbotWohnung | 15 | 13 | 0 | 2 | 1.000 | 0.867 | 
| StrassenbreiteVonBis | 14 | 12 | 0 | 2 | 1.000 | 0.857 | 
| AnordnungGaertnerischeAusgestaltungProzentual | 21 | 19 | 1 | 2 | 0.950 | 0.905 | 
| OeffentlicheVerkehrsflaecheBreiteMin | 18 | 15 | 0 | 3 | 1.000 | 0.833 | 
| VorbautenVerbot | 15 | 14 | 0 | 1 | 1.000 | 0.933 | 
| HoehenlageGrundflaeche | 3 | 1 | 1 | 2 | 0.500 | 0.333 | 
| VorbautenBeschraenkung | 8 | 7 | 1 | 1 | 0.875 | 0.875 | 
| AnteilDachbegruenung | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| EinleitungNiederschlagswaesser | 13 | 12 | 0 | 1 | 1.000 | 0.923 | 
| AbschlussDachMaxBezugGelaende | 6 | 2 | 0 | 4 | 1.000 | 0.333 | 
| VerbotStaffelung | 11 | 11 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeHoehe | 11 | 11 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzImNiveauZulaessig | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 
| MaxAnzahlGeschosseOberirdisch | 6 | 2 | 4 | 4 | 0.333 | 0.333 | 
| GebaeudeHoeheMin | 1 | 0 | 1 | 1 | 0.000 | 0.000 | 
| GaragengebaeudeAusfuehrung | 3 | 2 | 1 | 1 | 0.667 | 0.667 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben | 5 | 3 | 1 | 2 | 0.750 | 0.600 | 
| StellplatzregulativUmfangMaximumRelativ | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| Massengliederung | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| StellplatzregulativUmfangMaximumAbsolut | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzMax | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| OberflaecheBestimmungP | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| InSchutzzone | 8 | 6 | 0 | 2 | 1.000 | 0.750 | 
| AnzahlGebaeudeMax | 8 | 8 | 0 | 0 | 1.000 | 1.000 | 
| FBOKMinimumWohnungen | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| TechnischeAufbautenHoeheMax | 7 | 5 | 0 | 2 | 1.000 | 0.714 | 
| StellplatzregulativUmfangMinimumRelativ | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| GebaeudeEinschraenkungP | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| DurchfahrtHoehe | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMin | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| Kleinhaeuser | 6 | 4 | 2 | 2 | 0.667 | 0.667 | 
| BauklasseVIHoeheMax | 4 | 2 | 0 | 2 | 1.000 | 0.500 | 
| MaxAnzahlDachgeschosse | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| BauklasseVIHoeheMin | 2 | 0 | 0 | 2 | 1.000 | 0.000 | 
| StellplatzverpflichtungArt | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotBueroGeschaeftsgebaeude | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeVonWohnungenUnzulaessig | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| DurchfahrtBreite | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| Geschaeftsstrassen | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| VerbotUnterirdischeBauwerkeUeberBaufluchtlinie | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MindestraumhoeheEG | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| HochhausZulaessigGemaessBB | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativVorhanden | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxAnzahlGeschosseOberirdischOhneDachgeschoss | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotAufenthaltsraum | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungHoeheSockel | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| Einbautrasse | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| GelaendeneigungMin | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AnteilBaumbepflanzung | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| ZulaessigeGeschossanzahlEinkaufszentrum | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| VerbotStellplaetzeUndParkgebaeude | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeLaenge | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxHoeheWohngebaeude | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| LaubengangHoehe | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2795 | 2320 | 105 | 475 | 0.957 | 0.830 | 
| macro |  |  |  |  | 0.933 | 0.844 | 


### Annotator 02

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| Planzeichen | 447 | 439 | 1 | 8 | 0.998 | 0.982 | 
| WidmungUndZweckbestimmung | 242 | 88 | 26 | 154 | 0.772 | 0.364 | 
| Flaechen | 89 | 84 | 3 | 5 | 0.966 | 0.944 | 
| VerkehrsflaecheID | 67 | 63 | 2 | 4 | 0.969 | 0.940 | 
| AnFluchtlinie | 102 | 100 | 0 | 2 | 1.000 | 0.980 | 
| AnordnungGaertnerischeAusgestaltung | 97 | 93 | 3 | 4 | 0.969 | 0.959 | 
| GebaeudeHoeheMax | 72 | 63 | 9 | 9 | 0.875 | 0.875 | 
| Dachart | 76 | 69 | 4 | 7 | 0.945 | 0.908 | 
| WidmungInMehrerenEbenen | 14 | 11 | 0 | 3 | 1.000 | 0.786 | 
| GebaeudeHoeheArt | 77 | 12 | 62 | 65 | 0.162 | 0.156 | 
| VorkehrungBepflanzung | 100 | 93 | 0 | 7 | 1.000 | 0.930 | 
| ErrichtungGebaeude | 70 | 45 | 0 | 25 | 1.000 | 0.643 | 
| PlangebietAllgemein | 66 | 57 | 0 | 9 | 1.000 | 0.864 | 
| VonBebauungFreizuhalten | 50 | 45 | 0 | 5 | 1.000 | 0.900 | 
| BegruenungDach | 76 | 75 | 0 | 1 | 1.000 | 0.987 | 
| AbschlussDachMaxBezugGebaeude | 67 | 65 | 2 | 2 | 0.970 | 0.970 | 
| GehsteigbreiteMin | 51 | 51 | 0 | 0 | 1.000 | 1.000 | 
| StrassenbreiteMin | 54 | 53 | 0 | 1 | 1.000 | 0.981 | 
| GebaeudeBautyp | 61 | 45 | 15 | 16 | 0.750 | 0.738 | 
| AufbautenZulaessig | 49 | 44 | 2 | 5 | 0.957 | 0.898 | 
| UnterbrechungGeschlosseneBauweise | 50 | 50 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMax | 37 | 33 | 3 | 4 | 0.917 | 0.892 | 
| AnOeffentlichenVerkehrsflaechen | 21 | 19 | 0 | 2 | 1.000 | 0.905 | 
| BauweiseID | 46 | 30 | 1 | 16 | 0.968 | 0.652 | 
| Bauklasse | 47 | 37 | 0 | 10 | 1.000 | 0.787 | 
| EinfriedungAusgestaltung | 38 | 30 | 5 | 8 | 0.857 | 0.789 | 
| DurchgangBreite | 37 | 34 | 2 | 3 | 0.944 | 0.919 | 
| AusnahmeGaertnerischAuszugestaltende | 31 | 11 | 9 | 20 | 0.550 | 0.355 | 
| StrassenbreiteMax | 30 | 30 | 0 | 0 | 1.000 | 1.000 | 
| DurchgangHoehe | 25 | 24 | 1 | 1 | 0.960 | 0.960 | 
| UnterirdischeBaulichkeiten | 30 | 21 | 8 | 9 | 0.724 | 0.700 | 
| Struktureinheit | 37 | 26 | 2 | 11 | 0.929 | 0.703 | 
| VolumenUndUmbaubarerRaum | 25 | 24 | 1 | 1 | 0.960 | 0.960 | 
| EinfriedungHoeheGesamt | 20 | 13 | 5 | 7 | 0.722 | 0.650 | 
| Stockwerk | 32 | 26 | 2 | 6 | 0.929 | 0.812 | 
| DachflaecheMin | 26 | 21 | 0 | 5 | 1.000 | 0.808 | 
| EinfriedungLage | 24 | 22 | 1 | 2 | 0.957 | 0.917 | 
| AnlageZumEinstellenVorhanden | 19 | 14 | 4 | 5 | 0.778 | 0.737 | 
| VorstehendeBauelementeAusladungMax | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen | 27 | 26 | 0 | 1 | 1.000 | 0.963 | 
| EinfriedungZulaessig | 12 | 7 | 0 | 5 | 1.000 | 0.583 | 
| VerbotWohnung | 13 | 13 | 0 | 0 | 1.000 | 1.000 | 
| StrassenbreiteVonBis | 12 | 12 | 0 | 0 | 1.000 | 1.000 | 
| AnordnungGaertnerischeAusgestaltungProzentual | 19 | 12 | 0 | 7 | 1.000 | 0.632 | 
| OeffentlicheVerkehrsflaecheBreiteMin | 16 | 11 | 0 | 5 | 1.000 | 0.688 | 
| VorbautenVerbot | 19 | 19 | 0 | 0 | 1.000 | 1.000 | 
| HoehenlageGrundflaeche | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| VorbautenBeschraenkung | 2 | 1 | 1 | 1 | 0.500 | 0.500 | 
| AnteilDachbegruenung | 10 | 9 | 0 | 1 | 1.000 | 0.900 | 
| EinleitungNiederschlagswaesser | 10 | 8 | 1 | 2 | 0.889 | 0.800 | 
| AbschlussDachMaxBezugGelaende | 6 | 1 | 0 | 5 | 1.000 | 0.167 | 
| VerbotStaffelung | 13 | 13 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeHoehe | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzImNiveauZulaessig | 10 | 7 | 0 | 3 | 1.000 | 0.700 | 
| MaxAnzahlGeschosseOberirdisch | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| GebaeudeHoeheMin | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| GaragengebaeudeAusfuehrung | 6 | 2 | 2 | 4 | 0.500 | 0.333 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben | 4 | 3 | 0 | 1 | 1.000 | 0.750 | 
| StellplatzregulativUmfangMaximumRelativ | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| Massengliederung | 1 | 0 | 1 | 1 | 0.000 | 0.000 | 
| StellplatzregulativUmfangMaximumAbsolut | 3 | 2 | 0 | 1 | 1.000 | 0.667 | 
| StellplatzMax | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| OberflaecheBestimmungP | 6 | 4 | 0 | 2 | 1.000 | 0.667 | 
| InSchutzzone | 7 | 4 | 0 | 3 | 1.000 | 0.571 | 
| AnzahlGebaeudeMax | 8 | 8 | 0 | 0 | 1.000 | 1.000 | 
| FBOKMinimumWohnungen | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| TechnischeAufbautenHoeheMax | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| StellplatzregulativUmfangMinimumRelativ | 4 | 3 | 0 | 1 | 1.000 | 0.750 | 
| GebaeudeEinschraenkungP | 1 | 0 | 1 | 1 | 0.000 | 0.000 | 
| DurchfahrtHoehe | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMin | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| Kleinhaeuser | 4 | 0 | 4 | 4 | 0.000 | 0.000 | 
| BauklasseVIHoeheMax | 3 | 0 | 3 | 3 | 0.000 | 0.000 | 
| MaxAnzahlDachgeschosse | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| BauklasseVIHoeheMin | 3 | 0 | 3 | 3 | 0.000 | 0.000 | 
| StellplatzverpflichtungArt | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotBueroGeschaeftsgebaeude | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeVonWohnungenUnzulaessig | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| DurchfahrtBreite | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| Geschaeftsstrassen | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| VerbotUnterirdischeBauwerkeUeberBaufluchtlinie | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MindestraumhoeheEG | 5 | 1 | 0 | 4 | 1.000 | 0.200 | 
| HochhausZulaessigGemaessBB | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativVorhanden | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxAnzahlGeschosseOberirdischOhneDachgeschoss | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| VerbotAufenthaltsraum | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungHoeheSockel | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| Einbautrasse | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| GelaendeneigungMin | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AnteilBaumbepflanzung | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| ZulaessigeGeschossanzahlEinkaufszentrum | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| VerbotStellplaetzeUndParkgebaeude | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeLaenge | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxHoeheWohngebaeude | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| LaubengangHoehe | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2784 | 2282 | 189 | 502 | 0.924 | 0.820 | 
| macro |  |  |  |  | 0.900 | 0.799 | 


### Annotator 03

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| Planzeichen | 442 | 437 | 2 | 5 | 0.995 | 0.989 | 
| WidmungUndZweckbestimmung | 250 | 76 | 28 | 174 | 0.731 | 0.304 | 
| Flaechen | 83 | 81 | 1 | 2 | 0.988 | 0.976 | 
| VerkehrsflaecheID | 45 | 42 | 2 | 3 | 0.955 | 0.933 | 
| AnFluchtlinie | 89 | 87 | 0 | 2 | 1.000 | 0.978 | 
| AnordnungGaertnerischeAusgestaltung | 91 | 89 | 1 | 2 | 0.989 | 0.978 | 
| GebaeudeHoeheMax | 59 | 50 | 9 | 9 | 0.847 | 0.847 | 
| Dachart | 68 | 63 | 3 | 5 | 0.955 | 0.926 | 
| WidmungInMehrerenEbenen | 28 | 13 | 10 | 15 | 0.565 | 0.464 | 
| GebaeudeHoeheArt | 80 | 11 | 69 | 69 | 0.138 | 0.138 | 
| VorkehrungBepflanzung | 82 | 82 | 0 | 0 | 1.000 | 1.000 | 
| ErrichtungGebaeude | 56 | 40 | 0 | 16 | 1.000 | 0.714 | 
| PlangebietAllgemein | 56 | 44 | 0 | 12 | 1.000 | 0.786 | 
| VonBebauungFreizuhalten | 43 | 41 | 0 | 2 | 1.000 | 0.953 | 
| BegruenungDach | 65 | 63 | 0 | 2 | 1.000 | 0.969 | 
| AbschlussDachMaxBezugGebaeude | 80 | 78 | 2 | 2 | 0.975 | 0.975 | 
| GehsteigbreiteMin | 56 | 55 | 1 | 1 | 0.982 | 0.982 | 
| StrassenbreiteMin | 62 | 61 | 1 | 1 | 0.984 | 0.984 | 
| GebaeudeBautyp | 61 | 52 | 9 | 9 | 0.852 | 0.852 | 
| AufbautenZulaessig | 43 | 41 | 0 | 2 | 1.000 | 0.953 | 
| UnterbrechungGeschlosseneBauweise | 59 | 59 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMax | 48 | 46 | 1 | 2 | 0.979 | 0.958 | 
| AnOeffentlichenVerkehrsflaechen | 24 | 20 | 0 | 4 | 1.000 | 0.833 | 
| BauweiseID | 33 | 26 | 1 | 7 | 0.963 | 0.788 | 
| Bauklasse | 39 | 26 | 1 | 13 | 0.963 | 0.667 | 
| EinfriedungAusgestaltung | 34 | 26 | 2 | 8 | 0.929 | 0.765 | 
| DurchgangBreite | 43 | 43 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeGaertnerischAuszugestaltende | 21 | 2 | 7 | 19 | 0.222 | 0.095 | 
| StrassenbreiteMax | 36 | 36 | 0 | 0 | 1.000 | 1.000 | 
| DurchgangHoehe | 31 | 30 | 1 | 1 | 0.968 | 0.968 | 
| UnterirdischeBaulichkeiten | 27 | 20 | 4 | 7 | 0.833 | 0.741 | 
| Struktureinheit | 16 | 13 | 1 | 3 | 0.929 | 0.812 | 
| VolumenUndUmbaubarerRaum | 34 | 34 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungHoeheGesamt | 15 | 11 | 4 | 4 | 0.733 | 0.733 | 
| Stockwerk | 22 | 20 | 1 | 2 | 0.952 | 0.909 | 
| DachflaecheMin | 24 | 21 | 1 | 3 | 0.955 | 0.875 | 
| EinfriedungLage | 15 | 15 | 0 | 0 | 1.000 | 1.000 | 
| AnlageZumEinstellenVorhanden | 10 | 9 | 1 | 1 | 0.900 | 0.900 | 
| VorstehendeBauelementeAusladungMax | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen | 22 | 20 | 0 | 2 | 1.000 | 0.909 | 
| EinfriedungZulaessig | 13 | 11 | 0 | 2 | 1.000 | 0.846 | 
| VerbotWohnung | 15 | 14 | 0 | 1 | 1.000 | 0.933 | 
| StrassenbreiteVonBis | 16 | 16 | 0 | 0 | 1.000 | 1.000 | 
| AnordnungGaertnerischeAusgestaltungProzentual | 13 | 11 | 2 | 2 | 0.846 | 0.846 | 
| OeffentlicheVerkehrsflaecheBreiteMin | 16 | 16 | 0 | 0 | 1.000 | 1.000 | 
| VorbautenVerbot | 16 | 16 | 0 | 0 | 1.000 | 1.000 | 
| HoehenlageGrundflaeche | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| VorbautenBeschraenkung | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| AnteilDachbegruenung | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| EinleitungNiederschlagswaesser | 12 | 12 | 0 | 0 | 1.000 | 1.000 | 
| AbschlussDachMaxBezugGelaende | 3 | 2 | 0 | 1 | 1.000 | 0.667 | 
| VerbotStaffelung | 11 | 11 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeHoehe | 8 | 8 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzImNiveauZulaessig | 9 | 4 | 0 | 5 | 1.000 | 0.444 | 
| MaxAnzahlGeschosseOberirdisch | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| GebaeudeHoeheMin | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| GaragengebaeudeAusfuehrung | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben | 1 | 0 | 1 | 1 | 0.000 | 0.000 | 
| StellplatzregulativUmfangMaximumRelativ | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| Massengliederung | 5 | 0 | 5 | 5 | 0.000 | 0.000 | 
| StellplatzregulativUmfangMaximumAbsolut | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzMax | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| OberflaecheBestimmungP | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| InSchutzzone | 7 | 6 | 0 | 1 | 1.000 | 0.857 | 
| AnzahlGebaeudeMax | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| FBOKMinimumWohnungen | 11 | 10 | 1 | 1 | 0.909 | 0.909 | 
| TechnischeAufbautenHoeheMax | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativUmfangMinimumRelativ | 8 | 8 | 0 | 0 | 1.000 | 1.000 | 
| GebaeudeEinschraenkungP | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| DurchfahrtHoehe | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMin | 8 | 8 | 0 | 0 | 1.000 | 1.000 | 
| Kleinhaeuser | 4 | 2 | 1 | 2 | 0.667 | 0.500 | 
| BauklasseVIHoeheMax | 11 | 10 | 1 | 1 | 0.909 | 0.909 | 
| MaxAnzahlDachgeschosse | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| BauklasseVIHoeheMin | 11 | 9 | 1 | 2 | 0.900 | 0.818 | 
| StellplatzverpflichtungArt | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotBueroGeschaeftsgebaeude | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeVonWohnungenUnzulaessig | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| DurchfahrtBreite | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| Geschaeftsstrassen | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| VerbotUnterirdischeBauwerkeUeberBaufluchtlinie | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MindestraumhoeheEG | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| HochhausZulaessigGemaessBB | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativVorhanden | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxAnzahlGeschosseOberirdischOhneDachgeschoss | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotAufenthaltsraum | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungHoeheSockel | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| Einbautrasse | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| GelaendeneigungMin | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AnteilBaumbepflanzung | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| ZulaessigeGeschossanzahlEinkaufszentrum | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| VerbotStellplaetzeUndParkgebaeude | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeLaenge | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxHoeheWohngebaeude | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| LaubengangHoehe | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2634 | 2198 | 175 | 436 | 0.926 | 0.834 | 
| macro |  |  |  |  | 0.932 | 0.872 | 


### Annotator 04

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| Planzeichen | 541 | 532 | 4 | 9 | 0.993 | 0.983 | 
| WidmungUndZweckbestimmung | 263 | 80 | 36 | 183 | 0.690 | 0.304 | 
| Flaechen | 107 | 88 | 16 | 19 | 0.846 | 0.822 | 
| VerkehrsflaecheID | 62 | 59 | 2 | 3 | 0.967 | 0.952 | 
| AnFluchtlinie | 91 | 84 | 2 | 7 | 0.977 | 0.923 | 
| AnordnungGaertnerischeAusgestaltung | 94 | 80 | 8 | 14 | 0.909 | 0.851 | 
| GebaeudeHoeheMax | 72 | 53 | 12 | 19 | 0.815 | 0.736 | 
| Dachart | 84 | 75 | 7 | 9 | 0.915 | 0.893 | 
| WidmungInMehrerenEbenen | 22 | 18 | 1 | 4 | 0.947 | 0.818 | 
| GebaeudeHoeheArt | 73 | 31 | 36 | 42 | 0.463 | 0.425 | 
| VorkehrungBepflanzung | 82 | 72 | 0 | 10 | 1.000 | 0.878 | 
| ErrichtungGebaeude | 90 | 42 | 1 | 48 | 0.977 | 0.467 | 
| PlangebietAllgemein | 70 | 58 | 0 | 12 | 1.000 | 0.829 | 
| VonBebauungFreizuhalten | 49 | 42 | 1 | 7 | 0.977 | 0.857 | 
| BegruenungDach | 63 | 63 | 0 | 0 | 1.000 | 1.000 | 
| AbschlussDachMaxBezugGebaeude | 68 | 62 | 4 | 6 | 0.939 | 0.912 | 
| GehsteigbreiteMin | 53 | 49 | 1 | 4 | 0.980 | 0.925 | 
| StrassenbreiteMin | 56 | 52 | 2 | 4 | 0.963 | 0.929 | 
| GebaeudeBautyp | 58 | 35 | 17 | 23 | 0.673 | 0.603 | 
| AufbautenZulaessig | 42 | 38 | 1 | 4 | 0.974 | 0.905 | 
| UnterbrechungGeschlosseneBauweise | 59 | 57 | 0 | 2 | 1.000 | 0.966 | 
| DachneigungMax | 52 | 48 | 4 | 4 | 0.923 | 0.923 | 
| AnOeffentlichenVerkehrsflaechen | 21 | 17 | 4 | 4 | 0.810 | 0.810 | 
| BauweiseID | 34 | 17 | 4 | 17 | 0.810 | 0.500 | 
| Bauklasse | 36 | 10 | 6 | 26 | 0.625 | 0.278 | 
| EinfriedungAusgestaltung | 43 | 22 | 7 | 21 | 0.759 | 0.512 | 
| DurchgangBreite | 30 | 26 | 1 | 4 | 0.963 | 0.867 | 
| AusnahmeGaertnerischAuszugestaltende | 35 | 4 | 8 | 31 | 0.333 | 0.114 | 
| StrassenbreiteMax | 31 | 23 | 5 | 8 | 0.821 | 0.742 | 
| DurchgangHoehe | 21 | 20 | 0 | 1 | 1.000 | 0.952 | 
| UnterirdischeBaulichkeiten | 21 | 5 | 12 | 16 | 0.294 | 0.238 | 
| Struktureinheit | 21 | 12 | 1 | 9 | 0.923 | 0.571 | 
| VolumenUndUmbaubarerRaum | 33 | 32 | 0 | 1 | 1.000 | 0.970 | 
| EinfriedungHoeheGesamt | 22 | 10 | 9 | 12 | 0.526 | 0.455 | 
| Stockwerk | 24 | 0 | 19 | 24 | 0.000 | 0.000 | 
| DachflaecheMin | 23 | 15 | 4 | 8 | 0.789 | 0.652 | 
| EinfriedungLage | 20 | 15 | 2 | 5 | 0.882 | 0.750 | 
| AnlageZumEinstellenVorhanden | 13 | 3 | 5 | 10 | 0.375 | 0.231 | 
| VorstehendeBauelementeAusladungMax | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen | 24 | 22 | 1 | 2 | 0.957 | 0.917 | 
| EinfriedungZulaessig | 20 | 12 | 0 | 8 | 1.000 | 0.600 | 
| VerbotWohnung | 26 | 19 | 1 | 7 | 0.950 | 0.731 | 
| StrassenbreiteVonBis | 20 | 14 | 0 | 6 | 1.000 | 0.700 | 
| AnordnungGaertnerischeAusgestaltungProzentual | 15 | 13 | 0 | 2 | 1.000 | 0.867 | 
| OeffentlicheVerkehrsflaecheBreiteMin | 25 | 18 | 2 | 7 | 0.900 | 0.720 | 
| VorbautenVerbot | 13 | 10 | 1 | 3 | 0.909 | 0.769 | 
| HoehenlageGrundflaeche | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| VorbautenBeschraenkung | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| AnteilDachbegruenung | 18 | 17 | 1 | 1 | 0.944 | 0.944 | 
| EinleitungNiederschlagswaesser | 14 | 14 | 0 | 0 | 1.000 | 1.000 | 
| AbschlussDachMaxBezugGelaende | 4 | 1 | 0 | 3 | 1.000 | 0.250 | 
| VerbotStaffelung | 12 | 12 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeHoehe | 6 | 5 | 0 | 1 | 1.000 | 0.833 | 
| StellplatzImNiveauZulaessig | 10 | 8 | 2 | 2 | 0.800 | 0.800 | 
| MaxAnzahlGeschosseOberirdisch | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| GebaeudeHoeheMin | 4 | 3 | 1 | 1 | 0.750 | 0.750 | 
| GaragengebaeudeAusfuehrung | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativUmfangMaximumRelativ | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| Massengliederung | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativUmfangMaximumAbsolut | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| StellplatzMax | 10 | 10 | 0 | 0 | 1.000 | 1.000 | 
| OberflaecheBestimmungP | 3 | 0 | 0 | 3 | 1.000 | 0.000 | 
| InSchutzzone | 6 | 2 | 2 | 4 | 0.500 | 0.333 | 
| AnzahlGebaeudeMax | 7 | 5 | 1 | 2 | 0.833 | 0.714 | 
| FBOKMinimumWohnungen | 13 | 9 | 3 | 4 | 0.750 | 0.692 | 
| TechnischeAufbautenHoeheMax | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativUmfangMinimumRelativ | 5 | 3 | 0 | 2 | 1.000 | 0.600 | 
| GebaeudeEinschraenkungP | 4 | 2 | 0 | 2 | 1.000 | 0.500 | 
| DurchfahrtHoehe | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMin | 6 | 5 | 1 | 1 | 0.833 | 0.833 | 
| Kleinhaeuser | 5 | 0 | 4 | 5 | 0.000 | 0.000 | 
| BauklasseVIHoeheMax | 9 | 8 | 1 | 1 | 0.889 | 0.889 | 
| MaxAnzahlDachgeschosse | 6 | 5 | 0 | 1 | 1.000 | 0.833 | 
| BauklasseVIHoeheMin | 8 | 7 | 0 | 1 | 1.000 | 0.875 | 
| StellplatzverpflichtungArt | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotBueroGeschaeftsgebaeude | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeVonWohnungenUnzulaessig | 3 | 0 | 1 | 3 | 0.000 | 0.000 | 
| DurchfahrtBreite | 4 | 3 | 1 | 1 | 0.750 | 0.750 | 
| Geschaeftsstrassen | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| VerbotUnterirdischeBauwerkeUeberBaufluchtlinie | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MindestraumhoeheEG | 5 | 1 | 0 | 4 | 1.000 | 0.200 | 
| HochhausZulaessigGemaessBB | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| StellplatzregulativVorhanden | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxAnzahlGeschosseOberirdischOhneDachgeschoss | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| VerbotAufenthaltsraum | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungHoeheSockel | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| Einbautrasse | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| GelaendeneigungMin | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AnteilBaumbepflanzung | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| ZulaessigeGeschossanzahlEinkaufszentrum | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotStellplaetzeUndParkgebaeude | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeLaenge | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxHoeheWohngebaeude | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| LaubengangHoehe | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2934 | 2221 | 265 | 713 | 0.893 | 0.757 | 
| macro |  |  |  |  | 0.881 | 0.745 | 


### Annotator 05

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| Planzeichen | 523 | 514 | 0 | 9 | 1.000 | 0.983 | 
| WidmungUndZweckbestimmung | 257 | 87 | 19 | 170 | 0.821 | 0.339 | 
| Flaechen | 104 | 96 | 8 | 8 | 0.923 | 0.923 | 
| VerkehrsflaecheID | 48 | 46 | 1 | 2 | 0.979 | 0.958 | 
| AnFluchtlinie | 86 | 82 | 0 | 4 | 1.000 | 0.953 | 
| AnordnungGaertnerischeAusgestaltung | 96 | 83 | 7 | 13 | 0.922 | 0.865 | 
| GebaeudeHoeheMax | 72 | 62 | 9 | 10 | 0.873 | 0.861 | 
| Dachart | 72 | 65 | 5 | 7 | 0.929 | 0.903 | 
| WidmungInMehrerenEbenen | 16 | 13 | 2 | 3 | 0.867 | 0.812 | 
| GebaeudeHoeheArt | 90 | 12 | 77 | 78 | 0.135 | 0.133 | 
| VorkehrungBepflanzung | 92 | 88 | 1 | 4 | 0.989 | 0.957 | 
| ErrichtungGebaeude | 79 | 54 | 0 | 25 | 1.000 | 0.684 | 
| PlangebietAllgemein | 58 | 48 | 0 | 10 | 1.000 | 0.828 | 
| VonBebauungFreizuhalten | 50 | 47 | 0 | 3 | 1.000 | 0.940 | 
| BegruenungDach | 71 | 69 | 0 | 2 | 1.000 | 0.972 | 
| AbschlussDachMaxBezugGebaeude | 85 | 83 | 2 | 2 | 0.976 | 0.976 | 
| GehsteigbreiteMin | 52 | 52 | 0 | 0 | 1.000 | 1.000 | 
| StrassenbreiteMin | 65 | 64 | 0 | 1 | 1.000 | 0.985 | 
| GebaeudeBautyp | 51 | 43 | 8 | 8 | 0.843 | 0.843 | 
| AufbautenZulaessig | 54 | 54 | 0 | 0 | 1.000 | 1.000 | 
| UnterbrechungGeschlosseneBauweise | 47 | 47 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMax | 41 | 38 | 2 | 3 | 0.950 | 0.927 | 
| AnOeffentlichenVerkehrsflaechen | 11 | 9 | 0 | 2 | 1.000 | 0.818 | 
| BauweiseID | 28 | 1 | 2 | 27 | 0.333 | 0.036 | 
| Bauklasse | 39 | 22 | 6 | 17 | 0.786 | 0.564 | 
| EinfriedungAusgestaltung | 42 | 27 | 3 | 15 | 0.900 | 0.643 | 
| DurchgangBreite | 34 | 34 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeGaertnerischAuszugestaltende | 38 | 26 | 2 | 12 | 0.929 | 0.684 | 
| StrassenbreiteMax | 32 | 32 | 0 | 0 | 1.000 | 1.000 | 
| DurchgangHoehe | 33 | 32 | 1 | 1 | 0.970 | 0.970 | 
| UnterirdischeBaulichkeiten | 27 | 11 | 4 | 16 | 0.733 | 0.407 | 
| Struktureinheit | 27 | 19 | 5 | 8 | 0.792 | 0.704 | 
| VolumenUndUmbaubarerRaum | 32 | 32 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungHoeheGesamt | 15 | 10 | 4 | 5 | 0.714 | 0.667 | 
| Stockwerk | 14 | 8 | 5 | 6 | 0.615 | 0.571 | 
| DachflaecheMin | 25 | 20 | 1 | 5 | 0.952 | 0.800 | 
| EinfriedungLage | 16 | 13 | 1 | 3 | 0.929 | 0.812 | 
| AnlageZumEinstellenVorhanden | 10 | 3 | 1 | 7 | 0.750 | 0.300 | 
| VorstehendeBauelementeAusladungMax | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen | 18 | 18 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungZulaessig | 18 | 13 | 0 | 5 | 1.000 | 0.722 | 
| VerbotWohnung | 27 | 24 | 0 | 3 | 1.000 | 0.889 | 
| StrassenbreiteVonBis | 17 | 15 | 0 | 2 | 1.000 | 0.882 | 
| AnordnungGaertnerischeAusgestaltungProzentual | 17 | 16 | 0 | 1 | 1.000 | 0.941 | 
| OeffentlicheVerkehrsflaecheBreiteMin | 20 | 12 | 3 | 8 | 0.800 | 0.600 | 
| VorbautenVerbot | 16 | 16 | 0 | 0 | 1.000 | 1.000 | 
| HoehenlageGrundflaeche | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| VorbautenBeschraenkung | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| AnteilDachbegruenung | 16 | 15 | 1 | 1 | 0.938 | 0.938 | 
| EinleitungNiederschlagswaesser | 13 | 13 | 0 | 0 | 1.000 | 1.000 | 
| AbschlussDachMaxBezugGelaende | 6 | 1 | 0 | 5 | 1.000 | 0.167 | 
| VerbotStaffelung | 12 | 11 | 0 | 1 | 1.000 | 0.917 | 
| ArkadeHoehe | 12 | 11 | 0 | 1 | 1.000 | 0.917 | 
| StellplatzImNiveauZulaessig | 10 | 8 | 1 | 2 | 0.889 | 0.800 | 
| MaxAnzahlGeschosseOberirdisch | 9 | 9 | 0 | 0 | 1.000 | 1.000 | 
| GebaeudeHoeheMin | 7 | 6 | 0 | 1 | 1.000 | 0.857 | 
| GaragengebaeudeAusfuehrung | 3 | 1 | 1 | 2 | 0.500 | 0.333 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativUmfangMaximumRelativ | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| Massengliederung | 11 | 7 | 0 | 4 | 1.000 | 0.636 | 
| StellplatzregulativUmfangMaximumAbsolut | 4 | 2 | 0 | 2 | 1.000 | 0.500 | 
| StellplatzMax | 11 | 6 | 5 | 5 | 0.545 | 0.545 | 
| OberflaecheBestimmungP | 3 | 2 | 0 | 1 | 1.000 | 0.667 | 
| InSchutzzone | 5 | 2 | 0 | 3 | 1.000 | 0.400 | 
| AnzahlGebaeudeMax | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| FBOKMinimumWohnungen | 5 | 2 | 2 | 3 | 0.500 | 0.400 | 
| TechnischeAufbautenHoeheMax | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativUmfangMinimumRelativ | 5 | 3 | 0 | 2 | 1.000 | 0.600 | 
| GebaeudeEinschraenkungP | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| DurchfahrtHoehe | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMin | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| Kleinhaeuser | 4 | 2 | 2 | 2 | 0.500 | 0.500 | 
| BauklasseVIHoeheMax | 4 | 1 | 1 | 3 | 0.500 | 0.250 | 
| MaxAnzahlDachgeschosse | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| BauklasseVIHoeheMin | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| StellplatzverpflichtungArt | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotBueroGeschaeftsgebaeude | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeVonWohnungenUnzulaessig | 4 | 2 | 0 | 2 | 1.000 | 0.500 | 
| DurchfahrtBreite | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| Geschaeftsstrassen | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| VerbotUnterirdischeBauwerkeUeberBaufluchtlinie | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MindestraumhoeheEG | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| HochhausZulaessigGemaessBB | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativVorhanden | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxAnzahlGeschosseOberirdischOhneDachgeschoss | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| VerbotAufenthaltsraum | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungHoeheSockel | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| Einbautrasse | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| GelaendeneigungMin | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AnteilBaumbepflanzung | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| ZulaessigeGeschossanzahlEinkaufszentrum | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotStellplaetzeUndParkgebaeude | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeLaenge | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxHoeheWohngebaeude | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| LaubengangHoehe | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2855 | 2304 | 192 | 551 | 0.923 | 0.807 | 
| macro |  |  |  |  | 0.925 | 0.803 | 


### Annotator 06

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| Planzeichen | 483 | 475 | 3 | 8 | 0.994 | 0.983 | 
| WidmungUndZweckbestimmung | 263 | 60 | 27 | 203 | 0.690 | 0.228 | 
| Flaechen | 89 | 77 | 12 | 12 | 0.865 | 0.865 | 
| VerkehrsflaecheID | 50 | 47 | 2 | 3 | 0.959 | 0.940 | 
| AnFluchtlinie | 83 | 77 | 0 | 6 | 1.000 | 0.928 | 
| AnordnungGaertnerischeAusgestaltung | 93 | 85 | 6 | 8 | 0.934 | 0.914 | 
| GebaeudeHoeheMax | 98 | 87 | 11 | 11 | 0.888 | 0.888 | 
| Dachart | 76 | 65 | 8 | 11 | 0.890 | 0.855 | 
| WidmungInMehrerenEbenen | 21 | 15 | 0 | 6 | 1.000 | 0.714 | 
| GebaeudeHoeheArt | 85 | 81 | 3 | 4 | 0.964 | 0.953 | 
| VorkehrungBepflanzung | 81 | 76 | 0 | 5 | 1.000 | 0.938 | 
| ErrichtungGebaeude | 66 | 45 | 0 | 21 | 1.000 | 0.682 | 
| PlangebietAllgemein | 59 | 44 | 0 | 15 | 1.000 | 0.746 | 
| VonBebauungFreizuhalten | 52 | 47 | 2 | 5 | 0.959 | 0.904 | 
| BegruenungDach | 80 | 79 | 0 | 1 | 1.000 | 0.988 | 
| AbschlussDachMaxBezugGebaeude | 75 | 73 | 1 | 2 | 0.986 | 0.973 | 
| GehsteigbreiteMin | 47 | 42 | 0 | 5 | 1.000 | 0.894 | 
| StrassenbreiteMin | 64 | 60 | 0 | 4 | 1.000 | 0.938 | 
| GebaeudeBautyp | 51 | 25 | 25 | 26 | 0.500 | 0.490 | 
| AufbautenZulaessig | 59 | 54 | 1 | 5 | 0.982 | 0.915 | 
| UnterbrechungGeschlosseneBauweise | 44 | 42 | 0 | 2 | 1.000 | 0.955 | 
| DachneigungMax | 42 | 35 | 4 | 7 | 0.897 | 0.833 | 
| AnOeffentlichenVerkehrsflaechen | 14 | 11 | 1 | 3 | 0.917 | 0.786 | 
| BauweiseID | 19 | 11 | 0 | 8 | 1.000 | 0.579 | 
| Bauklasse | 27 | 20 | 1 | 7 | 0.952 | 0.741 | 
| EinfriedungAusgestaltung | 30 | 20 | 7 | 10 | 0.741 | 0.667 | 
| DurchgangBreite | 40 | 38 | 1 | 2 | 0.974 | 0.950 | 
| AusnahmeGaertnerischAuszugestaltende | 34 | 29 | 4 | 5 | 0.879 | 0.853 | 
| StrassenbreiteMax | 33 | 32 | 0 | 1 | 1.000 | 0.970 | 
| DurchgangHoehe | 26 | 25 | 0 | 1 | 1.000 | 0.962 | 
| UnterirdischeBaulichkeiten | 25 | 8 | 9 | 17 | 0.471 | 0.320 | 
| Struktureinheit | 44 | 30 | 9 | 14 | 0.769 | 0.682 | 
| VolumenUndUmbaubarerRaum | 27 | 25 | 1 | 2 | 0.962 | 0.926 | 
| EinfriedungHoeheGesamt | 7 | 5 | 2 | 2 | 0.714 | 0.714 | 
| Stockwerk | 18 | 3 | 13 | 15 | 0.188 | 0.167 | 
| DachflaecheMin | 24 | 23 | 0 | 1 | 1.000 | 0.958 | 
| EinfriedungLage | 12 | 10 | 2 | 2 | 0.833 | 0.833 | 
| AnlageZumEinstellenVorhanden | 14 | 6 | 3 | 8 | 0.667 | 0.429 | 
| VorstehendeBauelementeAusladungMax | 9 | 8 | 0 | 1 | 1.000 | 0.889 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen | 22 | 19 | 3 | 3 | 0.864 | 0.864 | 
| EinfriedungZulaessig | 19 | 17 | 0 | 2 | 1.000 | 0.895 | 
| VerbotWohnung | 26 | 25 | 0 | 1 | 1.000 | 0.962 | 
| StrassenbreiteVonBis | 19 | 17 | 1 | 2 | 0.944 | 0.895 | 
| AnordnungGaertnerischeAusgestaltungProzentual | 15 | 11 | 1 | 4 | 0.917 | 0.733 | 
| OeffentlicheVerkehrsflaecheBreiteMin | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 
| VorbautenVerbot | 13 | 13 | 0 | 0 | 1.000 | 1.000 | 
| HoehenlageGrundflaeche | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| VorbautenBeschraenkung | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| AnteilDachbegruenung | 15 | 12 | 3 | 3 | 0.800 | 0.800 | 
| EinleitungNiederschlagswaesser | 10 | 10 | 0 | 0 | 1.000 | 1.000 | 
| AbschlussDachMaxBezugGelaende | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| VerbotStaffelung | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeHoehe | 10 | 10 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzImNiveauZulaessig | 8 | 3 | 0 | 5 | 1.000 | 0.375 | 
| MaxAnzahlGeschosseOberirdisch | 12 | 8 | 4 | 4 | 0.667 | 0.667 | 
| GebaeudeHoeheMin | 4 | 3 | 1 | 1 | 0.750 | 0.750 | 
| GaragengebaeudeAusfuehrung | 4 | 2 | 0 | 2 | 1.000 | 0.500 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativUmfangMaximumRelativ | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| Massengliederung | 8 | 3 | 0 | 5 | 1.000 | 0.375 | 
| StellplatzregulativUmfangMaximumAbsolut | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzMax | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| OberflaecheBestimmungP | 4 | 3 | 0 | 1 | 1.000 | 0.750 | 
| InSchutzzone | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| AnzahlGebaeudeMax | 4 | 3 | 0 | 1 | 1.000 | 0.750 | 
| FBOKMinimumWohnungen | 4 | 2 | 1 | 2 | 0.667 | 0.500 | 
| TechnischeAufbautenHoeheMax | 5 | 3 | 0 | 2 | 1.000 | 0.600 | 
| StellplatzregulativUmfangMinimumRelativ | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| GebaeudeEinschraenkungP | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| DurchfahrtHoehe | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMin | 3 | 2 | 0 | 1 | 1.000 | 0.667 | 
| Kleinhaeuser | 3 | 1 | 2 | 2 | 0.333 | 0.333 | 
| BauklasseVIHoeheMax | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| MaxAnzahlDachgeschosse | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| BauklasseVIHoeheMin | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzverpflichtungArt | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotBueroGeschaeftsgebaeude | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeVonWohnungenUnzulaessig | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| DurchfahrtBreite | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| Geschaeftsstrassen | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotUnterirdischeBauwerkeUeberBaufluchtlinie | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MindestraumhoeheEG | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| HochhausZulaessigGemaessBB | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativVorhanden | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxAnzahlGeschosseOberirdischOhneDachgeschoss | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotAufenthaltsraum | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungHoeheSockel | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| Einbautrasse | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| GelaendeneigungMin | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AnteilBaumbepflanzung | 1 | 0 | 1 | 1 | 0.000 | 0.000 | 
| ZulaessigeGeschossanzahlEinkaufszentrum | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotStellplaetzeUndParkgebaeude | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeLaenge | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxHoeheWohngebaeude | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| LaubengangHoehe | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2732 | 2216 | 175 | 516 | 0.927 | 0.811 | 
| macro |  |  |  |  | 0.922 | 0.828 | 



## Full details
### Annotator 01

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| Planzeichen | 496 |  |  |  |  |  | 
| condition | 490 | 477 | 4 | 13 | 0.992 | 0.973 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 6 | 2 | 0 | 4 | 1.000 | 0.333 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 496 | 479 | 4 | 17 | 0.992 | 0.966 | 
| WidmungUndZweckbestimmung | 245 |  |  |  |  |  | 
| condition | 204 | 34 | 1 | 170 | 0.971 | 0.167 | 
| content | 37 | 31 | 18 | 6 | 0.633 | 0.838 | 
| conditionException | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| contentException | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| micro | 245 | 66 | 19 | 179 | 0.776 | 0.269 | 
| Flaechen | 98 |  |  |  |  |  | 
| condition | 23 | 21 | 0 | 2 | 1.000 | 0.913 | 
| content | 75 | 75 | 2 | 0 | 0.974 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 98 | 96 | 2 | 2 | 0.980 | 0.980 | 
| VerkehrsflaecheID | 50 |  |  |  |  |  | 
| condition | 46 | 41 | 2 | 5 | 0.953 | 0.891 | 
| content | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| conditionException | 4 | 0 | 0 | 4 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 50 | 41 | 3 | 9 | 0.932 | 0.820 | 
| AnFluchtlinie | 97 |  |  |  |  |  | 
| condition | 97 | 91 | 0 | 6 | 1.000 | 0.938 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 97 | 91 | 0 | 6 | 1.000 | 0.938 | 
| AnordnungGaertnerischeAusgestaltung | 113 |  |  |  |  |  | 
| condition | 47 | 44 | 0 | 3 | 1.000 | 0.936 | 
| content | 66 | 62 | 2 | 4 | 0.969 | 0.939 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 113 | 106 | 2 | 7 | 0.981 | 0.938 | 
| GebaeudeHoeheMax | 57 |  |  |  |  |  | 
| condition | 8 | 3 | 1 | 5 | 0.750 | 0.375 | 
| content | 49 | 47 | 5 | 2 | 0.904 | 0.959 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 57 | 50 | 6 | 7 | 0.893 | 0.877 | 
| Dachart | 78 |  |  |  |  |  | 
| condition | 24 | 23 | 1 | 1 | 0.958 | 0.958 | 
| content | 51 | 47 | 1 | 4 | 0.979 | 0.922 | 
| conditionException | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 78 | 71 | 2 | 7 | 0.973 | 0.910 | 
| WidmungInMehrerenEbenen | 15 |  |  |  |  |  | 
| condition | 2 | 0 | 0 | 2 | 1.000 | 0.000 | 
| content | 13 | 12 | 0 | 1 | 1.000 | 0.923 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 15 | 12 | 0 | 3 | 1.000 | 0.800 | 
| GebaeudeHoeheArt | 79 |  |  |  |  |  | 
| condition | 2 | 0 | 1 | 2 | 0.000 | 0.000 | 
| content | 77 | 73 | 2 | 4 | 0.973 | 0.948 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 79 | 73 | 3 | 6 | 0.961 | 0.924 | 
| VorkehrungBepflanzung | 97 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 97 | 93 | 0 | 4 | 1.000 | 0.959 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 97 | 93 | 0 | 4 | 1.000 | 0.959 | 
| ErrichtungGebaeude | 65 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 65 | 44 | 0 | 21 | 1.000 | 0.677 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 65 | 44 | 0 | 21 | 1.000 | 0.677 | 
| PlangebietAllgemein | 67 |  |  |  |  |  | 
| condition | 67 | 54 | 0 | 13 | 1.000 | 0.806 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 67 | 54 | 0 | 13 | 1.000 | 0.806 | 
| VonBebauungFreizuhalten | 44 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 44 | 43 | 0 | 1 | 1.000 | 0.977 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 44 | 43 | 0 | 1 | 1.000 | 0.977 | 
| BegruenungDach | 85 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 85 | 85 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 85 | 85 | 0 | 0 | 1.000 | 1.000 | 
| AbschlussDachMaxBezugGebaeude | 63 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 63 | 62 | 0 | 1 | 1.000 | 0.984 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 63 | 62 | 0 | 1 | 1.000 | 0.984 | 
| GehsteigbreiteMin | 51 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 51 | 50 | 0 | 1 | 1.000 | 0.980 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 51 | 50 | 0 | 1 | 1.000 | 0.980 | 
| StrassenbreiteMin | 53 |  |  |  |  |  | 
| condition | 53 | 51 | 0 | 2 | 1.000 | 0.962 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 53 | 51 | 0 | 2 | 1.000 | 0.962 | 
| GebaeudeBautyp | 62 |  |  |  |  |  | 
| condition | 60 | 42 | 0 | 18 | 1.000 | 0.700 | 
| content | 0 | 0 | 18 | 0 | 0.000 | 1.000 | 
| conditionException | 2 | 0 | 0 | 2 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 62 | 42 | 18 | 20 | 0.700 | 0.677 | 
| AufbautenZulaessig | 57 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 57 | 56 | 0 | 1 | 1.000 | 0.982 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 57 | 56 | 0 | 1 | 1.000 | 0.982 | 
| UnterbrechungGeschlosseneBauweise | 49 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 49 | 49 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 49 | 49 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMax | 44 |  |  |  |  |  | 
| condition | 35 | 31 | 0 | 4 | 1.000 | 0.886 | 
| content | 9 | 9 | 4 | 0 | 0.692 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 44 | 40 | 4 | 4 | 0.909 | 0.909 | 
| AnOeffentlichenVerkehrsflaechen | 17 |  |  |  |  |  | 
| condition | 17 | 17 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 17 | 17 | 0 | 0 | 1.000 | 1.000 | 
| BauweiseID | 24 |  |  |  |  |  | 
| condition | 6 | 2 | 0 | 4 | 1.000 | 0.333 | 
| content | 18 | 4 | 2 | 14 | 0.667 | 0.222 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 24 | 6 | 2 | 18 | 0.750 | 0.250 | 
| Bauklasse | 34 |  |  |  |  |  | 
| condition | 13 | 5 | 1 | 8 | 0.833 | 0.385 | 
| content | 21 | 14 | 4 | 7 | 0.778 | 0.667 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 34 | 19 | 5 | 15 | 0.792 | 0.559 | 
| EinfriedungAusgestaltung | 43 |  |  |  |  |  | 
| condition | 8 | 0 | 0 | 8 | 1.000 | 0.000 | 
| content | 34 | 33 | 5 | 1 | 0.868 | 0.971 | 
| conditionException | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 43 | 33 | 5 | 10 | 0.868 | 0.767 | 
| DurchgangBreite | 32 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 32 | 32 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 32 | 32 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeGaertnerischAuszugestaltende | 45 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| conditionException | 44 | 0 | 0 | 44 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 3 | 0 | 0.000 | 1.000 | 
| micro | 45 | 0 | 3 | 45 | 0.000 | 0.000 | 
| StrassenbreiteMax | 34 |  |  |  |  |  | 
| condition | 34 | 33 | 0 | 1 | 1.000 | 0.971 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 34 | 33 | 0 | 1 | 1.000 | 0.971 | 
| DurchgangHoehe | 24 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 24 | 24 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 24 | 24 | 0 | 0 | 1.000 | 1.000 | 
| UnterirdischeBaulichkeiten | 40 |  |  |  |  |  | 
| condition | 38 | 24 | 1 | 14 | 0.960 | 0.632 | 
| content | 1 | 0 | 6 | 1 | 0.000 | 0.000 | 
| conditionException | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 40 | 24 | 7 | 16 | 0.774 | 0.600 | 
| Struktureinheit | 17 |  |  |  |  |  | 
| condition | 5 | 3 | 1 | 2 | 0.750 | 0.600 | 
| content | 11 | 10 | 1 | 1 | 0.909 | 0.909 | 
| conditionException | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 17 | 14 | 2 | 3 | 0.875 | 0.824 | 
| VolumenUndUmbaubarerRaum | 25 |  |  |  |  |  | 
| condition | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| content | 24 | 24 | 1 | 0 | 0.960 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 25 | 24 | 1 | 1 | 0.960 | 0.960 | 
| EinfriedungHoeheGesamt | 17 |  |  |  |  |  | 
| condition | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| content | 16 | 16 | 1 | 0 | 0.941 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 17 | 16 | 1 | 1 | 0.941 | 0.941 | 
| Stockwerk | 20 |  |  |  |  |  | 
| condition | 19 | 17 | 0 | 2 | 1.000 | 0.895 | 
| content | 1 | 1 | 2 | 0 | 0.333 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 20 | 18 | 2 | 2 | 0.900 | 0.900 | 
| DachflaecheMin | 20 |  |  |  |  |  | 
| condition | 20 | 19 | 0 | 1 | 1.000 | 0.950 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 20 | 19 | 0 | 1 | 1.000 | 0.950 | 
| EinfriedungLage | 23 |  |  |  |  |  | 
| condition | 23 | 22 | 0 | 1 | 1.000 | 0.957 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 23 | 22 | 0 | 1 | 1.000 | 0.957 | 
| AnlageZumEinstellenVorhanden | 22 |  |  |  |  |  | 
| condition | 7 | 2 | 0 | 5 | 1.000 | 0.286 | 
| content | 15 | 11 | 2 | 4 | 0.846 | 0.733 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 22 | 13 | 2 | 9 | 0.867 | 0.591 | 
| VorstehendeBauelementeAusladungMax | 9 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 9 | 9 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 9 | 9 | 0 | 0 | 1.000 | 1.000 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen | 19 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 19 | 19 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 19 | 19 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungZulaessig | 14 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 14 | 11 | 0 | 3 | 1.000 | 0.786 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 14 | 11 | 0 | 3 | 1.000 | 0.786 | 
| VerbotWohnung | 15 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 15 | 13 | 0 | 2 | 1.000 | 0.867 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 15 | 13 | 0 | 2 | 1.000 | 0.867 | 
| StrassenbreiteVonBis | 14 |  |  |  |  |  | 
| condition | 14 | 12 | 0 | 2 | 1.000 | 0.857 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 14 | 12 | 0 | 2 | 1.000 | 0.857 | 
| AnordnungGaertnerischeAusgestaltungProzentual | 21 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 21 | 19 | 0 | 2 | 1.000 | 0.905 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 21 | 19 | 1 | 2 | 0.950 | 0.905 | 
| OeffentlicheVerkehrsflaecheBreiteMin | 18 |  |  |  |  |  | 
| condition | 18 | 15 | 0 | 3 | 1.000 | 0.833 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 18 | 15 | 0 | 3 | 1.000 | 0.833 | 
| VorbautenVerbot | 15 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 15 | 14 | 0 | 1 | 1.000 | 0.933 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 15 | 14 | 0 | 1 | 1.000 | 0.933 | 
| HoehenlageGrundflaeche | 3 |  |  |  |  |  | 
| condition | 1 | 0 | 1 | 1 | 0.000 | 0.000 | 
| content | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 1 | 1 | 2 | 0.500 | 0.333 | 
| VorbautenBeschraenkung | 8 |  |  |  |  |  | 
| condition | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| content | 7 | 7 | 1 | 0 | 0.875 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 8 | 7 | 1 | 1 | 0.875 | 0.875 | 
| AnteilDachbegruenung | 6 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| EinleitungNiederschlagswaesser | 13 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 13 | 12 | 0 | 1 | 1.000 | 0.923 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 13 | 12 | 0 | 1 | 1.000 | 0.923 | 
| AbschlussDachMaxBezugGelaende | 6 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 6 | 2 | 0 | 4 | 1.000 | 0.333 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 2 | 0 | 4 | 1.000 | 0.333 | 
| VerbotStaffelung | 11 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 11 | 11 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 11 | 11 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeHoehe | 11 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 11 | 11 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 11 | 11 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzImNiveauZulaessig | 7 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 
| MaxAnzahlGeschosseOberirdisch | 6 |  |  |  |  |  | 
| condition | 4 | 0 | 0 | 4 | 1.000 | 0.000 | 
| content | 2 | 2 | 4 | 0 | 0.333 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 2 | 4 | 4 | 0.333 | 0.333 | 
| GebaeudeHoeheMin | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| conditionException | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 0 | 1 | 1 | 0.000 | 0.000 | 
| GaragengebaeudeAusfuehrung | 3 |  |  |  |  |  | 
| condition | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| content | 2 | 2 | 1 | 0 | 0.667 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 2 | 1 | 1 | 0.667 | 0.667 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben | 5 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 5 | 3 | 0 | 2 | 1.000 | 0.600 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 3 | 1 | 2 | 0.750 | 0.600 | 
| StellplatzregulativUmfangMaximumRelativ | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| Massengliederung | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| StellplatzregulativUmfangMaximumAbsolut | 5 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzMax | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| OberflaecheBestimmungP | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| InSchutzzone | 8 |  |  |  |  |  | 
| condition | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 2 | 0 | 0 | 2 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 8 | 6 | 0 | 2 | 1.000 | 0.750 | 
| AnzahlGebaeudeMax | 8 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 8 | 8 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 8 | 8 | 0 | 0 | 1.000 | 1.000 | 
| FBOKMinimumWohnungen | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| TechnischeAufbautenHoeheMax | 7 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 7 | 5 | 0 | 2 | 1.000 | 0.714 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 7 | 5 | 0 | 2 | 1.000 | 0.714 | 
| StellplatzregulativUmfangMinimumRelativ | 6 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| GebaeudeEinschraenkungP | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| DurchfahrtHoehe | 6 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMin | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| Kleinhaeuser | 6 |  |  |  |  |  | 
| condition | 5 | 3 | 0 | 2 | 1.000 | 0.600 | 
| content | 1 | 1 | 2 | 0 | 0.333 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 4 | 2 | 2 | 0.667 | 0.667 | 
| BauklasseVIHoeheMax | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 4 | 2 | 0 | 2 | 1.000 | 0.500 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 2 | 0 | 2 | 1.000 | 0.500 | 
| MaxAnzahlDachgeschosse | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| BauklasseVIHoeheMin | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 0 | 0 | 2 | 1.000 | 0.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 0 | 0 | 2 | 1.000 | 0.000 | 
| StellplatzverpflichtungArt | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotBueroGeschaeftsgebaeude | 5 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeVonWohnungenUnzulaessig | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| DurchfahrtBreite | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| Geschaeftsstrassen | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| VerbotUnterirdischeBauwerkeUeberBaufluchtlinie | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MindestraumhoeheEG | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| HochhausZulaessigGemaessBB | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativVorhanden | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxAnzahlGeschosseOberirdischOhneDachgeschoss | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotAufenthaltsraum | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungHoeheSockel | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| Einbautrasse | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| GelaendeneigungMin | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AnteilBaumbepflanzung | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| ZulaessigeGeschossanzahlEinkaufszentrum | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| VerbotStellplaetzeUndParkgebaeude | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeLaenge | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxHoeheWohngebaeude | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| LaubengangHoehe | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 



## Full details
### Annotator 02

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| Planzeichen | 447 |  |  |  |  |  | 
| condition | 445 | 438 | 1 | 7 | 0.998 | 0.984 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 447 | 439 | 1 | 8 | 0.998 | 0.982 | 
| WidmungUndZweckbestimmung | 242 |  |  |  |  |  | 
| condition | 201 | 57 | 4 | 144 | 0.934 | 0.284 | 
| content | 35 | 28 | 16 | 7 | 0.636 | 0.800 | 
| conditionException | 5 | 3 | 6 | 2 | 0.333 | 0.600 | 
| contentException | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| micro | 242 | 88 | 26 | 154 | 0.772 | 0.364 | 
| Flaechen | 89 |  |  |  |  |  | 
| condition | 19 | 19 | 3 | 0 | 0.864 | 1.000 | 
| content | 70 | 65 | 0 | 5 | 1.000 | 0.929 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 89 | 84 | 3 | 5 | 0.966 | 0.944 | 
| VerkehrsflaecheID | 67 |  |  |  |  |  | 
| condition | 64 | 62 | 2 | 2 | 0.969 | 0.969 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 67 | 63 | 2 | 4 | 0.969 | 0.940 | 
| AnFluchtlinie | 102 |  |  |  |  |  | 
| condition | 102 | 100 | 0 | 2 | 1.000 | 0.980 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 102 | 100 | 0 | 2 | 1.000 | 0.980 | 
| AnordnungGaertnerischeAusgestaltung | 97 |  |  |  |  |  | 
| condition | 39 | 35 | 0 | 4 | 1.000 | 0.897 | 
| content | 57 | 57 | 3 | 0 | 0.950 | 1.000 | 
| conditionException | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 97 | 93 | 3 | 4 | 0.969 | 0.959 | 
| GebaeudeHoeheMax | 72 |  |  |  |  |  | 
| condition | 14 | 6 | 1 | 8 | 0.857 | 0.429 | 
| content | 58 | 57 | 8 | 1 | 0.877 | 0.983 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 72 | 63 | 9 | 9 | 0.875 | 0.875 | 
| Dachart | 76 |  |  |  |  |  | 
| condition | 19 | 19 | 2 | 0 | 0.905 | 1.000 | 
| content | 54 | 50 | 0 | 4 | 1.000 | 0.926 | 
| conditionException | 2 | 0 | 1 | 2 | 0.000 | 0.000 | 
| contentException | 1 | 0 | 1 | 1 | 0.000 | 0.000 | 
| micro | 76 | 69 | 4 | 7 | 0.945 | 0.908 | 
| WidmungInMehrerenEbenen | 14 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 14 | 11 | 0 | 3 | 1.000 | 0.786 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 14 | 11 | 0 | 3 | 1.000 | 0.786 | 
| GebaeudeHoeheArt | 77 |  |  |  |  |  | 
| condition | 5 | 3 | 60 | 2 | 0.048 | 0.600 | 
| content | 72 | 9 | 2 | 63 | 0.818 | 0.125 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 77 | 12 | 62 | 65 | 0.162 | 0.156 | 
| VorkehrungBepflanzung | 100 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 100 | 93 | 0 | 7 | 1.000 | 0.930 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 100 | 93 | 0 | 7 | 1.000 | 0.930 | 
| ErrichtungGebaeude | 70 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 70 | 45 | 0 | 25 | 1.000 | 0.643 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 70 | 45 | 0 | 25 | 1.000 | 0.643 | 
| PlangebietAllgemein | 66 |  |  |  |  |  | 
| condition | 66 | 57 | 0 | 9 | 1.000 | 0.864 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 66 | 57 | 0 | 9 | 1.000 | 0.864 | 
| VonBebauungFreizuhalten | 50 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 50 | 45 | 0 | 5 | 1.000 | 0.900 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 50 | 45 | 0 | 5 | 1.000 | 0.900 | 
| BegruenungDach | 76 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 76 | 75 | 0 | 1 | 1.000 | 0.987 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 76 | 75 | 0 | 1 | 1.000 | 0.987 | 
| AbschlussDachMaxBezugGebaeude | 67 |  |  |  |  |  | 
| condition | 1 | 0 | 1 | 1 | 0.000 | 0.000 | 
| content | 66 | 65 | 1 | 1 | 0.985 | 0.985 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 67 | 65 | 2 | 2 | 0.970 | 0.970 | 
| GehsteigbreiteMin | 51 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 51 | 51 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 51 | 51 | 0 | 0 | 1.000 | 1.000 | 
| StrassenbreiteMin | 54 |  |  |  |  |  | 
| condition | 54 | 53 | 0 | 1 | 1.000 | 0.981 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 54 | 53 | 0 | 1 | 1.000 | 0.981 | 
| GebaeudeBautyp | 61 |  |  |  |  |  | 
| condition | 59 | 43 | 0 | 16 | 1.000 | 0.729 | 
| content | 2 | 2 | 15 | 0 | 0.118 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 61 | 45 | 15 | 16 | 0.750 | 0.738 | 
| AufbautenZulaessig | 49 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 49 | 44 | 0 | 5 | 1.000 | 0.898 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 2 | 0 | 0.000 | 1.000 | 
| micro | 49 | 44 | 2 | 5 | 0.957 | 0.898 | 
| UnterbrechungGeschlosseneBauweise | 50 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 50 | 50 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 50 | 50 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMax | 37 |  |  |  |  |  | 
| condition | 27 | 24 | 0 | 3 | 1.000 | 0.889 | 
| content | 10 | 9 | 3 | 1 | 0.750 | 0.900 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 37 | 33 | 3 | 4 | 0.917 | 0.892 | 
| AnOeffentlichenVerkehrsflaechen | 21 |  |  |  |  |  | 
| condition | 19 | 19 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 2 | 0 | 0 | 2 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 21 | 19 | 0 | 2 | 1.000 | 0.905 | 
| BauweiseID | 46 |  |  |  |  |  | 
| condition | 15 | 9 | 1 | 6 | 0.900 | 0.600 | 
| content | 31 | 21 | 0 | 10 | 1.000 | 0.677 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 46 | 30 | 1 | 16 | 0.968 | 0.652 | 
| Bauklasse | 47 |  |  |  |  |  | 
| condition | 17 | 11 | 0 | 6 | 1.000 | 0.647 | 
| content | 30 | 26 | 0 | 4 | 1.000 | 0.867 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 47 | 37 | 0 | 10 | 1.000 | 0.787 | 
| EinfriedungAusgestaltung | 38 |  |  |  |  |  | 
| condition | 6 | 0 | 1 | 6 | 0.000 | 0.000 | 
| content | 32 | 30 | 4 | 2 | 0.882 | 0.938 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 38 | 30 | 5 | 8 | 0.857 | 0.789 | 
| DurchgangBreite | 37 |  |  |  |  |  | 
| condition | 0 | 0 | 2 | 0 | 0.000 | 1.000 | 
| content | 37 | 34 | 0 | 3 | 1.000 | 0.919 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 37 | 34 | 2 | 3 | 0.944 | 0.919 | 
| AusnahmeGaertnerischAuszugestaltende | 31 |  |  |  |  |  | 
| condition | 0 | 0 | 2 | 0 | 0.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 31 | 11 | 0 | 20 | 1.000 | 0.355 | 
| contentException | 0 | 0 | 7 | 0 | 0.000 | 1.000 | 
| micro | 31 | 11 | 9 | 20 | 0.550 | 0.355 | 
| StrassenbreiteMax | 30 |  |  |  |  |  | 
| condition | 30 | 30 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 30 | 30 | 0 | 0 | 1.000 | 1.000 | 
| DurchgangHoehe | 25 |  |  |  |  |  | 
| condition | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| content | 24 | 24 | 1 | 0 | 0.960 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 25 | 24 | 1 | 1 | 0.960 | 0.960 | 
| UnterirdischeBaulichkeiten | 30 |  |  |  |  |  | 
| condition | 24 | 18 | 3 | 6 | 0.857 | 0.750 | 
| content | 6 | 3 | 5 | 3 | 0.375 | 0.500 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 30 | 21 | 8 | 9 | 0.724 | 0.700 | 
| Struktureinheit | 37 |  |  |  |  |  | 
| condition | 17 | 11 | 2 | 6 | 0.846 | 0.647 | 
| content | 17 | 13 | 0 | 4 | 1.000 | 0.765 | 
| conditionException | 3 | 2 | 0 | 1 | 1.000 | 0.667 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 37 | 26 | 2 | 11 | 0.929 | 0.703 | 
| VolumenUndUmbaubarerRaum | 25 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 25 | 24 | 0 | 1 | 1.000 | 0.960 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 25 | 24 | 1 | 1 | 0.960 | 0.960 | 
| EinfriedungHoeheGesamt | 20 |  |  |  |  |  | 
| condition | 5 | 0 | 0 | 5 | 1.000 | 0.000 | 
| content | 15 | 13 | 5 | 2 | 0.722 | 0.867 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 20 | 13 | 5 | 7 | 0.722 | 0.650 | 
| Stockwerk | 32 |  |  |  |  |  | 
| condition | 31 | 25 | 0 | 6 | 1.000 | 0.806 | 
| content | 1 | 1 | 2 | 0 | 0.333 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 32 | 26 | 2 | 6 | 0.929 | 0.812 | 
| DachflaecheMin | 26 |  |  |  |  |  | 
| condition | 26 | 21 | 0 | 5 | 1.000 | 0.808 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 26 | 21 | 0 | 5 | 1.000 | 0.808 | 
| EinfriedungLage | 24 |  |  |  |  |  | 
| condition | 24 | 22 | 0 | 2 | 1.000 | 0.917 | 
| content | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 24 | 22 | 1 | 2 | 0.957 | 0.917 | 
| AnlageZumEinstellenVorhanden | 19 |  |  |  |  |  | 
| condition | 5 | 1 | 0 | 4 | 1.000 | 0.200 | 
| content | 14 | 13 | 4 | 1 | 0.765 | 0.929 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 19 | 14 | 4 | 5 | 0.778 | 0.737 | 
| VorstehendeBauelementeAusladungMax | 7 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen | 27 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 27 | 26 | 0 | 1 | 1.000 | 0.963 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 27 | 26 | 0 | 1 | 1.000 | 0.963 | 
| EinfriedungZulaessig | 12 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 12 | 7 | 0 | 5 | 1.000 | 0.583 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 12 | 7 | 0 | 5 | 1.000 | 0.583 | 
| VerbotWohnung | 13 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 13 | 13 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 13 | 13 | 0 | 0 | 1.000 | 1.000 | 
| StrassenbreiteVonBis | 12 |  |  |  |  |  | 
| condition | 12 | 12 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 12 | 12 | 0 | 0 | 1.000 | 1.000 | 
| AnordnungGaertnerischeAusgestaltungProzentual | 19 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 19 | 12 | 0 | 7 | 1.000 | 0.632 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 19 | 12 | 0 | 7 | 1.000 | 0.632 | 
| OeffentlicheVerkehrsflaecheBreiteMin | 16 |  |  |  |  |  | 
| condition | 16 | 11 | 0 | 5 | 1.000 | 0.688 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 16 | 11 | 0 | 5 | 1.000 | 0.688 | 
| VorbautenVerbot | 19 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 19 | 19 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 19 | 19 | 0 | 0 | 1.000 | 1.000 | 
| HoehenlageGrundflaeche | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| VorbautenBeschraenkung | 2 |  |  |  |  |  | 
| condition | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| content | 1 | 1 | 1 | 0 | 0.500 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 1 | 1 | 1 | 0.500 | 0.500 | 
| AnteilDachbegruenung | 10 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 10 | 9 | 0 | 1 | 1.000 | 0.900 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 10 | 9 | 0 | 1 | 1.000 | 0.900 | 
| EinleitungNiederschlagswaesser | 10 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 10 | 8 | 0 | 2 | 1.000 | 0.800 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| micro | 10 | 8 | 1 | 2 | 0.889 | 0.800 | 
| AbschlussDachMaxBezugGelaende | 6 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 6 | 1 | 0 | 5 | 1.000 | 0.167 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 1 | 0 | 5 | 1.000 | 0.167 | 
| VerbotStaffelung | 13 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 13 | 13 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 13 | 13 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeHoehe | 7 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzImNiveauZulaessig | 10 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 10 | 7 | 0 | 3 | 1.000 | 0.700 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 10 | 7 | 0 | 3 | 1.000 | 0.700 | 
| MaxAnzahlGeschosseOberirdisch | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| GebaeudeHoeheMin | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| GaragengebaeudeAusfuehrung | 6 |  |  |  |  |  | 
| condition | 0 | 0 | 2 | 0 | 0.000 | 1.000 | 
| content | 6 | 2 | 0 | 4 | 1.000 | 0.333 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 2 | 2 | 4 | 0.500 | 0.333 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 4 | 3 | 0 | 1 | 1.000 | 0.750 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 3 | 0 | 1 | 1.000 | 0.750 | 
| StellplatzregulativUmfangMaximumRelativ | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| Massengliederung | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 0 | 1 | 1 | 0.000 | 0.000 | 
| StellplatzregulativUmfangMaximumAbsolut | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 2 | 0 | 1 | 1.000 | 0.667 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 2 | 0 | 1 | 1.000 | 0.667 | 
| StellplatzMax | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| OberflaecheBestimmungP | 6 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 6 | 4 | 0 | 2 | 1.000 | 0.667 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 4 | 0 | 2 | 1.000 | 0.667 | 
| InSchutzzone | 7 |  |  |  |  |  | 
| condition | 6 | 3 | 0 | 3 | 1.000 | 0.500 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 7 | 4 | 0 | 3 | 1.000 | 0.571 | 
| AnzahlGebaeudeMax | 8 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 8 | 8 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 8 | 8 | 0 | 0 | 1.000 | 1.000 | 
| FBOKMinimumWohnungen | 3 |  |  |  |  |  | 
| condition | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| TechnischeAufbautenHoeheMax | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| StellplatzregulativUmfangMinimumRelativ | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 4 | 3 | 0 | 1 | 1.000 | 0.750 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 3 | 0 | 1 | 1.000 | 0.750 | 
| GebaeudeEinschraenkungP | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 0 | 1 | 1 | 0.000 | 0.000 | 
| DurchfahrtHoehe | 5 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMin | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| Kleinhaeuser | 4 |  |  |  |  |  | 
| condition | 4 | 0 | 0 | 4 | 1.000 | 0.000 | 
| content | 0 | 0 | 4 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 0 | 4 | 4 | 0.000 | 0.000 | 
| BauklasseVIHoeheMax | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 3 | 0 | 0.000 | 1.000 | 
| content | 3 | 0 | 0 | 3 | 1.000 | 0.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 0 | 3 | 3 | 0.000 | 0.000 | 
| MaxAnzahlDachgeschosse | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| BauklasseVIHoeheMin | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 3 | 0 | 0.000 | 1.000 | 
| content | 3 | 0 | 0 | 3 | 1.000 | 0.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 0 | 3 | 3 | 0.000 | 0.000 | 
| StellplatzverpflichtungArt | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotBueroGeschaeftsgebaeude | 6 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeVonWohnungenUnzulaessig | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| DurchfahrtBreite | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| Geschaeftsstrassen | 4 |  |  |  |  |  | 
| condition | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| VerbotUnterirdischeBauwerkeUeberBaufluchtlinie | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MindestraumhoeheEG | 5 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 5 | 1 | 0 | 4 | 1.000 | 0.200 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 1 | 0 | 4 | 1.000 | 0.200 | 
| HochhausZulaessigGemaessBB | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativVorhanden | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxAnzahlGeschosseOberirdischOhneDachgeschoss | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| VerbotAufenthaltsraum | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungHoeheSockel | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| Einbautrasse | 1 |  |  |  |  |  | 
| condition | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| GelaendeneigungMin | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AnteilBaumbepflanzung | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| ZulaessigeGeschossanzahlEinkaufszentrum | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| VerbotStellplaetzeUndParkgebaeude | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeLaenge | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxHoeheWohngebaeude | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| LaubengangHoehe | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 



## Full details
### Annotator 03

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| Planzeichen | 442 |  |  |  |  |  | 
| condition | 440 | 437 | 1 | 3 | 0.998 | 0.993 | 
| content | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| conditionException | 1 | 0 | 1 | 1 | 0.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 442 | 437 | 2 | 5 | 0.995 | 0.989 | 
| WidmungUndZweckbestimmung | 250 |  |  |  |  |  | 
| condition | 199 | 40 | 7 | 159 | 0.851 | 0.201 | 
| content | 46 | 36 | 15 | 10 | 0.706 | 0.783 | 
| conditionException | 5 | 0 | 0 | 5 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 6 | 0 | 0.000 | 1.000 | 
| micro | 250 | 76 | 28 | 174 | 0.731 | 0.304 | 
| Flaechen | 83 |  |  |  |  |  | 
| condition | 13 | 13 | 1 | 0 | 0.929 | 1.000 | 
| content | 70 | 68 | 0 | 2 | 1.000 | 0.971 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 83 | 81 | 1 | 2 | 0.988 | 0.976 | 
| VerkehrsflaecheID | 45 |  |  |  |  |  | 
| condition | 43 | 42 | 1 | 1 | 0.977 | 0.977 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 2 | 0 | 0 | 2 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| micro | 45 | 42 | 2 | 3 | 0.955 | 0.933 | 
| AnFluchtlinie | 89 |  |  |  |  |  | 
| condition | 89 | 87 | 0 | 2 | 1.000 | 0.978 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 89 | 87 | 0 | 2 | 1.000 | 0.978 | 
| AnordnungGaertnerischeAusgestaltung | 91 |  |  |  |  |  | 
| condition | 40 | 38 | 0 | 2 | 1.000 | 0.950 | 
| content | 51 | 51 | 1 | 0 | 0.981 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 91 | 89 | 1 | 2 | 0.989 | 0.978 | 
| GebaeudeHoeheMax | 59 |  |  |  |  |  | 
| condition | 13 | 8 | 4 | 5 | 0.667 | 0.615 | 
| content | 46 | 42 | 5 | 4 | 0.894 | 0.913 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 59 | 50 | 9 | 9 | 0.847 | 0.847 | 
| Dachart | 68 |  |  |  |  |  | 
| condition | 23 | 21 | 0 | 2 | 1.000 | 0.913 | 
| content | 43 | 41 | 3 | 2 | 0.932 | 0.953 | 
| conditionException | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| contentException | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| micro | 68 | 63 | 3 | 5 | 0.955 | 0.926 | 
| WidmungInMehrerenEbenen | 28 |  |  |  |  |  | 
| condition | 1 | 0 | 10 | 1 | 0.000 | 0.000 | 
| content | 27 | 13 | 0 | 14 | 1.000 | 0.481 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 28 | 13 | 10 | 15 | 0.565 | 0.464 | 
| GebaeudeHoeheArt | 80 |  |  |  |  |  | 
| condition | 2 | 2 | 69 | 0 | 0.028 | 1.000 | 
| content | 78 | 9 | 0 | 69 | 1.000 | 0.115 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 80 | 11 | 69 | 69 | 0.138 | 0.138 | 
| VorkehrungBepflanzung | 82 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 82 | 82 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 82 | 82 | 0 | 0 | 1.000 | 1.000 | 
| ErrichtungGebaeude | 56 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 56 | 40 | 0 | 16 | 1.000 | 0.714 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 56 | 40 | 0 | 16 | 1.000 | 0.714 | 
| PlangebietAllgemein | 56 |  |  |  |  |  | 
| condition | 56 | 44 | 0 | 12 | 1.000 | 0.786 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 56 | 44 | 0 | 12 | 1.000 | 0.786 | 
| VonBebauungFreizuhalten | 43 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 43 | 41 | 0 | 2 | 1.000 | 0.953 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 43 | 41 | 0 | 2 | 1.000 | 0.953 | 
| BegruenungDach | 65 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 65 | 63 | 0 | 2 | 1.000 | 0.969 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 65 | 63 | 0 | 2 | 1.000 | 0.969 | 
| AbschlussDachMaxBezugGebaeude | 80 |  |  |  |  |  | 
| condition | 1 | 0 | 1 | 1 | 0.000 | 0.000 | 
| content | 79 | 78 | 1 | 1 | 0.987 | 0.987 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 80 | 78 | 2 | 2 | 0.975 | 0.975 | 
| GehsteigbreiteMin | 56 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 56 | 55 | 0 | 1 | 1.000 | 0.982 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 56 | 55 | 1 | 1 | 0.982 | 0.982 | 
| StrassenbreiteMin | 62 |  |  |  |  |  | 
| condition | 62 | 61 | 0 | 1 | 1.000 | 0.984 | 
| content | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 62 | 61 | 1 | 1 | 0.984 | 0.984 | 
| GebaeudeBautyp | 61 |  |  |  |  |  | 
| condition | 61 | 52 | 0 | 9 | 1.000 | 0.852 | 
| content | 0 | 0 | 9 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 61 | 52 | 9 | 9 | 0.852 | 0.852 | 
| AufbautenZulaessig | 43 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 43 | 41 | 0 | 2 | 1.000 | 0.953 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 43 | 41 | 0 | 2 | 1.000 | 0.953 | 
| UnterbrechungGeschlosseneBauweise | 59 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 59 | 59 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 59 | 59 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMax | 48 |  |  |  |  |  | 
| condition | 27 | 26 | 0 | 1 | 1.000 | 0.963 | 
| content | 21 | 20 | 1 | 1 | 0.952 | 0.952 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 48 | 46 | 1 | 2 | 0.979 | 0.958 | 
| AnOeffentlichenVerkehrsflaechen | 24 |  |  |  |  |  | 
| condition | 21 | 20 | 0 | 1 | 1.000 | 0.952 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 3 | 0 | 0 | 3 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 24 | 20 | 0 | 4 | 1.000 | 0.833 | 
| BauweiseID | 33 |  |  |  |  |  | 
| condition | 8 | 5 | 0 | 3 | 1.000 | 0.625 | 
| content | 24 | 21 | 1 | 3 | 0.955 | 0.875 | 
| conditionException | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 33 | 26 | 1 | 7 | 0.963 | 0.788 | 
| Bauklasse | 39 |  |  |  |  |  | 
| condition | 15 | 11 | 1 | 4 | 0.917 | 0.733 | 
| content | 24 | 15 | 0 | 9 | 1.000 | 0.625 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 39 | 26 | 1 | 13 | 0.963 | 0.667 | 
| EinfriedungAusgestaltung | 34 |  |  |  |  |  | 
| condition | 7 | 0 | 0 | 7 | 1.000 | 0.000 | 
| content | 27 | 26 | 2 | 1 | 0.929 | 0.963 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 34 | 26 | 2 | 8 | 0.929 | 0.765 | 
| DurchgangBreite | 43 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 43 | 43 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 43 | 43 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeGaertnerischAuszugestaltende | 21 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 21 | 2 | 0 | 19 | 1.000 | 0.095 | 
| contentException | 0 | 0 | 7 | 0 | 0.000 | 1.000 | 
| micro | 21 | 2 | 7 | 19 | 0.222 | 0.095 | 
| StrassenbreiteMax | 36 |  |  |  |  |  | 
| condition | 36 | 36 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 36 | 36 | 0 | 0 | 1.000 | 1.000 | 
| DurchgangHoehe | 31 |  |  |  |  |  | 
| condition | 1 | 1 | 1 | 0 | 0.500 | 1.000 | 
| content | 30 | 29 | 0 | 1 | 1.000 | 0.967 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 31 | 30 | 1 | 1 | 0.968 | 0.968 | 
| UnterirdischeBaulichkeiten | 27 |  |  |  |  |  | 
| condition | 24 | 18 | 1 | 6 | 0.947 | 0.750 | 
| content | 3 | 2 | 2 | 1 | 0.500 | 0.667 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| micro | 27 | 20 | 4 | 7 | 0.833 | 0.741 | 
| Struktureinheit | 16 |  |  |  |  |  | 
| condition | 10 | 8 | 1 | 2 | 0.889 | 0.800 | 
| content | 5 | 4 | 0 | 1 | 1.000 | 0.800 | 
| conditionException | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 16 | 13 | 1 | 3 | 0.929 | 0.812 | 
| VolumenUndUmbaubarerRaum | 34 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 34 | 34 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 34 | 34 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungHoeheGesamt | 15 |  |  |  |  |  | 
| condition | 4 | 0 | 0 | 4 | 1.000 | 0.000 | 
| content | 11 | 11 | 4 | 0 | 0.733 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 15 | 11 | 4 | 4 | 0.733 | 0.733 | 
| Stockwerk | 22 |  |  |  |  |  | 
| condition | 22 | 20 | 0 | 2 | 1.000 | 0.909 | 
| content | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 22 | 20 | 1 | 2 | 0.952 | 0.909 | 
| DachflaecheMin | 24 |  |  |  |  |  | 
| condition | 24 | 21 | 0 | 3 | 1.000 | 0.875 | 
| content | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 24 | 21 | 1 | 3 | 0.955 | 0.875 | 
| EinfriedungLage | 15 |  |  |  |  |  | 
| condition | 15 | 15 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 15 | 15 | 0 | 0 | 1.000 | 1.000 | 
| AnlageZumEinstellenVorhanden | 10 |  |  |  |  |  | 
| condition | 1 | 1 | 1 | 0 | 0.500 | 1.000 | 
| content | 9 | 8 | 0 | 1 | 1.000 | 0.889 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 10 | 9 | 1 | 1 | 0.900 | 0.900 | 
| VorstehendeBauelementeAusladungMax | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen | 22 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 22 | 20 | 0 | 2 | 1.000 | 0.909 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 22 | 20 | 0 | 2 | 1.000 | 0.909 | 
| EinfriedungZulaessig | 13 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 13 | 11 | 0 | 2 | 1.000 | 0.846 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 13 | 11 | 0 | 2 | 1.000 | 0.846 | 
| VerbotWohnung | 15 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 15 | 14 | 0 | 1 | 1.000 | 0.933 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 15 | 14 | 0 | 1 | 1.000 | 0.933 | 
| StrassenbreiteVonBis | 16 |  |  |  |  |  | 
| condition | 16 | 16 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 16 | 16 | 0 | 0 | 1.000 | 1.000 | 
| AnordnungGaertnerischeAusgestaltungProzentual | 13 |  |  |  |  |  | 
| condition | 0 | 0 | 2 | 0 | 0.000 | 1.000 | 
| content | 13 | 11 | 0 | 2 | 1.000 | 0.846 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 13 | 11 | 2 | 2 | 0.846 | 0.846 | 
| OeffentlicheVerkehrsflaecheBreiteMin | 16 |  |  |  |  |  | 
| condition | 13 | 13 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 16 | 16 | 0 | 0 | 1.000 | 1.000 | 
| VorbautenVerbot | 16 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 16 | 16 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 16 | 16 | 0 | 0 | 1.000 | 1.000 | 
| HoehenlageGrundflaeche | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| VorbautenBeschraenkung | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| AnteilDachbegruenung | 5 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| EinleitungNiederschlagswaesser | 12 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 12 | 12 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 12 | 12 | 0 | 0 | 1.000 | 1.000 | 
| AbschlussDachMaxBezugGelaende | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 2 | 0 | 1 | 1.000 | 0.667 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 2 | 0 | 1 | 1.000 | 0.667 | 
| VerbotStaffelung | 11 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 11 | 11 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 11 | 11 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeHoehe | 8 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 8 | 8 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 8 | 8 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzImNiveauZulaessig | 9 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 9 | 4 | 0 | 5 | 1.000 | 0.444 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 9 | 4 | 0 | 5 | 1.000 | 0.444 | 
| MaxAnzahlGeschosseOberirdisch | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| GebaeudeHoeheMin | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| GaragengebaeudeAusfuehrung | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 0 | 1 | 1 | 0.000 | 0.000 | 
| StellplatzregulativUmfangMaximumRelativ | 5 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| Massengliederung | 5 |  |  |  |  |  | 
| condition | 0 | 0 | 5 | 0 | 0.000 | 1.000 | 
| content | 5 | 0 | 0 | 5 | 1.000 | 0.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 0 | 5 | 5 | 0.000 | 0.000 | 
| StellplatzregulativUmfangMaximumAbsolut | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzMax | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| OberflaecheBestimmungP | 3 |  |  |  |  |  | 
| condition | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| content | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| InSchutzzone | 7 |  |  |  |  |  | 
| condition | 7 | 6 | 0 | 1 | 1.000 | 0.857 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 7 | 6 | 0 | 1 | 1.000 | 0.857 | 
| AnzahlGebaeudeMax | 5 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| FBOKMinimumWohnungen | 11 |  |  |  |  |  | 
| condition | 1 | 1 | 1 | 0 | 0.500 | 1.000 | 
| content | 10 | 9 | 0 | 1 | 1.000 | 0.900 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 11 | 10 | 1 | 1 | 0.909 | 0.909 | 
| TechnischeAufbautenHoeheMax | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativUmfangMinimumRelativ | 8 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 8 | 8 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 8 | 8 | 0 | 0 | 1.000 | 1.000 | 
| GebaeudeEinschraenkungP | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| DurchfahrtHoehe | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMin | 8 |  |  |  |  |  | 
| condition | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| content | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 8 | 8 | 0 | 0 | 1.000 | 1.000 | 
| Kleinhaeuser | 4 |  |  |  |  |  | 
| condition | 4 | 2 | 0 | 2 | 1.000 | 0.500 | 
| content | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 2 | 1 | 2 | 0.667 | 0.500 | 
| BauklasseVIHoeheMax | 11 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 11 | 10 | 0 | 1 | 1.000 | 0.909 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 11 | 10 | 1 | 1 | 0.909 | 0.909 | 
| MaxAnzahlDachgeschosse | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| BauklasseVIHoeheMin | 11 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 11 | 9 | 0 | 2 | 1.000 | 0.818 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 11 | 9 | 1 | 2 | 0.900 | 0.818 | 
| StellplatzverpflichtungArt | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotBueroGeschaeftsgebaeude | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeVonWohnungenUnzulaessig | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| DurchfahrtBreite | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| Geschaeftsstrassen | 3 |  |  |  |  |  | 
| condition | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| VerbotUnterirdischeBauwerkeUeberBaufluchtlinie | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MindestraumhoeheEG | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| HochhausZulaessigGemaessBB | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativVorhanden | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxAnzahlGeschosseOberirdischOhneDachgeschoss | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotAufenthaltsraum | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungHoeheSockel | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| Einbautrasse | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| GelaendeneigungMin | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AnteilBaumbepflanzung | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| ZulaessigeGeschossanzahlEinkaufszentrum | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| VerbotStellplaetzeUndParkgebaeude | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeLaenge | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxHoeheWohngebaeude | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| LaubengangHoehe | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 



## Full details
### Annotator 04

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| Planzeichen | 541 |  |  |  |  |  | 
| condition | 536 | 532 | 4 | 4 | 0.993 | 0.993 | 
| content | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| conditionException | 4 | 0 | 0 | 4 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 541 | 532 | 4 | 9 | 0.993 | 0.983 | 
| WidmungUndZweckbestimmung | 263 |  |  |  |  |  | 
| condition | 215 | 50 | 8 | 165 | 0.862 | 0.233 | 
| content | 43 | 29 | 27 | 14 | 0.518 | 0.674 | 
| conditionException | 3 | 0 | 0 | 3 | 1.000 | 0.000 | 
| contentException | 2 | 1 | 1 | 1 | 0.500 | 0.500 | 
| micro | 263 | 80 | 36 | 183 | 0.690 | 0.304 | 
| Flaechen | 107 |  |  |  |  |  | 
| condition | 15 | 0 | 1 | 15 | 0.000 | 0.000 | 
| content | 92 | 88 | 15 | 4 | 0.854 | 0.957 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 107 | 88 | 16 | 19 | 0.846 | 0.822 | 
| VerkehrsflaecheID | 62 |  |  |  |  |  | 
| condition | 60 | 58 | 1 | 2 | 0.983 | 0.967 | 
| content | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| conditionException | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 62 | 59 | 2 | 3 | 0.967 | 0.952 | 
| AnFluchtlinie | 91 |  |  |  |  |  | 
| condition | 91 | 84 | 0 | 7 | 1.000 | 0.923 | 
| content | 0 | 0 | 2 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 91 | 84 | 2 | 7 | 0.977 | 0.923 | 
| AnordnungGaertnerischeAusgestaltung | 94 |  |  |  |  |  | 
| condition | 36 | 27 | 0 | 9 | 1.000 | 0.750 | 
| content | 58 | 53 | 8 | 5 | 0.869 | 0.914 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 94 | 80 | 8 | 14 | 0.909 | 0.851 | 
| GebaeudeHoeheMax | 72 |  |  |  |  |  | 
| condition | 17 | 4 | 1 | 13 | 0.800 | 0.235 | 
| content | 55 | 49 | 11 | 6 | 0.817 | 0.891 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 72 | 53 | 12 | 19 | 0.815 | 0.736 | 
| Dachart | 84 |  |  |  |  |  | 
| condition | 25 | 21 | 2 | 4 | 0.913 | 0.840 | 
| content | 59 | 54 | 4 | 5 | 0.931 | 0.915 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| micro | 84 | 75 | 7 | 9 | 0.915 | 0.893 | 
| WidmungInMehrerenEbenen | 22 |  |  |  |  |  | 
| condition | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| content | 21 | 17 | 0 | 4 | 1.000 | 0.810 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| micro | 22 | 18 | 1 | 4 | 0.947 | 0.818 | 
| GebaeudeHoeheArt | 73 |  |  |  |  |  | 
| condition | 0 | 0 | 36 | 0 | 0.000 | 1.000 | 
| content | 73 | 31 | 0 | 42 | 1.000 | 0.425 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 73 | 31 | 36 | 42 | 0.463 | 0.425 | 
| VorkehrungBepflanzung | 82 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 82 | 72 | 0 | 10 | 1.000 | 0.878 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 82 | 72 | 0 | 10 | 1.000 | 0.878 | 
| ErrichtungGebaeude | 90 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 90 | 42 | 0 | 48 | 1.000 | 0.467 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 90 | 42 | 1 | 48 | 0.977 | 0.467 | 
| PlangebietAllgemein | 70 |  |  |  |  |  | 
| condition | 70 | 58 | 0 | 12 | 1.000 | 0.829 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 70 | 58 | 0 | 12 | 1.000 | 0.829 | 
| VonBebauungFreizuhalten | 49 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 49 | 42 | 0 | 7 | 1.000 | 0.857 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| micro | 49 | 42 | 1 | 7 | 0.977 | 0.857 | 
| BegruenungDach | 63 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 63 | 63 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 63 | 63 | 0 | 0 | 1.000 | 1.000 | 
| AbschlussDachMaxBezugGebaeude | 68 |  |  |  |  |  | 
| condition | 0 | 0 | 4 | 0 | 0.000 | 1.000 | 
| content | 68 | 62 | 0 | 6 | 1.000 | 0.912 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 68 | 62 | 4 | 6 | 0.939 | 0.912 | 
| GehsteigbreiteMin | 53 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 53 | 49 | 0 | 4 | 1.000 | 0.925 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 53 | 49 | 1 | 4 | 0.980 | 0.925 | 
| StrassenbreiteMin | 56 |  |  |  |  |  | 
| condition | 56 | 52 | 0 | 4 | 1.000 | 0.929 | 
| content | 0 | 0 | 2 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 56 | 52 | 2 | 4 | 0.963 | 0.929 | 
| GebaeudeBautyp | 58 |  |  |  |  |  | 
| condition | 55 | 34 | 1 | 21 | 0.971 | 0.618 | 
| content | 2 | 1 | 15 | 1 | 0.062 | 0.500 | 
| conditionException | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| micro | 58 | 35 | 17 | 23 | 0.673 | 0.603 | 
| AufbautenZulaessig | 42 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 42 | 38 | 0 | 4 | 1.000 | 0.905 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 42 | 38 | 1 | 4 | 0.974 | 0.905 | 
| UnterbrechungGeschlosseneBauweise | 59 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 59 | 57 | 0 | 2 | 1.000 | 0.966 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 59 | 57 | 0 | 2 | 1.000 | 0.966 | 
| DachneigungMax | 52 |  |  |  |  |  | 
| condition | 28 | 24 | 0 | 4 | 1.000 | 0.857 | 
| content | 24 | 24 | 4 | 0 | 0.857 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 52 | 48 | 4 | 4 | 0.923 | 0.923 | 
| AnOeffentlichenVerkehrsflaechen | 21 |  |  |  |  |  | 
| condition | 21 | 17 | 0 | 4 | 1.000 | 0.810 | 
| content | 0 | 0 | 4 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 21 | 17 | 4 | 4 | 0.810 | 0.810 | 
| BauweiseID | 34 |  |  |  |  |  | 
| condition | 6 | 1 | 2 | 5 | 0.333 | 0.167 | 
| content | 27 | 16 | 0 | 11 | 1.000 | 0.593 | 
| conditionException | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 2 | 0 | 0.000 | 1.000 | 
| micro | 34 | 17 | 4 | 17 | 0.810 | 0.500 | 
| Bauklasse | 36 |  |  |  |  |  | 
| condition | 10 | 3 | 4 | 7 | 0.429 | 0.300 | 
| content | 26 | 7 | 1 | 19 | 0.875 | 0.269 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| micro | 36 | 10 | 6 | 26 | 0.625 | 0.278 | 
| EinfriedungAusgestaltung | 43 |  |  |  |  |  | 
| condition | 14 | 0 | 1 | 14 | 0.000 | 0.000 | 
| content | 28 | 22 | 5 | 6 | 0.815 | 0.786 | 
| conditionException | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| micro | 43 | 22 | 7 | 21 | 0.759 | 0.512 | 
| DurchgangBreite | 30 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 30 | 26 | 0 | 4 | 1.000 | 0.867 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 30 | 26 | 1 | 4 | 0.963 | 0.867 | 
| AusnahmeGaertnerischAuszugestaltende | 35 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 5 | 0 | 0.167 | 1.000 | 
| conditionException | 34 | 3 | 0 | 31 | 1.000 | 0.088 | 
| contentException | 0 | 0 | 3 | 0 | 0.000 | 1.000 | 
| micro | 35 | 4 | 8 | 31 | 0.333 | 0.114 | 
| StrassenbreiteMax | 31 |  |  |  |  |  | 
| condition | 31 | 23 | 0 | 8 | 1.000 | 0.742 | 
| content | 0 | 0 | 5 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 31 | 23 | 5 | 8 | 0.821 | 0.742 | 
| DurchgangHoehe | 21 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 21 | 20 | 0 | 1 | 1.000 | 0.952 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 21 | 20 | 0 | 1 | 1.000 | 0.952 | 
| UnterirdischeBaulichkeiten | 21 |  |  |  |  |  | 
| condition | 18 | 3 | 0 | 15 | 1.000 | 0.167 | 
| content | 3 | 2 | 12 | 1 | 0.143 | 0.667 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 21 | 5 | 12 | 16 | 0.294 | 0.238 | 
| Struktureinheit | 21 |  |  |  |  |  | 
| condition | 8 | 7 | 1 | 1 | 0.875 | 0.875 | 
| content | 13 | 5 | 0 | 8 | 1.000 | 0.385 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 21 | 12 | 1 | 9 | 0.923 | 0.571 | 
| VolumenUndUmbaubarerRaum | 33 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 33 | 32 | 0 | 1 | 1.000 | 0.970 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 33 | 32 | 0 | 1 | 1.000 | 0.970 | 
| EinfriedungHoeheGesamt | 22 |  |  |  |  |  | 
| condition | 10 | 0 | 0 | 10 | 1.000 | 0.000 | 
| content | 12 | 10 | 9 | 2 | 0.526 | 0.833 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 22 | 10 | 9 | 12 | 0.526 | 0.455 | 
| Stockwerk | 24 |  |  |  |  |  | 
| condition | 24 | 0 | 0 | 24 | 1.000 | 0.000 | 
| content | 0 | 0 | 19 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 24 | 0 | 19 | 24 | 0.000 | 0.000 | 
| DachflaecheMin | 23 |  |  |  |  |  | 
| condition | 23 | 15 | 0 | 8 | 1.000 | 0.652 | 
| content | 0 | 0 | 4 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 23 | 15 | 4 | 8 | 0.789 | 0.652 | 
| EinfriedungLage | 20 |  |  |  |  |  | 
| condition | 20 | 15 | 0 | 5 | 1.000 | 0.750 | 
| content | 0 | 0 | 2 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 20 | 15 | 2 | 5 | 0.882 | 0.750 | 
| AnlageZumEinstellenVorhanden | 13 |  |  |  |  |  | 
| condition | 9 | 1 | 0 | 8 | 1.000 | 0.111 | 
| content | 4 | 2 | 5 | 2 | 0.286 | 0.500 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 13 | 3 | 5 | 10 | 0.375 | 0.231 | 
| VorstehendeBauelementeAusladungMax | 6 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen | 24 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 24 | 22 | 0 | 2 | 1.000 | 0.917 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 24 | 22 | 1 | 2 | 0.957 | 0.917 | 
| EinfriedungZulaessig | 20 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 20 | 12 | 0 | 8 | 1.000 | 0.600 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 20 | 12 | 0 | 8 | 1.000 | 0.600 | 
| VerbotWohnung | 26 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 26 | 19 | 0 | 7 | 1.000 | 0.731 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| micro | 26 | 19 | 1 | 7 | 0.950 | 0.731 | 
| StrassenbreiteVonBis | 20 |  |  |  |  |  | 
| condition | 20 | 14 | 0 | 6 | 1.000 | 0.700 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 20 | 14 | 0 | 6 | 1.000 | 0.700 | 
| AnordnungGaertnerischeAusgestaltungProzentual | 15 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 15 | 13 | 0 | 2 | 1.000 | 0.867 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 15 | 13 | 0 | 2 | 1.000 | 0.867 | 
| OeffentlicheVerkehrsflaecheBreiteMin | 25 |  |  |  |  |  | 
| condition | 19 | 13 | 1 | 6 | 0.929 | 0.684 | 
| content | 6 | 5 | 1 | 1 | 0.833 | 0.833 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 25 | 18 | 2 | 7 | 0.900 | 0.720 | 
| VorbautenVerbot | 13 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 13 | 10 | 0 | 3 | 1.000 | 0.769 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 13 | 10 | 1 | 3 | 0.909 | 0.769 | 
| HoehenlageGrundflaeche | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| VorbautenBeschraenkung | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| AnteilDachbegruenung | 18 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 18 | 17 | 0 | 1 | 1.000 | 0.944 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 18 | 17 | 1 | 1 | 0.944 | 0.944 | 
| EinleitungNiederschlagswaesser | 14 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 14 | 14 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 14 | 14 | 0 | 0 | 1.000 | 1.000 | 
| AbschlussDachMaxBezugGelaende | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 4 | 1 | 0 | 3 | 1.000 | 0.250 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 1 | 0 | 3 | 1.000 | 0.250 | 
| VerbotStaffelung | 12 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 12 | 12 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 12 | 12 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeHoehe | 6 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 6 | 5 | 0 | 1 | 1.000 | 0.833 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 5 | 0 | 1 | 1.000 | 0.833 | 
| StellplatzImNiveauZulaessig | 10 |  |  |  |  |  | 
| condition | 1 | 0 | 1 | 1 | 0.000 | 0.000 | 
| content | 9 | 8 | 1 | 1 | 0.889 | 0.889 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 10 | 8 | 2 | 2 | 0.800 | 0.800 | 
| MaxAnzahlGeschosseOberirdisch | 5 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| GebaeudeHoeheMin | 4 |  |  |  |  |  | 
| condition | 3 | 2 | 0 | 1 | 1.000 | 0.667 | 
| content | 1 | 1 | 1 | 0 | 0.500 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 3 | 1 | 1 | 0.750 | 0.750 | 
| GaragengebaeudeAusfuehrung | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativUmfangMaximumRelativ | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| Massengliederung | 7 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativUmfangMaximumAbsolut | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| StellplatzMax | 10 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 10 | 10 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 10 | 10 | 0 | 0 | 1.000 | 1.000 | 
| OberflaecheBestimmungP | 3 |  |  |  |  |  | 
| condition | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| content | 2 | 0 | 0 | 2 | 1.000 | 0.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 0 | 0 | 3 | 1.000 | 0.000 | 
| InSchutzzone | 6 |  |  |  |  |  | 
| condition | 6 | 2 | 0 | 4 | 1.000 | 0.333 | 
| content | 0 | 0 | 2 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 2 | 2 | 4 | 0.500 | 0.333 | 
| AnzahlGebaeudeMax | 7 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 7 | 5 | 0 | 2 | 1.000 | 0.714 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 7 | 5 | 1 | 2 | 0.833 | 0.714 | 
| FBOKMinimumWohnungen | 13 |  |  |  |  |  | 
| condition | 3 | 0 | 0 | 3 | 1.000 | 0.000 | 
| content | 10 | 9 | 2 | 1 | 0.818 | 0.900 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| micro | 13 | 9 | 3 | 4 | 0.750 | 0.692 | 
| TechnischeAufbautenHoeheMax | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativUmfangMinimumRelativ | 5 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 5 | 3 | 0 | 2 | 1.000 | 0.600 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 3 | 0 | 2 | 1.000 | 0.600 | 
| GebaeudeEinschraenkungP | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 4 | 2 | 0 | 2 | 1.000 | 0.500 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 2 | 0 | 2 | 1.000 | 0.500 | 
| DurchfahrtHoehe | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMin | 6 |  |  |  |  |  | 
| condition | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| content | 5 | 5 | 1 | 0 | 0.833 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 5 | 1 | 1 | 0.833 | 0.833 | 
| Kleinhaeuser | 5 |  |  |  |  |  | 
| condition | 4 | 0 | 1 | 4 | 0.000 | 0.000 | 
| content | 1 | 0 | 3 | 1 | 0.000 | 0.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 0 | 4 | 5 | 0.000 | 0.000 | 
| BauklasseVIHoeheMax | 9 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 9 | 8 | 0 | 1 | 1.000 | 0.889 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| micro | 9 | 8 | 1 | 1 | 0.889 | 0.889 | 
| MaxAnzahlDachgeschosse | 6 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 6 | 5 | 0 | 1 | 1.000 | 0.833 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 5 | 0 | 1 | 1.000 | 0.833 | 
| BauklasseVIHoeheMin | 8 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 8 | 7 | 0 | 1 | 1.000 | 0.875 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 8 | 7 | 0 | 1 | 1.000 | 0.875 | 
| StellplatzverpflichtungArt | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotBueroGeschaeftsgebaeude | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeVonWohnungenUnzulaessig | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| conditionException | 2 | 0 | 0 | 2 | 1.000 | 0.000 | 
| contentException | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| micro | 3 | 0 | 1 | 3 | 0.000 | 0.000 | 
| DurchfahrtBreite | 4 |  |  |  |  |  | 
| condition | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| content | 3 | 3 | 1 | 0 | 0.750 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 3 | 1 | 1 | 0.750 | 0.750 | 
| Geschaeftsstrassen | 2 |  |  |  |  |  | 
| condition | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| VerbotUnterirdischeBauwerkeUeberBaufluchtlinie | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MindestraumhoeheEG | 5 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 5 | 1 | 0 | 4 | 1.000 | 0.200 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 1 | 0 | 4 | 1.000 | 0.200 | 
| HochhausZulaessigGemaessBB | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| StellplatzregulativVorhanden | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxAnzahlGeschosseOberirdischOhneDachgeschoss | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| VerbotAufenthaltsraum | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungHoeheSockel | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| Einbautrasse | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| GelaendeneigungMin | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AnteilBaumbepflanzung | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| ZulaessigeGeschossanzahlEinkaufszentrum | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotStellplaetzeUndParkgebaeude | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeLaenge | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxHoeheWohngebaeude | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| LaubengangHoehe | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 



## Full details
### Annotator 05

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| Planzeichen | 523 |  |  |  |  |  | 
| condition | 523 | 514 | 0 | 9 | 1.000 | 0.983 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 523 | 514 | 0 | 9 | 1.000 | 0.983 | 
| WidmungUndZweckbestimmung | 257 |  |  |  |  |  | 
| condition | 205 | 45 | 5 | 160 | 0.900 | 0.220 | 
| content | 45 | 38 | 11 | 7 | 0.776 | 0.844 | 
| conditionException | 5 | 4 | 3 | 1 | 0.571 | 0.800 | 
| contentException | 2 | 0 | 0 | 2 | 1.000 | 0.000 | 
| micro | 257 | 87 | 19 | 170 | 0.821 | 0.339 | 
| Flaechen | 104 |  |  |  |  |  | 
| condition | 15 | 8 | 1 | 7 | 0.889 | 0.533 | 
| content | 89 | 88 | 7 | 1 | 0.926 | 0.989 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 104 | 96 | 8 | 8 | 0.923 | 0.923 | 
| VerkehrsflaecheID | 48 |  |  |  |  |  | 
| condition | 46 | 45 | 1 | 1 | 0.978 | 0.978 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 48 | 46 | 1 | 2 | 0.979 | 0.958 | 
| AnFluchtlinie | 86 |  |  |  |  |  | 
| condition | 86 | 82 | 0 | 4 | 1.000 | 0.953 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 86 | 82 | 0 | 4 | 1.000 | 0.953 | 
| AnordnungGaertnerischeAusgestaltung | 96 |  |  |  |  |  | 
| condition | 36 | 28 | 0 | 8 | 1.000 | 0.778 | 
| content | 60 | 55 | 7 | 5 | 0.887 | 0.917 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 96 | 83 | 7 | 13 | 0.922 | 0.865 | 
| GebaeudeHoeheMax | 72 |  |  |  |  |  | 
| condition | 18 | 12 | 1 | 6 | 0.923 | 0.667 | 
| content | 54 | 50 | 6 | 4 | 0.893 | 0.926 | 
| conditionException | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| contentException | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| micro | 72 | 62 | 9 | 10 | 0.873 | 0.861 | 
| Dachart | 72 |  |  |  |  |  | 
| condition | 16 | 15 | 3 | 1 | 0.833 | 0.938 | 
| content | 52 | 47 | 2 | 5 | 0.959 | 0.904 | 
| conditionException | 4 | 3 | 0 | 1 | 1.000 | 0.750 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 72 | 65 | 5 | 7 | 0.929 | 0.903 | 
| WidmungInMehrerenEbenen | 16 |  |  |  |  |  | 
| condition | 1 | 0 | 2 | 1 | 0.000 | 0.000 | 
| content | 15 | 13 | 0 | 2 | 1.000 | 0.867 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 16 | 13 | 2 | 3 | 0.867 | 0.812 | 
| GebaeudeHoeheArt | 90 |  |  |  |  |  | 
| condition | 2 | 2 | 74 | 0 | 0.026 | 1.000 | 
| content | 88 | 10 | 0 | 78 | 1.000 | 0.114 | 
| conditionException | 0 | 0 | 2 | 0 | 0.000 | 1.000 | 
| contentException | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| micro | 90 | 12 | 77 | 78 | 0.135 | 0.133 | 
| VorkehrungBepflanzung | 92 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 92 | 88 | 0 | 4 | 1.000 | 0.957 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 92 | 88 | 1 | 4 | 0.989 | 0.957 | 
| ErrichtungGebaeude | 79 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 79 | 54 | 0 | 25 | 1.000 | 0.684 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 79 | 54 | 0 | 25 | 1.000 | 0.684 | 
| PlangebietAllgemein | 58 |  |  |  |  |  | 
| condition | 58 | 48 | 0 | 10 | 1.000 | 0.828 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 58 | 48 | 0 | 10 | 1.000 | 0.828 | 
| VonBebauungFreizuhalten | 50 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 50 | 47 | 0 | 3 | 1.000 | 0.940 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 50 | 47 | 0 | 3 | 1.000 | 0.940 | 
| BegruenungDach | 71 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 71 | 69 | 0 | 2 | 1.000 | 0.972 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 71 | 69 | 0 | 2 | 1.000 | 0.972 | 
| AbschlussDachMaxBezugGebaeude | 85 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 85 | 83 | 0 | 2 | 1.000 | 0.976 | 
| conditionException | 0 | 0 | 2 | 0 | 0.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 85 | 83 | 2 | 2 | 0.976 | 0.976 | 
| GehsteigbreiteMin | 52 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 52 | 52 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 52 | 52 | 0 | 0 | 1.000 | 1.000 | 
| StrassenbreiteMin | 65 |  |  |  |  |  | 
| condition | 65 | 64 | 0 | 1 | 1.000 | 0.985 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 65 | 64 | 0 | 1 | 1.000 | 0.985 | 
| GebaeudeBautyp | 51 |  |  |  |  |  | 
| condition | 50 | 42 | 0 | 8 | 1.000 | 0.840 | 
| content | 0 | 0 | 8 | 0 | 0.000 | 1.000 | 
| conditionException | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 51 | 43 | 8 | 8 | 0.843 | 0.843 | 
| AufbautenZulaessig | 54 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 54 | 54 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 54 | 54 | 0 | 0 | 1.000 | 1.000 | 
| UnterbrechungGeschlosseneBauweise | 47 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 47 | 47 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 47 | 47 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMax | 41 |  |  |  |  |  | 
| condition | 22 | 21 | 1 | 1 | 0.955 | 0.955 | 
| content | 19 | 17 | 1 | 2 | 0.944 | 0.895 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 41 | 38 | 2 | 3 | 0.950 | 0.927 | 
| AnOeffentlichenVerkehrsflaechen | 11 |  |  |  |  |  | 
| condition | 11 | 9 | 0 | 2 | 1.000 | 0.818 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 11 | 9 | 0 | 2 | 1.000 | 0.818 | 
| BauweiseID | 28 |  |  |  |  |  | 
| condition | 6 | 0 | 2 | 6 | 0.000 | 0.000 | 
| content | 22 | 1 | 0 | 21 | 1.000 | 0.045 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 28 | 1 | 2 | 27 | 0.333 | 0.036 | 
| Bauklasse | 39 |  |  |  |  |  | 
| condition | 15 | 9 | 6 | 6 | 0.600 | 0.600 | 
| content | 24 | 13 | 0 | 11 | 1.000 | 0.542 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 39 | 22 | 6 | 17 | 0.786 | 0.564 | 
| EinfriedungAusgestaltung | 42 |  |  |  |  |  | 
| condition | 9 | 0 | 0 | 9 | 1.000 | 0.000 | 
| content | 31 | 25 | 3 | 6 | 0.893 | 0.806 | 
| conditionException | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 42 | 27 | 3 | 15 | 0.900 | 0.643 | 
| DurchgangBreite | 34 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 34 | 34 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 34 | 34 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeGaertnerischAuszugestaltende | 38 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| conditionException | 38 | 26 | 0 | 12 | 1.000 | 0.684 | 
| contentException | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| micro | 38 | 26 | 2 | 12 | 0.929 | 0.684 | 
| StrassenbreiteMax | 32 |  |  |  |  |  | 
| condition | 32 | 32 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 32 | 32 | 0 | 0 | 1.000 | 1.000 | 
| DurchgangHoehe | 33 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 33 | 32 | 0 | 1 | 1.000 | 0.970 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 33 | 32 | 1 | 1 | 0.970 | 0.970 | 
| UnterirdischeBaulichkeiten | 27 |  |  |  |  |  | 
| condition | 26 | 11 | 0 | 15 | 1.000 | 0.423 | 
| content | 0 | 0 | 4 | 0 | 0.000 | 1.000 | 
| conditionException | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 27 | 11 | 4 | 16 | 0.733 | 0.407 | 
| Struktureinheit | 27 |  |  |  |  |  | 
| condition | 20 | 13 | 1 | 7 | 0.929 | 0.650 | 
| content | 7 | 6 | 4 | 1 | 0.600 | 0.857 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 27 | 19 | 5 | 8 | 0.792 | 0.704 | 
| VolumenUndUmbaubarerRaum | 32 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 32 | 32 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 32 | 32 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungHoeheGesamt | 15 |  |  |  |  |  | 
| condition | 5 | 0 | 0 | 5 | 1.000 | 0.000 | 
| content | 10 | 10 | 4 | 0 | 0.714 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 15 | 10 | 4 | 5 | 0.714 | 0.667 | 
| Stockwerk | 14 |  |  |  |  |  | 
| condition | 14 | 8 | 0 | 6 | 1.000 | 0.571 | 
| content | 0 | 0 | 4 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| micro | 14 | 8 | 5 | 6 | 0.615 | 0.571 | 
| DachflaecheMin | 25 |  |  |  |  |  | 
| condition | 25 | 20 | 0 | 5 | 1.000 | 0.800 | 
| content | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 25 | 20 | 1 | 5 | 0.952 | 0.800 | 
| EinfriedungLage | 16 |  |  |  |  |  | 
| condition | 16 | 13 | 0 | 3 | 1.000 | 0.812 | 
| content | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 16 | 13 | 1 | 3 | 0.929 | 0.812 | 
| AnlageZumEinstellenVorhanden | 10 |  |  |  |  |  | 
| condition | 7 | 2 | 0 | 5 | 1.000 | 0.286 | 
| content | 3 | 1 | 1 | 2 | 0.500 | 0.333 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 10 | 3 | 1 | 7 | 0.750 | 0.300 | 
| VorstehendeBauelementeAusladungMax | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen | 18 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 18 | 18 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 18 | 18 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungZulaessig | 18 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 18 | 13 | 0 | 5 | 1.000 | 0.722 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 18 | 13 | 0 | 5 | 1.000 | 0.722 | 
| VerbotWohnung | 27 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 27 | 24 | 0 | 3 | 1.000 | 0.889 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 27 | 24 | 0 | 3 | 1.000 | 0.889 | 
| StrassenbreiteVonBis | 17 |  |  |  |  |  | 
| condition | 17 | 15 | 0 | 2 | 1.000 | 0.882 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 17 | 15 | 0 | 2 | 1.000 | 0.882 | 
| AnordnungGaertnerischeAusgestaltungProzentual | 17 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 17 | 16 | 0 | 1 | 1.000 | 0.941 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 17 | 16 | 0 | 1 | 1.000 | 0.941 | 
| OeffentlicheVerkehrsflaecheBreiteMin | 20 |  |  |  |  |  | 
| condition | 17 | 12 | 3 | 5 | 0.800 | 0.706 | 
| content | 3 | 0 | 0 | 3 | 1.000 | 0.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 20 | 12 | 3 | 8 | 0.800 | 0.600 | 
| VorbautenVerbot | 16 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 16 | 16 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 16 | 16 | 0 | 0 | 1.000 | 1.000 | 
| HoehenlageGrundflaeche | 2 |  |  |  |  |  | 
| condition | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| VorbautenBeschraenkung | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| AnteilDachbegruenung | 16 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 16 | 15 | 0 | 1 | 1.000 | 0.938 | 
| conditionException | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 16 | 15 | 1 | 1 | 0.938 | 0.938 | 
| EinleitungNiederschlagswaesser | 13 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 13 | 13 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 13 | 13 | 0 | 0 | 1.000 | 1.000 | 
| AbschlussDachMaxBezugGelaende | 6 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 6 | 1 | 0 | 5 | 1.000 | 0.167 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 1 | 0 | 5 | 1.000 | 0.167 | 
| VerbotStaffelung | 12 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 12 | 11 | 0 | 1 | 1.000 | 0.917 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 12 | 11 | 0 | 1 | 1.000 | 0.917 | 
| ArkadeHoehe | 12 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 12 | 11 | 0 | 1 | 1.000 | 0.917 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 12 | 11 | 0 | 1 | 1.000 | 0.917 | 
| StellplatzImNiveauZulaessig | 10 |  |  |  |  |  | 
| condition | 1 | 1 | 1 | 0 | 0.500 | 1.000 | 
| content | 9 | 7 | 0 | 2 | 1.000 | 0.778 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 10 | 8 | 1 | 2 | 0.889 | 0.800 | 
| MaxAnzahlGeschosseOberirdisch | 9 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 9 | 9 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 9 | 9 | 0 | 0 | 1.000 | 1.000 | 
| GebaeudeHoeheMin | 7 |  |  |  |  |  | 
| condition | 3 | 2 | 0 | 1 | 1.000 | 0.667 | 
| content | 4 | 4 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 7 | 6 | 0 | 1 | 1.000 | 0.857 | 
| GaragengebaeudeAusfuehrung | 3 |  |  |  |  |  | 
| condition | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| content | 2 | 1 | 1 | 1 | 0.500 | 0.500 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 1 | 1 | 2 | 0.500 | 0.333 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativUmfangMaximumRelativ | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| Massengliederung | 11 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 11 | 7 | 0 | 4 | 1.000 | 0.636 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 11 | 7 | 0 | 4 | 1.000 | 0.636 | 
| StellplatzregulativUmfangMaximumAbsolut | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 4 | 2 | 0 | 2 | 1.000 | 0.500 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 2 | 0 | 2 | 1.000 | 0.500 | 
| StellplatzMax | 11 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 11 | 6 | 0 | 5 | 1.000 | 0.545 | 
| conditionException | 0 | 0 | 5 | 0 | 0.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 11 | 6 | 5 | 5 | 0.545 | 0.545 | 
| OberflaecheBestimmungP | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 2 | 0 | 1 | 1.000 | 0.667 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 2 | 0 | 1 | 1.000 | 0.667 | 
| InSchutzzone | 5 |  |  |  |  |  | 
| condition | 4 | 2 | 0 | 2 | 1.000 | 0.500 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 2 | 0 | 3 | 1.000 | 0.400 | 
| AnzahlGebaeudeMax | 6 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| FBOKMinimumWohnungen | 5 |  |  |  |  |  | 
| condition | 3 | 0 | 0 | 3 | 1.000 | 0.000 | 
| content | 2 | 2 | 2 | 0 | 0.500 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 2 | 2 | 3 | 0.500 | 0.400 | 
| TechnischeAufbautenHoeheMax | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativUmfangMinimumRelativ | 5 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 5 | 3 | 0 | 2 | 1.000 | 0.600 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 3 | 0 | 2 | 1.000 | 0.600 | 
| GebaeudeEinschraenkungP | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| DurchfahrtHoehe | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMin | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| Kleinhaeuser | 4 |  |  |  |  |  | 
| condition | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| content | 1 | 1 | 2 | 0 | 0.333 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 2 | 2 | 2 | 0.500 | 0.500 | 
| BauklasseVIHoeheMax | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 4 | 1 | 0 | 3 | 1.000 | 0.250 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 1 | 1 | 3 | 0.500 | 0.250 | 
| MaxAnzahlDachgeschosse | 6 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| BauklasseVIHoeheMin | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| StellplatzverpflichtungArt | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotBueroGeschaeftsgebaeude | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeVonWohnungenUnzulaessig | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 2 | 0 | 0 | 2 | 1.000 | 0.000 | 
| contentException | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 2 | 0 | 2 | 1.000 | 0.500 | 
| DurchfahrtBreite | 1 |  |  |  |  |  | 
| condition | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| Geschaeftsstrassen | 2 |  |  |  |  |  | 
| condition | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| VerbotUnterirdischeBauwerkeUeberBaufluchtlinie | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MindestraumhoeheEG | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| HochhausZulaessigGemaessBB | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativVorhanden | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxAnzahlGeschosseOberirdischOhneDachgeschoss | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| VerbotAufenthaltsraum | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungHoeheSockel | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| Einbautrasse | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| GelaendeneigungMin | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AnteilBaumbepflanzung | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| ZulaessigeGeschossanzahlEinkaufszentrum | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotStellplaetzeUndParkgebaeude | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeLaenge | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxHoeheWohngebaeude | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| LaubengangHoehe | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 



## Full details
### Annotator 06

|  Name | Freq | TP | FP | FN | Precision | Recall |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| Planzeichen | 483 |  |  |  |  |  | 
| condition | 480 | 475 | 3 | 5 | 0.994 | 0.990 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 3 | 0 | 0 | 3 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 483 | 475 | 3 | 8 | 0.994 | 0.983 | 
| WidmungUndZweckbestimmung | 263 |  |  |  |  |  | 
| condition | 230 | 37 | 3 | 193 | 0.925 | 0.161 | 
| content | 28 | 21 | 24 | 7 | 0.467 | 0.750 | 
| conditionException | 5 | 2 | 0 | 3 | 1.000 | 0.400 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 263 | 60 | 27 | 203 | 0.690 | 0.228 | 
| Flaechen | 89 |  |  |  |  |  | 
| condition | 13 | 1 | 0 | 12 | 1.000 | 0.077 | 
| content | 76 | 76 | 12 | 0 | 0.864 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 89 | 77 | 12 | 12 | 0.865 | 0.865 | 
| VerkehrsflaecheID | 50 |  |  |  |  |  | 
| condition | 47 | 46 | 2 | 1 | 0.958 | 0.979 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 50 | 47 | 2 | 3 | 0.959 | 0.940 | 
| AnFluchtlinie | 83 |  |  |  |  |  | 
| condition | 83 | 77 | 0 | 6 | 1.000 | 0.928 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 83 | 77 | 0 | 6 | 1.000 | 0.928 | 
| AnordnungGaertnerischeAusgestaltung | 93 |  |  |  |  |  | 
| condition | 30 | 25 | 0 | 5 | 1.000 | 0.833 | 
| content | 62 | 60 | 6 | 2 | 0.909 | 0.968 | 
| conditionException | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 93 | 85 | 6 | 8 | 0.934 | 0.914 | 
| GebaeudeHoeheMax | 98 |  |  |  |  |  | 
| condition | 20 | 14 | 5 | 6 | 0.737 | 0.700 | 
| content | 78 | 73 | 6 | 5 | 0.924 | 0.936 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 98 | 87 | 11 | 11 | 0.888 | 0.888 | 
| Dachart | 76 |  |  |  |  |  | 
| condition | 25 | 21 | 4 | 4 | 0.840 | 0.840 | 
| content | 49 | 44 | 4 | 5 | 0.917 | 0.898 | 
| conditionException | 2 | 0 | 0 | 2 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 76 | 65 | 8 | 11 | 0.890 | 0.855 | 
| WidmungInMehrerenEbenen | 21 |  |  |  |  |  | 
| condition | 3 | 0 | 0 | 3 | 1.000 | 0.000 | 
| content | 18 | 15 | 0 | 3 | 1.000 | 0.833 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 21 | 15 | 0 | 6 | 1.000 | 0.714 | 
| GebaeudeHoeheArt | 85 |  |  |  |  |  | 
| condition | 3 | 0 | 0 | 3 | 1.000 | 0.000 | 
| content | 82 | 81 | 3 | 1 | 0.964 | 0.988 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 85 | 81 | 3 | 4 | 0.964 | 0.953 | 
| VorkehrungBepflanzung | 81 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 81 | 76 | 0 | 5 | 1.000 | 0.938 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 81 | 76 | 0 | 5 | 1.000 | 0.938 | 
| ErrichtungGebaeude | 66 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 66 | 45 | 0 | 21 | 1.000 | 0.682 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 66 | 45 | 0 | 21 | 1.000 | 0.682 | 
| PlangebietAllgemein | 59 |  |  |  |  |  | 
| condition | 59 | 44 | 0 | 15 | 1.000 | 0.746 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 59 | 44 | 0 | 15 | 1.000 | 0.746 | 
| VonBebauungFreizuhalten | 52 |  |  |  |  |  | 
| condition | 0 | 0 | 2 | 0 | 0.000 | 1.000 | 
| content | 52 | 47 | 0 | 5 | 1.000 | 0.904 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 52 | 47 | 2 | 5 | 0.959 | 0.904 | 
| BegruenungDach | 80 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 80 | 79 | 0 | 1 | 1.000 | 0.988 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 80 | 79 | 0 | 1 | 1.000 | 0.988 | 
| AbschlussDachMaxBezugGebaeude | 75 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 75 | 73 | 0 | 2 | 1.000 | 0.973 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 75 | 73 | 1 | 2 | 0.986 | 0.973 | 
| GehsteigbreiteMin | 47 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 47 | 42 | 0 | 5 | 1.000 | 0.894 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 47 | 42 | 0 | 5 | 1.000 | 0.894 | 
| StrassenbreiteMin | 64 |  |  |  |  |  | 
| condition | 64 | 60 | 0 | 4 | 1.000 | 0.938 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 64 | 60 | 0 | 4 | 1.000 | 0.938 | 
| GebaeudeBautyp | 51 |  |  |  |  |  | 
| condition | 51 | 25 | 0 | 26 | 1.000 | 0.490 | 
| content | 0 | 0 | 25 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 51 | 25 | 25 | 26 | 0.500 | 0.490 | 
| AufbautenZulaessig | 59 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 59 | 54 | 0 | 5 | 1.000 | 0.915 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 59 | 54 | 1 | 5 | 0.982 | 0.915 | 
| UnterbrechungGeschlosseneBauweise | 44 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 44 | 42 | 0 | 2 | 1.000 | 0.955 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 44 | 42 | 0 | 2 | 1.000 | 0.955 | 
| DachneigungMax | 42 |  |  |  |  |  | 
| condition | 23 | 23 | 4 | 0 | 0.852 | 1.000 | 
| content | 19 | 12 | 0 | 7 | 1.000 | 0.632 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 42 | 35 | 4 | 7 | 0.897 | 0.833 | 
| AnOeffentlichenVerkehrsflaechen | 14 |  |  |  |  |  | 
| condition | 13 | 11 | 0 | 2 | 1.000 | 0.846 | 
| content | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| conditionException | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 14 | 11 | 1 | 3 | 0.917 | 0.786 | 
| BauweiseID | 19 |  |  |  |  |  | 
| condition | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| content | 16 | 8 | 0 | 8 | 1.000 | 0.500 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 19 | 11 | 0 | 8 | 1.000 | 0.579 | 
| Bauklasse | 27 |  |  |  |  |  | 
| condition | 10 | 7 | 0 | 3 | 1.000 | 0.700 | 
| content | 17 | 13 | 1 | 4 | 0.929 | 0.765 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 27 | 20 | 1 | 7 | 0.952 | 0.741 | 
| EinfriedungAusgestaltung | 30 |  |  |  |  |  | 
| condition | 6 | 0 | 4 | 6 | 0.000 | 0.000 | 
| content | 24 | 20 | 3 | 4 | 0.870 | 0.833 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 30 | 20 | 7 | 10 | 0.741 | 0.667 | 
| DurchgangBreite | 40 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 40 | 38 | 0 | 2 | 1.000 | 0.950 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 40 | 38 | 1 | 2 | 0.974 | 0.950 | 
| AusnahmeGaertnerischAuszugestaltende | 34 |  |  |  |  |  | 
| condition | 0 | 0 | 3 | 0 | 0.000 | 1.000 | 
| content | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| conditionException | 34 | 29 | 0 | 5 | 1.000 | 0.853 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 34 | 29 | 4 | 5 | 0.879 | 0.853 | 
| StrassenbreiteMax | 33 |  |  |  |  |  | 
| condition | 33 | 32 | 0 | 1 | 1.000 | 0.970 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 33 | 32 | 0 | 1 | 1.000 | 0.970 | 
| DurchgangHoehe | 26 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 26 | 25 | 0 | 1 | 1.000 | 0.962 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 26 | 25 | 0 | 1 | 1.000 | 0.962 | 
| UnterirdischeBaulichkeiten | 25 |  |  |  |  |  | 
| condition | 24 | 7 | 0 | 17 | 1.000 | 0.292 | 
| content | 1 | 1 | 9 | 0 | 0.100 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 25 | 8 | 9 | 17 | 0.471 | 0.320 | 
| Struktureinheit | 44 |  |  |  |  |  | 
| condition | 32 | 26 | 8 | 6 | 0.765 | 0.812 | 
| content | 11 | 4 | 1 | 7 | 0.800 | 0.364 | 
| conditionException | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 44 | 30 | 9 | 14 | 0.769 | 0.682 | 
| VolumenUndUmbaubarerRaum | 27 |  |  |  |  |  | 
| condition | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| content | 26 | 25 | 1 | 1 | 0.962 | 0.962 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 27 | 25 | 1 | 2 | 0.962 | 0.926 | 
| EinfriedungHoeheGesamt | 7 |  |  |  |  |  | 
| condition | 1 | 0 | 1 | 1 | 0.000 | 0.000 | 
| content | 6 | 5 | 1 | 1 | 0.833 | 0.833 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 7 | 5 | 2 | 2 | 0.714 | 0.714 | 
| Stockwerk | 18 |  |  |  |  |  | 
| condition | 18 | 3 | 0 | 15 | 1.000 | 0.167 | 
| content | 0 | 0 | 13 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 18 | 3 | 13 | 15 | 0.188 | 0.167 | 
| DachflaecheMin | 24 |  |  |  |  |  | 
| condition | 24 | 23 | 0 | 1 | 1.000 | 0.958 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 24 | 23 | 0 | 1 | 1.000 | 0.958 | 
| EinfriedungLage | 12 |  |  |  |  |  | 
| condition | 12 | 10 | 0 | 2 | 1.000 | 0.833 | 
| content | 0 | 0 | 2 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 12 | 10 | 2 | 2 | 0.833 | 0.833 | 
| AnlageZumEinstellenVorhanden | 14 |  |  |  |  |  | 
| condition | 5 | 1 | 0 | 4 | 1.000 | 0.200 | 
| content | 9 | 5 | 3 | 4 | 0.625 | 0.556 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 14 | 6 | 3 | 8 | 0.667 | 0.429 | 
| VorstehendeBauelementeAusladungMax | 9 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 9 | 8 | 0 | 1 | 1.000 | 0.889 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 9 | 8 | 0 | 1 | 1.000 | 0.889 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen | 22 |  |  |  |  |  | 
| condition | 0 | 0 | 3 | 0 | 0.000 | 1.000 | 
| content | 22 | 19 | 0 | 3 | 1.000 | 0.864 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 22 | 19 | 3 | 3 | 0.864 | 0.864 | 
| EinfriedungZulaessig | 19 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 19 | 17 | 0 | 2 | 1.000 | 0.895 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 19 | 17 | 0 | 2 | 1.000 | 0.895 | 
| VerbotWohnung | 26 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 26 | 25 | 0 | 1 | 1.000 | 0.962 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 26 | 25 | 0 | 1 | 1.000 | 0.962 | 
| StrassenbreiteVonBis | 19 |  |  |  |  |  | 
| condition | 19 | 17 | 0 | 2 | 1.000 | 0.895 | 
| content | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 19 | 17 | 1 | 2 | 0.944 | 0.895 | 
| AnordnungGaertnerischeAusgestaltungProzentual | 15 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 15 | 11 | 0 | 4 | 1.000 | 0.733 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 15 | 11 | 1 | 4 | 0.917 | 0.733 | 
| OeffentlicheVerkehrsflaecheBreiteMin | 7 |  |  |  |  |  | 
| condition | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 7 | 7 | 0 | 0 | 1.000 | 1.000 | 
| VorbautenVerbot | 13 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 13 | 13 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 13 | 13 | 0 | 0 | 1.000 | 1.000 | 
| HoehenlageGrundflaeche | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| VorbautenBeschraenkung | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 3 | 0 | 0 | 1.000 | 1.000 | 
| AnteilDachbegruenung | 15 |  |  |  |  |  | 
| condition | 0 | 0 | 3 | 0 | 0.000 | 1.000 | 
| content | 15 | 12 | 0 | 3 | 1.000 | 0.800 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 15 | 12 | 3 | 3 | 0.800 | 0.800 | 
| EinleitungNiederschlagswaesser | 10 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 10 | 10 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 10 | 10 | 0 | 0 | 1.000 | 1.000 | 
| AbschlussDachMaxBezugGelaende | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| VerbotStaffelung | 5 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeHoehe | 10 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 10 | 10 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 10 | 10 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzImNiveauZulaessig | 8 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 8 | 3 | 0 | 5 | 1.000 | 0.375 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 8 | 3 | 0 | 5 | 1.000 | 0.375 | 
| MaxAnzahlGeschosseOberirdisch | 12 |  |  |  |  |  | 
| condition | 4 | 0 | 0 | 4 | 1.000 | 0.000 | 
| content | 8 | 8 | 4 | 0 | 0.667 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 12 | 8 | 4 | 4 | 0.667 | 0.667 | 
| GebaeudeHoeheMin | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 3 | 1 | 0 | 0.750 | 1.000 | 
| conditionException | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 3 | 1 | 1 | 0.750 | 0.750 | 
| GaragengebaeudeAusfuehrung | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 4 | 2 | 0 | 2 | 1.000 | 0.500 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 2 | 0 | 2 | 1.000 | 0.500 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativUmfangMaximumRelativ | 5 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 5 | 0 | 0 | 1.000 | 1.000 | 
| Massengliederung | 8 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 8 | 3 | 0 | 5 | 1.000 | 0.375 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 8 | 3 | 0 | 5 | 1.000 | 0.375 | 
| StellplatzregulativUmfangMaximumAbsolut | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzMax | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| OberflaecheBestimmungP | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 4 | 3 | 0 | 1 | 1.000 | 0.750 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 3 | 0 | 1 | 1.000 | 0.750 | 
| InSchutzzone | 3 |  |  |  |  |  | 
| condition | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 1 | 0 | 2 | 1.000 | 0.333 | 
| AnzahlGebaeudeMax | 4 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 4 | 3 | 0 | 1 | 1.000 | 0.750 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 3 | 0 | 1 | 1.000 | 0.750 | 
| FBOKMinimumWohnungen | 4 |  |  |  |  |  | 
| condition | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| content | 3 | 2 | 1 | 1 | 0.667 | 0.667 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 4 | 2 | 1 | 2 | 0.667 | 0.500 | 
| TechnischeAufbautenHoeheMax | 5 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 5 | 3 | 0 | 2 | 1.000 | 0.600 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 5 | 3 | 0 | 2 | 1.000 | 0.600 | 
| StellplatzregulativUmfangMinimumRelativ | 6 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| GebaeudeEinschraenkungP | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| DurchfahrtHoehe | 6 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 6 | 6 | 0 | 0 | 1.000 | 1.000 | 
| DachneigungMin | 3 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 3 | 2 | 0 | 1 | 1.000 | 0.667 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 2 | 0 | 1 | 1.000 | 0.667 | 
| Kleinhaeuser | 3 |  |  |  |  |  | 
| condition | 2 | 0 | 0 | 2 | 1.000 | 0.000 | 
| content | 1 | 1 | 2 | 0 | 0.333 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 3 | 1 | 2 | 2 | 0.333 | 0.333 | 
| BauklasseVIHoeheMax | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| MaxAnzahlDachgeschosse | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| BauklasseVIHoeheMin | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzverpflichtungArt | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotBueroGeschaeftsgebaeude | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 1 | 0 | 1 | 1.000 | 0.500 | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AusnahmeVonWohnungenUnzulaessig | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| DurchfahrtBreite | 2 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| Geschaeftsstrassen | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotUnterirdischeBauwerkeUeberBaufluchtlinie | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MindestraumhoeheEG | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| HochhausZulaessigGemaessBB | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| StellplatzregulativVorhanden | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxAnzahlGeschosseOberirdischOhneDachgeschoss | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotAufenthaltsraum | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| EinfriedungHoeheSockel | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| Einbautrasse | 2 |  |  |  |  |  | 
| condition | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| content | 1 | 1 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 2 | 2 | 0 | 0 | 1.000 | 1.000 | 
| GelaendeneigungMin | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| AnteilBaumbepflanzung | 1 |  |  |  |  |  | 
| condition | 0 | 0 | 1 | 0 | 0.000 | 1.000 | 
| content | 1 | 0 | 0 | 1 | 1.000 | 0.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 1 | 0 | 1 | 1 | 0.000 | 0.000 | 
| ZulaessigeGeschossanzahlEinkaufszentrum | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| VerbotStellplaetzeUndParkgebaeude | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| ArkadeLaenge | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| MaxHoeheWohngebaeude | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| LaubengangHoehe | 0 |  |  |  |  |  | 
| condition | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| content | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| conditionException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| contentException | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 
| micro | 0 | 0 | 0 | 0 | 1.000 | 1.000 | 


