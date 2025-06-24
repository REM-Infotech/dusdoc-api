# noqa: D100, D104
from datetime import datetime

import pytz
from sqlalchemy import DateTime, LargeBinary, String

from dusdoc_api.app import db


class Funcionarios(db.Model):  # noqa: D101
    __tablename__ = "funcionarios"
    id = db.Column(db.Integer, primary_key=True)
    # Dados de login
    nome: str = db.Column(String(length=64))
    email: str = db.Column(String(length=64))
    password: str = db.Column(String(length=60))
    data_admissao: datetime = db.Column(DateTime, default=datetime.now(pytz.timezone("Etc/GMT+4")))
    login_time = db.Column(DateTime, default=datetime.now(pytz.timezone("America/Manaus")))
    verification_code: str = db.Column(String(length=45), unique=True)
    login_id: str = db.Column(String(length=64))
    filename: str = db.Column(String(length=128))
    blob_doc = db.Column(LargeBinary(length=(2**32) - 1))

    # Dados de cadastro
    codigo: str = db.Column(String(length=6), unique=True)
    deficiencia: str = db.Column(String(length=64))
    cargo: str = db.Column(String(length=64))
    departamento: str = db.Column(String(length=64))
    empresa: str = db.Column(String(length=64))
    cpf: str = db.Column(String(length=14), unique=True)


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
