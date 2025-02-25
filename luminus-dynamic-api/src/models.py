from datetime import datetime
from json import JSONEncoder

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class EnergyPrice(db.Model, JSONEncoder):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[datetime] = mapped_column(unique=True)
    price: Mapped[float] = mapped_column()

    def to_json(self):
        return {key: value for key, value in {
            "id": self.id,
            "date": self.date.isoformat(sep=" "),
            "price": self.price,
        }.items() if value is not None}
