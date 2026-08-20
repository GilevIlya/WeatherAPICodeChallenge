import asyncio
from app.api.forecast_api import get_forecast_raw
from app.models.forecast import Forecast
from config import settings


def parse_forecast(city: str, data: dict) -> Forecast:
    tomorrow = data["forecast"]["forecastday"][1]
    day = tomorrow["day"]
    midday = tomorrow["hour"][12]

    return Forecast(
        city=city,
        date=tomorrow["date"],
        min_temp=day["mintemp_c"],
        max_temp=day["maxtemp_c"],
        humidity=day["avghumidity"],
        wind_speed=day["maxwind_kph"],
        wind_direction=midday["wind_dir"],
    )


async def get_all_forecasts() -> list[Forecast]:
    tasks = [get_forecast_raw(city) for city in settings.cities]
    raw_data = await asyncio.gather(*tasks)
    return [parse_forecast(city, data) for city, data in zip(settings.cities, raw_data)]