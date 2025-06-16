import re

from quart import Quart, jsonify
from quart_cors import cors
from quart_jwt_extended import JWTManager
from quart_socketio import SocketIO

app = Quart(__name__)
jwt = JWTManager(app)
io = SocketIO()


@app.route("/", methods=["GET", "POST"])
async def test():
    return jsonify(ok="ok")


def cors_allowed_origins(orig: str | None = None):
    return True


async def create_app():
    from dusdoc_api.app.namespaces import register_namespace
    from dusdoc_api.app.routes import register_routes

    async with app.app_context():
        await io.init_app(app, cors_allowed_origins=cors_allowed_origins)
        await register_routes(app)
        await register_namespace(io)

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
