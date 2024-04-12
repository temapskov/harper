from fastapi import APIRouter

from actions_helper.coverage.api.v1.info.router import router as info_router

routers = [info_router]

router = APIRouter(prefix="/v1")

for route in routers:
    router.include_router(route)
