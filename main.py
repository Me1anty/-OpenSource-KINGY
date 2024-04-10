import configparser
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

config = configparser.ConfigParser()
config.read("config.ini")

bot_token = config["bot"]["token"]
referral_link = config["bot"]["referral_link"]

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    text = (
        "GM everyday and bring your daily rewards with KING\n"
        f"Invite your friend by referral link: {referral_link}"
    )
    
    inline_keyboard = types.InlineKeyboardMarkup()
    inline_keyboard.add(types.InlineKeyboardButton(text="GM", url=referral_link))
    
    await message.reply(text, reply_markup=inline_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
