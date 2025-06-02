"""Entrypoint for the server application."""

import asyncio
from quart_cors import cors
import uvicorn
from socketio import ASGIApp

from dusdoc_api.app import app
from dusdoc_api.socket_dusdoc import sio


async def main(app: ASGIApp) -> None:
    """Run socketio server."""
    config = uvicorn.Config(app, host="0.0.0.0", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    app = ASGIApp(sio, cors(app, allow_origin="*"))

    asyncio.run(main(app=app))
