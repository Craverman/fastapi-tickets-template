from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" ADD "name" TEXT;
        ALTER TABLE "ticketmodel" DROP COLUMN "sender_name";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" DROP COLUMN "name";
        ALTER TABLE "ticketmodel" ADD "sender_name" TEXT NOT NULL;"""
