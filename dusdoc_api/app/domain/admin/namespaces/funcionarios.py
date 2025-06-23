import json  # noqa: D100, F401
from pathlib import Path  # noqa: D100, F401

import aiofiles
from quart import request  # noqa: F401
from quart.datastructures import FileStorage  # noqa: F401
from quart_socketio import Namespace
from tqdm import tqdm


class FuncionariosNamespace(Namespace):  # noqa: D101
    async def on_connect(self) -> None:  # noqa: D102
        """Handle the connection event."""
        tqdm.write("FuncionariosNamespace connected")

    async def on_listagem_funcionarios(self) -> bool:  # noqa: D102
        data = []
        try:
            parent = Path(__file__).cwd().joinpath("dusdoc_api", "examples")
            async with aiofiles.open(parent.joinpath("funcionarios.json"), "r", encoding="utf-8") as f:
                read_buff = await f.read()
                data: list[list[str]] = json.loads(read_buff)

        except Exception as e:
            tqdm.write(e)
            return []

        tqdm.write(json.loads(data))
        return data

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
