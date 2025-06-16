from quart_socketio import SocketIO

from dusdoc_api.app.namespaces.system import DusdocNamespace


async def register_namespace(io: SocketIO):
    await io.register_namespace(DusdocNamespace("/", io))
