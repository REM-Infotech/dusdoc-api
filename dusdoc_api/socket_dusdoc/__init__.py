from socketio import AsyncServer
from dusdoc_api.socket_dusdoc.namespaces import DusdocNamespace
from dusdoc_api.app import app
import asyncio


async def get_socketio():
    async with app.app_context():
        # Ensure the app context is available for the namespace

        sio = AsyncServer(
            async_mode="asgi",
            cors_allowed_origins="*",
            ping_interval=25,
            ping_timeout=10,
            namespaces=["/bot", "/logs", "/"],
            transports=["websocket"],
        )
        sio.register_namespace(DusdocNamespace("/"))
        return sio


sio = asyncio.run(get_socketio())
