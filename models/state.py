#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', backref='state', cascade='all, delete')

    if (getenv("HBNB_TYPE_STORAGE") != "db"):
        @property
        def cities(self):
            """
            returns the list of City instances with state_id equals to the
            current State.id
            """
            city_list = []
            cities_list = models.storage.all(City).values()
            for city in cities_list:
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
