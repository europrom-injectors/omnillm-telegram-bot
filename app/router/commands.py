from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from core import start_message, models_info_message, agents_info_message
from keyboard_ import create_keyboard, create_agent_keyboard
from database import PostgresDB

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    return await message.reply(start_message)


@router.message(Command("clear"))
async def clear(message: Message, db: PostgresDB):
    await db.clear_messages()
    return await message.reply("🗑 История сообщений очищена!")


@router.message(Command("model"))
async def model(message: Message, db: PostgresDB):
    chat = await db.get_active_chat()

    model_descriptions = (
        "🤖 Выберите модель ИИ, получить их описание можно командой /model_info:\n\n"
    )

    return await message.reply(
        model_descriptions, reply_markup=create_keyboard(chat.llm_model)
    )


@router.message(Command("model_info"))
async def model_info(message: Message):
    return await message.reply(models_info_message)


@router.message(Command("online"))
async def switch_online(message: Message, db: PostgresDB):
    chat = await db.get_active_chat()

    await db.update_chat_online_model(not chat.online_model)
    return await message.answer(
        "Поиск по интернету " + ("отключен" if chat.online_model else "включен")
    )


@router.message(Command("agent"))
async def agent(message: Message, db: PostgresDB):
    chat = await db.get_active_chat()

    agent_descriptions = (
        "👥 Выберите стиль общения, получить описание можно командой /agent_info:\n\n"
    )

    return await message.reply(
        agent_descriptions, reply_markup=create_agent_keyboard(chat.agent)
    )


@router.message(Command("agent_info"))
async def agent_info(message: Message):
    return await message.reply(agents_info_message)
