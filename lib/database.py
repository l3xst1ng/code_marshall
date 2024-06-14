# lib/database.py
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL
from models import Base

def create_engine_with_retry(url, retries=3, delay=1):
    """
    Create a SQLAlchemy engine with retry functionality.

    Args:
        url (str): The database URL.
        retries (int): The number of retry attempts (default: 3).
        delay (int): The delay in seconds between retry attempts (default: 1).

    Returns:
        sqlalchemy.engine.Engine: The created SQLAlchemy engine.

    Raises:
        Exception: If the connection fails after the specified number of retries.
    """
    for attempt in range(retries):
        try:
            engine = create_engine(url)
            return engine
        except Exception as e:
            if attempt == retries - 1:
                raise e
            else:
                print(f"Connection attempt {attempt + 1} failed. Retrying in {delay} second(s)...")
                time.sleep(delay)

engine = create_engine_with_retry(DATABASE_URL)
Session = sessionmaker(bind=engine)

def create_tables():
    """
    Create the database tables based on the defined models.

    Raises:
        Exception: If an error occurs while creating the tables.
    """
    try:
        Base.metadata.create_all(engine)
    except Exception as e:
        print(f"An error occurred while creating tables: {str(e)}")
        raise