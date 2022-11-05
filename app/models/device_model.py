from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import relationship

from ..database.database import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    time = Column(Integer, index=True)
    energy_consumption_kw = Column(Float)
    temperature = Column(Float)
    icon = Column(String)
    humidity = Column(Float)
    visibility = Column(Float)
    summary= Column(String)
    apparent_temperature = Column(Float)
    pressure = Column(Float)
    wind_speed = Column(Float)
    cloud_cover = Column(Integer)
    wind_bearing = Column(Integer)
    precip_intensity = Column(Float)
    dew_point = Column(Float)
    precip_probability = Column(Float)