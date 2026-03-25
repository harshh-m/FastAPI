from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:1808@localhost:5432/fastapi_db"
engine = create_engine(db_url)
session = sessionmaker(bind=engine,autocommit=False,autoflush=False)