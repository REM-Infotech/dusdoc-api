from quart_socketio import Namespace

from dusdoc_api.wrappers.jwt import jwt_socketio_required

session = set()


class DusdocNamespace(Namespace):
    @jwt_socketio_required
    async def on_connect(self):
        """"""

    @jwt_socketio_required
    async def on_get_status_system(self):
        """Handle a request for the status of the server."""

        # If the token is valid, proceed with the request
        return True
