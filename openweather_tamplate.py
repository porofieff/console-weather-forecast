import os 


API_KEY = str(os.getenv("OW_API_KEY"))

API_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + API_KEY + "&lang=ru&"
    "units=metric"
)

USE_ROUND_COORDS = True
