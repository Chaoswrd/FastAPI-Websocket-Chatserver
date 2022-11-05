from typing import List, Optional

from pydantic import BaseModel

class DeviceBase(BaseModel):
    id: int 
    time: int
    energy_consumption_kw: float
    temperature: float
    icon: str 
    humidity: float
    visibility: float
    summary: str
    apparent_temperature:float
    pressure: float
    wind_speed: float
    cloud_cover: int
    wind_bearing: int
    precip_intensity: float
    dew_point: float
    precip_probability: float

class DeviceCreate(DeviceBase):
    pass

class Device(DeviceBase):

    class Config:
        orm_mode = True