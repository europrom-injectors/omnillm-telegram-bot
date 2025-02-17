from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboard_ import create_keyboard
from database import PostgresDB

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    return await message.reply(
        "👋 Добро пожаловать в Omnillm!\n\n"
        "Я бот, по типу ChatGPT, но тут вы не ограничены одной моделью (всего моделей 14). Также вы можете общатся со мной отправляя текстовые сообщения. Просто напишите сообщение в чат и отправьте его мне, я на него отвечу.\n\n"
        "Комманды:\n"
        "/model - Выбрать модель ИИ\n"
        "/model_info - Получить описание моделей\n"
        "/clear - Очистить историю сообщений\n"
    )


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
    return await message.reply(
        "Краткое описание каждой модели:\n"
        "\n"
        "- OpenAI: o3 Mini High: Самая продвинутая модель с технологией потока мысли от OpenAI.\n\n"
        "- OpenAI: o1: Более простая версия o3, все еще использует технологию потока мысли, но на удивление она дороже, чем o3.\n\n"
        "- OpenAI: GPT-4o: Обычный ChatGPT, о котором вы так наслышены. Самая популярная модель от OpenAI.\n\n"
        "- OpenAI: GPT-4o-mini: Мини-версия GPT-4o, предназначенная для более легких задач, также она дешевле и быстрее чем GPT-4o.\n\n"
        "- DeepSeek: R1: Первая модель от DeepSeek, использующая поток мысли, специальная технология позволяющая ИИ думать.\n\n"
        "- DeepSeek: DeepSeek V3: Обычная версия DeepSeek, без технологии потока мысли. Также она дешевле.\n\n"
        "- Google: Gemini Flash 2.0: Усовершенствованная версия языковой модели Gemini с улучшенной скоростью и эффективностью.\n\n"
        "- Google: Gemini Flash 1.5: Предшественник Gemini Flash 2.0, ориентированный на более быстрые ответы (в 2 раза быстрее, не глупее, чем Gemini Flash 2.0).\n\n"
        "- Anthropic: Claude 3.5 Sonnet: Модель серии Claude, оптимизированная для глубокого понимания и генерации текста. Очень умная модель, лучшая среди Claude.\n\n"
        "- Anthropic: Claude 3.5 Haiku: Как Anthropic: Claude 3.5 Sonnet только быстрее и дешевле, но глупее.\n\n"
        "- Amazon: Nova Pro 1.0: Профессиональная версия Nova с расширенными возможностями и высокой производительностью.\n\n"
        "- Amazon: Nova Lite 1.0: Облегченная версия Nova, предназначенная для экономичного использования ресурсов.\n\n"
        "- Amazon: Nova Micro 1.0: Минималистичная версия Nova, оптимизированная для малых задач и быстрых ответов.\n\n"
        "- xAI: Grok 2 1212: Усовершенствованная модель Grok с улучшенными возможностями понимания и генерации контента. Компания xAI принадлежит Илону Маску.\n\n"
    )
