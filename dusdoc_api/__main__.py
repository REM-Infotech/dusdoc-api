"""Entrypoint for the server application."""

import asyncio

import uvicorn

from dusdoc_api.app import create_app


async def main() -> None:
    """Run socketio server."""
    app = await create_app()
    config = uvicorn.Config(app, host="0.0.0.0", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
