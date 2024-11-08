from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dotenv import load_dotenv

# Load environment variables from `.env` file
load_dotenv()

# Create a connection to the database
DATABASE_URL = getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
metadata = Base.metadata

"""
Provides a database session to be used in a context manager.
Yields:
    Session: A SQLAlchemy database session.
Ensures that the database session is properly closed after use.
"""
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
