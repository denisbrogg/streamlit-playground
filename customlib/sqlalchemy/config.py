from dataclasses import dataclass


@dataclass
class PGConfig:
    USR: str = "postgres"
    PWD: str = "postgres"
    HOST: str = "localhost"
    PORT: str = "5432"
    DB: str = "streamlit-demo"
    DIALECT: str = "psycopg2"

    def __str__(self) -> str:
        return f"postgresql+{self.DIALECT}://{self.USR}:{self.PWD}@{self.HOST}:{self.PORT}/{self.DB}"
