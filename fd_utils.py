# Gemeinsame Funktionen für alle Modell-Notebooks (05 bis 09).
# Bitte nur über einen Pull Request ändern, damit alle mit derselben Bewertung arbeiten.

import pandas as pd
from sklearn.metrics import make_scorer, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_validate

RANDOM_STATE = 1

# Dieselben 5 Folds für alle Modelle, damit die Ergebnisse vergleichbar sind
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)


def evaluate_cv(model, X, y, name):
    # Cross-Validation auf dem Train-Teil, gibt eine Zeile mit den Mittelwerten zurück
    # zero_division=0: Sagt ein Modell nie "Betrug", ist die Precision 0 (statt einer Warnung)
    scoring = {
        "roc_auc": "roc_auc",
        "recall": "recall",
        "precision": make_scorer(precision_score, zero_division=0),
    }
    scores = cross_validate(model, X, y, cv=cv, scoring=scoring, n_jobs=-1)
    return pd.DataFrame({
        "ROC-AUC": [scores["test_roc_auc"].mean()],
        "ROC-AUC std": [scores["test_roc_auc"].std()],
        "Recall": [scores["test_recall"].mean()],
        "Precision": [scores["test_precision"].mean()],
    }, index=[name]).round(3)


def evaluate(y_true, y_proba, threshold=0.5):
    # Bewertung mit fertigen Wahrscheinlichkeiten (z. B. auf dem Test-Teil)
    y_pred = (y_proba >= threshold).astype(int)
    return {
        "ROC-AUC": round(roc_auc_score(y_true, y_proba), 3),
        "Recall": round(recall_score(y_true, y_pred), 3),
        "Precision": round(precision_score(y_true, y_pred, zero_division=0), 3),
    }


def lift_top(y_true, y_proba, anteil=0.10):
    # Wie viel Betrug steckt in den verdächtigsten 10 % der Kunden?
    df = pd.DataFrame({"target": list(y_true), "proba": list(y_proba)})
    df = df.sort_values("proba", ascending=False)
    top = df.head(int(len(df) * anteil))

    quote_top = top["target"].mean()
    quote_gesamt = df["target"].mean()
    return {
        "Betrugsquote Top": round(quote_top, 3),
        "Betrugsquote gesamt": round(quote_gesamt, 3),
        "Lift": round(quote_top / quote_gesamt, 2),
        "Anteil gefundener Betrüger": round(top["target"].sum() / df["target"].sum(), 3),
    }
