import html
import markdown

from aiogram import Router, F
from aiogram.types import Message, ContentType

from ai import agent_endpoint, Dependencies
from database import PostgresDB

router = Router()


def markdown_to_html_safe(md_text: str) -> str:
    escaped_text = html.escape(md_text, quote=False)
    html_text = markdown.markdown(escaped_text, output_format="html5")

    return html_text


@router.message(F.content_type == ContentType.TEXT)
async def reply(message: Message, db: PostgresDB):
    user = await db.get_user()

    loading = await message.answer_sticker(
        "CAACAgIAAxkBAAPaZ3K_UpoKOS2DU0xBfRF0b6v2j-oAArQjAAKYSylI3rm-zSpb5Nk2BA",
    )

    deps = Dependencies(db=db)

    result = await agent_endpoint(db, user.llm_model, message.text, deps)

    await loading.delete()

    if len(result) <= 4096:
        return await message.reply(markdown_to_html_safe(result), parse_mode="HTML")
    else:
        last_message = message

        for sub_message in [result[i : i + 4096] for i in range(0, len(result), 4096)]:
            last_message = await last_message.reply(
                markdown_to_html_safe(sub_message), parse_mode="HTML"
            )

        return last_message
