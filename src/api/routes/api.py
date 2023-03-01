from fastapi import APIRouter

from src.api.routes import tags

router = APIRouter()
router.include_router(tags.router, tags=["tags"], prefix="/tags")
