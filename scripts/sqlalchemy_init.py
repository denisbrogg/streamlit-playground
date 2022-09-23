from customlib.sqlalchemy import PGConfig
from customlib.sqlalchemy import Database
from customlib.sqlalchemy import Tag

config: PGConfig = PGConfig()

db: Database = Database(config)

db.nuke()

tags = [
    Tag(flight="F0001", condition="C68", parameter="P1234", user="User1", tag="GOOD"),
    Tag(flight="F0001", condition="C69", parameter="P1234", user="User1", tag="GOOD"),
    Tag(flight="F0001", condition="C70", parameter="P1234", user="User1", tag="GOOD"),
]

db.insert(entries=tags)
