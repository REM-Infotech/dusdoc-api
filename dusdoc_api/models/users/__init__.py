from datetime import datetime  # noqa: D104

import pytz
from quart_jwt_extended import get_current_user
from sqlalchemy import DateTime, ForeignKey, Integer, String

from dusdoc_api.app import db, jwt
from dusdoc_api.models.users.admin import LicensesUsers, SuperUser, Users, admins
from dusdoc_api.models.users.funcionarios import Cargos, Departamento, Empresa, Funcionarios

__all__ = ["Users", "SuperUser", "LicensesUsers", "admins", "Funcionarios", "Cargos", "Departamento", "Empresa"]


@jwt.user_identity_loader
def user_identity_lookup(*args: str, **kwargs: object) -> int:
    """
    Get the user's identity.

    Returns:
        int: The user's ID.

    """
    user: Users = args[0]

    return user.id


@jwt.token_in_blacklist_loader
def check_if_token_revoked(jwt_data: dict, *args: str, **kwargs: object) -> bool:
    """
    Check if the token is in the blocklist.

    Returns:
        bool: True if the token is revoked, False otherwise.

    """
    arg = args  # noqa: F841
    kw = kwargs  # noqa: F841

    jti = jwt_data["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()

    return token is not None


@jwt.user_loader_callback_loader
def user_lookup_callback(*args: str, **kwargs: object) -> Users | None:
    """
    Get the user from the JWT data.

    Returns:
        Users | None: The user object or None if not found.

    """
    id_: int = args[0]

    return db.session.query(Users).filter_by(id=id_).one_or_none()


class TokenBlocklist(db.Model):
    """Database model for token blocklist."""

    id: int = db.Column(Integer, primary_key=True)
    jti: str = db.Column(String(36), nullable=False, index=True)
    type: str = db.Column(String(16), nullable=False)
    user_id = db.Column(
        ForeignKey("users.id"),
        default=lambda: get_current_user().id,
        nullable=False,
    )
    created_at = db.Column(
        DateTime,
        server_default=datetime.now(pytz.timezone("America/Manaus")).isoformat(),
        nullable=False,
    )
