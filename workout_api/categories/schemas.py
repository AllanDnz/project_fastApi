from typing import Annotated
from pydantic import Field
from workout_api.common.schemas import BaseSchemas


class Categories(BaseSchemas):
    name: Annotated[str, Field(description='Name of the categories', example='Scale', max_length=10)]