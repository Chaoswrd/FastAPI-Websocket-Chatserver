from typing import Optional
from .routers import devices_router
from fastapi import FastAPI, Depends 
from .crud import device_crud
from .database.database import SessionLocal, engine
from .models import device_model
from .schemas import device_schema
from sqlalchemy.orm import Session


device_model.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(devices_router.router)