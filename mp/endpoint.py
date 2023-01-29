"""peak endpoints
"""

from typing import List
from http import HTTPStatus
from fastapi import Depends
from sqlalchemy.orm import Session
from . import app
from .store import session
from .model import PeakCreateModel, PeakUpdateModel, PeakFromDBModel, Latitude, Longitude
from .logic import create, read, update, delete, retrieve


@app.post("/peaks/create", response_model=PeakFromDBModel, status_code=HTTPStatus.CREATED)
def post_peak(
    session: Session = Depends(session),
    *, in_peak: PeakCreateModel
):
    db_peak = create(session, in_peak)
    return PeakFromDBModel.from_orm(db_peak)

@app.get("/peaks/read/{id}", response_model=PeakFromDBModel)
def get_peak(
    session: Session = Depends(session),
    *, id: int
):
    db_peak = read(session, id)
    return PeakFromDBModel.from_orm(db_peak)

@app.put("/peaks/update", status_code=HTTPStatus.NO_CONTENT)
def put_peak(
    session: Session = Depends(session),
    *, in_peak: PeakUpdateModel
):
    update(session, in_peak)

@app.delete("/peaks/delete/{id}", status_code=HTTPStatus.NO_CONTENT)
def delete_peak(
    session: Session = Depends(session),
    *, id: int
):
    db_peak = read(session, id)
    delete(session, db_peak)

@app.get(
    "/peaks/retrieve/{lat_1}/{long_1}/{lat_2}/{long_2}",
    response_model=List[PeakFromDBModel]
)
def retrieve_peak(
    session: Session = Depends(session),
    *,
    lat_1: Latitude, long_1: Longitude,
    lat_2: Latitude, long_2: Longitude,
    skip: int = 0, limit: int = 100
):
    db_peaks = retrieve(session, (lat_1, lat_2), (long_1, long_2), skip, limit)
    return [PeakFromDBModel.from_orm(_) for _ in db_peaks]
