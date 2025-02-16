import os
# from dotenv import load_dotenv

# load_dotenv()

APP_NAME = os.getenv("APP_NAME")
DEFAULT_LLM_MODEL = os.getenv("DEFAULT_LLM_MODEL", "google/gemini-2.0-flash-001:nitro")
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
    "Google: Gemini Flash 2.0": "google/gemini-2.0-flash-001:nitro",
    "DeepSeek: DeepSeek V3": "deepseek/deepseek-chat",
    "OpenAI: o1": "openai/o1",
    "OpenAI: GPT-4o": "openai/gpt-4o-2024-11-20",
    "Anthropic: Claude 3.5 Sonnet": "anthropic/claude-3.5-sonnet:beta",
    "Meta: Llama 3.1": "meta-llama/llama-3.1-405b-instruct",
}
