from pydantic import BaseModel


class Forecast(BaseModel):
    city: str
    date: str
    min_temp: float
    max_temp: float
    humidity: int
    wind_speed: float
    wind_direction: str