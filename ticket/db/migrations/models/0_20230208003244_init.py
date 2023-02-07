from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" TEXT
);
COMMENT ON TABLE "user" IS 'Model for user.';
CREATE TABLE IF NOT EXISTS "ticketmodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "tag" TEXT NOT NULL,
    "content" TEXT NOT NULL,
    "status" VARCHAR(6) NOT NULL  DEFAULT 'new',
    "created" TIMESTAMPTZ NOT NULL,
    "sender_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "ticketmodel"."status" IS 'NEW: new\nACTIVE: active\nCLOSED: closed';
COMMENT ON TABLE "ticketmodel" IS 'Ticket model.';
CREATE TABLE IF NOT EXISTS "ticketresponsemodel" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "content" TEXT NOT NULL,
    "created" TIMESTAMPTZ NOT NULL,
    "sender_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE,
    "ticket_id" INT NOT NULL REFERENCES "ticketmodel" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "ticketresponsemodel" IS 'Model for response on ticket.';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
