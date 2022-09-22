from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


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
