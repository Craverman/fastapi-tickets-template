from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY
);;
        CREATE TABLE IF NOT EXISTS "ticket" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "tag" TEXT NOT NULL,
    "content" TEXT NOT NULL,
    "status" VARCHAR(6) NOT NULL  DEFAULT 'new',
    "sender_name" TEXT NOT NULL,
    "created" TIMESTAMPTZ NOT NULL,
    "sender_id_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "ticket"."status" IS 'NEW: new\nACTIVE: active\nCLOSED: closed';;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "user";
        DROP TABLE IF EXISTS "ticket";"""
