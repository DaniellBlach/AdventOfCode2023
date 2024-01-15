from fastapi import APIRouter
from src import day_01, day_02

router = APIRouter()
router.include_router(day_01.router)
router.include_router(day_02.router)
