import logging

from aiogram.types import Message
from typing import Any, Dict, Callable, Awaitable
from database import PostgresDB
from aiogram import BaseMiddleware
from abc import abstractmethod


class DatabaseRelatedMiddleware(BaseMiddleware):
    def __init__(self, db: PostgresDB):
        super().__init__()
        self.db = db

    @abstractmethod
    async def __call__(self, handler, event, data):
        pass


class UserExistenceCheckMiddleware(DatabaseRelatedMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        if not await self.db.user_exists(event.from_user.id):
            logging.info(f"New user: {event.from_user.username}")
            await self.db.create_user(
                event.from_user.id,
                event.from_user.username,
                event.from_user.full_name,
            )

        return await handler(event, data)


class ChatExistenceCheckMiddleware(DatabaseRelatedMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        if not await self.db.has_active_chat(event.from_user.id):
            last_chat = await self.db.get_last_chat(event.from_user.id)

            if last_chat is not None:
                logging.info(f"Resuming chat for user: {event.from_user.username}")
                await self.db.set_active_chat(event.from_user.id, last_chat["id"])
            else:
                logging.info(f"New chat for user: {event.from_user.username}")
                created_chat = await self.db.create_chat(event.from_user.id, "New chat")
                await self.db.set_active_chat(event.from_user.id, created_chat["id"])

        return await handler(event, data)
