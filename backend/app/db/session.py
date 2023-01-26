from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

POSTGRES_DATABASE_URL = "postgresql+psycopg2://postgres:admin1234@localhost:5432/postgres"

engine = create_engine(url="sqlite:///", pool_pre_ping=True, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoFlush=False, bind=engine)
