from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


def get_engine(db_uri):
    return create_engine(db_uri)


def get_session(engine):
    return sessionmaker(bind=engine)


def init_db(engine):
    Base.metadata.create_all(engine)
