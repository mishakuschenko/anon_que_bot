import telebot
import os
from dotenv import load_dotenv
import handlers 

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))
handlers.start_handler(bot)


if __name__ == "__main__":
    bot.infinity_polling()

