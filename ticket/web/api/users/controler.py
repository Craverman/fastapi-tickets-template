from tortoise import Optional

from ticket.db.models.users_models import User


async def check_auth() -> Optional[User]:
    return await User.filter(id=2).first()
