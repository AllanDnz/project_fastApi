from http.client import HTTPException
from uuid import uuid4
from fastapi import APIRouter, Body, status
from pydantic import UUID4
from sqlalchemy.future import select

from workout_api.categories.models import CategoriesModel
from workout_api.categories.schemas import Categories, CategoriesOut
from workout_api.common.dependencies import DataBaseDependency

router = APIRouter()

@router.post(
        '/', 
        summary='Create a new category',
        status_code = status.HTTP_201_CREATED,
        response_model=CategoriesOut
        )
async def post(
    db_session: DataBaseDependency, 
    insert_category: Categories = Body(...)
    ) -> CategoriesOut:

    category_out = CategoriesOut(id=uuid4(), **insert_category.model_dump())
    category_model = CategoriesModel(**category_out.model_dump())

    db_session.add(category_model)
    await db_session.commit()

    return category_out
    
@router.get(
        '/', 
        summary='See all the categories',
        status_code = status.HTTP_200_OK,
        response_model=list[CategoriesOut]
        )
async def query(db_session: DataBaseDependency) -> list[CategoriesOut]:
    categories: list[CategoriesOut] =  (await db_session.execute(select(CategoriesModel))).scalars().all()

    return categories


@router.get(
        '/{id}', 
        summary='Consult category by id',
        status_code = status.HTTP_200_OK,
        response_model=CategoriesOut
        )
async def query(id: UUID4 ,db_session: DataBaseDependency) -> CategoriesOut:
    category: CategoriesOut =  (
        await db_session.execute(select(CategoriesModel).filter_by(id=id))
        ).scalars().first()
    
    if not category:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = f'Category not found by id'
            )
    return category
