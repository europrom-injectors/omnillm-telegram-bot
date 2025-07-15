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
    "OpenAI: o4 Mini High": "openai/o4-mini-high",
    "OpenAI: GPT-4o": "openai/gpt-4o-search-preview",
    "OpenAI: GPT-4o-mini": "openai/gpt-4o-mini-search-preview",
    "OpenAI: GPT-4.1": "openai/gpt-4.1",
    "xAI: Grok 4": "x-ai/grok-4",
    "MoonshotAI: Kimi K2": "moonshotai/kimi-k2:groq",
    "DeepSeek: R1": "deepseek/deepseek-r1",
    "DeepSeek: DeepSeek V3": "deepseek/deepseek-chat-v3-0324",
    "Google: Gemini 2.5 Pro": "google/gemini-2.5-pro",
    "Google: Gemini 2.5 Flash": "google/gemini-2.5-flash",
    "Google: Gemini 2.5 Flash Lite": "google/gemini-2.5-flash-lite-preview-06-17",
    "Anthropic: Claude 3.7 Sonnet": "anthropic/claude-3.7-sonnet",
    "Anthropic: Claude 3.5 Sonnet": "anthropic/claude-3.5-sonnet",
    "Anthropic: Claude 3.5 Haiku": "anthropic/claude-3.5-haiku",
    "Meta: Llama 4 Maverick": "meta-llama/llama-4-maverick",
    "Meta: Llama 4 Scout": "meta-llama/llama-4-scout",
    "Qwen: Qwen3 235B A22B": "qwen/qwen3-235b-a22b",
    "Amazon: Nova Pro 1.0": "amazon/nova-pro-v1",
    "Amazon: Nova Lite 1.0": "amazon/nova-lite-v1",
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
    '- OpenAI: o4 Mini High: Передовая модель от OpenAI с инновационной технологией "потока мысли", обеспечивающей глубокий анализ и креативные решения.\n\n'
    "- OpenAI: GPT-4o: Популярный флагман ChatGPT от OpenAI, с встроенным поиском в интернете для актуальной информации — идеальный выбор для повседневных запросов и исследований.\n\n"
    "- OpenAI: GPT-4o-mini: Компактная версия GPT-4o, быстрее и дешевле, с поддержкой веб-поиска, подходит для легких задач без потери качества.\n\n"
    "- OpenAI: GPT-4.1: Свежий релиз от OpenAI (апрель 2025), с улучшенным интеллектом и скоростью, продолжающий эволюцию GPT-линейки.\n\n"
    "- xAI: Grok 4: Революционная модель от xAI Илона Маска (лето 2025), выделяющаяся выдающимся качеством ответов и креативностью, опережает конкурентов.\n\n"
    "- MoonshotAI: Kimi K2: Дебютная модель от китайской MoonshotAI (июль 2025), сочетающая высокую скорость, доступность и конкурентоспособность с лидерами рынка.\n\n"
    '- DeepSeek: R1: Инновационная модель от DeepSeek с технологией "потока мысли", позволяющей ИИ глубоко размышлять и генерировать точные выводы.\n\n'
    '- DeepSeek: DeepSeek V3: Стандартная версия DeepSeek без "потока мысли", но с акцентом на доступность, скорость и экономию ресурсов.\n\n'
    "- Google: Gemini 2.5 Pro: Флагман от Google (апрель 2025), с передовыми возможностями в понимании контекста и мультимодальной обработке данных.\n\n"
    "- Google: Gemini 2.5 Flash: Ускоренная версия Gemini, фокусирующаяся на эффективности и быстроте для динамичных задач без компромиссов в точности.\n\n"
    "- Google: Gemini 2.5 Flash Lite: Легковесный вариант Gemini 2.5 Flash, еще дешевле и быстрее, идеален для простых сценариев с минимальными затратами.\n\n"
    "- Anthropic: Claude 3.7 Sonnet: Топ-модель линейки Claude, с выдающимся глубоким пониманием текстов и генерацией, — умный выбор для сложных аналитических задач.\n\n"
    "- Anthropic: Claude 3.5 Sonnet: Предшественник Claude 3.7, надежный в генерации coherentных ответов с балансом скорости и интеллекта.\n\n"
    "- Anthropic: Claude 3.5 Haiku: Быстрая и бюджетная версия Claude 3.5 Sonnet, с упрощенным, но эффективным подходом для повседневного использования.\n\n"
    "- Meta: Llama 4 Maverick: Новейшая модель от Meta с расширенными возможностями в понимании и создании контента, идеальна для креативных проектов.\n\n"
    "- Meta: Llama 4 Scout: Младшая сестра Llama 4 Maverick, компактная и эффективная для легких задач с открытым исходным кодом.\n\n"
    "- Qwen: Qwen3 235B A22B: Мощная китайская модель с огромным объемом параметров, предлагающая впечатляющую точность и универсальность — стоит попробовать для экспериментов.\n\n"
    "- Amazon: Nova Lite 1.0: Легкая версия Nova от Amazon, оптимизированная для экономии ресурсов, с фокусом на скорость и простоту интеграции.\n\n"
    "- Amazon: Nova Pro 1.0: Профессиональный вариант Nova с расширенными функциями, высокой производительностью и поддержкой сложных бизнес-задач.\n\n"
    "И немного рекомендаций:\n\n"
    "Для поиска в интернете используйте GPT-4o и GPT-4o-mini.\n"
    "Для программирования используйте Claude 3.7 Sonnet | GPT-4.1 | Gemini 2.5 Pro.\n"
    "Для сложных задач, требующих анализа, используйте o4 Mini High | Grok 4.\n"
    "Для остальных целей отлично подойдет GPT-4.1 и Gemini 2.5 Pro.\n"
    "Остальные модели можете пробовать по желанию."
)
