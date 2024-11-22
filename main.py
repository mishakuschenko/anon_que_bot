import telebot #проверяю
from os import getenv
from dotenv import load_dotenv
import handlers 


load_dotenv()
bot = telebot.TeleBot(getenv('TOKEN'))

def parse_handlers():
    handlers.start_handler(bot)
    handlers.callback_inline(bot)

if __name__ == "__main__":
    parse_handlers()
    bot.infinity_polling()
