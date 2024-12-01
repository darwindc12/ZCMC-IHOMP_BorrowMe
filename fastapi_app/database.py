from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace these details with your database information
DATABASE_URL = "postgresql://postgres:abracadabra@localhost/Borrow"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# This will help us get a session to interact with the database


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
