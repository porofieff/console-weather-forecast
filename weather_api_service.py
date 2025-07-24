from dataclasses import dataclass
from datetime import datetime
from typing import TypeAlias, Literal
from enum import Enum
import ssl
import urllib.request
from urllib.error import URLError
import json
from json.decoder import JSONDecodeError
import requests

from coordinates import Coordinates
from exceptions import api_service_error
import openweather_tamplate

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


def get_weather(coordinates: Coordinates) -> Weather:
    api_response_data = _get_api_response(longitude=coordinates.longitude, latitude=coordinates.latitude)
    parsed_data = _parse_data(api_response_data)

    return parsed_data


def _get_api_response(latitude: float, longitude: float) -> str:
    ssl._create_default_https_context = ssl._create_unverified_context

    my_url = openweather_tamplate.API_URL.format(latitude=latitude, longitude=longitude)

    try:
        data = requests.get(my_url)
        data = data.json()
        print(data)
        return data

    except URLError:
        raise api_service_error

    return Weather(
        temperature = round(weather_dict['main']['temp']),
        weather_type = _get_weather_type(weather_dict),
        sunrise = _parse_sun_time(weather_dict, 'sunrise'),
        sunset = _parse_sun_time(weather_dict, 'sunset'),
        city = weather_dict['name']
    )


def _get_weather_type(weather_dict: dict) -> WeatherType:
    try:
        weather_type_id = str(openweather_dict["weather"][0]["id"])
    except (IndexError, KeyError):
        raise api_service_error

    weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "80": WeatherType.CLOUDS
    }

    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return _weather_type

    raise api_service_error

def _parse_sun_time(openweather_dict: dict, time: Literal["sunrise"] | Literal["sunset"]) -> datetime:
    return datetime.fromtimestamp(openweather_dict["sys"][time])

if __name__ == "__main__":
    print(get_weather(Coordinates(latitude=59.9, longitude=30.3)))
