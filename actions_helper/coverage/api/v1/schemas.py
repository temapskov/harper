from pydantic import BaseModel


class CoverageInfo(BaseModel):
    name: str
    total_coverage: int


class CoverageInfoCreate(CoverageInfo): ...
