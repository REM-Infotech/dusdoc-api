from functools import wraps  # noqa: D100
from typing import Any, Callable

from quart_jwt_extended import decode_token
from socketio import AsyncServer

from dusdoc_api.app import app


def jwt_socketio_required(func: Callable[..., Any]):  # noqa: ANN201
    """Require JWT authentication for Socket.IO events."""

    @wraps(func)
    async def wrapper(  # noqa: ANN202
        self: AsyncServer = None,
        sid: str = None,
        data: str | int = None,
        *args: str | int | AsyncServer,
        **kwargs: str | int | AsyncServer,
    ):
        args = args
        kwargs = kwargs
        environ = list(self.server.environ.items())
        for key, _ in environ:
            environ = self.server.environ[key]
            break

        items = environ.get("QUERY_STRING", "").split("&")
        key_value_pairs = [item.split("=") for item in items if "=" in item]

        for key, value in key_value_pairs:
            environ[key] = value

        token = environ.get("token")
        if not token:
            return {"error": "Unauthorized", "status": 401}

        async with app.app_context():
            decoded_token = decode_token(token)  # noqa: F841

        # Call the original function
        return await func(self, sid, data, *args, **kwargs)

    return wrapper
