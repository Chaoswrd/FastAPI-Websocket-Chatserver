from app.routers.dependency_parameter_sets import GetDbParams, GetIdParams 
from fastapi import APIRouter, HTTPException, Depends 
from typing import List, Optional
from ..models import device_model
from ..schemas import device_schema
from ..crud import device_crud

router = APIRouter(
    prefix="/devices",
    tags=["devices"],
    responses={400: {"description": "Not Found"}},
)

@router.get("/", response_model=List[device_schema.Device])
async def get_devices(params: GetDbParams = Depends()):
    devices = device_crud.get_devices(params.db, params.skip, params.limit)
    return devices

@router.get("/{id}", response_model=device_schema.Device)
async def get_device(params: GetIdParams = Depends()):
    device = device_crud.get_device(params.db, params.id)
    return device 

@router.post("/", response_model=device_schema.Device, status_code=201)
async def create_device(device: device_schema.Device):
    return device
