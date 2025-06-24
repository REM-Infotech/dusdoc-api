from os import environ  # noqa: D104

from dotenv import load_dotenv
from quart import Quart

from dusdoc_api.app import db
from dusdoc_api.models.admissional import RegistryAdmissao
from dusdoc_api.models.users import Users

__all__ = [
    "RegistryAdmissao",
    "Users",
]

load_dotenv()


async def init_database(app: Quart) -> None:
    env = environ
    async with app.app_context():
        db.create_all()
        user = db.session.query(Users).filter(Users.login == env.get("ROOT_USERNAME")).first()
        if not user:
            user = Users(
                login=env.get("ROOT_USERNAME"),
                email=env.get("ROOT_EMAIL"),
                nome_usuario=env.get("ROOT_USERNAME"),
            )

            user.senhacrip = env.get("ROOT_PASSWORD")

            db.session.add(user)
            db.session.commit()
