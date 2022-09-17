from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base


class Owner(Base):
    __tablename__ = "owner"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String, unique=True, nullable=False)
    pets = relationship("Pet", backref="owner")


class Pet(Base):
    __tablename__ = "pet"

    id = Column(Integer, primary_key=True, autoincrement=True)
    serial_number = Column(String, unique=True, nullable=False)
    owner_name = Column(String, ForeignKey('owner.fullname'), nullable=True)