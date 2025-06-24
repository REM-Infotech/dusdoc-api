# noqa: D100, D104

# import pytz
# datetime.now(pytz.timezone("Etc/GMT+4"))
from sqlalchemy import Column, DateTime, Integer, LargeBinary, String

from dusdoc_api.app import db


class Funcionarios(db.Model):  # noqa: D101
    __tablename__ = "funcionarios"
    id = Column(Integer, primary_key=True)
    # Dados de login
    nome: str = Column(String(length=64))
    email: str = Column(String(length=64))
    password: str = Column(String(length=60))
    data_admissao = Column(DateTime)
    login_time = Column(DateTime)
    verification_code: str = Column(String(length=45), unique=True)
    login_id: str = Column(String(length=64))
    filename: str = Column(String(length=128))
    blob_doc = Column(LargeBinary(length=(2**32) - 1))

    # Dados de cadastro
    codigo: str = Column(String(length=6), unique=True)
    deficiencia: str = Column(String(length=64))
    cargo: str = Column(String(length=64))
    departamento: str = Column(String(length=64))
    empresa: str = Column(String(length=64))
    cpf: str = Column(String(length=14), unique=True)


class Cargos(db.Model):  # noqa: D101
    id = Column(Integer, primary_key=True)
    cargo = Column(String(length=64), nullable=False, unique=True)
    descricao = Column(String(length=512))


class Departamento(db.Model):  # noqa: D101
    __tablename__ = "departamentos"
    id = Column(Integer, primary_key=True)
    departamento = Column(String(length=64), nullable=False, unique=True)
    descricao = Column(String(length=512))


class Empresa(db.Model):  # noqa: D101
    __tablename__ = "empresa"
    id: int = Column(Integer, primary_key=True)
    nome_empresa: str = Column(String(length=64), unique=True)
    cnpj_empresa: str = Column(String(length=64), unique=True)
    filename: str = Column(String(length=128))
    blob_doc: LargeBinary = Column(db.LargeBinary(length=(2**32) - 1))
