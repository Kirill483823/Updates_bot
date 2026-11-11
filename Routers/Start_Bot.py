from aiogram.filters import Command
from aiogram import F, Router
from aiogram.types import Message

from Keyboards import battons_on_main_menu

start_router = Router()

@start_router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("🗃️ Привет,  отправь мне что нибудь и я отправлю тебе всю информацию "\
                         "о твоем сообщении (телеграм Update) в формате JSON", reply_markup=battons_on_main_menu())
