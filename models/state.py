#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
                "City", backref='states', cascade='all, delete-orphan')

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """returns list of City instances where state_id equals
            the current State.id
            """
            city_list = []
            for city in list(models.storage.all(City).values()):
                if self.id == city.state_id:
                    city_list.append(city)

            return (city_list)
