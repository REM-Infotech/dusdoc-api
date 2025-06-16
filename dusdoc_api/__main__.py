"""Entrypoint for the server application."""

import asyncio

import uvicorn
from socketio import ASGIApp

from dusdoc_api.app import create_app


async def main(app: ASGIApp) -> None:
    """Run socketio server."""
    config = uvicorn.Config(app, host="0.0.0.0", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main(app=create_app()))
