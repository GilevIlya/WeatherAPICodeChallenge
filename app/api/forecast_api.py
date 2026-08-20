from app.api.weather_client import WeatherApiClient
from config import settings


async def get_forecast_raw(city: str) -> dict:
    url = f"{settings.weather_api_base_url}/forecast.json"
    params = {
        "key": settings.weather_api_key,
        "q": city,
        "days": settings.forecast_days,
    }
    return await WeatherApiClient.get(url, params)