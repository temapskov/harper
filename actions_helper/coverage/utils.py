import pickle
from pathlib import Path
from typing import Any, Protocol

from actions_helper.coverage.api.v1.schemas import CoverageInfo


class CoverageStorage(Protocol):
    """Interface for any storage save object"""

    data: Any  # Это поле данных, обязательное для наследников этого протокола.

    def _set(self) -> None:
        pass  # pragma: no cover

    def _get(self) -> int | None:
        pass  # pragma: no cover

    def _remove(self) -> None:
        pass  # pragma: no cover

    def save(self, path_to_file: Path, data: Any):
        pass  # pragma: no cover


class PickleCoverageStorage:
    def __init__(self, path_to_file: Path) -> None:
        self.data = dict()
        self.path_to_file: Path = path_to_file

        self._read_file()

    def _read_file(self) -> None:
        if not self.path_to_file.exists():
            self.save()
        self._load_data()

    def save(self) -> None:
        with open(self.path_to_file, "wb") as file:
            pickle.dump(self.data, file)

    def _load_data(self) -> None:
        with open(self.path_to_file, "rb") as file:
            self.data = pickle.load(file)

    def _set(self, coverage: CoverageInfo) -> None:
        self.data[coverage.name] = coverage.total_coverage
        self.save()
        return self.data

    def _remove(self, name: str) -> None:
        if self.data.get(name):
            self.data.pop(name)
            return self.save()

    def _get(self, repo_name: str) -> int | None:
        return self.data.get(repo_name)


class CoverageManager:
    def __init__(self, storage: CoverageStorage) -> None:
        self.storage = storage

    def set_coverage_value(self, coverage: CoverageInfo) -> None:
        return self.storage._set(coverage)

    def get_coverage_value(self, repo_name: str) -> int:
        value = self.storage._get(repo_name)
        if not value:
            value = 0
        return value

    def remove_coverage_info(self, repo_name: str) -> None:
        return self.storage._remove(repo_name)
