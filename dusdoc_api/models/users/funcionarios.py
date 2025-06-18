# noqa: D100, D104
from datetime import datetime

import pytz
from sqlalchemy import LargeBinary

from dusdoc_api.app import db


class Funcionarios(db.Model):  # noqa: D101
    __tablename__ = "funcionarios"
    id = db.Column(db.Integer, primary_key=True)
    codigo: str = db.Column(db.String(length=6), nullable=False, unique=True)
    nome_funcionario: str = db.Column(db.String(length=64), nullable=False)
    cpf_funcionario: str = db.Column(db.String(length=14), unique=True)
    email_funcionario: str = db.Column(db.String(length=64))
    deficiencia: str = db.Column(db.String(length=64))
    data_admissao: datetime = db.Column(db.DateTime, default=datetime.now(pytz.timezone("Etc/GMT+4")))
    cargo: str = db.Column(db.String(length=64))
    departamento: str = db.Column(db.String(length=64))
    empresa: str = db.Column(db.String(length=64))


class Cargos(db.Model):  # noqa: D101
    id = db.Column(db.Integer, primary_key=True)
    cargo = db.Column(db.String(length=64), nullable=False, unique=True)
    descricao = db.Column(db.String(length=512))


class Departamento(db.Model):  # noqa: D101
    __tablename__ = "departamentos"
    id = db.Column(db.Integer, primary_key=True)
    departamento = db.Column(db.String(length=64), nullable=False, unique=True)
    descricao = db.Column(db.String(length=512))


class Empresa(db.Model):  # noqa: D101
    __tablename__ = "empresa"
    id: int = db.Column(db.Integer, primary_key=True)
    nome_empresa: str = db.Column(db.String(length=64), unique=True)
    cnpj_empresa: str = db.Column(db.String(length=64), unique=True)
    filename: str = db.Column(db.String(length=128))
    blob_doc: LargeBinary = db.Column(db.LargeBinary(length=(2**32) - 1))
