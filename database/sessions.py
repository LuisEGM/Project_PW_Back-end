from SQLAlchemy import create_engine
from SQLAlchemy.orm import sessionmaker
from SQLAlchemy.ext.declarative import declarative_base
from app.core.config import settings

engine = create_engine(settings.SQL_ALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
