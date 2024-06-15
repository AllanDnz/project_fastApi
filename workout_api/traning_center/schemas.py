from typing import Annotated
from pydantic import Field
from workout_api.common.schemas import BaseSchemas


class TraningCenter(BaseSchemas):
    name: Annotated[str, Field(description='Name of the traning center', example='Growth', max_length=20)]
    address: Annotated[str, Field(description='Addres of the traning center', example='Rua X, Num x', max_length=60)]
    owner: Annotated[str, Field(description='Owner of the traning center', example='Raphael', max_length=30)]