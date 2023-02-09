from datetime import datetime
from typing import List

from ticket.db.models.tickets_models import (
    TicketModel,
    TicketResponseModel,
    TicketStatus,
)
from ticket.web.api.ticket.shema import Ticket, TicketResponse
from ticket.web.api.users.controler import check_auth


class TicketResponseDAO:
    """Class for accessing ticketresponse table."""

    async def create_ticket_response_model(
        self,
        ticket_id: int,
        content: str,
    ) -> TicketResponse:
        """Add single ticketresponse to table.

        :param ticket_id: id of ticket
        :param content: content for ticket
        :return: ticketresponse
        """
        user = await check_auth()
        ticket = await TicketModel.filter(id=ticket_id).first()
        ticket_response = await TicketResponseModel.create(
            ticket=ticket,
            created=datetime.now(),
            sender=user,
            content=content,
        )
        return TicketResponse(**dict(ticket_response))


class TicketDAO:
    """Class for accessing ticket table."""

    async def create_ticket_model(self, tag: str, content: str) -> Ticket:
        """
        Add single ticket to table.

        :param tag: tag for ticket
        :param content: content for ticket
        :return: ticket
        """
        user = await check_auth()
        ticket = await TicketModel.create(
            status=TicketStatus.NEW,
            created=datetime.now(),
            sender=user,
            tag=tag,
            content=content,
        )
        return Ticket(**dict(ticket))

    async def get_all_tickets(self, limit: int, offset: int) -> List[Ticket]:
        """Get all ticket models with limit/offset pagination.

        :param limit: limit of ticket objects, defaults to 10.
        :param offset: offset of ticket objects, defaults to 0.
        :return: list of tickets
        """
        tickets = await TicketModel.all().offset(offset).limit(limit)
        return [Ticket(**dict(el)) for el in tickets]

    @staticmethod
    async def filter(ticket_id: int) -> Ticket | None:
        """Get specific ticket model by id.

        :param ticket_id: id of ticket
        :return: ticked filtered by id
        """
        ticket = await TicketModel.filter(id=ticket_id).first()
        if not ticket:
            return None
        return Ticket(**dict(ticket))
