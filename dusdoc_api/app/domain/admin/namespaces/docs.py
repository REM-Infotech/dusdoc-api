# from pathlib import Path  # noqa: D100

# from quart import request
# from quart.datastructures import FileStorage
import json  # noqa: F401
from pathlib import Path  # noqa: F401

import aiofiles  # noqa: F401
from quart_socketio import Namespace  # noqa: F401


# class FuncionarioDocsNamespace(Namespace):  # noqa: D101
#     async def on_meus_docs(self) -> list[dict[str, str]]:  # noqa: D102
#         path_parent = Path(__file__).parent.resolve().joinpath("example.json")
#         async with aiofiles.open(str(path_parent), "r", encoding="utf-8") as f:
#             print(f)
#             readfile = await f.read()
#             data = json.loads(readfile)
#             return data

#     async def on_solicitados(self) -> list[dict[str, str]]:
#         return [
#             {"solicitacao_desc": "Formulário admissional", "request_date": "01/02/2025"},
#         ]
