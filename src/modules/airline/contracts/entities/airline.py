from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime, timezone


class Airline(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), alias="_id")
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    flyghtDate: datetime = Field(alias="FL_DATE", description="Date of the flight, yy/mm/dd")
    airlineIdentifier: str | int = Field(alias="OP_CARRIER", description="Airline Identifier")
    flightNumber: int = Field(alias="OP_CARRIER_FL_NUM", description="Flight Number")
    originAirport: str = Field(alias="ORIGIN", description="Starting Airport Code")
    destinationAirport: str = Field(alias="DEST", description="Destination Airport Code")
    plannedDepartureTime: int | None = Field(default=0, alias="CRS_DEP_TIME", description="Planned Departure Time")
    actualDepartureTime: float | None = Field(default=0.0 , alias="DEP_TIME", description="Actual Departure Time")
    totalDelayOnDeparture: float | None = Field(default=0.0, alias="DEP_DELAY",description="Total Delay on Departure in minutes")
    taxiOut: float | None= Field(default=0.0, alias="TAXI_OUT", description="The time duration elapsed between departure from the origin airport gate and wheels off")
    wheelsOff: float | None = Field(default=0.0, alias="WHEELS_OFF", description="The time point that the aircraft's wheels leave the ground")
    wheelsOn: float | None = Field(default=0.0, alias="WHEELS_ON", description="The time point that the aircraft's wheels touch the ground")
    taxiIn: float | None = Field(default=0.0, alias="TAXI_IN", description="The time duration elapsed between wheels-on and gate arrival at the destination airport")
    plannedArrivalTime: int | None = Field(default=0, alias="CRS_ARR_TIME", description="Planned Arrival Time")
    actualArrivalTime: float | None = Field(default=0.0, alias="ARR_TIME", description="Actual Arrival Time")
    totalDelayOnArrival: float | None = Field(default=0.0, alias="ARR_DELAY", description="Total Delay on Arrival in minutes")
    cancelled: float | None = Field(default=0.0, alias="CANCELLED", description="Cancelled Flight Indicator")
    cancellationCode: str | None = Field(default="", alias="CANCELLATION_CODE", description="Code indicating the reason for cancellation")
    diverted: float | None = Field(default=0.0, alias="DIVERTED", description="Diverted Flight Indicator")
    plannedElapsedTime: float | None = Field(default=0.0, alias="CRS_ELAPSED_TIME", description="Planned Elapsed Time in minutes")
    actualElapsedTime: float | None = Field(default=0.0, alias="ACTUAL_ELAPSED_TIME", description="Actual Elapsed Time in minutes")
    airTime: float | None = Field(default=0.0, alias="AIR_TIME", description="Time spent in the air in minutes")
    distance: float | None = Field(default=0.0, alias="DISTANCE", description="Distance between airports in miles")
    carrierDelay: float | None = Field(default=0.0, alias="CARRIER_DELAY", description="Carrier Delay in minutes")
    weatherDelay: float | None = Field(default=0.0, alias="WEATHER_DELAY", description="Weather Delay in minutes")
    nasDelay: float | None = Field(default=0.0, alias="NAS_DELAY", description="National Air System Delay in minutes")
    securityDelay: float | None = Field(default=0.0, alias="SECURITY_DELAY", description="Security Delay in minutes")
    lateAircraftDelay: float | None = Field(default=0.0, alias="LATE_AIRCRAFT_DELAY", description="Late Aircraft Delay in minutes")

    class Settings:
        name = "airline"
        use_state_management = True
