"""peak logic
"""

from typing import Tuple, List
from http import HTTPStatus

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import conint
from sqlalchemy import select, and_, between
from sqlalchemy.orm import Session

from .model import PeakCreateModel, PeakFromDBModel, PeakUpdateModel, Latitude, Longitude
from .store import PeakSchema


def create(session: Session, in_peak: PeakCreateModel) -> PeakSchema:
    db_peak = PeakSchema(**in_peak.dict())
    session.add(db_peak)
    session.commit()
    session.refresh(db_peak)
    return db_peak

def read(session: Session, peak_id: conint(strict=True, gt=0)) -> PeakSchema:
    statement = select(PeakSchema).filter_by(id=peak_id)
    db_peak = session.execute(statement).scalar()
    if db_peak:
        return db_peak
    else:
        raise HTTPException(HTTPStatus.NOT_FOUND)

def update(session: Session, in_peak: PeakUpdateModel) -> None:
    db_peak = read(session, in_peak.id)
    db_peak_as_dict = jsonable_encoder(db_peak)
    in_peak_as_dict = in_peak.dict(exclude_unset=True)
    for attr in db_peak_as_dict:
        if attr != "id" and attr in in_peak_as_dict:
            setattr(db_peak, attr, in_peak_as_dict[attr])
    session.add(db_peak)
    session.commit()

def delete(session: Session, db_peak: PeakSchema) -> None:
    session.delete(db_peak)
    session.commit()

def retrieve(
    session: Session,
    latitudes: Tuple[Latitude,Latitude],
    longitudes: Tuple[Longitude, Longitude],
    skip: conint(strict=True, ge=0), limit: conint(strict=True, ge=0)
) -> List[PeakSchema]:
    """Retrieves a set of peaks included within a bounding box.
    a bounding box is defined by two positions.
    each with a latitude and a longitude
    """
    min_lat, max_lat = min(latitudes), max(latitudes)
    min_long, max_long = min(longitudes), max(longitudes)
    statement = select(PeakSchema).where(
        and_(
            between(PeakSchema.latitude, min_lat, max_lat),
            between(PeakSchema.longitude, min_long, max_long)
        )
    ).offset(skip).limit(limit)
    db_peaks = session.execute(statement).scalars()
    return db_peaks
