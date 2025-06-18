from quart import Quart  # noqa: D104
from quart_socketio import SocketIO

from dusdoc_api.app.domain.funcionarios.routes import register_routes_funcionarios
from dusdoc_api.app.domain.funcionarios.routes.forms import register_api_funcionario


async def register_quart(app: Quart, io: SocketIO) -> None:  # noqa: D103
    await register_routes_funcionarios()
    await register_api_funcionario()
