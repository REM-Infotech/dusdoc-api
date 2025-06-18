from quart_socketio import SocketIO  # noqa: D104

from dusdoc_api.app.domain.funcionarios.namespaces.docs import FuncionarioDocsNamespace
from dusdoc_api.app.domain.funcionarios.namespaces.forms import FuncionarioFormsNamespace
from dusdoc_api.app.domain.funcionarios.namespaces.system import DusdocNamespace


async def register_namespace(io: SocketIO) -> None:  # noqa: D103
    namespaces = [
        DusdocNamespace("/", io),
        FuncionarioFormsNamespace("/funcionario_forms", io),
        FuncionarioDocsNamespace("/funcionario_informacoes", io),
    ]

    for namespace in namespaces:
        await io.register_namespace(namespace)
