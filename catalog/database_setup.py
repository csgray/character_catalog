from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///characters.db')
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


class Race(Base):
    __tablename__ = 'races'

    name = Column(String, primary_key=True)
    patron = Column(String)
    description = Column(String)
    skills = Column(String, ForeignKey('skills.name'))


class Guild(Base):
    __tablename__ = 'guilds'

    name = Column(String, primary_key=True)
    description = Column(String)
    skills = Column(String, ForeignKey('skills.name'))


class Skill(Base):
    __tablename__ = 'skills'

    name = Column(String, primary_key=True)
    description = Column(String)
    time = Column(Integer)

Base.metadata.create_all(engine)
