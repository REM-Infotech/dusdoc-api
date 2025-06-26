import json  # noqa: D100, F401
from pathlib import Path  # noqa: D100, F401
from typing import TypedDict

import aiofiles  # noqa: F401
from flask_sqlalchemy import SQLAlchemy
from quart import current_app, request  # noqa: F401
from quart.datastructures import FileStorage  # noqa: F401
from quart_socketio import Namespace
from tqdm import tqdm  # noqa: F401


class ListagemFuncionarioDict(TypedDict):  # noqa: D101
    id: str
    nome: str
    codigo: str
    email: str
    status_admissao: str


class FuncionariosNamespace(Namespace):  # noqa: D101
    async def on_connect(self) -> None:  # noqa: D102
        """Handle the connection event."""

    async def on_listagem_funcionarios(self) -> bool:  # noqa: D102
        from dusdoc_api.models.users.funcionarios import Funcionarios as Users

        db: SQLAlchemy = current_app.extensions["sqlalchemy"]
        # data = []
        # try:
        #     parent = Path(__file__).cwd().joinpath("dusdoc_api", "examples")
        #     async with aiofiles.open(parent.joinpath("funcionarios.json"), "r", encoding="utf-8") as f:
        #         read_buff = await f.read()
        #         data: list[list[str]] = json.loads(read_buff)

        # except Exception as e:
        #     tqdm.write(e)
        #     return []

        # # tqdm.write(json.dumps(data))

        users = db.session.query(Users).all()
        data: list[ListagemFuncionarioDict] = [
            ListagemFuncionarioDict(
                id=user.id,
                nome=user.nome,
                codigo=user.codigo,
                email=user.email,
                status_admissao=user.status_admissao,
            )
            for user in users
        ]

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
