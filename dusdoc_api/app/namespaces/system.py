from quart_socketio import Namespace

session = set()


class DusdocNamespace(Namespace):
    async def on_connect(self):
        """"""

    async def on_get_status_system(self):
        """Handle a request for the status of the server."""

        # If the token is valid, proceed with the request
        return True

    async def on_test(self):
        return {"test": "test"}
