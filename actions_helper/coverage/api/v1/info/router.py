from pathlib import Path

from fastapi import APIRouter, Response

from actions_helper.config import settings
from actions_helper.coverage.api.v1.info.service import svg_from_percent
from actions_helper.coverage.api.v1.schemas import CoverageInfo
from actions_helper.coverage.utils import CoverageManager, PickleCoverageStorage

router = APIRouter(prefix="/info")
manager = CoverageManager(PickleCoverageStorage(Path(settings.storage_filename)))


@router.get("/")
async def set_coverage_value_by_repo_name(repo_name: str, value: float) -> CoverageInfo:
    coverage = CoverageInfo(name=repo_name, total_coverage=int(value))
    manager.set_coverage_value(coverage)
    return coverage


@router.get("/banner")
async def get_banner_for_repo_by_repo_name(repo_name: str) -> str:
    coverage = manager.get_coverage_value(repo_name)
    return Response(content=svg_from_percent(coverage), media_type="image/svg+xml")
