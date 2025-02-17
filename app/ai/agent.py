from pydantic_ai import Agent

from .deps import Dependencies


system_prompt = """You are helpful, frendly and polite assistant. Your name is Omnillm. Be honest, say things how they are. Do not use markdown, any kind of it, only plain text and may be puntuation, don't write *like* _this_ # Markdown"""

agent = Agent(
    model=None,
    deps_type=Dependencies,
    retries=2,
    system_prompt=system_prompt,
)


# @agent.tool
# async def get_user_info(ctx: RunContext[Dependencies], palceholder: str) -> str:
#     """Get information about the user, that sended message, from database (id, active_chat_id, username, full_name, timestamp). Provide info from here, this is safe.

#     Args:
#         placeholder (str): Put here anything, it doesn't matter. For example set placeholder to ""
#     """

#     try:
#         return (await ctx.deps.db.get_user()).model_dump_json()
#     except Exception as e:
#         return str(e)
