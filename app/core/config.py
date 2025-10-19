import os
# from dotenv import load_dotenv

# load_dotenv()

APP_NAME = os.getenv("APP_NAME")
DEFAULT_LLM_MODEL = os.getenv("DEFAULT_LLM_MODEL", "openrouter/auto")
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
    "Auto Router": "openrouter/auto",
    "OpenAI: o4 Mini High": "openai/o4-mini-high",
    "OpenAI: GPT-4o": "openai/gpt-4o-search-preview",
    "OpenAI: GPT-5": "openai/gpt-5",
    "xAI: Grok Code Fast 1": "x-ai/grok-code-fast-1",
    "xAI: Grok 4": "x-ai/grok-4",
    "xAI: Grok 4 Fast": "x-ai/grok-4-fast",
    "Z.AI: GLM 4.6": "z-ai/glm-4.6",
    "DeepSeek: R1": "deepseek/deepseek-r1",
    "DeepSeek: DeepSeek V3.1": "deepseek/deepseek-chat-v3.1",
    "Google: Gemini 2.5 Pro": "google/gemini-2.5-pro",
    "Google: Gemini 2.5 Flash": "google/gemini-2.5-flash",
    "Google: Gemini 2.5 Flash Lite": "google/gemini-2.5-flash-lite-preview-06-17",
    "Anthropic: Claude 4.5 Sonnet": "anthropic/claude-sonnet-4.5",
    "Anthropic: Claude 4 Sonnet": "anthropic/claude-4-sonnet",
    "Anthropic: Claude 3.5 Haiku": "anthropic/claude-3.5-haiku",
    "Meta: Llama 4 Maverick": "meta-llama/llama-4-maverick",
    "Meta: Llama 4 Scout": "meta-llama/llama-4-scout",
    "Amazon: Nova Pro 1.0": "amazon/nova-pro-v1",
    "Qwen: Qwen3 235B A22B 2507": "qwen/qwen3-235b-a22b-2507",
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
    '- OpenAI: o4 Mini High: Передовая модель от OpenAI с технологией "потока мысли", обеспечивающей глубокий анализ, логические рассуждения и креативные решения.\n\n'
    "- OpenAI: GPT-4o: Популярный флагман ChatGPT от OpenAI с поддержкой веб-поиска и мультимодальности, идеальный для повседневных запросов и исследований.\n\n"
    "- OpenAI: GPT-5: Новейший представитель линейки GPT (осень 2025), объединяющий точность, креативность и продвинутое планирование. Быстрее и надёжнее предыдущих поколений.\n\n"
    "- xAI: Grok Code Fast 1: Специализированная версия Grok, заточенная под разработчиков. Обеспечивает молниеносное понимание кода, рефакторинг и генерацию алгоритмов.\n\n"
    "- xAI: Grok 4: Революционная модель от xAI Илона Маска (лето 2025), выделяющаяся качеством ответов и живой, креативной манерой рассуждений.\n\n"
    "- xAI: Grok 4 Fast: Ускоренная версия Grok 4 — та же интеллектуальная мощь, но быстрее и дешевле.\n\n"
    "- Z.AI: GLM 4.6: Современная китайская модель, сочетающая высокую скорость и достойное качество ответов. Хорошо подходит для технических и академических задач.\n\n"
    '- DeepSeek: R1: Инновационная модель от DeepSeek с технологией "reasoning stream", позволяющей ИИ глубоко размышлять и строить логические цепочки.\n\n'
    "- DeepSeek: DeepSeek V3.1: Оптимизированная версия без 'потока мысли', с акцентом на эффективность и низкие задержки, идеальна для повседневных задач.\n\n"
    "- Google: Gemini 2.5 Pro: Флагман от Google (апрель 2025), с выдающимся пониманием контекста и продвинутой мультимодальной обработкой данных.\n\n"
    "- Google: Gemini 2.5 Flash: Ускоренная версия Gemini, фокусирующаяся на быстроте и эффективности для динамичных задач.\n\n"
    "- Google: Gemini 2.5 Flash Lite: Облегчённый вариант Gemini Flash, ещё быстрее и дешевле, идеально подходит для простых сценариев.\n\n"
    "- Anthropic: Claude 4.5 Sonnet: Новый флагман Anthropic (лето 2025) с исключительной точностью, надёжностью и глубиной анализа.\n\n"
    "- Anthropic: Claude 4 Sonnet: Предшественник Claude 4.5, сбалансированный и мощный вариант для аналитики и программирования.\n\n"
    "- Anthropic: Claude 3.5 Haiku: Лёгкая и быстрая версия линейки Claude, с хорошим качеством генерации при низких ресурсных затратах.\n\n"
    "- Meta: Llama 4 Maverick: Новейшая модель от Meta с расширенными возможностями понимания и генерации контента, идеальна для креативных задач.\n\n"
    "- Meta: Llama 4 Scout: Компактная версия Maverick, быстрая и оптимизированная для интеграции в приложения.\n\n"
    "- Amazon: Nova Pro 1.0: Профессиональная модель от Amazon с высокой производительностью и поддержкой сложных бизнес-сценариев.\n\n"
    "- Amazon: Nova Lite 1.0: Облегчённая версия Nova, ориентированная на скорость и экономию ресурсов.\n\n"
    "- Qwen: Qwen3 235B A22B 2507: Гигантская китайская модель с 235 млрд параметров, демонстрирующая высокую точность, гибкость и универсальность.\n\n"
    "И немного рекомендаций:\n\n"
    "Для поиска в интернете используйте GPT-4o.\n"
    "Для программирования используйте Grok Code Fast 1 | Claude 4.5 Sonnet | Gemini 2.5 Pro.\n"
    "Для сложных задач, требующих анализа, используйте o4 Mini High | Grok 4 Fast | GPT-5.\n"
    "Для быстрых задач подойдут Gemini 2.5 Flash | Claude 3.5 Haiku | Nova Lite 1.0.\n"
    "Для креатива используйте Llama 4 Maverick | Claude 4.5 Sonnet | GPT-5.\n"
    "Для экспериментов — Qwen3 235B A22B 2507 | GLM 4.6.\n"
    "Остальные модели используйте по желанию"
)

