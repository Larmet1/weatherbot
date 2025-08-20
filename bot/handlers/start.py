from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_command(message: types.Message):
    """
    Вітальне повідомлення при /start
    """
    await message.answer("Привіт 👋 Введіть назву міста українською або будь-якою мовою, "
                         "і я покажу вам погоду ☁️🌡️")