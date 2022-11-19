from uuid import uuid4
from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func

from ..database.database import Base

class CommonModel(Base):
    __abstract__ = True
    
    id = Column(String, primary_key=True, default=lambda: str(uuid4()), unique=True)
    created_time = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    updated_time = Column(DateTime(timezone=True), onupdate=func.now(), index=True)