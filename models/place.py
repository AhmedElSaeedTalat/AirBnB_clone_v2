#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from models import hb_storage
from models.review import Review
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity',
                      Base.metadata,
                      Column('place_id',
                             String(60),
                             ForeignKey('places.id'),
                             nullable=False,
                             primary_key=True),
                      Column('amenity_id',
                             String(60),
                             ForeignKey('amenities.id'),
                             nullable=False,
                             primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if hb_storage == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review',
                               cascade='all, delete',
                               backref='place')
        amenities = relationship('Amenity',
                                 secondary=place_amenity,
                                 viewonly=False,
                                 back_populates='place_amenities')
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
        @property
        def reviews(self):
            """ list of Review instances with place_id == current Place.id """
            review_instances = storage.all(Review)
            review_list = []
            for key, review in review_instances.items():
                if self.id == review.place_id:
                    riview_list.append(review)
            return review_list

        @property
        def amenities(self):
            """  list of Amenity instances based on attribute amenity_ids """
            amenity_instances = storage.all('Amenity')
            amenity_list = []
            for key, amenity in amenity_instances.items():
                if self.id == amenity.place_id:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """ setter """
            pass
