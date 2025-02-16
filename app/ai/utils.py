from database import PostgresDB
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.messages import ModelRequest, UserPromptPart, ModelResponse, TextPart
from typing import List


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


async def agent_endpoint(
    db: PostgresDB, user_input: str, agent: Agent, deps: BaseModel = None
):
    messages = await get_conversation_history(db)
    await store_message(db, "user", user_input)

    result = await agent.run(user_input, message_history=messages, deps=deps)

    await store_message(db, "assistant", result.data)

    return result.data
