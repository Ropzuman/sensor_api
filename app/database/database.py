from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./Sensor-API.db"

# Create the database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class
Base = declarative_base()


# Create a function that returns a new database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
