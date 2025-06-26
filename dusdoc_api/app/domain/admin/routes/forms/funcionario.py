# noqa: D100
import json
from datetime import datetime
from typing import TypedDict  # noqa: D100

from flask_sqlalchemy import SQLAlchemy
from quart import Response, current_app, jsonify, make_response, request
from quart.views import MethodView
from quart_jwt_extended import jwt_required
from werkzeug.datastructures import CombinedMultiDict, FileStorage, MultiDict

from dusdoc_api.models.admissional import RegistryAdmissao, RegistryContrato  # noqa: F401
from dusdoc_api.models.users.funcionarios import Funcionarios as Users


class FuncionarioDict(TypedDict):  # noqa: D101
    nome: str
    email: str
    cpf: str
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


class AdmissionalFormView(MethodView):  # noqa: D101
    init_every_request = False
    methods = ["GET", "POST"]

    def __init__(self, model: Users) -> None:  # noqa: D107
        self.model = model

    @jwt_required
    async def post(self) -> Response:
        db: SQLAlchemy = current_app.extensions["sqlalchemy"]
        data = await get_data()
        data = dict(list(data.items()))
        data["prazo"] = datetime.strptime(data["prazo"], "%Y-%m-%d")
        data = AdmissaoDict(**data)

        funcionario = db.session.query(Users).filter(Users.id == data["funcionario_id"]).first()

        admissao = RegistryAdmissao(prazo=data["prazo"])
        admissao.funcionario = funcionario

        contrato = RegistryContrato(
            contrato_name=data["contrato"].name,
            blob_doc=data["contrato"].stream.read(),
        )
        contrato.funcionario = funcionario

        db.session.add_all([admissao, contrato])
        db.session.commit()

        return await make_response(jsonify(message="Admissão realizada com sucesso!"))


class CadastroFuncionarioView(MethodView):  # noqa: D101
    init_every_request = False
    methods = ["GET", "POST"]

    def __init__(self, model: Users) -> None:  # noqa: D107
        self.model = model

    def check_user(self, name: str, cpf: str, db: SQLAlchemy) -> Users | None:
        return db.session.query(Users).filter(Users.nome == name).first()

    @jwt_required
    async def post(self) -> Response:
        db: SQLAlchemy = current_app.extensions["sqlalchemy"]

        data = FuncionarioDict(**(await get_data()))
        funcionario = data.get("nome")
        cpf = data.get("cpf")

        message = "Funcionário já existente!"
        returnCode = 403  # noqa: N806

        if not funcionario:
            message = "É necessário nome do funcionario"

        elif not self.check_user(name=funcionario, cpf=cpf, db=db):
            usr = Users(**data)
            db.session.add(usr)
            db.session.commit()
            returnCode = 200  # noqa: N806
            message = "Funcionário Cadastrado!"

        return await make_response(jsonify(message=message), returnCode)
