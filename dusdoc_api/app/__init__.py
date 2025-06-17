import re  # noqa: D104
from pathlib import Path

import quart_flask_patch  # noqa: F401
from flask_sqlalchemy import SQLAlchemy
from quart import Quart, Response, jsonify
from quart_cors import cors
from quart_jwt_extended import JWTManager
from quart_socketio import SocketIO

from dusdoc_api.app.routes.forms import register_api

app = Quart(__name__)
jwt = JWTManager(app)
io = SocketIO()
db = SQLAlchemy()


@app.route("/", methods=["GET", "POST"])
async def test() -> Response:  # noqa: D103
    return jsonify(ok="ok")


def cors_allowed_origins(orig: str | None = None) -> bool:  # noqa: D103
    return True


async def create_app() -> Quart:  # noqa: D103
    from dusdoc_api.app.namespaces import register_namespace
    from dusdoc_api.app.routes import register_routes
    from dusdoc_api.models import init_database

    app.config.from_pyfile(Path(__file__).parent.resolve().joinpath("quartconf.py"))
    async with app.app_context():
        db.init_app(app)
        await io.init_app(app, cors_allowed_origins=cors_allowed_origins)
        await register_api(app)
        await register_routes(app)
        await register_namespace(io)
        await init_database(app)

    re.compile(r"^https:\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    return cors(
        app,
        allow_credentials=True,
        allow_origin=[
            re.compile(r"^https:\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"),
            re.compile(r"^https:\/\/(?:\d{1,3}\.){3}\d{1,3}$"),
            re.compile(r"^http:\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"),
            re.compile(r"^http:\/\/(?:\d{1,3}\.){3}\d{1,3}$"),
        ],
    )
