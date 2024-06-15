from workout_api.common.models import BaseModels
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class TraningCenterModel(BaseModels):
    __tablename__ = 'traning_center'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    address: Mapped[str] = mapped_column(String(60), nullable=False)
    owner: Mapped[str] = mapped_column(String(30), nullable=False)
    categories: Mapped['AthleteModel'] = relationship(back_populates='traning_center')