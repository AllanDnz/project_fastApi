from datetime import datetime
from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.common.models import BaseModels


class AthleteModel(BaseModels):
    __tablename__ = 'athletes'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[int] = mapped_column(String(11), unique=True, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    weigth: Mapped[int] = mapped_column(Float, nullable=False)
    heigth: Mapped[int] = mapped_column(Float, nullable=False)
    gender: Mapped[int] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    categories: Mapped['CategoriesModel'] = relationship(back_populates='athlete')
    categories_id: Mapped[int] = mapped_column(ForeignKey('category.pk_id'), nullable=False)
    traning_center: Mapped['TraningCenterModel'] = relationship(back_populates='athlete')
    traning_center_id: Mapped[int] = mapped_column(ForeignKey('traning_center.pk_id'), nullable=False)