from socketio import AsyncNamespace
from quart_jwt_extended import decode_token
from dusdoc_api.app import app
from dusdoc_api.decorators.jwt import jwt_socketio_required

session = set()


class DusdocNamespace(AsyncNamespace):
    @jwt_socketio_required
    async def on_connect(self, sid, environ, *args, **kwargs):
        """"""

    @jwt_socketio_required
    async def on_get_status_system(self, sid, data, *args, **kwargs):
        """Handle a request for the status of the server."""

        # If the token is valid, proceed with the request
        await self.emit("status", dict(sid=sid))
        return dict(sid=sid)
