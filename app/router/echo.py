from aiogram import Router, F
from aiogram.types import Message, ContentType

from ai import agent_endpoint
from database import PostgresDB

router = Router()


@router.message(F.content_type == ContentType.TEXT)
async def reply(message: Message, db: PostgresDB):
    return message.reply(await agent_endpoint(db, message.text))
