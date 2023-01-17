# creating database
# docker run --name postgres -d -p 5432:5432 -e POSTGRES_PASSWORD=postgres postgres 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(DATABASE_URI)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
