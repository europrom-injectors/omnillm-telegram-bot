import asyncpg
from typing import Optional, List


class PostgresDB:
    def __init__(self, config: dict):
        self.config = config
        self.pool: Optional[asyncpg.Pool] = None

    async def __aenter__(self):
        self.pool = await asyncpg.create_pool(**self.config)
        await self.create_tables()

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.pool.close()

    async def create_tables(self) -> None:
        await self.do(
            """
            BEGIN;

            CREATE TABLE IF NOT EXISTS chats (
                id SERIAL PRIMARY KEY,
                user_id BIGINT,
                name VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS users (
                id BIGINT PRIMARY KEY,
                active_chat_id INTEGER,
                username VARCHAR(255),
                full_name VARCHAR(255),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS messages (
                id SERIAL PRIMARY KEY,
                chat_id INTEGER REFERENCES chats(id) ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED,
                role VARCHAR(50) NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            ALTER TABLE chats 
            ADD CONSTRAINT fk_user_id
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;

            ALTER TABLE users 
            ADD CONSTRAINT fk_active_chat_id
            FOREIGN KEY (active_chat_id) REFERENCES chats(id) ON DELETE SET NULL DEFERRABLE INITIALLY DEFERRED;

            COMMIT;
            """
        )

    async def do(self, sql: str, values=None, transaction=False) -> None:
        async with self.pool.acquire() as conn:
            if transaction:
                async with conn.transaction():
                    if values:
                        await conn.execute(sql, *values)
                    else:
                        await conn.execute(sql)
            else:
                if values:
                    await conn.execute(sql, *values)
                else:
                    await conn.execute(sql)

    async def read(self, sql: str, values=None, one=False):
        async with self.pool.acquire() as conn:
            rows = await conn.fetch(sql, *values) if values else await conn.fetch(sql)
            if one:
                return dict(rows[0]) if rows else None
            return [dict(r) for r in rows]

    async def create_user(self, user_id: int, username: str, full_name: str) -> dict:
        sql = """
            INSERT INTO users (id, username, full_name) 
            VALUES ($1, $2, $3)
            RETURNING id, username, full_name, active_chat_id, created_at
        """
        return await self.read(sql, (user_id, username, full_name), one=True)

    async def get_user(self, user_id: int) -> Optional[dict]:
        sql = """
            SELECT * 
            FROM users 
            WHERE id=$1
        """
        return await self.read(sql, (user_id,), one=True)

    async def user_exists(self, user_id: int) -> bool:
        return bool(await self.get_user(user_id))

    # Chat methods
    async def create_chat(self, user_id: int, name: str) -> dict:
        sql = """
            INSERT INTO chats (user_id, name) 
            VALUES ($1, $2) 
            RETURNING id, user_id, name, created_at
        """
        return await self.read(sql, (user_id, name), one=True)

    async def get_chat(self, chat_id: int) -> Optional[dict]:
        sql = """
            SELECT * 
            FROM chats 
            WHERE id=$1
        """
        return await self.read(sql, (chat_id,), one=True)

    async def get_last_chat(self, user_id: int) -> Optional[dict]:
        sql = """
            SELECT * 
            FROM chats 
            WHERE user_id=$1 
            ORDER BY id DESC 
            LIMIT 1
        """
        return await self.read(sql, (user_id,), one=True)

    async def has_active_chat(self, user_id: int) -> bool:
        sql = """
            SELECT active_chat_id 
            FROM users 
            WHERE id=$1 
            AND active_chat_id IS NOT NULL
        """
        result = await self.read(sql, (user_id,), one=True)
        return bool(result)

    async def set_active_chat(self, user_id: int, chat_id: int) -> dict:
        sql = """
            UPDATE users 
            SET active_chat_id=$1 
            WHERE id=$2
            RETURNING id, username, full_name, active_chat_id, created_at
        """
        return await self.read(sql, (chat_id, user_id), one=True)

    async def get_active_chat(self, user_id: int) -> Optional[dict]:
        sql = """
            SELECT c.* 
            FROM chats c 
            JOIN users u ON u.active_chat_id = c.id 
            WHERE u.id=$1
        """
        return await self.read(sql, (user_id,), one=True)

    # Message methods
    async def get_chat_messages(self, chat_id: int) -> List[dict]:
        sql = """
            SELECT * 
            FROM messages 
            WHERE chat_id=$1 
            ORDER BY created_at ASC
        """
        return await self.read(sql, (chat_id,))

    async def get_active_chat_messages(self, user_id: int) -> List[dict]:
        sql = """
            SELECT m.* 
            FROM messages m 
            JOIN users u ON u.active_chat_id = m.chat_id 
            WHERE u.id=$1 
            ORDER BY m.created_at ASC
        """
