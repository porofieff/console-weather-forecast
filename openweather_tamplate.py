import json

with open("data.json", "r") as file:
    data = json.load(file)

API_KEY = data['openweather']['api_key']

API_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + API_KEY + "&lang=ru&"
    "units=metric"
)

USE_ROUND_COORDS = True
