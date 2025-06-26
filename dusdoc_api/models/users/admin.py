"""Module for user-related models and authentication utilities."""

from __future__ import annotations

from datetime import datetime
from uuid import uuid4

import bcrypt
import pytz
from sqlalchemy import DateTime, ForeignKey, Integer, LargeBinary, String

from dusdoc_api.app import db, jwt  # noqa: F401

salt = bcrypt.gensalt()


class SuperUser(db.Model):
    """Database model for a super user."""

    __tablename__ = "superuser"
    id: int = db.Column(Integer, primary_key=True)
    users_id: int = db.Column(Integer, ForeignKey("users.id"))
    users = db.relationship("Users", backref=db.backref("supersu", lazy=True))


class Users(db.Model):
    """Database model for application users."""

    __tablename__ = "users"
    id: int = db.Column(db.Integer, primary_key=True)
    login: str = db.Column(String(length=30), nullable=False, unique=True)
    nome_usuario: str = db.Column(String(length=64), nullable=False, unique=True)
    email: str = db.Column(String(length=50), nullable=False, unique=True)
    password: str = db.Column(String(length=60), nullable=False)
    login_time = db.Column(DateTime, default=datetime.now(pytz.timezone("America/Manaus")))
    verification_code: str = db.Column(String(length=45), unique=True)
    login_id: str = db.Column(String(length=64), nullable=False, default=str(uuid4()))
    filename: str = db.Column(String(length=128))
    blob_doc = db.Column(LargeBinary(length=(2**32) - 1))

    licenseus_id: int = db.Column(Integer, ForeignKey("licenses_users.id"))
    licenseusr = db.relationship("LicensesUsers", backref="user")

    def __init__(self, login: str = None, nome_usuario: str = None, email: str = None) -> None:
        """
        Initialize a new user instance.

        Args:
            login (str, optional): The user's login name.
            nome_usuario (str, optional): The full name.
            email (str, optional): The user's email.

        """
        self.login = login
        self.nome_usuario = nome_usuario
        self.email = email

    @property
    def senhacrip(self) -> any:
        """
        Get the encrypted password.

        Returns:
            str: The encrypted password.

        """
        return self.senhacrip

    @senhacrip.setter
    def senhacrip(self, senha_texto: str) -> None:
        """
        Encrypt and set the user’s password.

        Args:
            senha_texto (str): Plain text password.

        """
        self.password = bcrypt.hashpw(senha_texto.encode(), salt=salt).decode("utf-8")

    def check_password(self, senha_texto_claro: str) -> bool:
        """
        Check if the provided password matches the stored encrypted password.

        Args:
            senha_texto_claro (str): Plain text password.

        Returns:
            bool: True if valid, False otherwise.

        """
        return bcrypt.checkpw(senha_texto_claro.encode("utf-8"), self.password.encode("utf-8"))

    @property
    def dict_query(self) -> dict[str, str | int]:
        """
        Return a dictionary representation of selected user attributes.

        Returns:
            dict: Dictionary of user attributes.

        """
        data = {
            "id": self.id,
            "login": self.login,
            "nome_usuario": self.nome_usuario,
            "email": self.email,
        }

        if len(self.admin) > 0:
            data.update({"tipo_user": "admin"})

        if len(self.supersu) > 0:
            data.update({"tipo_user": "supersu"})
            data.update({"licenses": self.licenseusr.license_token})

        return data


class LicensesUsers(db.Model):
    """Database model representing license users."""

    __tablename__ = "licenses_users"
    id: int = db.Column(Integer, primary_key=True)
    name_client: str = db.Column(String(length=60), nullable=False, unique=True)
    cpf_cnpj: str = db.Column(String(length=30), nullable=False, unique=True)
    license_token: str = db.Column(String(length=512), nullable=False, unique=True)

    # Relacionamento de muitos para muitos com users
    admins = db.relationship("Users", secondary="admins", backref="admin")


admins = db.Table(
    "admins",
    db.Column("users_id", Integer, ForeignKey("users.id"), primary_key=True),
    db.Column(
        "license_user_id",
        Integer,
        ForeignKey("licenses_users.id"),
        primary_key=True,
    ),
)
