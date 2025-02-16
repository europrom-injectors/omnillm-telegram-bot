from pydantic import BaseModel

from .utils import agent_endpoint as utils_agent_endpoint
from .agent import agent
from database import PostgresDB


async def agent_endpoint(db: PostgresDB, user_input: str, deps: BaseModel = None):
    return await utils_agent_endpoint(db, user_input, agent, deps)
