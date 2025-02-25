import os
# from dotenv import load_dotenv

# load_dotenv()

APP_NAME = os.getenv("APP_NAME")
DEFAULT_LLM_MODEL = os.getenv("DEFAULT_LLM_MODEL", "google/gemini-2.0-flash-001")
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
    "OpenAI: GPT-4o": "openai/gpt-4o",
    "OpenAI: GPT-4o-mini": "openai/gpt-4o-mini",
    "DeepSeek: R1": "deepseek/deepseek-r1",
    "DeepSeek: DeepSeek V3": "deepseek/deepseek-chat",
    "Google: Gemini Flash 2.0": "google/gemini-2.0-flash-001",
    "Google: Gemini Flash 1.5": "google/gemini-flash-1.5",
"Anthropic: Claude 3.7 Sonnet": "anthropic/claude-3.7-sonnet",
    "Anthropic: Claude 3.5 Sonnet": "anthropic/claude-3.5-sonnet",
    "Anthropic: Claude 3.5 Haiku": "anthropic/claude-3.5-haiku",
"Amazon: Nova Pro 1.0": "amazon/nova-pro-v1",
   "Amazon: Nova Lite 1.0": "amazon/nova-lite-v1",
    "Amazon: Nova Micro 1.0": "amazon/nova-micro-v1",
    "xAI: Grok 2 1212": "x-ai/grok-2-1212",
}
