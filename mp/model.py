"""peak models
"""
from pydantic import BaseModel, conint, confloat, constr, root_validator


MountainName = constr(strict=True, strip_whitespace=True, to_lower=True, min_length=2)
Latitude = confloat(ge=-90, le=90,)
Longitude = confloat(ge=-180, le=180)
Altitude = confloat(ge=0)


class PeakCreateModel(BaseModel):
    name: MountainName | None
    latitude: Latitude
    longitude: Longitude
    altitude: Altitude

    class Config:
        orm_mode=True


class PeakFromDBModel(PeakCreateModel):
    id: int


class PeakUpdateModel(PeakFromDBModel):
    name: MountainName | None = None
    latitude: Latitude = None
    longitude: Longitude = None
    altitude: Altitude = None

    @root_validator
    def at_least_one_field_set(cls, values):
        update_fields = [field for field in PeakUpdateModel.__fields__ if field != "id"]
        update_values = [values.get(field) for field in update_fields]
        if any(update_values):
            return values
        else:
            raise ValueError("at least one field should be set from: ", *update_fields)

