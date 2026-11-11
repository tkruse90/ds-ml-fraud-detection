# Machine-Learning-Projekt: Aufgabenstellung

Das ist euer zweites Projekt. Als Team bringt ihr einen echten Datensatz von den Rohdaten bis zu einem funktionierenden Machine-Learning-Modell und einer Präsentation für Stakeholder. Ziel ist, gemeinsam den gesamten Data-Science-Lebenszyklus zu üben: ein Problem formulieren, eine Baseline bauen, mit Fehleranalyse iterieren und eure Ergebnisse einem nicht-technischen Publikum vermitteln.

Dieses Vorlagen-Repository ist euer Ausgangspunkt. Es enthält eine fertig eingerichtete Umgebung und ein Beispiel-Notebook, das mit minimaler Bereinigung und Feature-Auswahl ein einfaches Modell trainiert. Betrachtet es als Gerüst für euer eigenes Projekt.

Arbeitet die folgenden Abschnitte der Reihe nach durch: Zuerst wählt ihr ein Projekt, dann plant ihr es auf einem Board, baut und iteriert, und zum Schluss bereitet ihr eure Abgaben vor.

## Ein Projekt wählen

Wählt als Team eine Option. Sucht euch ein Problem mit klaren Stakeholdern und einem klaren geschäftlichen Nutzen.

### Option A: Zindi-Challenge (leicht bis fortgeschritten)

