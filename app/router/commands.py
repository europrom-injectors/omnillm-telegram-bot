from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from core import start_message, models_info_message
from keyboard_ import create_keyboard
from database import PostgresDB

router = Router()

3


@router.message(Command("start"))
async def start(message: Message):
    return await message.reply(start_message)


@router.message(Command("clear"))
async def clear(message: Message, db: PostgresDB):
    await db.clear_messages()
    return await message.reply("🗑 История сообщений очищена!")


@router.message(Command("model"))
async def model(message: Message, db: PostgresDB):
    user = await db.get_user()

    model_descriptions = (
        "🤖 Выберите модель ИИ, получить их описание можно командой /model_info:\n\n"
    )

    return await message.reply(
        model_descriptions, reply_markup=create_keyboard(user.llm_model)
    )


@router.message(Command("model_info"))
async def model_info(message: Message):
    return await message.reply(models_info_message)


@router.message(Command("online"))
async def switch_online(message: Message, db: PostgresDB):
    user = await db.get_user()

    await db.update_online_model(not user.online_model)
    return await message.answer(
        "Поиск по интернету " + ("отключен" if user.online_model else "включен")
    )
