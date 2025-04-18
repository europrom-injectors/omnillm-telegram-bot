from aiogram import Router, F
from aiogram.types import Message, ContentType

from telegramify_markdown import markdownify


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
        await message.reply(
            "Произошла ошибка. Попробуйте написать команду /clear, если не помогло смените модель с помощью команды /model. Если и это не помогло, свяжитесь с разработчиком: @lixelv"
        )
        raise e

    if len(result) <= 4000:
        return await message.reply(markdownify(result), parse_mode="MarkdownV2")
    else:
        last_message = message

        for sub_message in [result[i : i + 4000] for i in range(0, len(result), 4000)]:
            last_message = await last_message.reply(
                markdownify(sub_message), parse_mode="MarkdownV2"
            )

        return last_message
