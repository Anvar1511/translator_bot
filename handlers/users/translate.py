from aiogram import types

from loader import dp
from googletrans import Translator
tarjimon = Translator()

@dp.message_handler(content_types=['text'])
async def translate(message):
	input_text = message.text
    tarjima = tarjimon.translate(input_text, src="uz", dest="en")
    await bot.answer(tarjima.text)

