from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Rocket(Base):
    __tablename__ = 'rockets'
    id = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    wikipedia = Column(String)


class Launch(Base):
    __tablename__ = 'launches'
    id = Column(String, primary_key=True)
    details = Column(String)
    mission_name = Column(String)
    