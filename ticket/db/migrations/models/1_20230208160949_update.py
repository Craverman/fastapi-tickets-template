from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "ticketmodel" DROP COLUMN "status";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "ticketmodel" ADD "status" VARCHAR(6) NOT NULL  DEFAULT 'new';"""
