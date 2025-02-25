from aiogram import Router
from aiogram.types import CallbackQuery

from keyboard_ import (
    create_keyboard,
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

    return await callback.message.edit_reply_markup(
        reply_markup=create_keyboard(model.llm_model)
    )


@router.callback_query(SelectAgentCallback.filter())
async def change_agent(callback: CallbackQuery, db: PostgresDB):
    callback_data = callback.data
    agent_data = SelectAgentCallback.unpack(callback_data)

    await db.update_chat_agent(agent_data.agent)

    return await callback.message.edit_reply_markup(
        reply_markup=create_agent_keyboard(agent_data.agent)
    )
