from sqlalchemy import create_engine, Column, String, Integer
from database import Base, engine


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    age = Column(Integer)


#создаем все таблицы, которые объявлены у нас в качестве классов, наследующих base
Base.metadata.create_all(engine)