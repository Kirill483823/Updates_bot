from aiogram.filters import Command
from aiogram import F, Router
from aiogram.types import Message

from Keyboards import battons_on_main_menu

start_router = Router()

@start_router.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        "🗃️ Привет! Отправь мне любое сообщение, и я пришлю его данные в формате JSON.",
        reply_markup=battons_on_main_menu(),
    )
