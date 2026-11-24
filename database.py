import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL", "postgresql://postgres:123@localhost:5433/appdb"))

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_session():
    session = SessionLocal()
    yield session
    session.close()
    