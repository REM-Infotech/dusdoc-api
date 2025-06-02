from socketio import AsyncNamespace

session = set()


class DusdocNamespace(AsyncNamespace):
    async def on_get_status_system(self, sid, *args, **kwargs):
        """Handle a request for the status of the server."""
        await self.emit("status", dict(sid=sid))
        return await self.get_session(sid)
