from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "ticketresponsemodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "content" TEXT NOT NULL,
    "created" TIMESTAMPTZ NOT NULL,
    "sender_id_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    "ticket_id_id" INT NOT NULL REFERENCES "ticketmodel" ("id") ON DELETE CASCADE
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "ticketresponsemodel";"""
