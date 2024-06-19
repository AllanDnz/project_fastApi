from typing import Annotated
from pydantic import UUID4, Field
from workout_api.common.schemas import BaseSchemas


class Categories(BaseSchemas):
    name: Annotated[str, Field(description='Name of the categories', example='Scale', max_length=10)]

class CategoriesOut(Categories):
    id: Annotated[UUID4, Field(description='Identifier of the Categories')]