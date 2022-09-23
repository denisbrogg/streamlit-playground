from sqlalchemy import Column, DateTime, Integer, String, Identity
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class Tag(Base):
    """Single row of the database"""

    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    time = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now())
    flight = Column(String)
    condition = Column(String)
    parameter = Column(String)
    user = Column(String)
    tag = Column(String)


