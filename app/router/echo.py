from aiogram import Router, F
from aiogram.types import Message, ContentType

from ai import agent_endpoint, Dependencies
from database import PostgresDB

router = Router()


@router.message(F.content_type == ContentType.TEXT)
async def reply(message: Message, db: PostgresDB):
    deps = Dependencies(db=db)
    return message.reply(
        await agent_endpoint(db, "google/gemini-2.0-flash-001", message.text, deps)
    )
