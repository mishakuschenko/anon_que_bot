from main import bot
import telebot

@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(msg.chat.id, "hello bro")
