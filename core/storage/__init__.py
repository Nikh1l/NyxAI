from .database import Base
from .database import SessionLocal
from .database import engine

from . import models # noqa: F401

def init_database():
    Base.metadata.create_all(bind=engine)