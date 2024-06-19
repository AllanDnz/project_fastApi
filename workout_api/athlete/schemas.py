from typing import Annotated
from pydantic import Field, PositiveFloat
from workout_api.common.schemas import BaseSchemas


class Athlete(BaseSchemas):
    name: Annotated[str, Field(description='Name of the athlete', example='Joao', max_length=50)]
    cpf: Annotated[str, Field(description='CPF of the athlete', example='12345678900', max_length=11)]
    Age: Annotated[int, Field(description='Age of the Athlete', example='18')]
    weight: Annotated[PositiveFloat, Field(description='Weight of the athlete', example='50.8')]
    height: Annotated[PositiveFloat, Field(description='Heigth of the athlete', example='1.70')]
    gender: Annotated[str, Field(description='athletes gender', example='M', max_length=1)]


class AtlheteOut(Athlete, OutMixin):
    pass
