from os import getenv
from dotenv import load_dotenv
load_dotenv()

bot = Bot(getenv('TOKEN'))
dsp = Dispatcher(bot)


