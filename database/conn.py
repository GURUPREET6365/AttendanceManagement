import os
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
"""
This Base is the identifier for the class that will converted into tables. This contains orm and other details to change the columns property into constraints.
"""


def get_db():
    db=sessionLocal
    return db()