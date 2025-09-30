#!/usr/bin/python3
"""DBStorage engine using SQLAlchemy"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """SQLAlchemy storage"""
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on current session and return dict of objects"""
        classes = {'User': User, 'State': State, 'City': City,
                   'Amenity': Amenity, 'Place': Place, 'Review': Review}
        result = {}
        if cls is None:
            for c in classes.values():
                for obj in self.__session.query(c).all():
                    key = obj.__class__.__name__ + '.' + obj.id
                    result[key] = obj
        else:
            c = cls if isinstance(cls, type) else classes.get(cls)
            if c is None:
                return result
            for obj in self.__session.query(c).all():
                key = obj.__class__.__name__ + '.' + obj.id
                result[key] = obj
        return result

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(factory)()

    def close(self):
        self.__session.close()


