# noqa: D104
import json
from datetime import datetime
from typing import TypedDict

from quart import request
from werkzeug.datastructures import CombinedMultiDict, FileStorage, MultiDict


class FuncionarioDict(TypedDict):  # noqa: D101
    id: str

    nome: str
    email: str
    cpf: str
    codigo: str
    departamento: str
    cargo: str
    empresa: str


class AdmissaoDict(TypedDict):  # noqa: D101
    prazo: datetime
    contrato: FileStorage
    funcionario_id: str


async def get_data() -> MultiDict:  # noqa: D103
    data = await request.json or await request.form or await request.data
    if isinstance(data, bytes):
        data = data.decode()
        if isinstance(data, str):
            data = json.loads(data)

    files = await request.files

    return CombinedMultiDict([data, files])


from .admissional import AdmissionalFormView  # noqa: E402
from .cadastro import CadastroFuncionarioView  # noqa: E402

__all__ = ["AdmissionalFormView", "CadastroFuncionarioView"]
