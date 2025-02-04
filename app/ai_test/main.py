from math import *
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel


# Инициализация модели с использованием OpenRouter
model = OpenAIModel(
    model_name="openai/gpt-4o-2024-11-20",  # Убедитесь, что используете поддерживаемую модель
    base_url="https://openrouter.ai/api/v1",
    api_key="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",  # Замените на ваш действующий API-ключ
)
agent = Agent(model=model)


@agent.tool
async def calculate(ctx, python_expression: str) -> float | str:
    """
    Calculates a Python or math expression and returns the result, also all math modules are available and imported

    Args:
        python_expression (str): Python or math expression to evaluate, for example 1 + 3 // (2 - 1).
    """
    try:
        return float(eval(python_expression))
    except Exception as e:
        return str(e)
