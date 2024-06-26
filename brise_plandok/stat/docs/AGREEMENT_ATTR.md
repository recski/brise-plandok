# Annotator agreement - Attributes
This statistics is calculated without the sentences with a segmentation error.  
Only sentences containing a rule (a.k.a. gold_modality != None) are taken into account.  
We use Cohen's kappa for calculating the inter-annotator agreement: [cohen_kappa_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html).  
Frequencies are calculated as the number of sentences where the attribute appears as either gold or annotated either in the first or in the second phase.
## Without kappa correction

|  Attr | Freq | Macro | Weighted | ('01', '02') | ('01', '03') | ('01', '04') | ('01', '05') | ('01', '06') | ('02', '03') | ('02', '04') | ('02', '05') | ('02', '06') | ('03', '04') | ('03', '05') | ('03', '06') | ('04', '05') | ('04', '06') | ('05', '06') |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| Number of sentences | - | - | - | 376 | 79 | 174 | 339 | 358 | 313 | 333 | 88 | 190 | 360 | 137 | 330 | 483 | 88 | 345 | 
| Planzeichen | 1987 | 0.9789 | 0.9862 | 0.9754 | 0.9480 | 0.9649 | 1.0000 | 1.0000 | 0.9865 | 0.9938 | 0.9741 | 0.9788 | 0.9884 | 0.9389 | 1.0000 | 1.0000 | 0.9526 | 0.9819 | 
| WidmungUndZweckbestimmung | 1161 | 0.8183 | 0.8774 | 0.9522 | 0.9341 | 0.9169 | 0.8637 | 0.9730 | 0.9245 | 0.9164 | 0.6430 | 0.6753 | 0.9735 | 0.8182 | 1.0000 | 0.8572 | 0.0000 | 0.8256 | 
| Flaechen | 791 | 0.8813 | 0.8999 | 0.9361 | 0.9017 | 0.7869 | 0.8205 | 0.9888 | 1.0000 | 0.9173 | 0.8394 | 0.9486 | 0.9519 | 0.7813 | 1.0000 | 0.9458 | 0.7454 | 0.6556 | 
| VerkehrsflaecheID | 457 | 0.9671 | 0.9799 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8764 | 1.0000 | 0.9367 | 0.8278 | 1.0000 | 0.9865 | 0.9036 | 0.9762 | 
| AnFluchtlinie | 393 | 0.8834 | 0.9281 | 0.9354 | 0.8433 | 0.6179 | 1.0000 | 0.9535 | 1.0000 | 1.0000 | 0.5937 | 0.8880 | 0.9809 | 0.9373 | 1.0000 | 0.9051 | 0.6489 | 0.9476 | 
| AnordnungGaertnerischeAusgestaltung | 356 | 0.9448 | 0.9460 | 0.9142 | 1.0000 | 0.9493 | 0.9568 | 0.9699 | 0.9770 | 0.9194 | 0.9410 | 0.9035 | 0.9803 | 1.0000 | 1.0000 | 0.9051 | 0.8211 | 0.9341 | 
| GebaeudeHoeheMax | 333 | 0.9314 | 0.9516 | 0.9572 | 0.9023 | 1.0000 | 1.0000 | 0.9741 | 1.0000 | 0.9644 | 0.7944 | 0.9757 | 0.9257 | 0.7426 | 1.0000 | 0.9242 | 0.8514 | 0.9597 | 
| Dachart | 303 | 0.9697 | 0.9812 | 1.0000 | 1.0000 | 0.9201 | 0.9780 | 1.0000 | 0.9466 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9193 | 1.0000 | 1.0000 | 0.8072 | 0.9741 | 
| WidmungInMehrerenEbenen | 294 | 0.8913 | 0.9027 | 0.8991 | 1.0000 | 0.9169 | 0.9196 | 1.0000 | 0.8195 | 0.7894 | 1.0000 | 0.8774 | 1.0000 | 0.4389 | 1.0000 | 0.9240 | nan | 0.8938 | 
| GebaeudeHoeheArt | 290 | 0.9075 | 0.9486 | 0.9260 | 0.6550 | 0.7972 | 1.0000 | 1.0000 | 1.0000 | 0.9681 | 0.6508 | 0.8716 | 1.0000 | 1.0000 | 1.0000 | 0.9519 | 0.8215 | 0.9699 | 
| VorkehrungBepflanzung | 282 | 0.9630 | 0.9776 | 0.9685 | 1.0000 | 1.0000 | 0.9808 | 1.0000 | 0.9779 | 0.9714 | 0.9170 | 0.9537 | 1.0000 | 0.9087 | 0.9780 | 1.0000 | 0.7885 | 1.0000 | 
| ErrichtungGebaeude | 271 | 0.6791 | 0.7547 | 0.9460 | 0.0000 | 0.5029 | 0.8651 | 1.0000 | 0.8305 | 0.8136 | 0.0000 | 1.0000 | 0.9138 | 0.6532 | 1.0000 | 0.3216 | nan | 0.6609 | 
| PlangebietAllgemein | 269 | 0.7709 | 0.8606 | 0.5846 | nan | 0.8543 | 1.0000 | 0.9551 | 1.0000 | 1.0000 | -0.0280 | 0.7450 | 0.7943 | 1.0000 | 1.0000 | 0.9059 | -0.0185 | 1.0000 | 
| VonBebauungFreizuhalten | 255 | 0.8493 | 0.8693 | 0.9203 | 0.6489 | 0.8211 | 0.9614 | 1.0000 | 0.8821 | 0.9066 | 1.0000 | 0.9446 | 0.8607 | 0.4888 | 1.0000 | 0.7409 | 0.7885 | 0.7752 | 
| BegruenungDach | 247 | 0.9846 | 0.9865 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9639 | 1.0000 | 1.0000 | 0.9494 | 1.0000 | 1.0000 | 0.9719 | 0.8830 | 1.0000 | 
| AbschlussDachMaxBezugGebaeude | 235 | 0.9729 | 0.9841 | 1.0000 | 1.0000 | 0.8543 | 1.0000 | 1.0000 | 1.0000 | 0.9681 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9819 | 0.7885 | 1.0000 | 
| GehsteigbreiteMin | 213 | 0.9831 | 0.9885 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9384 | 1.0000 | 1.0000 | 1.0000 | 0.9562 | 0.8514 | 1.0000 | 
| StrassenbreiteMin | 207 | 0.9454 | 0.9583 | 0.8517 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6918 | 1.0000 | 0.9099 | 0.7927 | 1.0000 | 1.0000 | 1.0000 | 0.9345 | 
| GebaeudeBautyp | 207 | 0.9691 | 0.9695 | 0.9773 | 0.8823 | 1.0000 | 0.9614 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9193 | 1.0000 | 0.9312 | 1.0000 | 0.8651 | 
| AufbautenZulaessig | 176 | 0.9752 | 0.9828 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9572 | 0.9641 | 1.0000 | 0.9458 | 1.0000 | 0.7944 | 0.9662 | 
| UnterbrechungGeschlosseneBauweise | 158 | 0.9935 | 0.9928 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9384 | 1.0000 | 1.0000 | 1.0000 | 0.9645 | 1.0000 | 1.0000 | 
| DachneigungMax | 146 | 0.9803 | 0.9873 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8862 | 1.0000 | 1.0000 | 1.0000 | 0.9667 | 0.8514 | 1.0000 | 
| AnOeffentlichenVerkehrsflaechen | 143 | 0.6950 | 0.7779 | 0.9510 | 0.6609 | 0.7941 | 0.7472 | 0.9077 | 0.8982 | 0.6915 | 0.0000 | 0.6643 | 0.9257 | 0.0000 | 1.0000 | 0.6919 | 0.6615 | 0.8305 | 
| BauweiseID | 123 | 0.7122 | 0.8209 | 1.0000 | 0.7937 | 0.0000 | 1.0000 | 1.0000 | 0.9395 | 0.9396 | nan | 0.0000 | 1.0000 | -0.0139 | 1.0000 | nan | nan | 0.8874 | 
| Bauklasse | 118 | 0.9196 | 0.9088 | 1.0000 | 1.0000 | nan | 0.8274 | 1.0000 | 0.9613 | 0.9076 | nan | 0.8153 | 1.0000 | nan | 1.0000 | 0.6639 | nan | 0.9397 | 
| EinfriedungAusgestaltung | 117 | 0.8816 | 0.9211 | 1.0000 | 1.0000 | 1.0000 | 0.9459 | 0.9551 | 1.0000 | 1.0000 | 1.0000 | 0.6643 | 0.8306 | 1.0000 | 1.0000 | 0.9401 | 0.0000 | 0.8874 | 
| DurchgangBreite | 113 | 0.9067 | 0.9407 | 1.0000 | nan | 0.9061 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8722 | 0.3893 | 1.0000 | 0.9323 | 0.6615 | 0.9319 | 
| AusnahmeGaertnerischAuszugestaltende | 110 | 0.7221 | 0.8220 | 0.7726 | 0.0000 | 0.7445 | 1.0000 | 1.0000 | 1.0000 | 0.6653 | nan | 0.7450 | 1.0000 | nan | 1.0000 | 0.7990 | 0.0000 | 0.6614 | 
| StrassenbreiteMax | 105 | 0.8405 | 0.9151 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8830 | 1.0000 | 0.8653 | 0.0000 | 1.0000 | 0.9513 | 0.0000 | 0.9076 | 
| DurchgangHoehe | 105 | 0.9301 | 0.9552 | 1.0000 | nan | 1.0000 | 0.9614 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6643 | 0.8544 | 0.8852 | 1.0000 | 1.0000 | 0.6562 | 1.0000 | 
| UnterirdischeBaulichkeiten | 99 | 0.7808 | 0.8237 | 0.9586 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 0.8539 | 0.8720 | 0.6615 | 0.0000 | 0.9217 | 1.0000 | 1.0000 | 0.6636 | nan | 1.0000 | 
| Struktureinheit | 97 | 0.7700 | 0.7664 | 0.9078 | nan | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | nan | 0.6545 | nan | 1.0000 | 1.0000 | 0.0000 | nan | 0.9076 | 
| VolumenUndUmbaubarerRaum | 94 | 0.9875 | 0.9877 | 1.0000 | 1.0000 | 0.9443 | 1.0000 | 1.0000 | 1.0000 | 0.9614 | nan | 1.0000 | 0.9319 | 1.0000 | 1.0000 | 1.0000 | nan | 1.0000 | 
| EinfriedungHoeheGesamt | 90 | 0.9766 | 0.9653 | 0.9460 | 1.0000 | 1.0000 | 0.9397 | 1.0000 | 1.0000 | 0.9550 | 1.0000 | 1.0000 | 0.9217 | 1.0000 | 1.0000 | 0.8868 | 1.0000 | 1.0000 | 
| Stockwerk | 85 | 0.7537 | 0.8402 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9396 | 0.0000 | 0.8545 | 0.7959 | 0.3251 | 1.0000 | 0.7244 | 0.0000 | 0.6654 | 
| DachflaecheMin | 84 | 0.9713 | 0.9751 | 1.0000 | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.7472 | 0.8514 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| EinfriedungLage | 77 | 0.7606 | 0.8664 | 1.0000 | 1.0000 | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.6643 | 0.8306 | 0.0000 | 1.0000 | 1.0000 | 0.4884 | 0.6654 | 
| AnlageZumEinstellenVorhanden | 77 | 0.8121 | 0.8682 | 0.8973 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | nan | 1.0000 | 1.0000 | 0.6600 | 1.0000 | 1.0000 | nan | 1.0000 | 
| VorstehendeBauelementeAusladungMax | 69 | 0.9187 | 0.9454 | 1.0000 | nan | 0.8543 | 1.0000 | 1.0000 | 1.0000 | 0.7971 | 0.4913 | 0.7974 | 1.0000 | 1.0000 | 1.0000 | 0.9220 | 1.0000 | 1.0000 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen | 68 | 0.9106 | 0.9631 | 0.9320 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.7944 | 1.0000 | 0.9319 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| EinfriedungZulaessig | 66 | 0.7921 | 0.8859 | 1.0000 | 0.0000 | 0.7184 | 1.0000 | 0.9077 | 1.0000 | 0.7971 | 0.0000 | 1.0000 | 0.6642 | 1.0000 | 1.0000 | 1.0000 | 0.7944 | 1.0000 | 
| VerbotWohnung | 61 | 0.9868 | 0.9806 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8558 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9463 | 1.0000 | 1.0000 | 
| StrassenbreiteVonBis | 59 | 0.7476 | 0.7642 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8722 | -0.0098 | 1.0000 | 0.4961 | 0.0000 | 0.8557 | 
| AnordnungGaertnerischeAusgestaltungProzentual | 55 | 0.8332 | 0.8663 | 0.7974 | 1.0000 | nan | 0.8541 | 1.0000 | 0.6638 | 0.8304 | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8879 | 0.0000 | 0.7986 | 
| OeffentlicheVerkehrsflaecheBreiteMin | 54 | 0.7157 | 0.7575 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | nan | 0.0000 | 0.0000 | 0.9398 | 0.6634 | 1.0000 | 0.7008 | nan | 1.0000 | 
| VorbautenVerbot | 48 | 0.8243 | 0.9104 | 1.0000 | 0.0000 | 1.0000 | 0.8557 | 0.8558 | 1.0000 | 1.0000 | 1.0000 | 0.7974 | 0.8558 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 
| HoehenlageGrundflaeche | 47 | 0.7047 | 0.6952 | 1.0000 | nan | 0.7972 | 0.0000 | 0.4979 | 1.0000 | 0.8541 | nan | 1.0000 | 1.0000 | nan | nan | 0.8979 | nan | 0.0000 | 
| VorbautenBeschraenkung | 41 | 0.6303 | 0.7365 | 1.0000 | 0.0000 | 0.6641 | 0.7986 | 0.9398 | 1.0000 | 0.0000 | nan | nan | 0.6642 | nan | 1.0000 | 1.0000 | 0.0000 | 0.4971 | 
| AnteilDachbegruenung | 41 | 0.8499 | 0.9139 | 1.0000 | nan | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.4979 | nan | nan | 1.0000 | 0.8514 | 1.0000 | 
| EinleitungNiederschlagswaesser | 39 | 0.9897 | 0.9881 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8556 | 1.0000 | 1.0000 | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| AbschlussDachMaxBezugGelaende | 37 | 0.4601 | 0.5767 | 1.0000 | 0.0000 | 0.0000 | 0.6654 | nan | 1.0000 | 0.0000 | nan | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 0.3960 | nan | nan | 
| VerbotStaffelung | 34 | 0.7821 | 0.8687 | 1.0000 | 0.0000 | 0.7972 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.7987 | 0.6634 | 1.0000 | 0.9081 | nan | nan | 
| ArkadeHoehe | 32 | 0.8678 | 0.9244 | 1.0000 | nan | nan | 0.7472 | 1.0000 | 1.0000 | nan | 1.0000 | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.7986 | 
| StellplatzImNiveauZulaessig | 31 | 0.9000 | 0.9747 | 1.0000 | 0.0000 | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | nan | nan | 1.0000 | 1.0000 | nan | 1.0000 | nan | 1.0000 | 
| MaxAnzahlGeschosseOberirdisch | 27 | 0.8729 | 0.8679 | 1.0000 | nan | nan | nan | 1.0000 | 0.0000 | 1.0000 | nan | 1.0000 | 1.0000 | 1.0000 | nan | 0.8561 | nan | 1.0000 | 
| GebaeudeHoeheMin | 27 | 0.8076 | 0.8931 | 1.0000 | nan | nan | nan | 1.0000 | nan | nan | 0.0000 | 0.6643 | 1.0000 | 1.0000 | nan | 0.7969 | nan | 1.0000 | 
| GaragengebaeudeAusfuehrung | 26 | 0.7273 | 0.8746 | 1.0000 | nan | 0.0000 | 1.0000 | 1.0000 | nan | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 0.0000 | nan | 1.0000 | nan | 1.0000 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben | 26 | 0.7147 | 0.8565 | 1.0000 | 0.0000 | nan | 1.0000 | nan | 0.6652 | nan | nan | nan | nan | nan | nan | 0.9081 | nan | nan | 
| StellplatzregulativUmfangMaximumRelativ | 25 | 0.6962 | 0.8013 | 1.0000 | nan | 0.0000 | 0.6654 | 1.0000 | 1.0000 | 0.6640 | nan | nan | 0.6654 | 0.6634 | 1.0000 | 1.0000 | 0.0000 | nan | 
| Massengliederung | 24 | 0.6250 | 0.8593 | nan | 0.0000 | nan | 1.0000 | nan | nan | nan | 0.0000 | nan | 1.0000 | 0.0000 | 1.0000 | 1.0000 | nan | 1.0000 | 
| StellplatzregulativUmfangMaximumAbsolut | 23 | 0.9077 | 0.9059 | 1.0000 | nan | nan | 0.7971 | 1.0000 | 0.6652 | 1.0000 | nan | nan | nan | nan | 1.0000 | 0.7990 | nan | 1.0000 | 
| StellplatzMax | 23 | 0.9522 | 0.9584 | 1.0000 | nan | nan | 1.0000 | nan | 0.6652 | 1.0000 | nan | nan | nan | nan | 1.0000 | 1.0000 | nan | 1.0000 | 
| OberflaecheBestimmungP | 23 | 0.5297 | 0.6373 | 0.4980 | nan | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | nan | nan | nan | nan | 0.7986 | 
| InSchutzzone | 22 | 0.9656 | 0.9917 | 1.0000 | 0.7937 | nan | nan | nan | nan | 1.0000 | nan | nan | 1.0000 | nan | 1.0000 | 1.0000 | nan | nan | 
| AnzahlGebaeudeMax | 21 | 0.9565 | 0.9479 | 0.8558 | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | nan | 1.0000 | nan | nan | 1.0000 | 1.0000 | 0.6654 | 
| FBOKMinimumWohnungen | 20 | 0.8889 | 0.9340 | nan | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | nan | 0.0000 | 1.0000 | nan | 1.0000 | 1.0000 | nan | nan | 
| TechnischeAufbautenHoeheMax | 18 | 0.7248 | 0.8943 | 0.7987 | nan | nan | 1.0000 | nan | 1.0000 | 1.0000 | 0.0000 | nan | 1.0000 | nan | nan | 1.0000 | 0.0000 | nan | 
| StellplatzregulativUmfangMinimumRelativ | 18 | 0.6847 | 0.7344 | 1.0000 | nan | 0.6641 | 0.4978 | 1.0000 | 1.0000 | nan | nan | nan | 0.0000 | 0.0000 | 1.0000 | nan | nan | 1.0000 | 
| GebaeudeEinschraenkungP | 17 | 0.8333 | 0.9159 | 1.0000 | nan | 0.0000 | nan | 1.0000 | nan | 1.0000 | nan | nan | nan | nan | nan | 1.0000 | nan | 1.0000 | 
| DurchfahrtHoehe | 17 | 0.4998 | 0.5379 | 1.0000 | nan | nan | nan | 1.0000 | nan | 1.0000 | nan | 1.0000 | 0.4979 | 0.0000 | nan | 0.0000 | 0.0000 | 0.0000 | 
| DachneigungMin | 17 | 0.8182 | 0.9006 | nan | 1.0000 | 1.0000 | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | nan | 1.0000 | 1.0000 | 0.0000 | nan | 
| Kleinhaeuser | 16 | 0.7770 | 0.9219 | 1.0000 | 0.0000 | nan | 1.0000 | 1.0000 | 1.0000 | 1.0000 | nan | nan | 1.0000 | -0.0074 | nan | 1.0000 | nan | nan | 
| BauklasseVIHoeheMax | 16 | 0.6000 | 0.6819 | nan | nan | 0.0000 | 1.0000 | nan | 0.0000 | nan | nan | nan | 1.0000 | nan | nan | nan | nan | 1.0000 | 
| MaxAnzahlDachgeschosse | 14 | 0.9325 | 0.9528 | nan | nan | nan | 1.0000 | 1.0000 | nan | 0.7985 | nan | nan | 1.0000 | 0.7964 | nan | 1.0000 | nan | nan | 
| BauklasseVIHoeheMin | 14 | 0.6667 | 0.6925 | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | 1.0000 | nan | nan | nan | nan | 1.0000 | 
| StellplatzverpflichtungArt | 12 | 0.6665 | 0.7529 | 1.0000 | nan | nan | 0.0000 | 1.0000 | 0.6652 | 1.0000 | nan | nan | nan | nan | nan | nan | 0.0000 | 1.0000 | 
| VerbotBueroGeschaeftsgebaeude | 11 | 0.7248 | 0.7893 | 0.7987 | nan | 1.0000 | nan | 1.0000 | 1.0000 | 1.0000 | nan | nan | 0.0000 | nan | nan | 1.0000 | 0.0000 | nan | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau | 11 | 0.0000 | 0.0000 | nan | nan | 0.0000 | nan | nan | nan | 0.0000 | nan | nan | 0.0000 | nan | nan | nan | nan | nan | 
| AusnahmeVonWohnungenUnzulaessig | 10 | 0.5994 | 0.5895 | nan | nan | 1.0000 | nan | 1.0000 | nan | nan | nan | nan | -0.0028 | nan | nan | 1.0000 | nan | 0.0000 | 
| DurchfahrtBreite | 9 | 0.7328 | 0.8745 | 1.0000 | nan | nan | nan | 1.0000 | nan | nan | nan | nan | 0.6642 | nan | nan | 1.0000 | 0.0000 | nan | 
| Geschaeftsstrassen | 8 | 0.7500 | 0.9302 | 1.0000 | nan | nan | nan | nan | 1.0000 | nan | nan | nan | nan | nan | nan | 1.0000 | 0.0000 | nan | 
| VerbotUnterirdischeBauwerkeUeberBaufluchtlinie | 7 | 0.4000 | 0.3962 | nan | nan | nan | nan | nan | 1.0000 | nan | nan | nan | 0.0000 | 0.0000 | 1.0000 | 0.0000 | nan | nan | 
| MindestraumhoeheEG | 7 | 1.0000 | 1.0000 | nan | nan | nan | nan | nan | 1.0000 | nan | nan | nan | nan | nan | 1.0000 | 1.0000 | nan | nan | 
| HochhausZulaessigGemaessBB | 7 | 0.7331 | 0.6736 | 0.6655 | nan | nan | nan | nan | 1.0000 | 1.0000 | nan | nan | 1.0000 | nan | nan | 0.0000 | nan | nan | 
| StellplatzregulativVorhanden | 6 | 0.9330 | 0.9386 | 1.0000 | nan | nan | 1.0000 | nan | 0.6652 | 1.0000 | nan | nan | nan | nan | nan | nan | nan | 1.0000 | 
| MaxAnzahlGeschosseOberirdischOhneDachgeschoss | 6 | 1.0000 | 1.0000 | nan | nan | nan | nan | nan | nan | 1.0000 | nan | nan | 1.0000 | nan | nan | 1.0000 | nan | nan | 
| VerbotAufenthaltsraum | 4 | 0.5000 | 0.5303 | 1.0000 | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | 
| EinfriedungHoeheSockel | 4 | 0.5000 | 0.5919 | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | nan | nan | 1.0000 | nan | nan | 
| Einbautrasse | 4 | 0.6667 | 0.6178 | nan | nan | nan | 0.0000 | 1.0000 | nan | nan | nan | 1.0000 | nan | nan | nan | nan | nan | nan | 
| GelaendeneigungMin | 3 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| AnteilBaumbepflanzung | 3 | 0.3333 | 0.2867 | nan | nan | 1.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | 0.0000 | 
| ZulaessigeGeschossanzahlEinkaufszentrum | 2 | 1.0000 | 1.0000 | 1.0000 | nan | nan | nan | nan | 1.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 
| VerbotStellplaetzeUndParkgebaeude | 2 | 1.0000 | 1.0000 | nan | nan | nan | nan | nan | nan | 1.0000 | nan | nan | nan | 1.0000 | nan | nan | nan | nan | 
| ArkadeLaenge | 2 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | nan | nan | 
| MaxHoeheWohngebaeude | 1 | 0.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | 0.0000 | nan | nan | nan | nan | nan | nan | 
| LaubengangHoehe | 1 | 1.0000 | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | nan | 1.0000 | nan | nan | 


