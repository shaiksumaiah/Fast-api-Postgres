# database.py
import os
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_user = os.getenv("POSTGRES_USER", "postgres")
db_pass = os.getenv("POSTGRES_PASSWORD", "example")
db_host = os.getenv("POSTGRES_HOST", "db")  # when using docker-compose service name "db"
db_port = os.getenv("POSTGRES_PORT", "5432")
db_name = os.getenv("POSTGRES_DB", "fastapi")

db_pass_quoted = quote_plus(db_pass)

DATABASE_URL = f"postgresql://{db_user}:{db_pass_quoted}@{db_host}:{db_port}/{db_name}"

# pool_pre_ping helps with dropped connections in containers
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
