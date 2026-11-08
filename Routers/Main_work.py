from html import escape

from aiogram.types import CallbackQuery, Message
from aiogram import Router
from aiogram.filters import Command

main_work_router = Router()


async def send_update_json(message: Message, update: Message | CallbackQuery):
    update_json_data_str = update.model_dump_json(
        indent=4,
        ensure_ascii=False,
        exclude_none=True,
    )

    chunks = []
    current_chunk = ""
    for line in update_json_data_str.splitlines(keepends=True):
        if current_chunk and len(current_chunk) + len(line) > 4000:
            chunks.append(current_chunk)
            current_chunk = ""
        current_chunk += line
    if current_chunk:
        chunks.append(current_chunk)

    for chunk in chunks:
        await message.answer(f"<pre><code class='language-json'>{escape(chunk)}</code></pre>",
                             parse_mode="HTML")


@main_work_router.message(~Command("start"))
async def main_work(message: Message):
    await send_update_json(message, message)


@main_work_router.callback_query()
async def show_callback_json(callback_query: CallbackQuery):
    await callback_query.answer()
    if isinstance(callback_query.message, Message):
        await send_update_json(callback_query.message, callback_query)