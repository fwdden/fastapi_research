from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/")
async def get_all_tags():
    return {"name": 'denis'}
