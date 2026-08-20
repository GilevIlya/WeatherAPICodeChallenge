from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    weather_api_key: str
    weather_api_base_url: str = "http://api.weatherapi.com/v1"
    forecast_days: int = 2
    cities: list[str] = ["Chisinau", "Madrid", "Kyiv", "Amsterdam"]

    class Config:
        env_file = ".env"


settings = Settings()