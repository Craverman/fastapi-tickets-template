from fastapi.routing import APIRouter

from ticket.web.api import docs, monitoring, ticket

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(ticket.router, prefix="/ticket", tags=["ticket"])
