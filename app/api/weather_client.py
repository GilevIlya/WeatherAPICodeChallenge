import httpx


class WeatherApiClient:

    @staticmethod
    async def get(url: str, params: dict) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()