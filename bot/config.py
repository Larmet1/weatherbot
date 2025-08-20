import os 
from dotenv import load_dotenv

# завантажуємо змінні з .env
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
