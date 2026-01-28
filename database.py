from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database credentials
DB_USER = "budget_user"
DB_PASSWORD = "mehwar123"
DB_HOST = "localhost"
DB_NAME = "budget_tracker"

# Create Database URL
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Create SQLAlchemy Engine
engine = create_engine(DATABASE_URL)

# Create Session Local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class for models
Base = declarative_base()
