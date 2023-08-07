"""This module creates a new engine DBStorage"""

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, MetaData
from models.base_model import Base
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.review import Review


class DBStorage():
    """class to create engine"""
    __engine = None
    __session = None

    def __init__(self):
        """initialization"""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', 'localhost')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'. format(
            user, pwd, host, database), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query the current session depending on class name argument"""
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            new_objs = self.__session.query(cls)
        else:
            cls_list = [State, City, Place, User, Review, Amenity]
            for cls in cls_list:
                new_objs = self.__session.query(cls).all()

        return {"{}.{}".format(
                  type(obj).__name__, obj.id): obj for obj in new_objs}

    def new(self, obj):
        """adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commits all changes to database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from current database session if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                        bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """closes the current session"""
        self.__session.close()
