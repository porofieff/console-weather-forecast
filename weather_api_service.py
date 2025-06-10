from dataclasses import dataclass
from datetime import datetime
from typing import TypeAlias
from enum import Enum
import json

from coordinates import Coordinates

Celsius: TypeAlias = int

class WeatherType(Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"

@dataclass(slots=True, frozen=True)
class Weather:
    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str

def get_weather(coordinates: Coordinates):
    with open("data.json", "r") as file:
        data = json.load(file)

    API_KEY = data['openweather']['api_key']

    API_URL = (
        "https://api.openweathermap.org/data/2.5/weather?"
        "lat={latitude}&lon={longitude}&"
        "appid=" + API_KEY + "&lang=ru&"
        "units=metric"
    )





    return Weather(
        temperature=20,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat("1970-05-01 04:00:00"),
        sunset=datetime.fromisoformat("1970-01-01 20:25:00"),
        city="Moscow"
    )


get_weather(Coordinates(30, 60))
