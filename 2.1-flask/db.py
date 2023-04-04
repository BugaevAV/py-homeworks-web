import atexit
import os
import uuid
from dotenv import load_dotenv
from sqlalchemy import Column, ForeignKey, String, Integer, DateTime, create_engine, func
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import EmailType, UUIDType

load_dotenv('./env/.env')
dsn = os.getenv('PG_DSN')

engine = create_engine(dsn)
Session = sessionmaker(bind=engine)
atexit.register(engine.dispose)

Base = declarative_base()


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    email_address = Column(EmailType, unique=True, nullable=False)
    password = Column(String, unique=True, nullable=False)
    ads = relationship('Ad', back_populates='user', cascade='save-update, merge, delete')


class Ad(Base):

    __tablename__ = 'ad'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ad_header = Column(String, unique=True, nullable=False, index=True)
    description = Column(String, unique=True, nullable=False)
    creation_date = Column(DateTime, server_default=func.now())
    owner_id = Column(Integer, ForeignKey("user.id"), index=True)
    user = relationship('User', back_populates='ads')


class Token(Base):

    __tablename__ = "tokens"

    id = Column(UUIDType, primary_key=True, default=uuid.uuid4)
    creation_time = Column(DateTime, server_default=func.now())
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    user = relationship("User", lazy="joined")


Base.metadata.create_all(bind=engine)
