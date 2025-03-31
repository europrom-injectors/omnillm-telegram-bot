from core import models
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class SelectModelCallback(CallbackData, prefix="select_model"):
    llm_model: str


def create_model_keyboard(active_llm_model: str = "google/gemini-2.0-flash-001:online"):
    builder = InlineKeyboardBuilder()

    for model_name, model_value in models.items():
        if model_value.replace("DOUBLE_DOT", ":") == active_llm_model:
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
