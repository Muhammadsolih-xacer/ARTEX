import types
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import aiogram
from aiogram import Bot, Dispatcher
from aiogram.utils import executor

bot = Bot(token='6469265686:AAHWnL5vFhYNflSw5B4V27_t-KtNB0G5bfY')
dp = Dispatcher(bot)

buttons = [
    types.KeyboardButton("1"),
    types.KeyboardButton("2"),
    types.KeyboardButton("3"),
    types.KeyboardButton("4"),
    types.KeyboardButton("5"),

]
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text=f"Salom {message.from_user.full_name} ARTEX brendining sotuv bolimiga xush kelibsiz pastdan o'zingizgakerakli mahsulotning raqamini tanlang"
                         "1-Yopishadigan ko'zlar"
                         "2-Tikiladigan ayiqlar"
                         "3-Tikiladigan naklekalar"
                         "4-Ko'nus toshlar"
                         "5-Dazmollanadigan naklekalar")


    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    keyboard.add(*buttons)
    # @dp.message_handler(lambda message: message.text == "1")
    # async def button1(message: types.Message):
    #     with open("C:\Users\Professional\PycharmProjects\ARTEX\photo_2024-03-15_13-19-48.jpg", "rb") as rasm:
    #         await bot.send_photo(message.chat.id, rasm, caption="Mahsulot nomi: Yopishadigan ko'z"
    #                                                             "Nimalarga ishlatiladi: Bu ko'zlar listga yopishgan bo'ladi listdan olib kiyimlarga yopishtirish mumkin"
    #                                                             "Narxi: Donasi 10 000 so'm")


    @dp.message_handler(lambda message: message.text == "2")
    async def button1(message: types.Message):
        with open("photo_2024-03-15_13-19-30.jpg", "rb") as rasm:
            await bot.send_photo(message.chat.id, rasm, caption="Mahsulot nomi: Tikiladigan ayiqlar"
                                                                "Nimalarga ishlatiladi: Kiyimlarga tikib qo'ysangiz kiyim chiroyli bo'ladi"
                                                                "Narxi: Donasi 5 000 so'm")

    @dp.message_handler(lambda message: message.text == "3")
    async def button1(message: types.Message):
        with open("C:\Users\Professional\PycharmProjects\ARTEX\photo_2024-03-15_13-19-45.jpg", "rb") as rasm:
            await bot.send_photo(message.chat.id, rasm, caption="Mahsulot nomi: Tikiladigan naklekalar"
                                                                "Nimalarga ishlatiladi: Bu ham ayiqlarga o'xshab kiyimlarga tikiladi bu ham o'zgacha chiroy beradi")


    @dp.message_handler(lambda message: message.text == "4")
    async def button1(message: types.Message):
        with open("C:\Users\Professional\Downloads\photo_2024-04-24_20-27-15.jpg.jpg", "rb") as rasm:
            await bot.send_photo(message.chat.id, rasm, caption="Mahsulot nomi: Ko'nus toshlar"
                                                                "Nimalarga ishlatiladi: Ko'nus toshlarni kiyimlarga yopishtirsangiz chiroyli bo'ladi"
                                                                "Narxi: 1kg 100 000 so'm")


    @dp.message_handler(lambda message: message.text == "5")
    async def button1(message: types.Message):
        with open("C:\Users\Professional\PycharmProjects\ARTEX\photo_2024-03-15_13-20-18.jpg", "rb") as rasm:
            await bot.send_photo(message.chat.id, rasm, caption="Mahsulot nomi: Dazmollanadigan naklekalar"
                                                                "Nimalarga ishlatiladi: Bu naklekalar tikilmaydi bular dazmollanib yopishtiriladi"
                                                                "Narxi 1listi 35 000 so'm")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
