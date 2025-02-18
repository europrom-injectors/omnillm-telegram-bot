import json

from typing import Optional, List

from .context import PostgresConnectionWithContext
from .models import User, Chat, Message
from core import async_logfire_class_decorator


@async_logfire_class_decorator
class UserMethods(PostgresConnectionWithContext):
    async def create_user(self) -> None:
        query = "INSERT INTO users (id, username, full_name) VALUES ($1, $2, $3)"
        await self.execute(
            query,
            (
                self.context.user.id,
                self.context.user.username,
                self.context.user.full_name,
            ),
        )

    async def get_user(self) -> Optional[User]:
        query = "SELECT * FROM users WHERE id=$1"
        result = await self.fetch_one(query, (self.context.user.id,), User)

        return result

    async def get_all_users(self) -> Optional[List[User]]:
        query = "SELECT * FROM users"
        result = await self.fetch_all(query, (), User)

        return result

    async def update_active_chat_id(self, chat_id: int) -> None:
        query = "UPDATE users SET active_chat_id = $1 WHERE id = $2"
        await self.execute(query, (chat_id, self.context.user.id))

    async def update_llm_model(self, model: str) -> None:
        query = "UPDATE users SET llm_model = $1 WHERE id = $2"
        await self.execute(query, (model, self.context.user.id))

    async def update_online_model(self, online_model: bool) -> None:
        query = "UPDATE users SET online_model = $1 WHERE id = $2"
        await self.execute(query, (online_model, self.context.user.id))

    async def delete_user(self) -> None:
        query = "DELETE FROM users WHERE id=$1"
        await self.execute(query, (self.context.user.id,))


@async_logfire_class_decorator
class ChatMethods(PostgresConnectionWithContext):
    async def create_chat(self) -> Chat:
        query = "INSERT INTO chats (user_id, name) VALUES ($1, $2) RETURNING *"
        result = await self.fetch_one(
            query,
            (
                self.context.user.id,
                "New chat",
            ),
            Chat,
        )

        return result

    async def get_chat(self, chat_id: int) -> Optional[Chat]:
        query = "SELECT * FROM chats WHERE id = $1"
        result = await self.fetch_one(query, (chat_id,), Chat)

        return result

    async def get_active_chat(self) -> Optional[Chat]:
        query = "SELECT * FROM chats WHERE id = (SELECT active_chat_id FROM users WHERE id=$1)"
        result = await self.fetch_one(query, (self.context.user.id,), Chat)

        return result

    async def get_all_chats(self) -> Optional[List[Chat]]:
        query = "SELECT * FROM chats WHERE user_id=$1"
        result = await self.fetch_all(query, (self.context.user.id,), Chat)

        return result

    async def update_chat_name(self, name: str, chat_id: int = None) -> None:
        query = "UPDATE chats SET name = $1 WHERE id = $2"
        await self.execute(query, (name, chat_id or await self.get_active_chat().id))

    async def delete_chat(self, chat_id: int = None) -> None:
        query = "DELETE FROM chats WHERE id=$1"
        await self.execute(query, (chat_id or await self.get_active_chat().id,))


@async_logfire_class_decorator
class MessageMethods(PostgresConnectionWithContext):
    async def create_message(self, content: dict) -> None:
        query = "INSERT INTO messages (chat_id, content) VALUES ((SELECT active_chat_id FROM users WHERE id=$1), $2)"
        await self.execute(query, (self.context.user.id, json.dumps(content)))

    async def get_all_messages(self, limit: int = 16) -> Optional[List[Message]]:
        query = "SELECT * FROM messages WHERE chat_id = (SELECT active_chat_id FROM users WHERE id=$1) ORDER BY id ASC LIMIT $2"
        result = await self.fetch_all(query, (self.context.user.id, limit), Message)

        return result

    async def clear_messages(self) -> None:
        query = "DELETE FROM messages WHERE chat_id = (SELECT active_chat_id FROM users WHERE id=$1)"
        await self.execute(query, (self.context.user.id,))


class PostgresDB(UserMethods, ChatMethods, MessageMethods):
    async def create_active_chat(self) -> None:
        chat = await self.create_chat()
        await self.update_active_chat_id(chat.id)
