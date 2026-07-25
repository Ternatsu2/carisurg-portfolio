import warnings
from time import perf_counter
from typing import Any, Dict, Mapping, Tuple

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


LABELS = [1, 2, 3, 4, 5]


def build_classifier(
    model_name: str,
    hyperparameters: Mapping[str, Any],
    random_state: int,
) -> Pipeline:
    """Build the pinned model selected in the Week 7 decision journal."""
    if model_name != "tuned_logistic_regression":
        raise ValueError(f"Unsupported final model: {model_name}")

    parameters = dict(hyperparameters)
    class_weight = parameters.get("class_weight")
    if isinstance(class_weight, dict):
        parameters["class_weight"] = {
            int(label): weight for label, weight in class_weight.items()
        }
    parameters["random_state"] = random_state

    return Pipeline(
        [
            ("scale", StandardScaler()),
            ("model", LogisticRegression(**parameters)),
        ]
    )


def evaluate_predictions(
    labels: pd.Series,
    predictions: np.ndarray,
) -> Dict[str, Any]:
    """Return the headline and ESI 1 metrics used in Weeks 6-8."""
    matrix = confusion_matrix(labels, predictions, labels=LABELS)
    esi_1_caught = int(matrix[0, 0])
    esi_1_total = int(matrix[0].sum())

    return {
        "accuracy": float(accuracy_score(labels, predictions)),
        "macro_precision": float(
            precision_score(
                labels,
                predictions,
                labels=LABELS,
                average="macro",
                zero_division=0,
            )
        ),
        "macro_recall": float(
            recall_score(
                labels,
                predictions,
                labels=LABELS,
                average="macro",
                zero_division=0,
            )
        ),
        "macro_f1": float(
            f1_score(
                labels,
                predictions,
                labels=LABELS,
                average="macro",
                zero_division=0,
            )
        ),
        "esi_1_recall": float(
            recall_score(
                labels,
                predictions,
                labels=[1],
                average=None,
                zero_division=0,
            )[0]
        ),
        "esi_1_caught": esi_1_caught,
        "esi_1_total": esi_1_total,
        "confusion_matrix": matrix.tolist(),
    }


def fit_and_evaluate(
    model: Pipeline,
    train_features: pd.DataFrame,
    train_labels: pd.Series,
    test_features: pd.DataFrame,
    test_labels: pd.Series,
) -> Tuple[Pipeline, Dict[str, Any]]:
    """Fit once, predict once, and record reproducible evaluation timings."""
    fit_started = perf_counter()
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=RuntimeWarning)
        model.fit(train_features, train_labels)
    train_seconds = perf_counter() - fit_started

    predict_started = perf_counter()
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=RuntimeWarning)
        predictions = model.predict(test_features)
    inference_seconds = perf_counter() - predict_started

    metrics = evaluate_predictions(test_labels, predictions)
    metrics["train_seconds"] = float(train_seconds)
    metrics["inference_ms_per_patient"] = float(
        1000 * inference_seconds / len(test_features)
    )
    return model, metrics
