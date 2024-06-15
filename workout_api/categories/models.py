from workout_api.common.models import BaseModels
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class CategoriesModel(BaseModels):
    __tablename__ = 'category'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    categories: Mapped['AthleteModel'] = relationship(back_populates='category')