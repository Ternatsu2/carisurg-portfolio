import hashlib
import json
import os
from pathlib import Path
from typing import Any, Dict, Iterable, Mapping, Union

import yaml


PathLike = Union[str, Path]


def load_config(path: PathLike) -> Dict[str, Any]:
    """Load the YAML configuration used by the command-line entry point."""
    config_path = Path(path)
    with config_path.open(encoding="utf-8") as stream:
        config = yaml.safe_load(stream)
    if not isinstance(config, dict):
        raise ValueError("Configuration root must be a mapping")
    return config


def resolve_data_path(
    data_config: Mapping[str, Any],
    project_root: Path,
) -> Path:
    """Prefer the private environment path, then the configured local path."""
    environment_variable = data_config["environment_variable"]
    environment_path = os.getenv(environment_variable)
    configured_path = Path(data_config["raw_path"]).expanduser()
    if not configured_path.is_absolute():
        configured_path = project_root / configured_path

    candidates = [
        Path(environment_path).expanduser() if environment_path else None,
        configured_path,
    ]
    data_path = next(
        (candidate for candidate in candidates if candidate and candidate.exists()),
        None,
    )
    if data_path is None:
        raise FileNotFoundError(
            f"Set {environment_variable} to the private programme CSV path"
        )
    return data_path


def index_sha256(index_values: Iterable[Any]) -> str:
    """Hash a split index so later runs can verify row-for-row parity."""
    payload = ",".join(map(str, index_values)).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def write_json(payload: Mapping[str, Any], path: PathLike) -> None:
    """Write a readable JSON artefact, creating its parent directory."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
