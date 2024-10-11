from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine('sqlite:///myDatabase.db', echo = True)
Session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass





def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()