from typing import Generic, TypeVar, List, Optional
from fastapi import HTTPException, Depends
from ..database.database import SessionLocal 
from sqlalchemy.orm import Session
from pydantic.generics import GenericModel

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class GetParams:
    def __init__(self, skip: int = 0, limit: int = 5):
        if skip < 0:
            raise HTTPException(status_code=400, detail="skip must be non-negative")
        if limit < 1:
            raise HTTPException(status_code=400, detail="limit must be larger than zero")
        self.skip = skip
        self.limit = limit

class GetDbParams(GetParams):
    def __init__(self, db: Session = Depends(get_db), skip: int = 0, limit: int = 5):
        super().__init__(skip, limit)
        self.db = db

class GetIdParams:
    def __init__(self, id: int, db: Session = Depends(get_db)):
        self.db = db
        self.id = id