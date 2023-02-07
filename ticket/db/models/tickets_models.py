from enum import Enum

from tortoise import ForeignKeyFieldInstance, fields, models

from ticket.db.models.users_models import User


class TicketStatus(Enum):
    """Status for TicketModel status field."""

    NEW = "new"
    ACTIVE = "active"
    CLOSED = "closed"


class TicketModel(models.Model):
    """Ticket model."""

    id = fields.IntField(pk=True)
    tag = fields.TextField()
    content = fields.TextField()
    status = fields.CharEnumField(TicketStatus, default="new")
    sender: ForeignKeyFieldInstance[User] = fields.ForeignKeyField(
        "models.User",
        related_name="sender_id",
    )
    created = fields.DatetimeField()


class TicketResponseModel(models.Model):
    """Model for response on ticket."""

    id = fields.IntField(pk=True)
    content = fields.TextField()
    sender: ForeignKeyFieldInstance[User] = fields.ForeignKeyField(
        "models.User",
        related_name="ticket_sender",
    )
    ticket: ForeignKeyFieldInstance[TicketModel] = fields.ForeignKeyField(
        "models.TicketModel",
        related_name="ticket_response",
    )
    created = fields.DatetimeField()
