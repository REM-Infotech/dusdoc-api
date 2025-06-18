import re  # noqa: D104
from pathlib import Path

import quart_flask_patch  # noqa: F401
from flask_sqlalchemy import SQLAlchemy
from quart import Quart, Response, jsonify
from quart_cors import cors
from quart_jwt_extended import JWTManager
from quart_socketio import SocketIO
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

from dusdoc_api.app.domain import register_quart

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
    from dusdoc_api.models import init_database

    app.config.from_pyfile(Path(__file__).parent.resolve().joinpath("quartconf.py"))
    async with app.app_context():
        db.init_app(app)
        await io.init_app(app, cors_allowed_origins=cors_allowed_origins)
        await register_quart(app, io)
        await init_database(app)

    re.compile(r"^https:\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    app.asgi_app = ProxyHeadersMiddleware(app.asgi_app)
    return cors(
        app,
        allow_origin="*",
        allow_methods=["GET", "POST"],
    )
