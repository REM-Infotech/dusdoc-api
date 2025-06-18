from pathlib import Path  # noqa: D100, F401

from quart import request
from quart.datastructures import FileStorage
from quart_socketio import Namespace


class FuncionariosNamespace(Namespace):  # noqa: D101
    async def on_listagem_funcionarios(self) -> bool:  # noqa: D102
        try:
            data = request.socket_data
            for _k, v in list(data.items()):
                if not isinstance(v, FileStorage):
                    if v is not None and v != "":
                        print(v)

            return True

        except Exception as e:
            print(e)
            return False

    async def on_filter_listagem_funcionarios(self) -> bool | None:  # noqa: D102
        try:
            data = request.socket_data
            for _k, v in list(data.items()):
                if not isinstance(v, FileStorage):
                    if v is not None and v != "":
                        print(v)

            return True

        except Exception as e:
            print(e)
            return False

    # async def on_admissional_files(self) -> bool:
    #     try:
    #         data = request.socket_data
    #         for _k, v in list(data.items()):
    #             if isinstance(v, FileStorage):
    #                 print(v.stream.read())

    #                 parent = Path(__file__).cwd().joinpath("dusdoc_api", "examples")
    #                 v.save(parent.joinpath(v.filename))
    #         return True

    #     except Exception as e:
    #         print(e)
    #         return False

    #     return True
