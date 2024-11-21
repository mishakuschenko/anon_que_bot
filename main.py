import telebot
from os import getenv
from dotenv import load_dotenv
import handlers 

load_dotenv()
global bot = telebot.TeleBot(getenv('TOKEN'))

def parse_handlers():
    handlers.start_handler(bot)

if __name__ == "__main__":
    bot.infinity_polling()
