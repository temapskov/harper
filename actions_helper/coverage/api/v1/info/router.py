from fastapi import APIRouter, Response

from actions_helper.coverage.api.v1.info.service import svg_from_percent
from actions_helper.coverage.api.v1.schemas import CoverageInfo, CoverageInfoCreate
from actions_helper.coverage.utils import PickleCoverageStorage, save_coverage

router = APIRouter(prefix="/info")


@router.get("/")
async def get_coverage_info_by_repo_name(repo_name: str) -> CoverageInfo:
    coverage = CoverageInfo(name=repo_name, total_coverage=1)
    save_coverage(coverage, PickleCoverageStorage())

    return coverage


@router.get("/banner")
async def get_banner() -> str:
    return Response(content=svg_from_percent(60), media_type="image/svg+xml")


@router.post("/")
async def set_coverage_for_repo(coverage_info: CoverageInfoCreate) -> CoverageInfo:
    return
