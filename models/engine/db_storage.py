#!/usr/bin/python3
"""
This module defines a class to manage db for Airbnb clone
"""
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session

classes = {
    'State': State, 'City': City, 'User': User,
    'Place': Place, 'Review': Review, 'Amenity': Amenity,
}


class DBStorage:
    """
    Class to manage db for Airbnb clone
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initialization"""
        db_env = getenv("HBNB_ENV")
        db_user = getenv("HBNB_MYSQL_USER")
        db_pwd = getenv("HBNB_MYSQL_PWD")
        db_host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            f"mysql+mysqldb://{db_user}:{db_pwd}@{db_host}/{db}",
            pool_pre_ping=True)

        if db_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """doc"""

        obj_dict = {}
        if cls is not None and cls in classes:
            objs = self.__session.query(classes[cls]).all()
            for obj in objs:
                key = obj.__class__.__name__ + "." + obj.id
                obj_dict[key] = obj
        else:
            for cla in classes:
                for obj in self.__session.query(classes[cla]).all():
                    key = obj.__class__.__name__ + "." + obj.id
                    obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """
        add the object to the current database session (self.__session)
        """
        # if obj.__class__.__name__ in classes:
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        create the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_tory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_tory)
        self.__session = Session()

    def close(self):
        """Remove private session attribute"""
        self.__session.close()
