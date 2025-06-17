from quart import Quart

from dusdoc_api.app import db
from dusdoc_api.models import forms, users

__all__ = ["forms", "users"]


async def init_database(app: Quart):
    async with app.app_context():
        db.create_all()
