from fastapi import APIRouter, Body, status

from workout_api.athlete.schemas import Athlete
from workout_api.common.dependencies import DataBaseDependency

router = APIRouter()

@router.post(
        '/', 
        summary='Create a new athlete',
        status_code = status.HTTP_201_CREATED
        )
async def post(
    db_session: DataBaseDependency, 
    insert_athlete: Athlete = Body(...)
    ):
    pass
