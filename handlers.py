from lib.files import ReadFile

read = ReadFile()

def start_handler(bot):
    @bot.message_handler(commands=["start"])
    def start(msg):
        bot.send_message(msg.chat.id, read.read("./texts/start.txt"))
