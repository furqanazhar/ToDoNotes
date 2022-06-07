from datetime import datetime
from xmlrpc.client import DateTime
from pydantic import BaseModel
from enum import Enum


class Status(str, Enum):
    PENDING = 'PENDING'
    STARTED = 'STARTED'
    COMPLETED = 'COMPLETED'
    BLOCKED = 'BLOCKED'


class Priority(str, Enum):
    LOW = 'LOW'
    NORMAL = 'NORMAL'
    HIGH = 'HIGH'
    CRITICAL = 'CRITICAL'


class Category(str, Enum):
    WORK = 'WORK'
    GROCERY = 'GROCERY'
    SHOPPING = 'SHOPPING'
    TRAVELLING = 'TRAVELLING'
    MISCELLANEOUS = 'MISCELLANEOUS'


class Note(BaseModel):
    name: str
    description: str
    status: Status = Status.PENDING
    priority: Priority = Priority.NORMAL
    category: Category = Category.MISCELLANEOUS
    date: DateTime = datetime.now()
