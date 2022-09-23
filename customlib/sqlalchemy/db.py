from typing import List, Optional, Union
from customlib.sqlalchemy import PGConfig
from customlib.sqlalchemy.models import Base, Tag
from sqlalchemy import create_engine, select
from sqlalchemy_utils import create_database, database_exists, drop_database
from sqlalchemy.orm import Session


class Database:

    def __init__(self, config: PGConfig) -> None:
        self.url: str = str(config)
        self.engine = create_engine(self.url, echo=True, future=True)
        self.session = Session(self.engine)

    def nuke(self, ) -> None:
        if database_exists(self.url):
            drop_database(self.url)
        create_database(self.url)  
        Base.metadata.create_all(self.engine)

    def insert(self, entries: Union[List[Tag], Tag]):
        if isinstance(entries, Tag):
            self.session.add(entries)
        elif isinstance(entries, List):
            self.session.add_all(entries)
        self.session.commit()

    def select(self, ) -> Optional[List[Tag]]:
        stmt = select(Tag)
        results = self.session.scalars(stmt)
        return results