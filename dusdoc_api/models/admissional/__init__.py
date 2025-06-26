# noqa: D104
from sqlalchemy import Column, DateTime, ForeignKey, Integer, LargeBinary, String

from dusdoc_api.app import db

files = db.Table(
    "files",
    Column("file_id", Integer, ForeignKey("file.id"), primary_key=True),
    Column("cached_form_id", Integer, ForeignKey("cached_form.id"), primary_key=True),
)


class RegistryAdmissao(db.Model):  # noqa: D101
    id = Column(Integer, primary_key=True)
    data_solicitacao = Column(DateTime, nullable=False)
    prazo = Column(DateTime, nullable=False)
    funcionario_id = Column(Integer, ForeignKey("funcionarios.id"))
    funcionario = db.relationship("Funcionarios", backref="registry_admissao")


class RegistryContrato(db.Model):  # noqa: D101
    id = Column(Integer, primary_key=True)
    contrato_name: str = Column(String(length=128))
    blob_doc = Column(LargeBinary(length=(2**32) - 1))
    funcionario_id = Column(Integer, ForeignKey("funcionarios.id"))
    funcionario = db.relationship("Funcionarios", backref="registry_contrato")


class FileModel(db.Model):  # noqa: D101
    __tablename__ = "file"
    id = Column(Integer, primary_key=True)
    filename = Column(String)
    blob = Column(LargeBinary)


class CacheForms(db.Model):  # noqa: D101
    __tablename__ = "cached_form"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    files = db.relationship(
        "FileModel",
        secondary="files",
        backref=db.backref("cached_form", lazy=True),
    )
