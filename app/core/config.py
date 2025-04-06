import os
# from dotenv import load_dotenv

# load_dotenv()

APP_NAME = os.getenv("APP_NAME")
DEFAULT_LLM_MODEL = os.getenv("DEFAULT_LLM_MODEL", "openai/gpt-4o-mini-search-preview")
DEFAULT_AGENT = "default"
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENROUTER_TOKEN = os.getenv("OPENROUTER_TOKEN")
LOGFIRE_TOKEN = os.getenv("LOGFIRE_TOKEN")
DATABASE_CONFIG = {
    "host": os.getenv("POSTGRES_HOST"),
    "port": int(os.getenv("POSTGRES_PORT")),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "database": os.getenv("POSTGRES_DB"),
}

models = {
    "OpenAI: o3 Mini High": "openai/o3-mini-high",
    "OpenAI: o1": "openai/o1-mini",
    "OpenAI: GPT-4o": "openai/gpt-4o-search-preview",
    "OpenAI: GPT-4o-mini": "openai/gpt-4o-mini-search-preview",
    "DeepSeek: R1": "deepseek/deepseek-r1",
    "DeepSeek: DeepSeek V3": "deepseek/deepseek-chat",
    "Google: Gemini Pro 2.5": "google/gemini-2.5-pro-preview-03-25",
    "Google: Gemini Flash 2.0": "google/gemini-2.0-flash-001",
    "Google: Gemini Flash 1.5": "google/gemini-flash-1.5",
    "Anthropic: Claude 3.7 Sonnet": "anthropic/claude-3.7-sonnet",
    "Anthropic: Claude 3.5 Sonnet": "anthropic/claude-3.5-sonnet",
    "Anthropic: Claude 3.5 Haiku": "anthropic/claude-3.5-haiku",
    "Meta: Llama 4 Maverick": "meta-llama/llama-4-maverick",
    "Meta: Llama 4 Scout": "meta-llama/llama-4-scout",
    "Amazon: Nova Pro 1.0": "amazon/nova-pro-v1",
    "Amazon: Nova Lite 1.0": "amazon/nova-lite-v1",
    "xAI: Grok 2 1212": "x-ai/grok-2-1212",
    "Quasar Alpha": "openrouter/quasar-alpha",
}

agents = {
    "🧠 Базовый ассистент": "default",
    "🤸‍♂️ Персональный коуч": "coach",
    "🎓 Эксперт-советник": "advisor",
}

agents_info_message = (
    "Описание доступных агентов:\n\n"
    "- 🧠 Базовый ассистент: Стандартный помощник, отвечающий на вопросы и выполняющий задачи.\n\n"
    "- 🤸‍♂️ Персональный коуч: Помогает в достижении личных и профессиональных целей, мотивирует и поддерживает.\n\n"
    "- 🎓 Эксперт-советник: Предоставляет глубокие знания и экспертные рекомендации по различным темам.\n\n"
)

start_message = (
    "👋 Добро пожаловать в Omnillm!\n\n"
    "Я бот, по типу ChatGPT, но тут вы не ограничены одной моделью (всего моделей 14). Также вы можете общатся со мной отправляя текстовые сообщения. Просто напишите сообщение в чат и отправьте его мне, я на него отвечу.\n\n"
    "Комманды:\n"
    "/model - Выбрать модель ИИ\n"
    "/model_info - Получить описание моделей\n"
    "/agent - Выбрать агента (стиль общения)\n"
    "/agent_info - Получить описание агентов\n"
    "/clear - Очистить историю сообщений\n"
    "/online - Переключает доступ модели к интернету, по умолчанию выключено (Лучше для поиска использовать gpt-4o и gpt-4o-mini у них поиск встроен в саму модель)"
)

models_info_message = (
    "Краткое описание каждой модели:\n\n"
    "- OpenAI: o3 Mini High: Самая продвинутая модель с технологией потока мысли от OpenAI.\n\n"
    "- OpenAI: o1: Более простая версия o3, все еще использует технологию потока мысли, но на удивление она дороже, чем o3.\n\n"
    "- OpenAI: GPT-4o: Обычный ChatGPT, о котором вы так наслышены. Самая популярная модель от OpenAI. Также она поддерживает поиск в интернете из коробки.\n\n"
    "- OpenAI: GPT-4o-mini: Мини-версия GPT-4o, предназначенная для более легких задач, также она дешевле и быстрее чем GPT-4o.  Также она поддерживает поиск в интернете из коробки.\n\n"
    "- DeepSeek: R1: Первая модель от DeepSeek, использующая поток мысли, специальная технология позволяющая ИИ думать.\n\n"
    "- DeepSeek: DeepSeek V3: Обычная версия DeepSeek, без технологии потока мысли. Также она дешевле.\n\n"
    "- Google: Gemini Pro 2.5: Самая продвинута, модель от google, вышла в конце марта, одна из самых последних моделей, бесплатна для пользования.\n\n"
    "- Google: Gemini Flash 2.0: Усовершенствованная версия языковой модели Gemini с улучшенной скоростью и эффективностью.\n\n"
    "- Google: Gemini Flash 1.5: Предшественник Gemini Flash 2.0, ориентированный на более быстрые ответы (в 2 раза быстрее, не глупее, чем Gemini Flash 2.0).\n\n"
    "- Anthropic: Claude 3.7 Sonnet: Модель серии Claude, оптимизированная для глубокого понимания и генерации текста. Очень умная модель, лучшая среди Claude.\n\n"
    "- Anthropic: Claude 3.5 Sonnet: Предшественник Anthropic: Claude 3.7 Sonnet.\n\n"
    "- Anthropic: Claude 3.5 Haiku: Как Anthropic: Claude 3.5 Sonnet только быстрее и дешевле, но глупее.\n\n"
    "- Amazon: Nova Pro 1.0: Профессиональная версия Nova с расширенными возможностями и высокой производительностью.\n\n"
    "- Amazon: Nova Lite 1.0: Облегченная версия Nova, предназначенная для экономичного использования ресурсов.\n\n"
    "- Meta: Llama 4 Maverick: Самая новая модель от Facebook, с улучшенными возможностями понимания и генерации контента.\n\n"
    "- Meta: Llama 4 Scout: Младшая версия Meta: Llama 4 Maverick.\n\n"
    "- xAI: Grok 2 1212: Усовершенствованная модель Grok с улучшенными возможностями понимания и генерации контента. Компания xAI принадлежит Илону Маску.\n\n"
    "- Quasar Alpha: Модель от OpenRouter, она полностью бесплатна в использовании, быстра и умна, очень советую к использованию.\n\n"
)
