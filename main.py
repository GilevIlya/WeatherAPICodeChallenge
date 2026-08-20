import asyncio
from app.services.forecast_service import get_all_forecasts
from app.display.forecast_table import render_table


async def main():
    forecasts = await get_all_forecasts()
    render_table(forecasts)


if __name__ == "__main__":
    asyncio.run(main())