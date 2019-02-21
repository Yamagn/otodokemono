from sqlalchemy import Column, Integer, String, Float, DateTime
from db.database import Base
from datetime import datetime


class Noise(Base):
    __tablename__ = "noise"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    noise = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, name=None, noise=None, latitude=None, longitude=None, date=None):
        self.name = name
        self.noise = noise
        self.latitude = latitude
        self.longitude = longitude
        self.date = date