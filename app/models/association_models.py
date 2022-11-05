from sqlalchemy import Column, Integer 

from ..database.database import Base

class UserGroup(Base):
    __tablename__ = "users_groups"
    user_id = Column(Integer, primary_key=True)
    group_id = Column(Integer, primary_key=True)