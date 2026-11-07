from aiogram.types import Message
from aiogram import F, Router
from aiogram.filters import Command
import json

main_work_router = Router()

@main_work_router.message(~Command("start"))
async def main_work(message: Message):
    message_json_data_str = message.model_dump_json(
        indent=4,
        ensure_ascii=False,
        exclude_none=True,
    )

    chunks = []
    current_chunk = ""
    for line in message_json_data_str.splitlines(keepends=True):
        if current_chunk and len(current_chunk) + len(line) > 4000:
            chunks.append(current_chunk)
            current_chunk = ""
        current_chunk += line
    if current_chunk:
        chunks.append(current_chunk)

    for chunk in chunks:
        await message.answer(f"<pre><code class='language-json'>{chunk}</code></pre>",
                             parse_mode="HTML")
