from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from keyboard_ import (
    create_model_keyboard,
    create_agent_keyboard,
    SelectModelCallback,
    SelectAgentCallback,
)

from database import PostgresDB

router = Router()


@router.callback_query(SelectModelCallback.filter())
async def change_model(callback: CallbackQuery, db: PostgresDB):
    callback_data = callback.data
    model = SelectModelCallback.unpack(callback_data)

    await db.update_chat_llm_model(model.llm_model)

    try:
        return await callback.message.edit_reply_markup(
            reply_markup=create_model_keyboard(model.llm_model)
        )
    except TelegramBadRequest as e:
        return None


@router.callback_query(SelectAgentCallback.filter())
async def change_agent(callback: CallbackQuery, db: PostgresDB):
    callback_data = callback.data
    agent_data = SelectAgentCallback.unpack(callback_data)

    await db.update_chat_agent(agent_data.agent)

    try:
        return await callback.message.edit_reply_markup(
            reply_markup=create_agent_keyboard(agent_data.agent)
        )
    except TelegramBadRequest as e:
        return None
