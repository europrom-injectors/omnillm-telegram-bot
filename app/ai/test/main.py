from math import *
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

system_prompt = "You are a helpful assistant. Your name is Gemini. Answer on any questions using your knowlage. Use tool `calculate` only if you need to calculate something."

# Инициализация модели с использованием OpenRouter
model = OpenAIModel(
    model_name="openai/gpt-4o:online",  # Убедитесь, что используете поддерживаемую модель
    base_url="https://openrouter.ai/api/v1",
    api_key="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",  # Замените на ваш действующий API-ключ
)
agent = Agent(model=model, system_prompt=system_prompt)


@agent.tool_plain
async def calculate(python_expression: str) -> float | str:
    """
    Calculates a Python or math expression and returns the result, also all math modules are available and imported

    Args:
        python_expression (str): Python or math expression to evaluate, for example 1 + 3 // (2 - 1).
    """
    try:
        return float(eval(python_expression))
    except Exception as e:
        return str(e)
