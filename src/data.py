from pathlib import Path
from typing import Iterable, Optional, Tuple, Union

import pandas as pd
from sklearn.model_selection import train_test_split


ESI_LABELS: Tuple[int, ...] = (1, 2, 3, 4, 5)
PathLike = Union[str, Path]


def validate_triage_data(
    frame: pd.DataFrame,
    target: str = "esi",
    required_columns: Iterable[str] = (),
    expected_rows: Optional[int] = None,
    expected_columns: Optional[int] = None,
) -> None:
    """Fail early when the input no longer matches the modelling contract."""
    required = {target, *required_columns}
    missing_columns = sorted(required.difference(frame.columns))
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    if expected_rows is not None and len(frame) != expected_rows:
        raise ValueError(f"Expected {expected_rows} rows, found {len(frame)}")

    if expected_columns is not None and frame.shape[1] != expected_columns:
        raise ValueError(
            f"Expected {expected_columns} columns, found {frame.shape[1]}"
        )

    if frame.isna().any().any():
        raise ValueError("The modelling data contains missing values")

    duplicate_count = int(frame.duplicated().sum())
    if duplicate_count:
        raise ValueError(f"The modelling data contains {duplicate_count} duplicates")

    labels = set(frame[target].unique())
    if labels != set(ESI_LABELS):
        raise ValueError(f"Expected ESI labels 1-5, found {sorted(labels)}")


def load_triage_data(
    path: PathLike,
    target: str = "esi",
    required_columns: Iterable[str] = (),
    expected_rows: Optional[int] = None,
    expected_columns: Optional[int] = None,
) -> pd.DataFrame:
    """Load the programme CSV and enforce its expected schema."""
    csv_path = Path(path).expanduser()
    if not csv_path.exists():
        raise FileNotFoundError(f"Triage CSV not found: {csv_path}")

    frame = pd.read_csv(csv_path).drop(columns=["Unnamed: 0"], errors="ignore")
    validate_triage_data(
        frame,
        target=target,
        required_columns=required_columns,
        expected_rows=expected_rows,
        expected_columns=expected_columns,
    )
    return frame


def split_model_data(
    features: pd.DataFrame,
    target: pd.Series,
    test_size: float,
    random_state: int,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Create the fixed, stratified Week 6-8 development split."""
    return train_test_split(
        features,
        target,
        test_size=test_size,
        stratify=target,
        random_state=random_state,
    )
