from __future__ import annotations  # noqa: D104

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from quart import Quart


async def register_routes(app: Quart) -> None:
    """Register all routes with the Quart application."""
    from .auth import auth
    from .forms import forms

    blueprints = [auth, forms]

    for blueprint in blueprints:
        app.register_blueprint(blueprint)
    # Add any additional routes or blueprints here as needed
