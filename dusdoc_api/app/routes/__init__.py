
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    
    from quart import Quart


async def register_routes(app: Quart):
    """
    Register all routes with the Quart application.
    """
    from .auth import auth


    app.register_blueprint(auth)
    # Add any additional routes or blueprints here as needed