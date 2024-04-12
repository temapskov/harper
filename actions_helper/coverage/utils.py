import pickle
from pathlib import Path
from typing import Any, Protocol

from actions_helper.coverage.api.v1.schemas import CoverageInfo


class CoverageStorage(Protocol):
    """Interface for any storage save object"""

    def __init__(self) -> None:
        self.data: Any

    def _set(self) -> None:
        pass

    def _get(self) -> CoverageInfo:
        pass

    def save(self, path_to_file: Path, data: Any):
        pass


class PickleCoverageStorage:
    def __init__(self, path_to_file: Path) -> None:
        self.data = dict()
        self.path_to_file: Path = path_to_file

        self._read_file()

    def _read_file(self):
        if not self.path_to_file.exists():
            self.save()
        self._load_data()

    def save(self):
        with open(self.path_to_file, "wb") as file:
            pickle.dump(self.data, file)

    def _load_data(self):
        with open(self.path_to_file, "rb") as file:
            self.data = pickle.load(file)

    def _set(self, coverage: CoverageInfo) -> None:
        self.data[coverage.name] = coverage.total_coverage
        self.save()
        return self.data

    def _get(self, repo_name: str) -> int | None:
        return self.data.get(repo_name)
