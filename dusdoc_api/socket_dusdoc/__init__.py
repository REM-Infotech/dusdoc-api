from socketio import AsyncServer
from dusdoc_api.socket_dusdoc.namespaces import DusdocNamespace


class DusdocSocketIO(AsyncServer):
    def is_asyncio_based(self):
        return True

    def attach(self, app, socketio_path="socket.io"):
        """Attach the Socket.IO server to a web application."""
        return self.attach(app, socketio_path=socketio_path)

    def get_namespace_class(self):
        """Return the namespace class to be used by this server."""
        return DusdocNamespace

    def get_async_mode(self):
        """Return the async mode used by this server."""
        return "asyncio"


sio = DusdocSocketIO(async_handlers=True, logger=True, json=None, async_mode="asyncio")
sio.register_namespace(DusdocNamespace("/"))  # Register the custom namespace
sio.async_handlers = True  # Ensure async handlers are enabled
