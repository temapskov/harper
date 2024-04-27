from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from actions_helper.config import settings
from actions_helper.coverage.api.router import router as coverage_router

app = FastAPI()

print(settings.GH_TOKEN)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


app.include_router(coverage_router)
