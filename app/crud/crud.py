from typing import Union
from sqlalchemy.orm import Session

from ..models.models import User, Group, Message
from ..models.abstract_models import CommonModel

def get_entity(db: Session, cls: type[CommonModel], id: int):
    if not cls.issubclass(CommonModel):
        raise TypeError(f"{cls.__name__} is not a subclass of {CommonModel.__name__}")
    entity = db.query(cls).get(id)
    if entity is None:
        raise ValueError(f"No {cls.__name__} with id: {id}")
    return entity

def get_user_groups(entity: Union[User, Group]):
    if type(entity) not in [User,Group]:
        raise TypeError(f"{type(entity).__name___} is not an allowed type of entity")
    if entity == User:
        return entity.groups.all()
    elif entity == Group:
        return entity.users.all()

def get_received_messages(entity: Union[User,Group]):
    if type(entity) not in [User,Group]:
        raise TypeError(f"{type(entity).__name___} is not an allowed type of entity")
    return entity.received_messages.all()

def get_sent_messages(user: User):
    return user.sent_messages.all()

