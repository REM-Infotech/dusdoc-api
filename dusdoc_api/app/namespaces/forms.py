from pathlib import Path

from quart import request
from quart.datastructures import FileStorage
from quart_socketio import Namespace


class FuncionarioFormsNamespace(Namespace):
    async def on_admissional_form(self):
        try:
            file = await request.files
            for k, v in list(file.items()):
                v: FileStorage
                print(v.stream.read())

                parent = Path(__file__).parent.resolve()
                await v.save(parent.joinpath("test.xlsx"))
            return True

        except Exception as e:
            print(e)
            return False
