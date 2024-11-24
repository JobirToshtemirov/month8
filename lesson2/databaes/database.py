import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

from main.config import DB_HOST, DB_USER, DB_PORT, DB_NAME, DB_PASS

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

database = databases.Database(DATABASE_URL)

Base = declarative_base()
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)
