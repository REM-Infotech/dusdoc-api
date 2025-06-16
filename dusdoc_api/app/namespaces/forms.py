from quart import request
from quart_socketio import Namespace


class FuncionarioFormsNamespace(Namespace):
    async def on_admissional_form(self):
        request
        return True
