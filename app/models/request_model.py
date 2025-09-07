from pydantic import BaseModel

class FlightInput(BaseModel):
    YEAR: int
    MONTH: int
    DAY: int
    AIRLINE: str
    FLIGHT_NUMBER: int
    ORIGIN_AIRPORT: str
    ORIGIN_LATITUDE: float
    ORIGIN_LONGITUDE: float
    DESTINATION_AIRPORT: str
    SCHEDULED_DEPARTURE: int
    SCHEDULED_TIME: int
    ORIGIN_WEATHER: str
    ORIGIN_WIND_SPEED: float
