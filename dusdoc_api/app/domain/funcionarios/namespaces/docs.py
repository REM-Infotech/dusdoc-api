# from pathlib import Path  # noqa: D100

# from quart import request
# from quart.datastructures import FileStorage
import json
from datetime import datetime
from pathlib import Path
from typing import TypedDict

import aiofiles
from flask_sqlalchemy import SQLAlchemy
from quart import current_app, request
from quart_jwt_extended import jwt_required  # noqa: F401
from quart_socketio import Namespace


class RegistroAdmissao(TypedDict):  # noqa: D101
    solicitacao_desc: str
    data_solicitacao: datetime
    prazo: datetime
    extension_file: str


class FuncionarioDocsNamespace(Namespace):  # noqa: D101
    async def on_my_docs(self) -> list[dict[str, str]]:  # noqa: D102
        path_parent = Path(__file__).cwd().joinpath("dusdoc_api", "examples", "example.json")
        async with aiofiles.open(str(path_parent), "r", encoding="utf-8") as f:
            readfile = await f.read()
            data = json.loads(readfile)
            return data

    async def on_solicitados(self) -> list[dict[str, str]]:
        from dusdoc_api.models.admissional import RegistryAdmissao
        from dusdoc_api.models.users.funcionarios import Funcionarios

        data = request.socket_data
        db: SQLAlchemy = current_app.extensions["sqlalchemy"]
        user = (
            db.session.query(RegistryAdmissao)
            .select_from(Funcionarios)
            .join(RegistryAdmissao.funcionario)
            .filter(Funcionarios.id == data["id"])
            .all()
        )  # noqa: F841

        dataReturn = [  # noqa: N806
            RegistroAdmissao(
                data_solicitacao=item.data_solicitacao.strftime("%d/%m/%Y"),
                prazo=item.prazo.strftime("%d/%m/%Y"),
                solicitacao_desc="Formulário Admissional",
                extension_file="pdf",
            )
            for item in user
        ]

        return dataReturn
        # path_parent = Path(__file__).cwd().joinpath("dusdoc_api", "examples", "example_solicitados.json")
        # async with aiofiles.open(str(path_parent), "r", encoding="utf-8") as f:
        #     readfile = await f.read()
        #     data = json.loads(readfile)
        #     return data
