# noqa: D100
from datetime import datetime

import pytz
from flask_sqlalchemy import SQLAlchemy
from quart import Response, current_app, jsonify, make_response
from quart.views import MethodView
from quart_jwt_extended import jwt_required

from dusdoc_api.models.admissional import RegistryAdmissao, RegistryContrato
from dusdoc_api.models.users.funcionarios import Funcionarios as Users

from . import AdmissaoDict, get_data


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

        admissao = RegistryAdmissao(
            prazo=data["prazo"],
            data_solicitacao=datetime.now(pytz.timezone("America/Manaus")),
        )
        admissao.funcionario = funcionario

        contrato = RegistryContrato(
            contrato_name=data["contrato"].name,
            blob_doc=data["contrato"].stream.read(),
        )
        contrato.funcionario = funcionario
        funcionario.status_admissao = "EM ANDAMENTO"
        db.session.add_all([admissao, contrato])
        db.session.commit()

        return await make_response(jsonify(message="Admissão realizada com sucesso!"))
