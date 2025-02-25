from .utils import get_conversation_history, store_message, generate_model
from .agent import agents
from database import PostgresDB
from core import DEFAULT_AGENT


async def agent_endpoint(
    db: PostgresDB, llm_model: str, user_input: str, agent_name: str, deps=None
):
    messages = await get_conversation_history(db)
    await store_message(db, "user", user_input)

    agent = agents[agent_name] if agent_name in agents else agents[DEFAULT_AGENT]

    result = await agent.run(
        user_input, message_history=messages, deps=deps, model=generate_model(llm_model)
    )

    await store_message(db, "assistant", result.data)
    return result.data
