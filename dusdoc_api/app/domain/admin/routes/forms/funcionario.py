# noqa: D100
import json
from typing import TypedDict  # noqa: D100

from flask_sqlalchemy import SQLAlchemy
from quart import Response, current_app, jsonify, make_response, request
from quart.views import MethodView
from quart_jwt_extended import jwt_required

from dusdoc_api.models.users.funcionarios import Funcionarios as Users


class FuncionarioDict(TypedDict):  # noqa: D101
    nome: str
    email: str
    cpf: str
    departamento: str
    cargo: str
    empresa: str


class AdmissionalFormView(MethodView):  # noqa: D101
    init_every_request = False
    methods = ["GET", "POST"]

    def __init__(self, model: Users) -> None:  # noqa: D107
        self.model = model

    async def post(self) -> Response:
        return await make_response(jsonify(ok="ok"))


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
        data = await request.json or await request.form or await request.data
        if isinstance(data, bytes):
            data = data.decode()
            if isinstance(data, str):
                data = json.loads(data)

        data = FuncionarioDict(**data)
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
