from dataclasses import dataclass
from datetime import datetime
from typing import TypeAlias, Literal
from enum import Enum
from urllib.error import URLError
import requests

from coordinates import Coordinates
from exceptions import api_service_error
import openweather_tamplate

Celsius: TypeAlias = int


class WeatherType(str, Enum):
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
    feels_like_temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    humidity: int
    wind_speed: int
    city: str


def get_weather(coordinates: Coordinates) -> Weather:
    api_response_data = _get_api_response(longitude=coordinates.longitude, latitude=coordinates.latitude)
    parsed_data = _parse_data(api_response_data)

    return parsed_data


def _get_api_response(latitude: float, longitude: float) -> dict:
    my_url = openweather_tamplate.API_URL.format(latitude=latitude, longitude=longitude)

    try:
        data = requests.get(my_url)
        data = data.json()

        return data

    except URLError:
        raise api_service_error


def _parse_data(api_data: dict) -> Weather:
    return Weather(
    temperature=_parse_weather_temperature(api_data),
    feels_like_temperature=_parse_feels_like_temperature(api_data),
    weather_type=_parse_weather_type(api_data),
    sunrise=_parse_sun_time(api_data, "sunrise"),
    sunset=_parse_sun_time(api_data, "sunset"),
    humidity=_parse_weather_humidity(api_data),
    wind_speed=_parse_wind_speed(api_data),
    city=_parse_city(api_data)
    )


def _parse_weather_temperature(api_data: dict) -> Celsius:
    return round(api_data["main"]["temp"])


def _parse_feels_like_temperature(api_data: dict) -> Celsius:
    return round(api_data["main"]["feels_like"])


def _parse_weather_type(data_weather: dict) -> WeatherType:
    try:
        weather_type_id = str(data_weather["weather"][0]["id"])
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

    
def _parse_sun_time(api_data: dict, time: Literal["sunrise"] | Literal["sunset"]) -> datetime:
    return datetime.fromtimestamp(api_data["sys"][time])


def _parse_weather_humidity(api_data: dict) -> int:
    return api_data["main"]["humidity"]


def _parse_wind_speed(api_data: dict) -> int:
    return api_data["wind"]["speed"]


def _parse_city(api_data: dict) -> str:
    return api_data["name"]


if __name__ == "__main__":
    print(get_weather(Coordinates(latitude=59.9, longitude=30.3)))
