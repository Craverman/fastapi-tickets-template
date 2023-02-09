from typing import List

from ticket.settings import settings

MODELS_MODULES: List[str] = [
    "ticket.db.models.users_models",
    "ticket.db.models.tickets_models",
]


TORTOISE_CONFIG = {  # noqa: WPS407
    "connections": {
        "default": str(settings.db_url),
    },
    "apps": {
        "models": {
            "models": MODELS_MODULES + ["aerich.models"],
            "default_connection": "default",
        },
    },
}
