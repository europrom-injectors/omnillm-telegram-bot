from core import models, agents
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class SelectModelCallback(CallbackData, prefix="select_model"):
    llm_model: str


class SelectAgentCallback(CallbackData, prefix="select_agent"):
    agent: str


def create_keyboard(active_llm_model: str = "google/gemini-2.0-flash-001:online"):
    builder = InlineKeyboardBuilder()

    for model_name, model_value in models.items():
        if model_value == active_llm_model:
            builder.button(
                text="✅ " + model_name,
                callback_data=SelectModelCallback(llm_model=model_value).pack(),
            )
        else:
            builder.button(
                text=model_name,
                callback_data=SelectModelCallback(llm_model=model_value).pack(),
            )

    builder.adjust(2)  # Set width to 2 buttons per row
    return builder.as_markup()


def create_agent_keyboard(active_agent: str = "default"):
    builder = InlineKeyboardBuilder()

    for agent_name, agent_key in agents.items():
        if agent_key == active_agent:
            builder.button(
                text="✅ " + agent_name,
                callback_data=SelectAgentCallback(agent=agent_key).pack(),
            )
        else:
            builder.button(
                text=agent_name,
                callback_data=SelectAgentCallback(agent=agent_key).pack(),
            )

    builder.adjust(1)  # Set width to 1 button per row
    return builder.as_markup()
