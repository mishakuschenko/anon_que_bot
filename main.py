from os import getenv
from dotenv import load_dotenv


load_dotenv()
bot = telebot.TeleBot(getenv('TOKEN'))


