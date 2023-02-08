from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "ticketmodel" ALTER COLUMN "created" TYPE TIMESTAMPTZ USING "created"::TIMESTAMPTZ;
        ALTER TABLE "ticketmodel" ALTER COLUMN "created" TYPE TIMESTAMPTZ USING "created"::TIMESTAMPTZ;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "ticketmodel" ALTER COLUMN "created" TYPE TIMESTAMPTZ USING "created"::TIMESTAMPTZ;
        ALTER TABLE "ticketmodel" ALTER COLUMN "created" TYPE TIMESTAMPTZ USING "created"::TIMESTAMPTZ;"""