Wählt eine Challenge auf [Zindi](https://zindi.africa/competitions). Erfüllt die Anforderungen der Challenge und bereitet zusätzlich eine Präsentation für Stakeholder vor.

1. [Tanzania Tourism Prediction](https://zindi.africa/competitions/tanzania-tourism-prediction/data) (leicht, 2 Personen)
2. [Fraud Detection in Electricity and Gas Consumption](https://zindi.africa/competitions/fraud-detection-in-electricity-and-gas-consumption-challenge) (Betrugserkennung beim Strom- und Gasverbrauch; mittel, mit Starter-Notebook, 2 bis 3 Personen)
3. [Urban Air Pollution Challenge](https://zindi.africa/competitions/zindiweekendz-learning-urban-air-pollution-challenge) (mittel bis fortgeschritten, 3 Personen und etwas Fachwissen)
4. [Flight Delay Prediction](https://zindi.africa/competitions/flight-delay-prediction-challenge) (mittel, 3 Personen; Flughafendaten über [airportsdata](https://pypi.org/project/airportsdata/))
5. [Financial Inclusion in Africa](https://zindi.africa/competitions/financial-inclusion-in-africa) (leicht, 2 Personen)

### Option B: Erfolg von Kickstarter-Projekten (mittel)

In den letzten Jahren sind die Finanzierungsmöglichkeiten für Projekte von Einzelpersonen und kleinen Unternehmen deutlich vielfältiger geworden. Neben Ersparnissen, Bankkrediten und Geld von Freunden und Familie hat sich Crowdfunding zu einer beliebten und leicht zugänglichen Alternative entwickelt.

Kickstarter, gegründet 2009, ist eine bekannte Crowdfunding-Plattform. Sie arbeitet nach dem Alles-oder-nichts-Prinzip: Ein Projekt wird nur finanziert, wenn es seinen Zielbetrag erreicht. Andernfalls zahlen die Unterstützer dem Projekt kein Geld.

Viele Faktoren tragen zum Erfolg oder Misserfolg eines Projekts bei, allgemein und auch auf Kickstarter. Einige davon lassen sich messen oder in Kategorien einteilen. Damit lässt sich ein Modell bauen, das vorhersagt, ob ein Projekt erfolgreich sein wird. Ziel dieses Projekts ist, ein solches Modell zu bauen und die Daten der Kickstarter-Projekte allgemein zu analysieren. So könnt ihr potenziellen Projektgründern helfen einzuschätzen, ob Kickstarter eine gute Finanzierungsoption für sie ist und wie ihre Erfolgschancen stehen.

Daten: [Kickstarter Projects auf Kaggle](https://www.kaggle.com/datasets/kemical/kickstarter-projects).

### Option C: Andere tabellarische Datensätze (Kaggle)

Strukturierte, tabellarische Datensätze von echten Unternehmen mit einem klaren Business Case. Wählt ein Regressions- oder ein Klassifikationsproblem.

**Regression (stetige Zielvariable):**

- [Zillow Prize: Home Value Prediction](https://www.kaggle.com/competitions/zillow-prize-1): den logarithmischen Fehler zwischen Zillows automatischer Preisschätzung und dem tatsächlichen Verkaufspreis vorhersagen. Zielvariable: `logerror`.
- [Mercedes-Benz Greener Manufacturing](https://www.kaggle.com/competitions/mercedes-benz-greener-manufacturing): aus der Konfiguration eines Autos vorhersagen, wie lange es auf dem Prüfstand braucht. Zielvariable: Testdauer (`y`).
- [Santander Value Prediction Challenge](https://www.kaggle.com/competitions/santander-value-prediction-challenge): aus anonymisierten Daten einen stetigen Kundenwert vorhersagen. Zielvariable: `target`.
- [Allstate Claims Severity](https://www.kaggle.com/competitions/allstate-claims-severity): die Kosten von Versicherungsschäden vorhersagen. Zielvariable: `loss`.
- [Expedia Hotel Recommendations](https://www.kaggle.com/competitions/expedia-hotel-recommendations) (Regressionsvariante): die Wahrscheinlichkeit vorhersagen, dass ein Nutzer einen Hotel-Cluster bucht.

**Klassifikation (kategoriale Zielvariable):**

- [Porto Seguro Safe Driver Prediction](https://www.kaggle.com/competitions/porto-seguro-safe-driver-prediction): vorhersagen, ob ein Fahrer im nächsten Jahr einen Schaden meldet. Zielvariable: binär.
- [Santander Customer Transaction Prediction](https://www.kaggle.com/competitions/santander-customer-transaction-prediction): vorhersagen, welche Kunden eine bestimmte Transaktion durchführen werden. Zielvariable: binär.
- [Expedia Hotel Recommendations](https://www.kaggle.com/competitions/expedia-hotel-recommendations): klassifizieren, welchen Hotel-Cluster ein Nutzer am wahrscheinlichsten bucht. Zielvariable: mehrere Klassen (`hotel_cluster`).
- [Avito Demand Prediction](https://www.kaggle.com/competitions/avito-demand-prediction): vorhersagen, ob eine Anzeige erfolgreich sein wird (Nachfrage). Zielvariable: Klassifikation.
- [Home Credit Default Risk](https://www.kaggle.com/competitions/home-credit-default-risk): vorhersagen, ob ein Kreditantragsteller zahlungsunfähig wird. Zielvariable: binär (`TARGET`).

## Zeitplan und Meilensteine

Das Projekt läuft über vier Tage. Verfolgt euren Fortschritt auf einem Kanban-Board in GitHub. Wie ihr das Board einrichtet, steht in [02_kanban_board.md](02_kanban_board.md).

| Meilenstein | Was es ist | Ziel |
| --- | --- | --- |
| Meilenstein 0 | Daten einlesen (Data Ingestion) | Tag 1, 12:00 |
| Meilenstein 1 | EDA | Tag 2, 12:00 |
| Meilenstein 2 | Erstes Modell, die Baseline | Tag 3, 12:00 |
| Meilenstein 3 | Ein Modell mit Fehleranalyse | Tag 4, 12:00 |
| Meilenstein 4 | Finale Abgaben und Präsentation | Tag 5, 14:00 |

Schreibt für jeden Meilenstein zwei Dinge in das GitHub-Issue:

1. Was erledigt sein muss, damit der Meilenstein abgeschlossen ist.
2. Die Definition of Done: wie euer Ergebnis aussieht, wenn der Meilenstein abgeschlossen ist.

### Beispiel für ein Baseline-Modell (Meilenstein 2)

Eine Baseline ist das Einfachste, das funktionieren könnte. Sie liefert euch einen Wert, den ihr schlagen müsst. Zum Beispiel für ein Projekt zur Betrugserkennung:

- **Nutzen des Produkts:** betrügerische Transaktionen finden, Geld sparen, Rufschäden vermeiden und Geldwäsche verhindern.
- **Vorhersage:** ob eine Transaktion betrügerisch ist.
- **Bewertungsmetrik:** F1-Score. Wir wollen Verluste durch Betrug minimieren und gleichzeitig vermeiden, Kunden fälschlich zu beschuldigen (und sie dadurch vielleicht zu verlieren). Sowohl falsch-positive als auch falsch-negative Vorhersagen haben starke negative Folgen, darum passt eine ausgewogene Metrik wie der F1-Score.
- **Baseline-Modell:** Annahme, dass Transaktionen um Mitternacht wahrscheinlich betrügerisch sind.
- **Score:** F1-Score = 0.1.

## Worüber ihr nachdenken solltet

Behaltet beim Bauen und Weiterentwickeln eurer Modelle Folgendes im Kopf:

- Prüft, ob die Daten unausgewogen (imbalanced) sind.
- Welche Bewertungsmetrik passt zu eurem Problem: Precision, Recall, Accuracy, F1-Score oder etwas anderes? (Denkt an die True Positive Rate.)
- Probiert mindestens drei verschiedene Machine-Learning-Algorithmen aus, um zu sehen, welcher am besten abschneidet, einschließlich Cross-Validation und Hyperparameter-Tuning.

## Finale Abgaben

1. Eine Foliensammlung (PDF, auf GitHub gepusht) für nicht-technische Stakeholder, die eure Ergebnisse, Empfehlungen und mögliche nächste Schritte darstellt. Sie begleitet eine 10-minütige Präsentation.
2. Ein Jupyter Notebook nach PEP 8 für ein Data-Science- und technisches Publikum. Das Notebook sollte gut dokumentiert und reproduzierbar sein, einen klaren roten Faden haben und Visualisierungen enthalten, die eure Ergebnisse stützen. Es sollte auf GitHub gepusht werden.
3. Eine Folie zu einem möglichen Datenprodukt: Wie könnten die Vorhersagen genutzt werden?

## Ressourcen

Wenn euer Datensatz unausgewogen ist, sind das nützliche Einstiegspunkte (auf Englisch):

- [8 Tactics to Combat Imbalanced Classes](https://machinelearningmastery.com/tactics-to-combat-imbalanced-classes-in-your-machine-learning-dataset/)
- [Random Oversampling and Undersampling for Imbalanced Classification](https://machinelearningmastery.com/random-oversampling-and-undersampling-for-imbalanced-classification/)
