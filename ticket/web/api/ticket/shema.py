import datetime

from pydantic import BaseModel

from ticket.db.models.tickets_models import TicketStatus


class TicketCreate(BaseModel):
    """DTO for creating new TicketModel."""

    tag: str
    content: str

    class Config:
        orm_mode = True


class Ticket(TicketCreate):
    """DTO for TicketModel."""

    id: int
    sender_id: int
    created: datetime.datetime
    status: TicketStatus

    class Config:
        orm_mode = True


class TicketResponseCreate(BaseModel):
    """DTO for creating TicketResponseModel."""

    ticket_id: int
    content: str

    class Config:
        orm_mode = True


class TicketResponse(TicketResponseCreate):
    """DTO for TicketResponseModel."""

    id: int
    created: datetime.datetime
    sender_id: int
