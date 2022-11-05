from sqlalchemy.orm import Session
from fastapi import HTTPException

from ..models import device_model
from ..schemas import device_schema

def get_device(db: Session, id: int):
    device = db.query(device_model.Device).filter(device_model.Device.id == id).first()
    if device is None:
        raise HTTPException(status_code=404, detail=f"No device with id: {id}")
    return device

def get_devices(db: Session, skip: int, limit: int):
    return db.query(device_model.Device).offset(skip).limit(limit).all() 
