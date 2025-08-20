import requests
import asyncio
from bot.config import WEATHER_API_KEY

async def get_weather(city: str):
    """
    Шукає координати міста через Geo API, а потім отримує погоду за ними.
    Повертає dict з даними погоди або None при помилці/неуспіху.
    """
    if not WEATHER_API_KEY:
        return None

    try:
        # 1. Отримуємо координати міста
        geo_response = await asyncio.to_thread(
            requests.get,
            "https://api.openweathermap.org/geo/1.0/direct",
            params={
                "q": city,
                "limit": 1,
                "appid": WEATHER_API_KEY,
            },
            timeout=10,
        )

        if geo_response.status_code != 200:
            return None

        geo_json = geo_response.json()
        if not geo_json:
            return None

        geo_data = geo_json[0]
        latitude, longitude = geo_data.get("lat"), geo_data.get("lon")
        if latitude is None or longitude is None:
            return None

        # 2. Отримуємо погоду за координатами
        weather_response = await asyncio.to_thread(
            requests.get,
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "lat": latitude,
                "lon": longitude,
                "units": "metric",
                "lang": "uk",
                "appid": WEATHER_API_KEY,
            },
            timeout=10,
        )

        if weather_response.status_code != 200:
            return None

        return weather_response.json()

    except requests.RequestException:
        return None