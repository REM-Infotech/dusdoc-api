from quart import Quart
import asyncio
from dusdoc_api.app.routes import register_routes
from quart_jwt_extended import JWTManager
from uuid import uuid4

app = Quart(__name__)

app.config["JWT_SECRET_KEY"] = uuid4().hex  # Use a random secret key for JWT

jwt = JWTManager(app)


@app.after_request
async def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    return response


asyncio.run(register_routes(app))
