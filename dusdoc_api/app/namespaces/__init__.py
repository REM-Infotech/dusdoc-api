from quart_socketio import SocketIO  # noqa: D104

from dusdoc_api.app.namespaces.forms import FuncionarioFormsNamespace
from dusdoc_api.app.namespaces.system import DusdocNamespace


async def register_namespace(io: SocketIO) -> None:  # noqa: D103
    await io.register_namespace(DusdocNamespace("/", io))
    await io.register_namespace(FuncionarioFormsNamespace("/funcionario_forms", io))
