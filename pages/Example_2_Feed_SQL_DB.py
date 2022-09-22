"""_summary_ """

from dataclasses import dataclass
from datetime import datetime
from turtle import onclick

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy_utils import database_exists, create_database

from sqlalchemy import Column, ForeignKey, Integer, String, Date

import streamlit as st
import numpy as np

Base = declarative_base()

@dataclass
class PGConfig:
    USR: str = "postgres"
    PWD: str = "postgres"
    HOST: str = "localhost"
    PORT: str = "5432"
    DB: str = "tags"
    DIALECT: str = "psycopg2"

    def __str__(self) -> str:
        return f"postgresql+{self.DIALECT}://{self.USR}:{self.PWD}@{self.HOST}:{self.PORT}/{self.DB}"
class Tag(Base):
    """Single row of the database"""
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    timestamp: Column(Date)
    flight: Column(String(10))
    condition: Column(String(10))
    parameter: Column(String(10))
    user: Column(String(10))
    tag: Column(String(10))


def get_engine(config: PGConfig):
    url: str = str(config)
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine

def get_session(engine):
    return sessionmaker(bind=engine)()

config = PGConfig()
engine = get_engine(config)
session = get_session(engine)


st.title("SQL DB Feed Demo")
st.write(PGConfig())
st.write(session)

cf, cc, cp, cu, ct = st.columns(5)

with cf:
    flight = st.selectbox("Flight", ("1245", "1250", "1322"))
with cc:
    condition = st.selectbox("Condition", ("-7", "14", "21"))
with cp:
    param = st.selectbox("Param", ("1111", "2222", "3333"))
with cu:
    user = st.selectbox("User", ("LHD1", "LHD2", "LHD3"))
with ct:
    tag = st.selectbox("Tag", ("GOOD", "BAD", "DK"))

def write_tag():
    st.write("yolo")

button = st.button("Write on DB", onclick=write_tag())