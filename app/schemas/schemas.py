from pydantic import BaseModel

class UserBase(BaseModel):
    pass
class UserCreate(UserBase):
    pass
class User(UserBase):
    class Config:
        orm_mode = True

class GroupBase(BaseModel):
    pass
class GroupCreate(GroupBase):
    pass
class Group(GroupBase):
    class Config:
        orm_mode = True

class MessageBase(BaseModel):
    pass
class MessageCreate(MessageBase):
    pass
class Message(MessageBase):
    class Config:
        orm_mode = True