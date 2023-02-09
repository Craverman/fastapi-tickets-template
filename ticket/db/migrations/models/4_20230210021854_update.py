from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "user" RENAME TO "users";
        ALTER TABLE "ticketmodel" RENAME TO "tickets";
        ALTER TABLE "ticketresponsemodel" RENAME TO "ticket_responses";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" RENAME TO "user";
        ALTER TABLE "tickets" RENAME TO "ticketmodel";
        ALTER TABLE "ticket_responses" RENAME TO "ticketresponsemodel";"""
