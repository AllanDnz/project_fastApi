from workout_api.common.models import BaseModels


class BaseSchemas(BaseModels):
    class Config:
        extra = 'forbid'
        from_attributes = True