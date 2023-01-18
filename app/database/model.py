from sqlalchemy import Column, Date, Float, Integer

from . import Base


class Statistics(Base):
    __tablename__ = 'statistics'
    date = Column(Date, primary_key=True)
    views = Column(Integer)
    clicks = Column(Integer)
    cost = Column(Float)
    cpc = Column(Float)
    cpm = Column(Float)
