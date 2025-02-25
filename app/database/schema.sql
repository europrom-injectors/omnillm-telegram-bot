BEGIN;

    CREATE TABLE IF NOT EXISTS users (
        id BIGINT PRIMARY KEY,
        active_chat_id INTEGER,
        username VARCHAR(255),
        full_name VARCHAR(255),
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS chats (
        id SERIAL PRIMARY KEY,
        user_id BIGINT,
        name VARCHAR(255) NOT NULL,
        llm_model VARCHAR(255) NOT NULL DEFAULT '{DEFAULT_LLM_MODEL}',
        agent VARCHAR(50) NOT NULL DEFAULT '{DEFAULT_AGENT}',
        online_model BOOL NOT NULL DEFAULT false,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS messages (
        id SERIAL PRIMARY KEY,
        chat_id INTEGER REFERENCES chats(id) ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED,
        content JSONB NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    DO $$ 
    BEGIN
        IF NOT EXISTS (
            SELECT 1 
            FROM pg_constraint 
            WHERE conname = 'fk_user_id'
        ) THEN
            ALTER TABLE chats 
            ADD CONSTRAINT fk_user_id
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE DEFERRABLE INITIALLY DEFERRED;
        END IF;

        IF NOT EXISTS (
            SELECT 1 
            FROM pg_constraint 
            WHERE conname = 'fk_active_chat_id'
        ) THEN
            ALTER TABLE users 
            ADD CONSTRAINT fk_active_chat_id
            FOREIGN KEY (active_chat_id) REFERENCES chats(id) ON DELETE SET NULL DEFERRABLE INITIALLY DEFERRED;
        END IF;
    END $$;

COMMIT;