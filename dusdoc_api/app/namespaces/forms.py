from pathlib import Path

from quart import request
from quart.datastructures import FileStorage
from quart_socketio import Namespace


class FuncionarioFormsNamespace(Namespace):
    async def on_admissional_form(self):
        try:
            data = await request.socket_data
            for k, v in list(data.items()):
                v: FileStorage
                print(v.stream.read())

                parent = Path(__file__).parent.resolve()
                await v.save(parent.joinpath("test.xlsx"))
            return True

        except Exception as e:
            print(e)
            return False

    async def on_admissional_files(self):
        try:
            data = request.socket_data
            for k, v in list(data.items()):
                if isinstance(v, FileStorage):
                    print(v.stream.read())

                    parent = Path(__file__).parent.resolve()
                    v.save(parent.joinpath(v.filename))
            return True

        except Exception as e:
            print(e)
            return False
