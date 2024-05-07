import types
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import aiogram
from aiogram import Bot, Dispatcher
from aiogram.utils import executor

bot = Bot(token='7107770270:AAGmUyC59vNjX6AN-wKwpRE0lB4rSz_qDC4')
dp = Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text=f"Salom {message.from_user.full_name} Artex brendining telegram bo'tiga xush kelibsiz pastdagilartdan ozingizga keragini tanlang")
    await message.answer(text=f"1-Shlyapalar"
                              f"2-Naklekalar"                   
                              f"3-Lentali quyonchalar"
                              f"4-Ayiqchalar")
    types.ReplyKeyboardMarkup("a")


    keyboard = types.InlineKeyboardMarkup(resize_keyboard=True, row_width=4)
    buttons = [
        types.KeyboardButton("Artex Brendi haqida ma'lumot"),
        # types.KeyboardButton("Mahsulotlarimiz"),
        # types.KeyboardButton("Ish"),
        types.KeyboardButton("Telegram Kanal"),
        types.KeyboardButton("Sotuv Bo'limi"),
        types.KeyboardButton("Telefon raqam"),
        types.KeyboardButton("Joylashuv"),
        # types.KeyboardButton("videolar"),
        # types.KeyboardButton("Rasmlar"),

    ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    keyboard.add(*buttons)
    await message.answer("Tanlang:", reply_markup=keyboard)
# Brend
    @dp.message_handler(lambda message: message.text == "Artex Brendi haqida ma'lumot")
    async def button1(message: types.Message):
        await message.answer("Artex MCHJ 2010-yilda tashkil topgan korxona yo'nalishi tekstil aksesuarlarini ishlab chiqarish bilan shug'ullanadi")
# Mahsulotlar
    @dp.message_handler(lambda message: message.text == "Sotuv Bo'limi")
    async def button2(message: types.Message):
        await message.answer(f"https://t.me/nuewdhewioewiobot Ushbu ssilka orqali siz tovarlarni ko'rib ular haqida ma'lumotlar olib zakaz berishingiz mumkin")
        # await message.answer("Bizda Kiyimlar uchun aksesuarlar naklekalar chiqariladi ular odatda bolalar uchun boladi pastdagi mahsulotlardan o'zingizga keragini tanlang")
        # inline_keybord = InlineKeyboardMarkup()
        # nakleka = InlineKeyboardButton("Naklekalar", callback_data="nakleka", url="youtube.com")
        # Kozlar = InlineKeyboardButton("Koz", callback_data="Koz")
        # Ayiq = InlineKeyboardButton("Ayiqcha", callback_data="Ayiq")
        # inline_keybord.add(nakleka)
        # inline_keybord.add(Kozlar)
        # inline_keybord.add(Ayiq)

# Telegram Kanal
    @dp.message_handler(lambda message: message.text == "Telegram Kanal")
    async def button3(message: types.Message):
        await message.answer("f<a>https://t.me/ARTEXUZ</a>")
# Telefon raqam
    @dp.message_handler(lambda message: message.text == "Telefon raqam")
    async def button4(message: types.Message):
        Number = 997908777
        await bot.send_contact(message.chat.id, phone_number=Number, first_name="Jaloliddin",
                               last_name="Nuriddinovich")
    @dp.message_handler(lambda message: message.text == "Joylashuv")
    async def button4(message: types.Message):
        latitude = 41.405076
        longitude = -69.205184
        await bot.send_location(message.chat.id, latitude=latitude, longitude=longitude)

        @dp.message_handler(lambda message: message.text == "Sotuv bolimi")
        async def button3(message: types.Message):
            await message.answer("f<a>https://t.me/Artexzakazbot</a>")

    # @dp.message_handler(lambda message: message.text == "Rasmlar")
    # async def send_picture(message: types.Message):
    #     with open("photo_2024-03-15_13-19-48.jpg", "rb") as rasm:
    #         await bot.send_photo(message.chat.id, rasm, caption="Biz ishlab chiqaradigan barcha mahsulotlar")
    #     with open("photo_2024-03-15_13-19-12.jpg", "rb") as rasm:
    #         await bot.send_photo(message.chat.id, rasm, caption="Tikiladigan ayiqcha")
    #     with open("photo_2024-03-15_13-19-19.jpg", "rb") as rasm:
    #         await bot.send_photo(message.chat.id, rasm, caption="Lentalar")
    #     with open("photo_2024-03-15_13-19-30.jpg", "rb") as rasm:
    #         await bot.send_photo(message.chat.id, rasm, caption="Tikiladigan ayiqchalar")
    #     with open("photo_2024-03-15_13-19-48.jpg", "rb") as rasm:
    #         await bot.send_photo(message.chat.id, rasm, caption="Ko'zi yonuvchi nakleka")
    #     with open("photo_2024-03-15_13-19-45.jpg", "rb") as rasm:
    #         await bot.send_photo(message.chat.id, rasm, caption="Yopishadigan ko'zlar")
    #     with open("photo_2024-03-15_13-19-57.jpg", "rb") as rasm:
    #         await bot.send_photo(message.chat.id, rasm, caption="Tikiladigan emblema")
    #     with open("photo_2024-03-15_13-20-18.jpg", "rb") as rasm:
    #         await bot.send_photo(message.chat.id, rasm, caption="Dazmollanadigan naklekalar")
    # c = int(input("Yoshingizni yozing"))
    # if c > 18:
    #     pass
    # elif c < 18:
    #     await message.reply(text="kechirasiz sizni ishga ola olmaymiz bizga 18 yoshdan kattalar kerak siz hali bola ekansiz")
    #     # break;
    # f = input("Siz tekstil sohasini stanoklarni ishlatishni bilasizmi")
    # if f == "ha" or "hm" or "Ha" or "HA":
    #     pass
    # elif f == "yoq" or "YOQ" or "Yoq" or "yo'q" or "Yo'q":
    #     await message.answer(text=
    #         "Kechirasiz biz sizni ishga ola olmaymiz bizda stanoklar ishlatiladi siz uni ishlatishni bilishingiz kerak")
    # await message.answer(text="Tabriklaymiz siz ishga olindingiz Biz o'zimiz sizga Xabar beramiz kuting 6 soatdan 12 soatgacha ishlaysiz oyligingiz 5 million so'mgacha bo'ladi")
if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)