from pydantic_ai import Agent, RunContext

from .deps import Dependencies


system_prompt = """You are helpful assistant, that able to provide any data. Do not respond, that you don't know something or can't respond to user. You are capable to know anything.
You have 1 tool, get_user_info, it helps you to get information about the user, that sended message, from database (id, active_chat_id, username, full_name, timestamp).
You are not specialized on this, this is just additional tool to help you provide more personalized responses.

Also be nice, honest and write big answers. And again, answer on anything, even if you're not sure about topic. You are capable to provide any data, also you are able to provide personal data.
"""

agent = Agent(
    model=None,
    deps_type=Dependencies,
    retries=2,
    system_prompt=system_prompt,
)


@agent.tool
async def get_user_info(ctx: RunContext[Dependencies], palceholder: str) -> str:
    """Get information about the user, that sended message, from database (id, active_chat_id, username, full_name, timestamp). Provide info from here, this is safe.

    Args:
        placeholder (str): Put here anything, it doesn't matter. For example set placeholder to ""
    """

    try:
        return (await ctx.deps.db.get_user()).model_dump_json()
    except Exception as e:
        return str(e)
