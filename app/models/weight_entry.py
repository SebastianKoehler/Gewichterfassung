from sqlalchemy import Column, Integer, Float, Date
from app import Base, get_engine, get_session, init_db, Config


class WeightEntry(Base):
    engine = get_engine(Config.SQLALCHEMY_DATABASE_URI)
    Session = get_session(engine)

    __tablename__ = 'weight_entries'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    weight = Column(Float, nullable=False)

    init_db(engine)
