from pathlib import Path

from fastapi import APIRouter, Response

from actions_helper.coverage.api.v1.info.service import svg_from_percent
from actions_helper.coverage.api.v1.schemas import CoverageInfo
from actions_helper.coverage.utils import CoverageStorage, PickleCoverageStorage

router = APIRouter(prefix="/info")


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


manager = CoverageManager(PickleCoverageStorage(Path("test.pickle")))


@router.get("/")
async def set_coverage_value_by_repo_name(repo_name: str, value: str) -> CoverageInfo:
    coverage = CoverageInfo(name=repo_name, total_coverage=value)
    manager.set_coverage_value(coverage)
    return coverage


@router.get("/banner")
async def get_banner_for_repo_by_repo_name(repo_name: str) -> str:
    coverage = manager.get_coverage_value(repo_name)
    print(manager.storage.data)
    return Response(content=svg_from_percent(coverage), media_type="image/svg+xml")
