#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path

import joblib


PROJECT_ROOT = Path(__file__).resolve().parents[1]
# Support the documented `python scripts/train.py` entry point.
sys.path.insert(0, str(PROJECT_ROOT))

from src.data import load_triage_data, split_model_data
from src.features import select_model_features
from src.model import build_classifier, fit_and_evaluate
from src.utils import index_sha256, load_config, resolve_data_path, write_json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train the pinned triage model")
    parser.add_argument("--config", default="config.yaml")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = PROJECT_ROOT / config_path
    config = load_config(config_path)

    data_config = config["data"]
    data_path = resolve_data_path(data_config, PROJECT_ROOT)
    frame = load_triage_data(
        data_path,
        target=data_config["target"],
        required_columns=data_config["required_columns"],
        expected_rows=data_config["expected_rows"],
        expected_columns=data_config["expected_columns"],
    )
    features, labels, feature_names = select_model_features(
        frame,
        target=data_config["target"],
        leakage_columns=config["features"]["leakage_columns"],
        use_engineered_features=config["features"]["use_engineered_features"],
    )
    if len(feature_names) != config["features"]["expected_count"]:
        raise ValueError(
            f"Expected {config['features']['expected_count']} features, "
            f"found {len(feature_names)}"
        )

    train_x, test_x, train_y, test_y = split_model_data(
        features,
        labels,
        test_size=config["split"]["test_size"],
        random_state=config["seed"],
    )
    if len(train_x) != config["split"]["expected_train_rows"]:
        raise ValueError("Training split size does not match the recorded run")
    if len(test_x) != config["split"]["expected_test_rows"]:
        raise ValueError("Test split size does not match the recorded run")

    split_hash = index_sha256(test_x.index)
    if split_hash != config["split"]["expected_test_index_sha256"]:
        raise ValueError("Test split does not match the Week 6-7 holdout")

    model = build_classifier(
        config["model"]["name"],
        config["model"]["hyperparameters"],
        random_state=config["seed"],
    )
    model, metrics = fit_and_evaluate(model, train_x, train_y, test_x, test_y)
    metrics.update(
        {
            "model": config["model"]["name"],
            "feature_count": len(feature_names),
            "test_index_sha256": split_hash,
            "training_visits": len(train_x),
            "test_visits": len(test_x),
        }
    )

    model_path = PROJECT_ROOT / config["outputs"]["model_path"]
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    write_json(metrics, PROJECT_ROOT / config["outputs"]["metrics_path"])

    print(f"Model: {metrics['model']}")
    print(f"Accuracy: {metrics['accuracy']:.6f}")
    print(f"Macro F1: {metrics['macro_f1']:.6f}")
    print(
        "ESI 1 recall: "
        f"{metrics['esi_1_recall']:.4f} "
        f"({metrics['esi_1_caught']}/{metrics['esi_1_total']})"
    )
    print(f"Test index SHA-256: {split_hash}")


if __name__ == "__main__":
    main()
