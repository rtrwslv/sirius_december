import datetime
from sqlalchemy import DECIMAL, Date, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from webapp.models.meta import DEFAULT_SCHEMA, Base


class Deal(Base):
    __tablename__ = 'deal'
    __table_args__ = {'schema': DEFAULT_SCHEMA}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    title: Mapped[str] = mapped_column(String, unique=True)

    amount: Mapped[float] = mapped_column(DECIMAL(10, 2))

    date: Mapped[datetime.date] = mapped_column(Date)
