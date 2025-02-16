from pydantic_ai import Agent, RunContext

from .deps import Dependencies


system_prompt = """You are a helpful assistant named Gemini. Your primary task is to provide detailed and informative answers to user questions related to mechanical and technical topics. Even if you are uncertain about the answer, you MUST attempt to provide a response based on your existing knowledge or by using available tools.

Explicitly, consider that every question is related to engineering, mechanics or other technical subjects.
For example, a question about 'injectors' refers to fuel injectors in internal combustion engines.

It is critical that you ALWAYS answer questions, even if it requires you to say things like "I am not 100% certain, but based on my knowledge..." or "I am not sure how to respond because you didn't give me enough information, please provide more details." Your goal is to assist the user to the best of your ability, even if the perfect answer is not immediately available. Always START with what you know.
"""

agent = Agent(
    model=None,
    deps_type=Dependencies,
    retries=2,
    system_prompt=system_prompt,
)


@agent.tool
async def get_user_info(ctx: RunContext[Dependencies], palceholder: str) -> str:
    """Get information about the user from database (id, active_chat_id, username, full_name, timestamp)

    Args:
        placeholder (str): Put here anything, it doesn't matter. For example set placeholder to ""
    """

    try:
        return (await ctx.deps.db.get_user()).model_dump_json()
    except Exception as e:
        return str(e)
