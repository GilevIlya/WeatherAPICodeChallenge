from rich.console import Console
from rich.table import Table
from app.models.forecast import Forecast

console = Console()


def render_table(forecasts: list[Forecast]) -> None:
    table = Table(title=f"Weather Forecast — {forecasts[0].date}")

    table.add_column("City", style="bold cyan")
    table.add_column("Min °C", justify="center")
    table.add_column("Max °C", justify="center")
    table.add_column("Humidity %", justify="center")
    table.add_column("Wind kph", justify="center")
    table.add_column("Wind Direction", justify="center")

    for forecast in forecasts:
        table.add_row(
            forecast.city,
            str(forecast.min_temp),
            str(forecast.max_temp),
            str(forecast.humidity),
            str(forecast.wind_speed),
            forecast.wind_direction,
        )

    console.print(table)