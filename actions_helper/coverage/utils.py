from typing import Protocol

from actions_helper.coverage.api.v1.schemas import CoverageInfo


class CoverageStorage(Protocol):
    """Interface for any storage save object"""

    def save(self, coverage: CoverageInfo):
        pass


class PickleCoverageStorage:
    def save(self, coverage: CoverageInfo):
        pass

    def read(self, coverage: CoverageInfo):
        pass


def save_coverage(coverage: CoverageInfo, storage: CoverageStorage):
    print(coverage)
    print(type(storage))
