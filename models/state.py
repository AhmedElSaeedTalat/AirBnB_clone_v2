#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import hb_storage, storage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if hb_storage == 'db':
        cities = relationship("City",
                              cascade="all, delete",
                              passive_deletes=True,
                              backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """ getter cities """
            cities_list = storage.all(City)
            related_cities = []
            for city in cities_list.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
