from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime, timezone


class Airline(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    flyghtDate: datetime = Field(alias="FL_DATE")
    airlineIdentifier: int = Field(alias="OP_CARRIER")
    flightNumber: int = Field(alias="OP_CARRIER_FL_NUM")
    originAirport: str = Field(alias="ORIGIN")
    destinationAirport: str = Field(alias="DEST")
    plannedDepartureTime: datetime = Field(alias="CRS_DEP_TIME")
    actualDepartureTime: datetime = Field(alias="DEP_TIME")
    totalDelayOnDeparture: int = Field(alias="DEP_DELAY")
    taxiOut: int = Field(alias="TAXI_OUT")
    wheelsOff: datetime = Field(alias="WHEELS_OFF")

    class Settings:
        name = "airline"
        use_state_management = True
