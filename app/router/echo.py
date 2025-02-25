from aiogram import Router, F
from aiogram.types import Message, ContentType

from ai import agent_endpoint, Dependencies
from database import PostgresDB

router = Router()


@router.message(F.content_type == ContentType.TEXT)
async def reply(message: Message, db: PostgresDB):
    chat = await db.get_active_chat()

    loading = await message.answer_sticker(
        "CAACAgIAAxkBAAPaZ3K_UpoKOS2DU0xBfRF0b6v2j-oAArQjAAKYSylI3rm-zSpb5Nk2BA",
    )

    deps = Dependencies(db=db)

    try:
        chat = await db.get_active_chat()
        result = await agent_endpoint(
            db,
            chat.llm_model + (":online" if chat.online_model else ""),
            message.text,
            chat.agent,
            deps,
        )
        await loading.delete()
    except Exception as e:
        await loading.delete()
        return await message.reply(
            "Произошла ошибка. Свяжитесь с разработчиком: @lixelv"
        )

    if len(result) <= 4096:
        return await message.reply(result)
    else:
        last_message = message

        for sub_message in [result[i : i + 4096] for i in range(0, len(result), 4096)]:
            last_message = await last_message.reply(sub_message)

        return last_message
