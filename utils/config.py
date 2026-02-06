"""Configuration utilities.

Loads constants from config.json and exposes them to the simulation.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


def load_config(config_path: str | Path) -> Dict[str, Any]:
    """Load a configuration file (placeholder for validation logic)."""

    path = Path(config_path)
    with path.open("r", encoding="utf-8") as file_handle:
        return json.load(file_handle)
