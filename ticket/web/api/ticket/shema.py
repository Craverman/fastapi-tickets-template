from pydantic import BaseModel


class Ticket(BaseModel):
    """For model TicketModel."""

    tag: str
    content: str


class TicketResponse(BaseModel):
    """For model TicketResponseModel."""

    ticket_id: int
    content: str
