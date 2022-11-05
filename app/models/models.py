from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .abstract_models import CommonModel
from .association_models import UserGroup

class User(CommonModel):
    __tablename__ = "users"
    name = Column(String, nullable=False)
    sent_messages = relationship("Message", back_populates="sender")
    received_messages = relationship("Message", back_populates="receiver_user")
    groups = relationship("Group", secondary=UserGroup)


class Group(CommonModel):
    __tablename__ = "groups"
    name = Column(String, nullable=False)
    received_messages = relationship("Message")

class Message(CommonModel):
    __tablename__ = "messages"
    content = Column(String, nullable=False)
    sender_id = Column(Integer, ForeignKey("users.id"))
    sender = relationship("User", back_populates="sent_messages")
    receiver_user_id = Column(Integer, ForeignKey("users.id"))
    receiver_user = relationship("User", back_populates="received_messages")
    receiver_group_id = Column(Integer, ForeignKey("groups.id"))
    receiver_group = relationship("Group", back_populates="received_messages")
