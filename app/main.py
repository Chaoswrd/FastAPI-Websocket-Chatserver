from .routers import users_router
from fastapi import FastAPI 
from .database.database import engine, Base
from .models import models
from .database.database import SessionLocal 


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users_router.router)

if (db := SessionLocal()).query(models.User).count() == 0:
    user = models.User(name="Chaosward")
    db.add(user)
    db.commit()