from typing import Iterable, List, Tuple

import numpy as np
import pandas as pd


def add_clinical_features(frame: pd.DataFrame) -> pd.DataFrame:
    """Reproduce the 11 Week 7 features used by the complex-model benchmark."""
    enriched = frame.copy()
    systolic = enriched["triage_vital_sbp"].replace(0, np.nan)
    respiratory_rate = enriched["triage_vital_rr"].replace(0, np.nan)

    enriched["shock_index"] = enriched["triage_vital_hr"] / systolic
    enriched["pulse_pressure"] = (
        enriched["triage_vital_sbp"] - enriched["triage_vital_dbp"]
    )
    enriched["spo2_rr_ratio"] = (
        enriched["triage_vital_o2"] / respiratory_rate
    )
    enriched["red_flag_hypoxia"] = (
        enriched["triage_vital_o2"] < 92
    ).astype(int)
    enriched["red_flag_tachypnea"] = (
        enriched["triage_vital_rr"] > 20
    ).astype(int)
    enriched["red_flag_fever"] = (
        enriched["triage_vital_temp"] >= 100.4
    ).astype(int)
    enriched["red_flag_hypothermia"] = (
        enriched["triage_vital_temp"] < 96.8
    ).astype(int)
    enriched["red_flag_bradycardia"] = (
        enriched["triage_vital_hr"] < 60
    ).astype(int)
    enriched["red_flag_hyperglycaemia"] = (
        enriched["triage_glucose"] > 180
    ).astype(int)
    enriched["respiratory_distress"] = (
        (enriched["red_flag_hypoxia"] == 1)
        | (enriched["red_flag_tachypnea"] == 1)
    ).astype(int)
    enriched["red_flag_count"] = enriched[
        [
            "red_flag_hypoxia",
            "red_flag_tachypnea",
            "red_flag_fever",
            "red_flag_hypothermia",
            "red_flag_bradycardia",
            "red_flag_hyperglycaemia",
        ]
    ].sum(axis=1)

    return enriched.replace([np.inf, -np.inf], np.nan).fillna(0)


def select_model_features(
    frame: pd.DataFrame,
    target: str,
    leakage_columns: Iterable[str],
    use_engineered_features: bool = False,
) -> Tuple[pd.DataFrame, pd.Series, List[str]]:
    """Build the numeric modelling table used in the Week 6 and Week 7 work."""
    non_numeric = frame.select_dtypes(exclude="number").columns
    excluded = {target, *leakage_columns, *non_numeric}
    feature_columns = [
        column
        for column in frame.columns
        if column not in excluded
        and pd.api.types.is_numeric_dtype(frame[column])
    ]

    features = frame[feature_columns].copy()
    if use_engineered_features:
        features = add_clinical_features(features)

    if features.empty:
        raise ValueError("No numeric model features were selected")
    if features.isna().any().any():
        raise ValueError("Selected features contain missing values")
    if not np.isfinite(features.to_numpy()).all():
        raise ValueError("Selected features contain non-finite values")

    labels = frame[target].astype(int).copy()
    return features, labels, features.columns.tolist()
