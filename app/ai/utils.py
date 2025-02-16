from typing import List
from pydantic_ai.messages import ModelRequest, UserPromptPart, ModelResponse, TextPart
from pydantic_ai.models.openai import OpenAIModel

from database import PostgresDB
from core import OPENROUTER_TOKEN


def generate_model(model_name: str):
    return OpenAIModel(
        model_name=model_name,
        base_url="https://openrouter.ai/api/v1",
        api_key=OPENROUTER_TOKEN,
    )


async def store_message(
    db: PostgresDB, message_type: str, message: str, **kwargs
) -> None:
    await db.create_message({"type": message_type, "content": message, **kwargs})


async def get_conversation_history(
    db: PostgresDB,
) -> List[ModelRequest | ModelResponse]:
    messages = []

    for message in await db.get_all_messages() or []:
        message_type = message.content["type"]
        message_content = message.content["content"]

        message = (
            ModelRequest(parts=[UserPromptPart(content=message_content)])
            if message_type == "user"
            else ModelResponse(parts=[TextPart(content=message_content)])
        )

        messages.append(message)

    return messages
