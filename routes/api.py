from fastapi import APIRouter
from src import day_01, day_02, day_03, day_04, day_05

router = APIRouter()
router.include_router(day_01.router)
router.include_router(day_02.router)
router.include_router(day_03.router)
router.include_router(day_04.router)
router.include_router(day_05.router)
