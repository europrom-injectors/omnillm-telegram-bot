import logfire

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Any, Dict, Callable, Awaitable

from database import PostgresDB, PostgresPool, Context


class UserExistsMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        db_pool: PostgresPool = data["db_pool"]
        context: Context = data["context"]

        async with PostgresDB(db_pool, context) as db:
            with logfire.span("Checking if user exists..."):
                data["db"] = db

                if await db.get_user() is None:
                    await db.create_user()
                    logfire.info("User created!")
                else:
                    logfire.info("User exists!")

            result = await handler(event, data)

        return result


class ActiveChatExistsMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        db: PostgresDB = data["db"]

        with logfire.span("Checking if active chat exists..."):
            if await db.get_active_chat() is None:
                await db.create_active_chat()
                logfire.info("Active chat created!")
            else:
                logfire.info("Active chat exists!")

        return await handler(event, data)
