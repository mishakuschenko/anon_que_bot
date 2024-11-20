import telebot
import os
from dotenv import load_dotenv
import routes 

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))


@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(msg.chat.id, "hello")

if __name__ == "__main__":
    bot.infinity_polling()