## With kappa correction
[cohen_kappa_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.cohen_kappa_score.html) results in `nan` if both vectors are uniform and the same.
In the table below, we substituted these `nan` values by the value of complete agreement (1.0).

|  Attr | Freq | Macro | Weighted | ('01', '02') | ('01', '03') | ('01', '04') | ('01', '05') | ('01', '06') | ('02', '03') | ('02', '04') | ('02', '05') | ('02', '06') | ('03', '04') | ('03', '05') | ('03', '06') | ('04', '05') | ('04', '06') | ('05', '06') |
|-------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | 
| Overall | - | 0.8878 | 0.9103 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | 
| Overall weighted | - | 0.9019 | 0.9273 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | 
| Number of sentences | - | - | - | 376 | 79 | 174 | 339 | 358 | 313 | 333 | 88 | 190 | 360 | 137 | 330 | 483 | 88 | 345 | 
| Planzeichen | 1987 | 0.9789 | 0.9862 | 0.9754 | 0.9480 | 0.9649 | 1.0000 | 1.0000 | 0.9865 | 0.9938 | 0.9741 | 0.9788 | 0.9884 | 0.9389 | 1.0000 | 1.0000 | 0.9526 | 0.9819 | 
| WidmungUndZweckbestimmung | 1161 | 0.8183 | 0.8774 | 0.9522 | 0.9341 | 0.9169 | 0.8637 | 0.9730 | 0.9245 | 0.9164 | 0.6430 | 0.6753 | 0.9735 | 0.8182 | 1.0000 | 0.8572 | 0.0000 | 0.8256 | 
| Flaechen | 791 | 0.8813 | 0.8999 | 0.9361 | 0.9017 | 0.7869 | 0.8205 | 0.9888 | 1.0000 | 0.9173 | 0.8394 | 0.9486 | 0.9519 | 0.7813 | 1.0000 | 0.9458 | 0.7454 | 0.6556 | 
| VerkehrsflaecheID | 457 | 0.9671 | 0.9799 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8764 | 1.0000 | 0.9367 | 0.8278 | 1.0000 | 0.9865 | 0.9036 | 0.9762 | 
| AnFluchtlinie | 393 | 0.8834 | 0.9281 | 0.9354 | 0.8433 | 0.6179 | 1.0000 | 0.9535 | 1.0000 | 1.0000 | 0.5937 | 0.8880 | 0.9809 | 0.9373 | 1.0000 | 0.9051 | 0.6489 | 0.9476 | 
| AnordnungGaertnerischeAusgestaltung | 356 | 0.9448 | 0.9460 | 0.9142 | 1.0000 | 0.9493 | 0.9568 | 0.9699 | 0.9770 | 0.9194 | 0.9410 | 0.9035 | 0.9803 | 1.0000 | 1.0000 | 0.9051 | 0.8211 | 0.9341 | 
| GebaeudeHoeheMax | 333 | 0.9314 | 0.9516 | 0.9572 | 0.9023 | 1.0000 | 1.0000 | 0.9741 | 1.0000 | 0.9644 | 0.7944 | 0.9757 | 0.9257 | 0.7426 | 1.0000 | 0.9242 | 0.8514 | 0.9597 | 
| Dachart | 303 | 0.9697 | 0.9812 | 1.0000 | 1.0000 | 0.9201 | 0.9780 | 1.0000 | 0.9466 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9193 | 1.0000 | 1.0000 | 0.8072 | 0.9741 | 
| WidmungInMehrerenEbenen | 294 | 0.8986 | 0.9049 | 0.8991 | 1.0000 | 0.9169 | 0.9196 | 1.0000 | 0.8195 | 0.7894 | 1.0000 | 0.8774 | 1.0000 | 0.4389 | 1.0000 | 0.9240 | 1.0000 | 0.8938 | 
| GebaeudeHoeheArt | 290 | 0.9075 | 0.9486 | 0.9260 | 0.6550 | 0.7972 | 1.0000 | 1.0000 | 1.0000 | 0.9681 | 0.6508 | 0.8716 | 1.0000 | 1.0000 | 1.0000 | 0.9519 | 0.8215 | 0.9699 | 
| VorkehrungBepflanzung | 282 | 0.9630 | 0.9776 | 0.9685 | 1.0000 | 1.0000 | 0.9808 | 1.0000 | 0.9779 | 0.9714 | 0.9170 | 0.9537 | 1.0000 | 0.9087 | 0.9780 | 1.0000 | 0.7885 | 1.0000 | 
| ErrichtungGebaeude | 271 | 0.7005 | 0.7601 | 0.9460 | 0.0000 | 0.5029 | 0.8651 | 1.0000 | 0.8305 | 0.8136 | 0.0000 | 1.0000 | 0.9138 | 0.6532 | 1.0000 | 0.3216 | 1.0000 | 0.6609 | 
| PlangebietAllgemein | 269 | 0.7862 | 0.8633 | 0.5846 | 1.0000 | 0.8543 | 1.0000 | 0.9551 | 1.0000 | 1.0000 | -0.0280 | 0.7450 | 0.7943 | 1.0000 | 1.0000 | 0.9059 | -0.0185 | 1.0000 | 
| VonBebauungFreizuhalten | 255 | 0.8493 | 0.8693 | 0.9203 | 0.6489 | 0.8211 | 0.9614 | 1.0000 | 0.8821 | 0.9066 | 1.0000 | 0.9446 | 0.8607 | 0.4888 | 1.0000 | 0.7409 | 0.7885 | 0.7752 | 
| BegruenungDach | 247 | 0.9846 | 0.9865 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9639 | 1.0000 | 1.0000 | 0.9494 | 1.0000 | 1.0000 | 0.9719 | 0.8830 | 1.0000 | 
| AbschlussDachMaxBezugGebaeude | 235 | 0.9729 | 0.9841 | 1.0000 | 1.0000 | 0.8543 | 1.0000 | 1.0000 | 1.0000 | 0.9681 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9819 | 0.7885 | 1.0000 | 
| GehsteigbreiteMin | 213 | 0.9831 | 0.9885 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9384 | 1.0000 | 1.0000 | 1.0000 | 0.9562 | 0.8514 | 1.0000 | 
| StrassenbreiteMin | 207 | 0.9454 | 0.9583 | 0.8517 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6918 | 1.0000 | 0.9099 | 0.7927 | 1.0000 | 1.0000 | 1.0000 | 0.9345 | 
| GebaeudeBautyp | 207 | 0.9691 | 0.9695 | 0.9773 | 0.8823 | 1.0000 | 0.9614 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9193 | 1.0000 | 0.9312 | 1.0000 | 0.8651 | 
| AufbautenZulaessig | 176 | 0.9752 | 0.9828 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9572 | 0.9641 | 1.0000 | 0.9458 | 1.0000 | 0.7944 | 0.9662 | 
| UnterbrechungGeschlosseneBauweise | 158 | 0.9935 | 0.9928 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9384 | 1.0000 | 1.0000 | 1.0000 | 0.9645 | 1.0000 | 1.0000 | 
| DachneigungMax | 146 | 0.9803 | 0.9873 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8862 | 1.0000 | 1.0000 | 1.0000 | 0.9667 | 0.8514 | 1.0000 | 
| AnOeffentlichenVerkehrsflaechen | 143 | 0.6950 | 0.7779 | 0.9510 | 0.6609 | 0.7941 | 0.7472 | 0.9077 | 0.8982 | 0.6915 | 0.0000 | 0.6643 | 0.9257 | 0.0000 | 1.0000 | 0.6919 | 0.6615 | 0.8305 | 
| BauweiseID | 123 | 0.7698 | 0.8505 | 1.0000 | 0.7937 | 0.0000 | 1.0000 | 1.0000 | 0.9395 | 0.9396 | 1.0000 | 0.0000 | 1.0000 | -0.0139 | 1.0000 | 1.0000 | 1.0000 | 0.8874 | 
| Bauklasse | 118 | 0.9410 | 0.9199 | 1.0000 | 1.0000 | 1.0000 | 0.8274 | 1.0000 | 0.9613 | 0.9076 | 1.0000 | 0.8153 | 1.0000 | 1.0000 | 1.0000 | 0.6639 | 1.0000 | 0.9397 | 
| EinfriedungAusgestaltung | 117 | 0.8816 | 0.9211 | 1.0000 | 1.0000 | 1.0000 | 0.9459 | 0.9551 | 1.0000 | 1.0000 | 1.0000 | 0.6643 | 0.8306 | 1.0000 | 1.0000 | 0.9401 | 0.0000 | 0.8874 | 
| DurchgangBreite | 113 | 0.9129 | 0.9419 | 1.0000 | 1.0000 | 0.9061 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8722 | 0.3893 | 1.0000 | 0.9323 | 0.6615 | 0.9319 | 
| AusnahmeGaertnerischAuszugestaltende | 110 | 0.7592 | 0.8320 | 0.7726 | 0.0000 | 0.7445 | 1.0000 | 1.0000 | 1.0000 | 0.6653 | 1.0000 | 0.7450 | 1.0000 | 1.0000 | 1.0000 | 0.7990 | 0.0000 | 0.6614 | 
| StrassenbreiteMax | 105 | 0.8405 | 0.9151 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8830 | 1.0000 | 0.8653 | 0.0000 | 1.0000 | 0.9513 | 0.0000 | 0.9076 | 
| DurchgangHoehe | 105 | 0.9348 | 0.9561 | 1.0000 | 1.0000 | 1.0000 | 0.9614 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6643 | 0.8544 | 0.8852 | 1.0000 | 1.0000 | 0.6562 | 1.0000 | 
| UnterirdischeBaulichkeiten | 99 | 0.7954 | 0.8276 | 0.9586 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 0.8539 | 0.8720 | 0.6615 | 0.0000 | 0.9217 | 1.0000 | 1.0000 | 0.6636 | 1.0000 | 1.0000 | 
| Struktureinheit | 97 | 0.8313 | 0.8024 | 0.9078 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6545 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.9076 | 
| VolumenUndUmbaubarerRaum | 94 | 0.9892 | 0.9882 | 1.0000 | 1.0000 | 0.9443 | 1.0000 | 1.0000 | 1.0000 | 0.9614 | 1.0000 | 1.0000 | 0.9319 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| EinfriedungHoeheGesamt | 90 | 0.9766 | 0.9653 | 0.9460 | 1.0000 | 1.0000 | 0.9397 | 1.0000 | 1.0000 | 0.9550 | 1.0000 | 1.0000 | 0.9217 | 1.0000 | 1.0000 | 0.8868 | 1.0000 | 1.0000 | 
| Stockwerk | 85 | 0.7537 | 0.8402 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9396 | 0.0000 | 0.8545 | 0.7959 | 0.3251 | 1.0000 | 0.7244 | 0.0000 | 0.6654 | 
| DachflaecheMin | 84 | 0.9732 | 0.9756 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.7472 | 0.8514 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| EinfriedungLage | 77 | 0.7766 | 0.8722 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.6643 | 0.8306 | 0.0000 | 1.0000 | 1.0000 | 0.4884 | 0.6654 | 
| AnlageZumEinstellenVorhanden | 77 | 0.8372 | 0.8740 | 0.8973 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6600 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| VorstehendeBauelementeAusladungMax | 69 | 0.9241 | 0.9464 | 1.0000 | 1.0000 | 0.8543 | 1.0000 | 1.0000 | 1.0000 | 0.7971 | 0.4913 | 0.7974 | 1.0000 | 1.0000 | 1.0000 | 0.9220 | 1.0000 | 1.0000 | 
| VerbotFensterZuOeffentlichenVerkehrsflaechen | 68 | 0.9106 | 0.9631 | 0.9320 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.7944 | 1.0000 | 0.9319 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| EinfriedungZulaessig | 66 | 0.7921 | 0.8859 | 1.0000 | 0.0000 | 0.7184 | 1.0000 | 0.9077 | 1.0000 | 0.7971 | 0.0000 | 1.0000 | 0.6642 | 1.0000 | 1.0000 | 1.0000 | 0.7944 | 1.0000 | 
| VerbotWohnung | 61 | 0.9868 | 0.9806 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8558 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9463 | 1.0000 | 1.0000 | 
| StrassenbreiteVonBis | 59 | 0.7476 | 0.7642 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8722 | -0.0098 | 1.0000 | 0.4961 | 0.0000 | 0.8557 | 
| AnordnungGaertnerischeAusgestaltungProzentual | 55 | 0.8555 | 0.8750 | 0.7974 | 1.0000 | 1.0000 | 0.8541 | 1.0000 | 0.6638 | 0.8304 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8879 | 0.0000 | 0.7986 | 
| OeffentlicheVerkehrsflaecheBreiteMin | 54 | 0.7536 | 0.7830 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 0.9398 | 0.6634 | 1.0000 | 0.7008 | 1.0000 | 1.0000 | 
| VorbautenVerbot | 48 | 0.8243 | 0.9104 | 1.0000 | 0.0000 | 1.0000 | 0.8557 | 0.8558 | 1.0000 | 1.0000 | 1.0000 | 0.7974 | 0.8558 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 
| HoehenlageGrundflaeche | 47 | 0.8031 | 0.7503 | 1.0000 | 1.0000 | 0.7972 | 0.0000 | 0.4979 | 1.0000 | 0.8541 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8979 | 1.0000 | 0.0000 | 
| VorbautenBeschraenkung | 41 | 0.7042 | 0.7639 | 1.0000 | 0.0000 | 0.6641 | 0.7986 | 0.9398 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 0.6642 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.4971 | 
| AnteilDachbegruenung | 41 | 0.8900 | 0.9294 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.4979 | 1.0000 | 1.0000 | 1.0000 | 0.8514 | 1.0000 | 
| EinleitungNiederschlagswaesser | 39 | 0.9904 | 0.9887 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8556 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| AbschlussDachMaxBezugGelaende | 37 | 0.6041 | 0.6699 | 1.0000 | 0.0000 | 0.0000 | 0.6654 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 0.3960 | 1.0000 | 1.0000 | 
| VerbotStaffelung | 34 | 0.8112 | 0.8830 | 1.0000 | 0.0000 | 0.7972 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.7987 | 0.6634 | 1.0000 | 0.9081 | 1.0000 | 1.0000 | 
| ArkadeHoehe | 32 | 0.9031 | 0.9391 | 1.0000 | 1.0000 | 1.0000 | 0.7472 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.7986 | 
| StellplatzImNiveauZulaessig | 31 | 0.9333 | 0.9802 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| MaxAnzahlGeschosseOberirdisch | 27 | 0.9237 | 0.9042 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.8561 | 1.0000 | 1.0000 | 
| GebaeudeHoeheMin | 27 | 0.8974 | 0.9374 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.6643 | 1.0000 | 1.0000 | 1.0000 | 0.7969 | 1.0000 | 1.0000 | 
| GaragengebaeudeAusfuehrung | 26 | 0.8000 | 0.9001 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| BestimmmungenFuerHochhausUndGrossbauvorhaben | 26 | 0.9049 | 0.9429 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6652 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9081 | 1.0000 | 1.0000 | 
| StellplatzregulativUmfangMaximumRelativ | 25 | 0.7772 | 0.8362 | 1.0000 | 1.0000 | 0.0000 | 0.6654 | 1.0000 | 1.0000 | 0.6640 | 1.0000 | 1.0000 | 0.6654 | 0.6634 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 
| Massengliederung | 24 | 0.8000 | 0.9239 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| StellplatzregulativUmfangMaximumAbsolut | 23 | 0.9508 | 0.9322 | 1.0000 | 1.0000 | 1.0000 | 0.7971 | 1.0000 | 0.6652 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.7990 | 1.0000 | 1.0000 | 
| StellplatzMax | 23 | 0.9777 | 0.9738 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6652 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| OberflaecheBestimmungP | 23 | 0.6864 | 0.7387 | 0.4980 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.7986 | 
| InSchutzzone | 22 | 0.9862 | 0.9959 | 1.0000 | 0.7937 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| AnzahlGebaeudeMax | 21 | 0.9681 | 0.9575 | 0.8558 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6654 | 
| FBOKMinimumWohnungen | 20 | 0.9333 | 0.9524 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| TechnischeAufbautenHoeheMax | 18 | 0.8532 | 0.9370 | 0.7987 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 
| StellplatzregulativUmfangMinimumRelativ | 18 | 0.8108 | 0.8183 | 1.0000 | 1.0000 | 0.6641 | 0.4978 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| GebaeudeEinschraenkungP | 17 | 0.9333 | 0.9564 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| DurchfahrtHoehe | 17 | 0.6999 | 0.6910 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.4979 | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 0.0000 | 
| DachneigungMin | 17 | 0.8667 | 0.9304 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 
| Kleinhaeuser | 16 | 0.8662 | 0.9457 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | -0.0074 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| BauklasseVIHoeheMax | 16 | 0.8667 | 0.8780 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| MaxAnzahlDachgeschosse | 14 | 0.9730 | 0.9762 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.7985 | 1.0000 | 1.0000 | 1.0000 | 0.7964 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| BauklasseVIHoeheMin | 14 | 0.9333 | 0.9216 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| StellplatzverpflichtungArt | 12 | 0.8443 | 0.8668 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.6652 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 
| VerbotBueroGeschaeftsgebaeude | 11 | 0.8532 | 0.8688 | 0.7987 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 
| AusnuetzbarkeitWidmungskategorieGefoerderterWohnbau | 11 | 0.8000 | 0.7829 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| AusnahmeVonWohnungenUnzulaessig | 10 | 0.8665 | 0.8232 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | -0.0028 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 
| DurchfahrtBreite | 9 | 0.9109 | 0.9477 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6642 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 
| Geschaeftsstrassen | 8 | 0.9333 | 0.9780 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 
| VerbotUnterirdischeBauwerkeUeberBaufluchtlinie | 7 | 0.8000 | 0.7546 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 
| MindestraumhoeheEG | 7 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| HochhausZulaessigGemaessBB | 7 | 0.9110 | 0.8475 | 0.6655 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 
| StellplatzregulativVorhanden | 6 | 0.9777 | 0.9738 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.6652 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| MaxAnzahlGeschosseOberirdischOhneDachgeschoss | 6 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| VerbotAufenthaltsraum | 4 | 0.9333 | 0.9166 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| EinfriedungHoeheSockel | 4 | 0.9333 | 0.9166 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| Einbautrasse | 4 | 0.9333 | 0.9151 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| GelaendeneigungMin | 3 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| AnteilBaumbepflanzung | 3 | 0.8667 | 0.8916 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 
| ZulaessigeGeschossanzahlEinkaufszentrum | 2 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| VerbotStellplaetzeUndParkgebaeude | 2 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| ArkadeLaenge | 2 | 0.9333 | 0.9098 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| MaxHoeheWohngebaeude | 1 | 0.9333 | 0.9524 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 
| LaubengangHoehe | 1 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 


