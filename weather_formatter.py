from weather_api_service import Weather

def format_weather(weather: Weather) -> str:
    """Formats weather data in string"""
    return (f"{weather.city}, Tемпература {weather.temperature}°C, "
            f"{weather.weather_type.value}\n"
            f"Восход: {weather.sunrise.strftime('%H:%M')}\n"
            f"Закат: {weather.sunset.strftime('%H:%M')}\n")


if __name__ == '__main__':
    from datetime import datetime
    from weather_api_service import WeatherType

    print(format_weather(Weather(
        temperature=25,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat("2000-01-01 08:01:01"),
        sunset=datetime.fromisoformat("2000-01-01 20:25:00"),
        city="Saint-Petersburg"
    )))
