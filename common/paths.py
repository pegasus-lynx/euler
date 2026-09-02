"""Shared paths for repository resources."""

from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def get_data_path(filename: str) -> Path:
	"""Return the path to a file in the repository data directory."""
	return DATA_DIR / filename