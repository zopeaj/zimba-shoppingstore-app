from fastapi import FastAPI
from startlette.middleware.cors import CORSMiddleware

from app.api_v1.Api import api_router
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, opeanapi_url=f"{settings.API_V1_STR}/openapi.json")


# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
       CORSMiddleware,
       allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)

