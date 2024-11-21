from lib.files import ReadFile
from telebot import types
from main import bot

read = ReadFile()

def start_handler(bot):
    @bot.message_handler(commands=["start"])
    def start(msg):
        inline_kbd = types.InlineKeyboardMarkup(row_width=3)
        start_button = types.InlineKeyboardButton(text="тестовая кнопка", callback_data="START")
        inline_kbd.add(start_button)
        bot.send_message(msg.chat.id, read.read("./texts/start.txt"), reply_markup=inline_kbd)


def callback_inline(bot):
    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        call_id = call.message.chat.id

        if call.message:
            if call.data == "START":
                bot.send_message(call_id, "all is good!")
                bot.answer_callback_query(callback_query_id=call.id, text="")


