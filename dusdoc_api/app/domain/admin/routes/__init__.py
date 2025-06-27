# noqa: D104

import json
from pathlib import Path
from typing import TypedDict
from uuid import uuid4

from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Environment, FileSystemLoader
from quart import Blueprint, current_app, jsonify, make_response, request
from quart.views import MethodView

admin = Blueprint("admin", __name__, url_prefix="/admin")
environment = Environment(
    loader=FileSystemLoader(Path(__file__).cwd().joinpath("dusdoc_api", "jinja")), autoescape=True
)


class Funcionario(TypedDict):  # noqa: D101
    id: str
    nome: str
    email: str
    cpf: str
    codigo: str
    departamento: str
    cargo: str
    empresa: str


class PainelFuncionario(MethodView):  # noqa: D101
    async def post(self) -> None:
        from dusdoc_api.models.users.funcionarios import Funcionarios as Users

        mail: Mail = current_app.extensions["mail"]
        db: SQLAlchemy = current_app.extensions["sqlalchemy"]

        data = await request.data or await request.form or await request.json

        if isinstance(data, bytes):
            data = data.decode()
            if isinstance(data, str):
                data = json.loads(data)

        data = Funcionario(**dict(list(data.items())))

        user = db.session.query(Users).filter(Users.id == data["id"]).first()
        message = "Acesso Liberado! Foi enviado um E-mail com instruções enviado para o funcionário"
        if user.password:
            message = "Senha resetada! Foi enviado um E-mail com instruções enviado para o funcionário"

        senha = uuid4().hex[:4].upper()
        user.senhacrip = senha

        template_file = environment.get_template("password.jinja")
        rendered_template = template_file.render(user_name=user.nome, user_password=senha, empresa=user.empresa)

        mail.send(
            Message(
                subject="Senha de Acesso ao App DusDoc",
                sender=f"Mensagem do Sistema <{current_app.config['MAIL_DEFAULT_SENDER']}>",
                recipients=[user.email],
                html=rendered_template,
            )
        )

        db.session.commit()
        return await make_response(
            jsonify(
                message=message,
            ),
            200,
        )


def registry_endpoint_admin() -> None:  # noqa: D103
    form_admissional = PainelFuncionario.as_view("AdmissionalForm")
    admin.add_url_rule("/acesso_app", view_func=form_admissional)
