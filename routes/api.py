from fastapi import APIRouter
from src import day_01

router = APIRouter()
router.include_router(day_01.router)
