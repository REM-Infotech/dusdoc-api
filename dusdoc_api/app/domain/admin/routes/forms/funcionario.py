import json  # noqa: D100

from flask_sqlalchemy import SQLAlchemy
from quart import Response, current_app, jsonify, make_response, request
from quart.views import MethodView
from werkzeug.datastructures import MultiDict

from dusdoc_api.models.users.funcionarios import Funcionarios as Users


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

    async def post(self) -> Response:
        db: SQLAlchemy = current_app.extensions["sqlalchemy"]

        data = await request.json or await request.form or await request.data
        if isinstance(data, bytes):
            data = data.decode()
            if isinstance(data, str):
                data: MultiDict = json.loads(data)

        usr = db.session.query(Users).filter(Users.nome == data.get("nome"), Users.cpf == data.get("cpf")).first()
        if usr:
            return await make_response(jsonify(message="Funcionário já existente!"), 403)

        usr = Users(**data)
        db.session.add(usr)
        db.session.commit()

        return await make_response(jsonify(message="Funcionário Cadastrado!"), 200)
