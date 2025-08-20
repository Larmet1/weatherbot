import asyncio
import os
import sys
from aiogram import Bot, Dispatcher

# Дозволяємо запускати файл як модуль (python -m bot.main) і напряму (python bot/main.py)
if __package__ in (None, ""):
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bot.config import BOT_TOKEN
from bot.handlers import start, weather

async def main():
    """
    Запуск бота:
    - створюємо бот і диспетчер
    - підключаємо хендлери
    - запускаємо long polling
    """
    if not BOT_TOKEN:
        raise RuntimeError("Environment variable BOT_TOKEN is not set. Add it to your .env file.")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Реєструємо хендлери
    dp.include_router(start.router)
    dp.include_router(weather.router)

    # Видаляємо старий webhook і стартуємо polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
