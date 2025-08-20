from aiogram import Router, types, F
from bot.services.weather_api import get_weather

router = Router()

@router.message(F.text)
async def weather_handler(message: types.Message):
    """
    Обробляє введення міста та показує погоду
    """
    city = message.text.strip()
    weather_data = await get_weather(city)

    if not weather_data:
        await message.answer(f"Не вдалося знайти місто: {city}")
        return

    # Витягуємо потрібні дані
    temperature = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    wind_speed = weather_data["wind"]["speed"]
    cloud_cover = weather_data["weather"][0]["description"]
    humidity = weather_data["main"]["humidity"]

    # Відправляємо користувачу
    await message.answer(
        f"Погода у місті {city}:\n"
        f"🌡️ Температура: {temperature}°C\n"
        f"🤔 Відчувається як: {feels_like}°C\n"
        f"💨 Вітер: {wind_speed} м/с\n"
        f"☁️ Хмарність: {cloud_cover}\n"
        f"💧 Вологість: {humidity}%"
    )