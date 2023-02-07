from datetime import datetime
from typing import List

from fastapi import APIRouter

from ticket.db.models.tickets_models import (
    TicketModel,
    TicketResponseModel,
    TicketStatus,
)
from ticket.web.api.ticket.shema import Ticket, TicketResponse
from ticket.web.api.users.controler import check_auth

router = APIRouter()


@router.get("/tickets", response_model=None)
async def get_ticket_models(
    user_id: int,
    limit: int = 10,
    offset: int = 0,
) -> List[TicketModel]:
    return await TicketModel.filter(sender_id=user_id).offset(offset).limit(limit)


@router.post("/tickets", response_model=Ticket)
async def post_ticket_models(ticket: Ticket) -> TicketModel:
    user = await check_auth()
    return await TicketModel.create(
        status=TicketStatus.NEW,
        created=datetime.now(),
        sender=user,
        tag=ticket.tag,
        content=ticket.content,
    )


@router.post("/ticketResponse", response_model=TicketResponse)
async def post_ticket_response_models(
    ticket_response: TicketResponse,
) -> TicketResponse:
    user = await check_auth()
    ticket = await TicketModel.filter(id=ticket_response.ticket_id).first()
    await TicketResponseModel.create(
        created=datetime.now(),
        sender=user,
        ticket=ticket,
        content=ticket_response.content,
    )
    return ticket_response


@router.get("/tickets/{ticket_id}", response_model=None)
async def get_ticket_models_by_id(ticket_id: int) -> TicketModel:
    return await TicketModel.get(id=ticket_id)


# @app.get("/items/{item_id}")
# async def read_item(item_id):
