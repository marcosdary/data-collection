from sqlalchemy.orm import DeclarativeBase

from sqlalchemy.orm import DeclarativeBase

class BaseModel(DeclarativeBase):
    __abstract__ = True