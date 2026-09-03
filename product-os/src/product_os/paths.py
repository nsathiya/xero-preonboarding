from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RepoPaths:
    root: Path

    @property
    def config_dir(self) -> Path:
        return self.root / "config"

    @property
    def evidence_dir(self) -> Path:
        return self.root / "evidence"

    @property
    def context_dir(self) -> Path:
        return self.root / "context"

    @property
    def derived_dir(self) -> Path:
        return self.root / "derived"

    @property
    def notes_dir(self) -> Path:
        return self.root / "notes"


def find_repo_root(start: Path | None = None) -> Path:
    """
    Finds the product-os repo root by looking for pyproject.toml.
    """
    cur = (start or Path.cwd()).resolve()
    for p in [cur, *cur.parents]:
        if (p / "pyproject.toml").exists() and (p / "evidence").exists():
            return p
    return cur

