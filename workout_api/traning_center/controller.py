from http.client import HTTPException
from uuid import uuid4
from fastapi import APIRouter, Body, status
from pydantic import UUID4
from sqlalchemy.future import select

from workout_api.traning_center.models import TraningCenterModel
from workout_api.traning_center.schemas import TraningCenter, TraningCenterOut
from workout_api.common.dependencies import DataBaseDependency

router = APIRouter()

@router.post(
        '/', 
        summary='Create a new traning center',
        status_code = status.HTTP_201_CREATED,
        response_model=TraningCenterOut
        )
async def post(
    db_session: DataBaseDependency, 
    insert_traningCenter: TraningCenter = Body(...)
    ) -> TraningCenterOut:

    traningCenter_out = TraningCenterOut(id=uuid4(), **insert_traningCenter.model_dump())
    traingCenter_model = TraningCenterModel(**traningCenter_out.model_dump())

    db_session.add(traingCenter_model)
    await db_session.commit()

    return traningCenter_out
    
@router.get(
        '/', 
        summary='See all the traning center',
        status_code = status.HTTP_200_OK,
        response_model=list[TraningCenterOut]
        )
async def query(db_session: DataBaseDependency) -> list[TraningCenterOut]:
    traningCenters: list[TraningCenterOut] =  (await db_session.execute(select(TraningCenterModel))).scalars().all()

    return traningCenters


@router.get(
        '/{id}', 
        summary='Consult traning center by id',
        status_code = status.HTTP_200_OK,
        response_model=TraningCenterOut
        )
async def query(id: UUID4 ,db_session: DataBaseDependency) -> TraningCenterOut:
    traning_center: TraningCenterOut =  (
        await db_session.execute(select(TraningCenterModel).filter_by(id=id))
        ).scalars().first()
    
    if not traning_center:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f'Traning center not found by id'
            )
    return traning_center
