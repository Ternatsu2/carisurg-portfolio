import numpy as np
import pandas as pd
import pytest

from src.data import load_triage_data
from src.features import select_model_features
from src.model import build_classifier


def make_tiny_triage_frame(rows: int = 50) -> pd.DataFrame:
    sequence = np.arange(rows)
    return pd.DataFrame(
        {
            "dep_name": ["ED"] * rows,
            "esi": np.resize(np.arange(1, 6), rows),
            "age": 18 + sequence,
            "triage_vital_hr": 65 + sequence % 35,
            "triage_vital_sbp": 105 + sequence % 45,
            "triage_vital_dbp": 60 + sequence % 25,
            "triage_vital_rr": 12 + sequence % 10,
            "triage_vital_o2": 92 + sequence % 8,
            "triage_vital_o2_device": sequence % 2,
            "triage_vital_temp": 97.0 + (sequence % 15) / 10,
            "triage_glucose": 80 + sequence,
            "visit_sequence": sequence,
            "disposition": ["unknown"] * rows,
            "previousdispo": ["unknown"] * rows,
        }
    )


def test_data_loading_enforces_expected_schema(tmp_path):
    input_path = tmp_path / "triage.csv"
    make_tiny_triage_frame().to_csv(input_path, index=False)

    frame = load_triage_data(
        input_path,
        required_columns=[
            "esi",
            "disposition",
            "previousdispo",
            "triage_vital_o2",
        ],
        expected_rows=50,
        expected_columns=14,
    )
    features, labels, names = select_model_features(
        frame,
        target="esi",
        leakage_columns=["disposition", "previousdispo"],
    )

    assert features.shape == (50, 10)
    assert set(labels) == {1, 2, 3, 4, 5}
    assert "disposition" not in names
    assert features.select_dtypes(exclude="number").empty

    invalid_path = tmp_path / "triage-missing-o2.csv"
    frame.drop(columns=["triage_vital_o2"]).to_csv(invalid_path, index=False)
    with pytest.raises(ValueError, match="Missing required columns"):
        load_triage_data(
            invalid_path,
            required_columns=["esi", "triage_vital_o2"],
        )


def test_tiny_training_smoke_predicts_one_label_per_row():
    frame = make_tiny_triage_frame()
    features, labels, _ = select_model_features(
        frame,
        target="esi",
        leakage_columns=["disposition", "previousdispo"],
    )
    model = build_classifier(
        "tuned_logistic_regression",
        {"max_iter": 1500, "class_weight": {1: 8}},
        random_state=42,
    )
    model.fit(features.iloc[:40], labels.iloc[:40])
    predictions = model.predict(features.iloc[40:])

    assert len(predictions) == 10
    assert set(predictions).issubset({1, 2, 3, 4, 5})
