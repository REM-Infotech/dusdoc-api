from socketio import AsyncNamespace


class DusdocNamespace(AsyncNamespace):
    def is_asyncio_based(self):
        return True

    async def trigger_event(self, event, *args):
        """Dispatch an event to the proper handler method."""
        return await self.trigger_event(event, *args)

    async def emit(
        self,
        event,
        data=None,
        to=None,
        room=None,
        skip_sid=None,
        namespace=None,
        callback=None,
        ignore_queue=False,
    ):
        """Emit a custom event to one or more connected clients."""
        return await self.emit(
            event,
            data=data,
            to=to,
            room=room,
            skip_sid=skip_sid,
            namespace=namespace or self.namespace,
            callback=callback,
            ignore_queue=ignore_queue,
        )

    async def on_connect(self, sid, environ):
        """Handle a new client connection."""
        return await self.on_connect(sid, environ)

    async def on_get_status(self, sid):
        """Handle a request for the status of the server."""
        return await self.on_get_status(sid)
