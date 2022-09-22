from customlib.sqlalchemy import PGConfig
from sqlalchemy import Column, Date, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_utils import create_database, database_exists

Base = declarative_base()


class Tag(Base):
    """Single row of the database"""

    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    flight: Column(String)
    condition: Column(String)
    parameter: Column(String)
    user: Column(String)
    tag: Column(String)


class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)
    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"))
    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


config_url: str = str(PGConfig())

if not database_exists(config_url):
    create_database(config_url)

engine = create_engine(config_url, echo=True, future=True)

Base.metadata.create_all(engine)
