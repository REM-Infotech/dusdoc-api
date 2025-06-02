from socketio import AsyncNamespace

class DusdocNamespace(AsyncNamespace):
    def is_asyncio_based(self):
        return True

    async def trigger_event(self, event, *args):
        """Dispatch an event to the proper handler method."""
        return await self.trigger_event(event, *args)
    
    async def emit(self, event, data=None, to=None, room=None, skip_sid=None,
                   namespace=None, callback=None, ignore_queue=False):
        """Emit a custom event to one or more connected clients."""
        return await self.emit(event, data=data, to=to, room=room,
                                skip_sid=skip_sid,
                                namespace=namespace or self.namespace,
                                callback=callback,
                                ignore_queue=ignore_queue)