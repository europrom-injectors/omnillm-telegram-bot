from core import agents
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class SelectAgentCallback(CallbackData, prefix="select_agent"):
    agent: str


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
