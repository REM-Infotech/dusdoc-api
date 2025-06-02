from quart import Quart
import asyncio
from dusdoc_api.app.routes import register_routes

app = Quart(__name__)


asyncio.run(register_routes(app))
