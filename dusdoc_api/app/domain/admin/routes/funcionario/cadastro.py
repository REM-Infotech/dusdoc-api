# noqa: D100

from flask_sqlalchemy import SQLAlchemy
from quart import Response, current_app, jsonify, make_response
from quart.views import MethodView
from quart_jwt_extended import jwt_required

from dusdoc_api.models.users.funcionarios import Funcionarios as Users

from . import FuncionarioDict, get_data


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

        cod = str(len(db.session.query(Users).all()) + 1).zfill(6)

        data = await get_data()
        data = dict(list(data.items()))
        data["codigo"] = cod
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
