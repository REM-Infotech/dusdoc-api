from socketio import AsyncServer, AsyncNamespace



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
        
        
class DusdocSocketIO(AsyncServer):
    def is_asyncio_based(self):
        return True

    def attach(self, app, socketio_path='socket.io'):
        """Attach the Socket.IO server to a web application."""
        return self.attach(app, socketio_path=socketio_path)

    def get_namespace_class(self):
        """Return the namespace class to be used by this server."""
        return DusdocNamespace
    
    def get_async_mode(self):
        """Return the async mode used by this server."""
        return 'asyncio'
    
    
sio = DusdocSocketIO(async_handlers=True, logger=True, json=None)

sio.register_namespace(DusdocNamespace('/'))  # Register the custom namespace
sio.async_mode = 'asyncio'  # Set the async mode to asyncio
sio.async_handlers = True  # Ensure async handlers are enabled

