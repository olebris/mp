"""peak data store
"""
from typing import Generator
from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker, registry
from . import settings


engine = create_engine(
    settings.DATABASE_URL, echo=settings.ECHO_SQL,
    future=True, pool_pre_ping=True
)
SessionLocal = sessionmaker(bind=engine)
mapper = registry()


@mapper.mapped
class PeakSchema:
    __tablename__ = "peak"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=True)

    latitude = Column(Numeric, nullable=False)
    longitude = Column(Numeric, nullable=False)
    altitude = Column(Numeric, nullable=False)


def session() -> Generator:
    """Dependency to be injected in endpoints
    """
    _ = SessionLocal()
    try:
        yield _
    finally:
        _.close()

with engine.begin() as transaction:
    mapper.metadata.create_all(transaction)
