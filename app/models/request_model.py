from pydantic import BaseModel

class FlightData(BaseModel):
    DEPARTURE_DELAY: float
    TAXI_OUT: float
    TAXI_IN: float
    AIR_TIME: float
    ELAPSED_TIME: float
    SCHEDULED_TIME: float
    WEATHER_DELAY: float
    ORIGIN_AIRPORT: int
    DESTINATION_AIRPORT: int
    AIRLINE: int