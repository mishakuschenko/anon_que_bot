from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
import asyncio

load_dotenv()
bot = Bot(getenv('TOKEN'))
dsp = Dispatcher()

@dsp.message()
async def start(message: types.Message):
    await message.answer("ты чета написал")


if __name__ == "__main__":
    asyncio.run(dsp.start_polling(bot))

