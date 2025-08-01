from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

url = URL.create(
    drivername=os.environ.get('DRIVERNAME'),
    username=os.environ.get('USERNAME'),
    password=os.environ.get('PASSWORD'),
    host=os.environ.get('HOST'),
    port=os.environ.get('PORT'),
    database=os.environ.get('DATABASE')
)

engine = create_engine(url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
