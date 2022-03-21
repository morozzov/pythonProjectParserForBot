from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


class Quote(DeclarativeBase):
    __tablename__ = 'quotes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column("number", String)
    text = Column('text', String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}