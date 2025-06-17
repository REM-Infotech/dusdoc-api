from quart import Quart

from dusdoc_api.app import db

from .forms import CacheForms

__all__ = ["CacheForms"]


async def init_database(app: Quart):
    async with app.app_context():
        db.create_all()
