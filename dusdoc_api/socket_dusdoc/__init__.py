from socketio import AsyncServer
from dusdoc_api.socket_dusdoc.namespaces import DusdocNamespace


def get_socketio():
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


sio = get_socketio()
