from fastapi import APIRouter
from workout_api.athlete.controller import router as athlete
from workout_api.categories.controller import router as categories
from workout_api.traning_center.controller import router as traning_center


router = APIRouter()
router.include_router(athlete, prefix='/athletes', tags=['athletes'])

router.include_router(categories, prefix='/categories', tags=['categories'])

router.include_router(traning_center, prefix='/traning_centers', tags=['traning_centers'])

