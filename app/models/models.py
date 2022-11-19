from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from .abstract_models import CommonModel
from .association_models import UserGroup



class Group(CommonModel):
    __tablename__ = "groups"
    name = Column(String, nullable=False)
    received_messages = relationship("Message")

class Message(CommonModel):
    __tablename__ = "messages"
    content = Column(String, nullable=False)
    sender_id = Column(String, ForeignKey("users.id"))
    sender = relationship("User", back_populates="sent_messages")
    receiver_user_id = Column(String, ForeignKey("users.id"))
    receiver_user = relationship("User", back_populates="received_messages")
    receiver_group_id = Column(String, ForeignKey("groups.id"))
    receiver_group = relationship("Group", back_populates="received_messages")

class User(CommonModel):
    __tablename__ = "users"
    name = Column(String, nullable=False)
    sent_messages = relationship("Message", back_populates="sender", foreign_keys=[Message.id])
    received_messages = relationship("Message", back_populates="receiver_user", foreign_keys=[Message.id])
    groups = relationship("Group", secondary=UserGroup)